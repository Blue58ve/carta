#!/usr/bin/env python3
"""Maquetas: coloca cada etiqueta sobre las fotos reales del empaque.

Las esquinas de destino son estimaciones hechas a ojo sobre cada foto
(píxeles de la imagen original). La luz de la foto se aplica sobre la
etiqueta para que el resultado se vea natural.
"""
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
PREV = ROOT.parent / "vista-previa"
OUT = ROOT.parent / "maquetas"
OUT.mkdir(exist_ok=True)


def H_from(src, dst):
    return cv2.getPerspectiveTransform(np.float32(src), np.float32(dst))


def map_pts(Hm, pts):
    p = cv2.perspectiveTransform(np.float32(pts).reshape(-1, 1, 2), Hm)
    return p.reshape(-1, 2)


def place_on_surface(surface_px, surface_mm, rect_mm):
    """surface_px: 4 esquinas (TL,TR,BR,BL) de una superficie real de surface_mm=(w,h).
    rect_mm: (x0,y0,x1,y1) zona de la etiqueta dentro de esa superficie."""
    w, h = surface_mm
    Hm = H_from([(0, 0), (w, 0), (w, h), (0, h)], surface_px)
    x0, y0, x1, y1 = rect_mm
    return map_pts(Hm, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


D = 1932 / 1500   # las formas de enfoque se midieron sobre la foto a 1500 px de ancho


def focus_mask(shape, focus, feather, erode=0):
    h, w = shape[:2]
    mask = np.zeros((h, w), np.uint8)
    for kind, data, *scale in focus:
        k = scale[0] if scale else D
        if kind == "poly":
            cv2.fillPoly(mask, [np.int32(np.array(data, np.float64) * k)], 255)
        elif kind == "ellipse":
            cx, cy, ax, ay = [v * k for v in data]
            cv2.ellipse(mask, (int(cx), int(cy)), (int(ax), int(ay)), 0, 0, 360, 255, -1)
        elif kind == "rect":
            x0, y0, x1, y1 = [int(v * k) for v in data]
            mask[y0:y1, x0:x1] = 255
    if erode:
        mask = cv2.erode(mask, np.ones((erode * 2 + 1, erode * 2 + 1), np.uint8))
    hard = mask.astype(np.float32) / 255
    return cv2.GaussianBlur(hard, (0, 0), feather)[..., None], hard


def disguise_background(img, focus, feather=6, blur=46, glass=None, glass_cut=None, protect=None):
    """Desenfoque profundo + desaturado + tono azul noche fuera del producto (y la mano),
    con viñeta suave: el fondo se vuelve una atmósfera y el empaque queda en primer plano."""
    f = img.astype(np.float32) / 255
    m, hard = focus_mask(img.shape, focus, feather, erode=5)
    # desenfoque normalizado: el brillo del producto no se derrama sobre el fondo (sin halo)
    keep = cv2.dilate(hard, np.ones((61, 61), np.uint8))
    outside = (1 - keep)[..., None]
    num = cv2.GaussianBlur(f * outside, (0, 0), blur)
    den = cv2.GaussianBlur(outside, (0, 0), blur)[..., None] if outside.ndim == 2 else cv2.GaussianBlur(outside[..., 0], (0, 0), blur)[..., None]
    far = cv2.GaussianBlur(f, (0, 0), blur * 3)
    bg = np.where(den > 0.02, num / np.maximum(den, 1e-4), far)
    bg = cv2.GaussianBlur(bg, (0, 0), 12)
    g = bg.mean(2, keepdims=True)
    bg = g + (bg - g) * 0.25
    navy = np.array([48, 28, 15], np.float32) / 255           # #0F1C30 en BGR
    bg = bg * 0.40 + navy * 0.60
    h, w = img.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    vig = np.clip(1.05 - 0.38 * r ** 1.6, 0.45, 1)[..., None]
    out = f * m + bg * vig * (1 - m)
    if glass:
        # plástico transparente: deja ver el fondo ya disimulado y conserva sus brillos
        gm, _ = focus_mask(img.shape, glass, 8)
        if glass_cut:
            cut, _ = focus_mask(img.shape, glass_cut, 8)
            gm = gm * (1 - cut)
        if protect is not None:
            gm = gm * (1 - protect[..., None])
        # solo donde el plástico deja ver el fondo claro (no sobre la bandeja negra)
        lum = cv2.GaussianBlur(f.mean(2), (0, 0), 6)
        gm = gm * np.clip((lum - 0.2) / 0.16, 0, 1)[..., None]
        spec = np.clip(f - cv2.GaussianBlur(f, (0, 0), 20), 0, 1) * 1.6
        gray = f.mean(2, keepdims=True)
        fd = gray + (f - gray) * 0.15            # lo que se ve a través del plástico, sin color
        glassy = bg * vig * 0.7 + fd * 0.3 + spec
        out = out * (1 - gm) + np.clip(glassy, 0, 1) * gm
    out = out * (0.9 + 0.1 * vig)
    return (np.clip(out, 0, 1) * 255).astype(np.uint8)


def finish(out, out_name, crop=None, max_side=1600, focus=None, **glass):
    if focus:
        out = disguise_background(out, focus, **glass)
    if crop:
        x0, y0, x1, y1 = crop
        out = out[y0:y1, x0:x1]
    h, w = out.shape[:2]
    s = max_side / max(h, w)
    if s < 1:
        out = cv2.resize(out, (int(w * s), int(h * s)), interpolation=cv2.INTER_AREA)
    cv2.imwrite(str(OUT / out_name), out, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print("ok", out_name)


def composite(photo_path, label_rgba, quad, out_name, gloss=0.35, shade=0.55, crop=None,
              max_side=1600, ignore=None, focus=None, glass=None, glass_cut=None):
    photo = cv2.imread(str(photo_path), cv2.IMREAD_COLOR).astype(np.float32) / 255
    Hh, Wh = photo.shape[:2]
    lh, lw = label_rgba.shape[:2]
    Hm = H_from([(0, 0), (lw, 0), (lw, lh), (0, lh)], quad)
    warped = cv2.warpPerspective(label_rgba, Hm, (Wh, Hh), flags=cv2.INTER_AREA,
                                 borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    warped = warped.astype(np.float32) / 255
    rgb, a = warped[..., :3], warped[..., 3:4]
    # luz de la foto
    L8 = cv2.cvtColor((photo * 255).astype(np.uint8), cv2.COLOR_BGR2GRAY)
    if ignore:  # zonas que no son luz (p. ej. una etiqueta blanca que queda tapada)
        mask = np.zeros_like(L8)
        for x0, y0, x1, y1 in ignore:
            mask[y0:y1, x0:x1] = 255
        L8 = cv2.inpaint(L8, mask, 25, cv2.INPAINT_TELEA)
        # también se borra de la foto (la etiqueta del fabricante no va en el kit)
        p8 = cv2.inpaint((photo * 255).astype(np.uint8), mask, 9, cv2.INPAINT_TELEA)
        photo = p8.astype(np.float32) / 255
    L = L8.astype(np.float32) / 255
    Lb = cv2.GaussianBlur(L, (0, 0), 18)
    m = a[..., 0] > 0.5
    mean = float(Lb[m].mean()) if m.any() else 0.5
    factor = np.clip(Lb / max(mean, 1e-3), 0.7, 1.25) ** shade
    rgb = rgb * factor[..., None]
    # brillos (reflejos del plástico) sobre la etiqueta
    Ls = cv2.GaussianBlur(L, (0, 0), 3)
    hl = np.clip((Ls - 0.82) / 0.18, 0, 1)[..., None] * gloss
    rgb = rgb + (1 - rgb) * hl
    out = photo * (1 - a) + np.clip(rgb, 0, 1) * a
    out = (out * 255).astype(np.uint8)
    extra = dict(glass=glass, glass_cut=glass_cut, protect=a[..., 0]) if glass else {}
    finish(out, out_name, crop, max_side, focus, **extra)


def load(name):
    return cv2.imread(str(PREV / name), cv2.IMREAD_UNCHANGED)


FOTOS = ROOT / "fotos"

# Zonas que quedan nítidas (producto + mano). El resto se disimula.
F_LID = [("poly", [(220, 570), (1165, 548), (1238, 616), (1284, 800), (1326, 1100), (1300, 1335), (1180, 1395),
                   (150, 1400), (60, 1290), (70, 1000), (190, 635)]),
         ("poly", [(95, 690), (175, 655), (215, 700), (205, 820), (130, 1100), (260, 1420),
                   (170, 1570), (0, 1640), (0, 820)])]
F_HALL = [("poly", [(60, 430), (1145, 322), (1145, 350), (1095, 590), (1050, 640), (1052, 1590), (1185, 1640),
                    (1175, 1700), (255, 1815), (250, 1770), (330, 1000), (60, 455)]),
          ("poly", [(160, 1000), (300, 955), (425, 1010), (390, 1400), (300, 1560), (200, 1630),
                    (0, 1720), (0, 1460), (140, 1310)])]
F_BAG = [("poly", [(20, 0), (1500, 0), (1500, 40), (1470, 60), (1312, 1565), (283, 1712),
                   (150, 470), (20, 40)])]
F_PAN = [("poly", [(893, 92), (1318, 288), (1306, 322), (700, 1742), (520, 1800), (300, 1705),
                   (155, 1628), (875, 110)]),
]
G_DOME = [("ellipse", (990, 1143, 420, 420), 1), ("rect", (570, 1143, 1410, 1500), 1),
          ("ellipse", (998, 1440, 428, 290), 1)]
G_DOME_CUT = [("poly", [(300, 1000), (445, 690), (485, 880), (560, 1335), (870, 1385), (885, 1450),
                        (700, 1500), (420, 1530), (300, 1720), (0, 1720), (0, 1250)])]
HAND_DOME = [(300, 1000), (445, 690), (485, 880), (560, 1335), (870, 1385), (885, 1450), (700, 1500),
             (420, 1530), (300, 1720), (0, 1720), (0, 1250)]
F_DOME = [("ellipse", (990, 1143, 398, 398), 1), ("rect", (592, 1143, 1388, 1400), 1),
          ("ellipse", (998, 1440, 426, 288), 1), ("poly", HAND_DOME)]

# 1 · Tapa del envase (zona plana ≈ 160 × 110 mm)
lid = [(322, 889), (1546, 902), (1610, 1688), (168, 1700)]
composite(FOTOS / "envase-tapa.jpg", load("etiqueta-asado-negro.png"),
          place_on_surface(lid, (140, 80), (25, 12, 115, 68)),
          "maqueta-envase-asado-negro.jpg", gloss=0.4, crop=(0, 560, 1932, 2000),
          ignore=[(735, 1250, 1065, 1440)], focus=F_LID)
composite(FOTOS / "envase-tapa.jpg", load("etiqueta-ensalada-de-gallina.png"),
          place_on_surface(lid, (140, 80), (25, 12, 115, 68)),
          "maqueta-envase-ensalada-de-gallina.jpg", gloss=0.4, crop=(0, 560, 1932, 2000),
          ignore=[(735, 1250, 1065, 1440)], focus=F_LID)

# 2 · Bolsa de hallacas (bloque 2×2 ≈ 220 × 345 mm)
hall = [(451, 787), (1303, 761), (1393, 2141), (464, 2180)]
composite(FOTOS / "hallacas.jpg", load("etiqueta-hallacas.png"),
          place_on_surface(hall, (220, 345), (45, 132, 175, 212)),
          "maqueta-hallacas.jpg", gloss=0.5, crop=(0, 300, 1932, 2576), focus=F_HALL)

# 3 · Bolsa esmerilada (cuerpo bajo la solapa ≈ 300 × 310 mm)
bag = [(193, 605), (1893, 567), (1687, 2009), (367, 2190)]
composite(FOTOS / "bolsa.jpg", load("sticker-bolsa.png"),
          place_on_surface(bag, (300, 310), (100, 62, 200, 202)),
          "maqueta-bolsa.jpg", gloss=0.15, shade=0.35, focus=F_BAG)

# 4 · Pan de jamón: etiqueta frontal de 80 × 60 mm, a 2 cm de la boca de la bolsa
front = load("etiqueta-pan-de-jamon.png")
c = np.array([1430, 248.0]); u = np.array([0.910, 0.414]); v = np.array([-0.414, 0.910])
px = 5.07  # px por mm en la foto
c = c + 20 * px * v
TL = c - 40 * px * u; TR = c + 40 * px * u
quad = [TL, TR, TR + 60 * px * v, TL + 60 * px * v]
composite(FOTOS / "pan-de-jamon.jpg", front, quad, "maqueta-pan-de-jamon.jpg", gloss=0.2,
          focus=F_PAN)

# 5 · Domo de la torta negra: la cinta pasa por encima siguiendo la curva del domo
import math


def dome_ribbon(photo_path, ribbon, out_name, crop):
    """Modelo 3D simple del domo (cilindro + media esfera) visto en proyección ortográfica,
    ajustado a la foto: aro de la base centrado en (1001, 1378) px, 8,3 px/mm, cámara a 43°."""
    photo = cv2.imread(str(photo_path), cv2.IMREAD_COLOR)
    Hh, Wh = photo.shape[:2]
    R, hc, S, phi = 50.0, 36.6, 8.3, math.radians(43)
    O = np.array([1001.0, 1378.0])
    cam = np.array([0, math.cos(phi), math.sin(phi)])
    light = np.array([-0.45, 0.45, 0.77]); light /= np.linalg.norm(light)
    al = math.radians(35)                     # la cinta cruza en diagonal y baja por el frente derecho
    u = np.array([math.cos(al), math.sin(al), 0.0]); n = np.array([-math.sin(al), math.cos(al), 0.0])
    arc = math.pi * R
    Lm = 2 * hc + arc

    def proj(p):
        return O + np.array([S * p[0], S * math.sin(phi) * p[1] - S * math.cos(phi) * p[2]])

    def center(s):
        if s < 0:                              # sobre la base, del lado izquierdo
            return -(R - s) * u
        if s < hc:
            return -R * u + np.array([0, 0, s])
        if s < hc + arc:
            th = math.pi - (s - hc) / R
            return R * math.cos(th) * u + np.array([0, 0, hc + R * math.sin(th)])
        if s < Lm:
            return R * u + np.array([0, 0, Lm - s])
        return (R + (s - Lm)) * u

    def surf(s, v):
        c = center(s) + v * n
        if s < 0 or s > Lm:                     # tramo pegado a la base: visible si su lado lo es
            side = -u if s < 0 else u
            return c, np.array([side[0], side[1], 0.0])
        if c[2] <= hc:
            xy = c[:2] / np.linalg.norm(c[:2])
            return np.array([xy[0] * R, xy[1] * R, c[2]]), np.array([xy[0], xy[1], 0.0])
        d = c - np.array([0, 0, hc]); d /= np.linalg.norm(d)
        return np.array([0, 0, hc]) + R * d, d

    rh, rw = ribbon.shape[:2]
    Wr = 25.0                                  # ancho de la cinta en mm; el largo sale del archivo
    Lr = Wr * rw / rh
    over = (Lr - Lm) / 2
    map_x = np.full((Hh, Wh), -1, np.float32)
    map_y = np.full((Hh, Wh), -1, np.float32)
    shade = np.ones((Hh, Wh), np.float32)
    NX, NY = 220, 6
    for i in range(NX):
        for j in range(NY):
            xs = [Lr * i / NX, Lr * (i + 1) / NX]
            ys = [Wr * j / NY, Wr * (j + 1) / NY]
            corners = [(xs[0], ys[0]), (xs[1], ys[0]), (xs[1], ys[1]), (xs[0], ys[1])]
            pts, nrms = [], []
            for x, y in corners:
                q, nr = surf(x - over, y - Wr / 2)
                pts.append(proj(q)); nrms.append(nr)
            nm = np.mean(nrms, axis=0)
            if nm @ cam <= 0.03:
                continue
            dst = np.float32(pts)
            src = np.float32([(x / Lr * rw, y / Wr * rh) for x, y in corners])
            Hinv = cv2.getPerspectiveTransform(dst, src)
            x0, y0 = np.floor(dst.min(0)).astype(int) - 1
            x1, y1 = np.ceil(dst.max(0)).astype(int) + 1
            x0, y0 = max(x0, 0), max(y0, 0); x1, y1 = min(x1, Wh - 1), min(y1, Hh - 1)
            if x1 <= x0 or y1 <= y0:
                continue
            mask = np.zeros((y1 - y0 + 1, x1 - x0 + 1), np.uint8)
            cv2.fillConvexPoly(mask, np.int32(np.round((dst - [x0, y0]) * 16)), 1, cv2.LINE_8, 4)
            yy, xx = np.nonzero(mask)
            if not len(xx):
                continue
            P = np.stack([xx + x0, yy + y0, np.ones_like(xx)], 0).astype(np.float64)
            Q = Hinv @ P
            map_x[yy + y0, xx + x0] = (Q[0] / Q[2]).astype(np.float32)
            map_y[yy + y0, xx + x0] = (Q[1] / Q[2]).astype(np.float32)
            shade[yy + y0, xx + x0] = 0.74 + 0.34 * max(0.0, float(nm @ light))
    warped = cv2.remap(ribbon, map_x, map_y, cv2.INTER_LINEAR,
                       borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0)).astype(np.float32) / 255
    rgb, a = warped[..., :3], warped[..., 3:4]
    shade = cv2.GaussianBlur(shade, (0, 0), 2)[..., None]
    rgb = rgb * shade
    L = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
    hl = np.clip((cv2.GaussianBlur(L, (0, 0), 3) - 0.82) / 0.18, 0, 1)[..., None] * 0.45
    rgb = rgb + (1 - rgb) * hl
    out = photo.astype(np.float32) / 255 * (1 - a) + np.clip(rgb, 0, 1) * a
    out = (out * 255).astype(np.uint8)
    finish(out, out_name, crop, 1600, F_DOME, glass=G_DOME, glass_cut=G_DOME_CUT, protect=a[..., 0])


# sello redondo Ø 50 mm en el tope del domo (visto en escorzo), con el domo tratado como plástico
composite(FOTOS / "domo-torta.jpg", load("sello-torta-negra.png"),
          [(800, 790), (1172, 790), (1188, 996), (784, 996)], "maqueta-torta-negra.jpg",
          gloss=0.5, crop=(300, 450, 1700, 1900), focus=F_DOME, glass=G_DOME, glass_cut=G_DOME_CUT)
