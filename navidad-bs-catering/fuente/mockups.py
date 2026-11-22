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
          place_on_surface(lid, (160, 110), (25, 12, 135, 82)),
          "maqueta-envase-asado-negro.jpg", gloss=0.4, crop=(0, 560, 1932, 2000),
          ignore=[(735, 1250, 1065, 1440)])
composite(FOTOS / "envase-tapa.jpg", load("etiqueta-ensalada-de-gallina.png"),
          place_on_surface(lid, (160, 110), (25, 12, 135, 82)),
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

# 5 · Domo de la torta negra (etiqueta Ø 50 mm vista en escorzo)
composite(FOTOS / "domo-torta.jpg", load("etiqueta-torta-negra.png"),
          [(792, 786), (1180, 786), (1196, 1000), (776, 1000)],
          "maqueta-torta-negra.jpg", gloss=0.55, crop=(300, 450, 1700, 1900))
