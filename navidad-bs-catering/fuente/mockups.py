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


def composite(photo_path, label_rgba, quad, out_name, gloss=0.35, shade=0.55, crop=None,
              max_side=1600, ignore=None):
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
    if crop:
        x0, y0, x1, y1 = crop
        out = out[y0:y1, x0:x1]
    h, w = out.shape[:2]
    s = max_side / max(h, w)
    if s < 1:
        out = cv2.resize(out, (int(w * s), int(h * s)), interpolation=cv2.INTER_AREA)
    cv2.imwrite(str(OUT / out_name), out, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print("ok", out_name)


def load(name):
    return cv2.imread(str(PREV / name), cv2.IMREAD_UNCHANGED)


FOTOS = ROOT / "fotos"

# 1 · Tapa del envase (zona plana ≈ 160 × 110 mm)
lid = [(322, 889), (1546, 902), (1610, 1688), (168, 1700)]
composite(FOTOS / "envase-tapa.jpg", load("etiqueta-asado-negro.png"),
          place_on_surface(lid, (160, 110), (35, 21, 125, 77)),
          "maqueta-envase-asado-negro.jpg", gloss=0.4, crop=(0, 560, 1932, 2000),
          ignore=[(735, 1250, 1065, 1440)])
composite(FOTOS / "envase-tapa.jpg", load("etiqueta-ensalada-de-gallina.png"),
          place_on_surface(lid, (160, 110), (35, 21, 125, 77)),
          "maqueta-envase-ensalada-de-gallina.jpg", gloss=0.4, crop=(0, 560, 1932, 2000),
          ignore=[(735, 1250, 1065, 1440)])

# 2 · Bolsa de hallacas (bloque 2×2 ≈ 220 × 345 mm)
hall = [(451, 787), (1303, 761), (1393, 2141), (464, 2180)]
composite(FOTOS / "hallacas.jpg", load("etiqueta-hallacas.png"),
          place_on_surface(hall, (220, 345), (45, 132, 175, 212)),
          "maqueta-hallacas.jpg", gloss=0.5, crop=(0, 300, 1932, 2576))

# 3 · Bolsa esmerilada (cuerpo bajo la solapa ≈ 300 × 310 mm)
bag = [(193, 605), (1893, 567), (1687, 2009), (367, 2190)]
composite(FOTOS / "bolsa.jpg", load("sticker-bolsa.png"),
          place_on_surface(bag, (300, 310), (85, 48, 215, 238)),
          "maqueta-bolsa.jpg", gloss=0.15, shade=0.35)

# 4 · Pan de jamón: panel frontal de la etiqueta de cierre sobre la boca de la bolsa
pan = load("etiqueta-pan-de-jamon.png")
front = pan[pan.shape[0] // 2:, :]
c = np.array([1430, 248.0]); u = np.array([0.910, 0.414]); v = np.array([-0.414, 0.910])
px = 5.07  # px por mm en la foto
TL = c - 40 * px * u; TR = c + 40 * px * u
quad = [TL, TR, TR + 60 * px * v, TL + 60 * px * v]
composite(FOTOS / "pan-de-jamon.jpg", front, quad, "maqueta-pan-de-jamon.jpg", gloss=0.2)

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
    Lr, Wr = 240.0, 25.0                       # medidas de la cinta en mm
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
    x0, y0, x1, y1 = crop
    out = out[y0:y1, x0:x1]
    h, w = out.shape[:2]
    s = 1600 / max(h, w)
    if s < 1:
        out = cv2.resize(out, (int(w * s), int(h * s)), interpolation=cv2.INTER_AREA)
    cv2.imwrite(str(OUT / out_name), out, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print("ok", out_name)


dome_ribbon(FOTOS / "domo-torta.jpg", load("cinta-torta-negra.png"), "maqueta-torta-negra.jpg",
            crop=(300, 450, 1700, 1900))
