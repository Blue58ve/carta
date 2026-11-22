#!/usr/bin/env python3
"""Generador de piezas gráficas — Kit Navideño BS Catering.

Todas las medidas están en milímetros (1 unidad SVG = 1 mm).
Cambia los textos de la sección CONFIGURACIÓN y vuelve a ejecutar:

    python3 fuente/build.py && node fuente/render.js

Salida:
  fuente/svg/*.svg     piezas editables (fuentes incrustadas)
  fuente/_build/*.html páginas que render.js convierte en PDF/PNG
"""
import base64
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT_SVG = ROOT / "svg"
BUILD = ROOT / "_build"

# ───────────────────────── CONFIGURACIÓN ─────────────────────────
KIT = "Navidad en Casa"          # nombre del kit
ANIO = "2026"
ANIO_NUEVO = "2027"
INSTAGRAM = "@bscatering"        # ← CONFIRMAR usuario de Instagram

PRODUCTOS_ENVASE = [             # etiquetas para envases Safe-T-Fresh
    ("asado-negro", "Asado Negro"),
    ("ensalada-de-gallina", "Ensalada de Gallina"),
]

MENSAJE_TARJETA = [
    "Querida familia:",
    "La Navidad tiene un sabor que nos lleva a casa: el de las hallacas "
    "envueltas entre risas, el pan de jamón recién cortado y esa mesa "
    "donde siempre cabe uno más.",
    "Este año quisimos ser parte de la suya. Preparamos cada plato con el "
    "mismo cariño con el que cocinamos para los nuestros, para que ustedes "
    "solo se ocupen de lo más importante: abrazarse, compartir y celebrar juntos.",
    "Que esta Navidad llene su hogar de paz, su mesa de alegría y su "
    "corazón de gratitud.",
    f"¡Feliz Navidad y un próspero {ANIO_NUEVO}!",
]
FIRMA = ["Con cariño,", "la familia de BS Catering"]

# Paleta (RGB para pantalla; equivalentes CMYK/Pantone en LEEME.md)
NAVY = "#0F1C30"
NAVY_2 = "#182A45"
GOLD = "#C9A45C"
IVORY = "#F4EDE0"
INK = "#13213A"        # texto sobre marfil

BLEED = 3.0
# ─────────────────────────────────────────────────────────────────


def font_face_css():
    fonts = [
        ("Cormorant Garamond", 400, "normal", "CormorantGaramond-400.woff"),
        ("Cormorant Garamond", 500, "normal", "CormorantGaramond-500.woff"),
        ("Cormorant Garamond", 600, "normal", "CormorantGaramond-600.woff"),
        ("Cormorant Garamond", 400, "italic", "CormorantGaramond-400i.woff"),
        ("Cormorant Garamond", 500, "italic", "CormorantGaramond-500i.woff"),
        ("Cormorant Garamond", 600, "italic", "CormorantGaramond-600i.woff"),
        ("Josefin Sans", 300, "normal", "JosefinSans-300.woff"),
        ("Josefin Sans", 400, "normal", "JosefinSans-400.woff"),
        ("Josefin Sans", 600, "normal", "JosefinSans-600.woff"),
        ("Pinyon Script", 400, "normal", "PinyonScript-400.woff"),
    ]
    css = []
    for fam, w, st, f in fonts:
        b64 = base64.b64encode((ROOT / "fuentes" / f).read_bytes()).decode()
        css.append(
            f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};"
            f"src:url(data:font/woff;base64,{b64}) format('woff');}}"
        )
    return "\n".join(css)


FONT_CSS = font_face_css()
TEXT_CSS = """
.serif{font-family:'Cormorant Garamond',serif}
.sans{font-family:'Josefin Sans',sans-serif}
.script{font-family:'Pinyon Script',cursive}
"""


def logo_symbols():
    """Símbolos del logo vectorizado (sin color: heredan fill del <use>)."""
    out = []
    for sid, fname in [("logo", "bs-catering-logo-negro.svg"),
                       ("mono", "bs-catering-monograma-negro.svg"),
                       ("word", "bs-catering-wordmark-negro.svg")]:
        s = (ROOT / "logo" / fname).read_text()
        vb = re.search(r'viewBox="([^"]+)"', s).group(1)
        body = re.search(r'<g fill="#000000">(.*)</g></svg>', s, re.S).group(1)
        out.append(f'<symbol id="{sid}" viewBox="{vb}">{body}</symbol>')
    return "\n".join(out)


SYMBOLS = logo_symbols()
LOGO_AR = 2805.865348 / 2626.484787     # ancho/alto logo completo
MONO_AR = 2805.865348 / 2186.625460


def f(v):
    return f"{v:.3f}".rstrip("0").rstrip(".")


# ───────────────────────── PRIMITIVAS ─────────────────────────

def logo(cx, y, h, color=GOLD, kind="logo"):
    ar = LOGO_AR if kind == "logo" else MONO_AR
    w = h * ar
    return (f'<use href="#{kind}" x="{f(cx - w / 2)}" y="{f(y)}" '
            f'width="{f(w)}" height="{f(h)}" fill="{color}"/>')


def text(x, y, s, size, cls="serif", color=IVORY, weight=400, italic=False,
         ls=0.0, anchor="middle", opacity=1.0, extra=""):
    # el letter-spacing añade espacio al final: se compensa al centrar
    dx = ls / 2 if (anchor == "middle" and ls) else 0
    st = ' font-style="italic"' if italic else ""
    op = f' opacity="{opacity}"' if opacity != 1 else ""
    lsa = f' letter-spacing="{f(ls)}"' if ls else ""
    return (f'<text x="{f(x + dx)}" y="{f(y)}" class="{cls}" font-size="{f(size)}" '
            f'font-weight="{weight}"{st}{lsa} text-anchor="{anchor}" fill="{color}"'
            f'{op} {extra}>{s}</text>')


def sparkle(cx, cy, s, color=GOLD, k=0.13):
    p = (f"M{f(cx)},{f(cy - s)} Q{f(cx + k*s)},{f(cy - k*s)} {f(cx + s)},{f(cy)} "
         f"Q{f(cx + k*s)},{f(cy + k*s)} {f(cx)},{f(cy + s)} "
         f"Q{f(cx - k*s)},{f(cy + k*s)} {f(cx - s)},{f(cy)} "
         f"Q{f(cx - k*s)},{f(cy - k*s)} {f(cx)},{f(cy - s)}Z")
    return f'<path d="{p}" fill="{color}"/>'


def sparkle_cluster(cx, cy, s, color=GOLD):
    return (sparkle(cx, cy, s, color)
            + sparkle(cx - s * 1.45, cy + s * 0.55, s * 0.42, color)
            + sparkle(cx + s * 1.35, cy - s * 0.5, s * 0.32, color)
            + f'<circle cx="{f(cx + s*1.1)}" cy="{f(cy + s*0.85)}" r="{f(s*0.07)}" fill="{color}"/>'
            + f'<circle cx="{f(cx - s*1.0)}" cy="{f(cy - s*0.8)}" r="{f(s*0.06)}" fill="{color}"/>')


def divider(cx, cy, half, color=GOLD, star=1.5, gap=3.2, sw=0.2):
    return (f'<g stroke="{color}" stroke-width="{sw}" stroke-linecap="round">'
            f'<line x1="{f(cx - half)}" y1="{f(cy)}" x2="{f(cx - gap)}" y2="{f(cy)}"/>'
            f'<line x1="{f(cx + gap)}" y1="{f(cy)}" x2="{f(cx + half)}" y2="{f(cy)}"/></g>'
            f'<circle cx="{f(cx - half - 1.1)}" cy="{f(cy)}" r="{f(sw*1.1)}" fill="{color}"/>'
            f'<circle cx="{f(cx + half + 1.1)}" cy="{f(cy)}" r="{f(sw*1.1)}" fill="{color}"/>'
            + sparkle(cx, cy, star, color))


def sprig(x, y, length, angle, mirror=False, color=GOLD, sw=0.2, berries=True):
    """Ramita de pino de línea fina. (x,y)=base; angle en grados (0 = hacia arriba)."""
    L = length
    bend = L * 0.10
    pts = []
    n = 40
    for i in range(n + 1):
        t = i / n
        # curva cuadrática: base (0,0) → control (bend, -L/2) → punta (0,-L)
        px = 2 * (1 - t) * t * bend
        py = -L * t
        pts.append((px, py))
    stem = "M" + " L".join(f"{f(a)},{f(b)}" for a, b in pts)
    needles = []
    steps = 9
    for i in range(1, steps + 1):
        t = 0.12 + 0.82 * (i - 1) / (steps - 1)
        px = 2 * (1 - t) * t * bend
        py = -L * t
        dlen = L * (0.20 - 0.11 * t)
        for side in (-1, 1):
            ang = math.radians(38) * side
            ex = px + math.sin(ang) * dlen
            ey = py - math.cos(ang) * dlen
            needles.append(f"M{f(px)},{f(py)} L{f(ex)},{f(ey)}")
    sx = -1 if mirror else 1
    g = (f'<g transform="translate({f(x)},{f(y)}) rotate({f(angle)}) scale({sx},1)">'
         f'<path d="{stem} {" ".join(needles)}" fill="none" stroke="{color}" '
         f'stroke-width="{sw}" stroke-linecap="round"/>')
    if berries:
        r = L * 0.035
        for bx, by in [(-L*0.07, -L*0.02), (L*0.06, L*0.035), (-L*0.005, L*0.075)]:
            g += f'<circle cx="{f(bx)}" cy="{f(by)}" r="{f(r)}" fill="{color}"/>'
    return g + "</g>"


def rrect_path(x, y, w, h, r):
    return (f"M{f(x + r)},{f(y)} H{f(x + w - r)} A{f(r)},{f(r)} 0 0 1 {f(x + w)},{f(y + r)} "
            f"V{f(y + h - r)} A{f(r)},{f(r)} 0 0 1 {f(x + w - r)},{f(y + h)} "
            f"H{f(x + r)} A{f(r)},{f(r)} 0 0 1 {f(x)},{f(y + h - r)} "
            f"V{f(y + r)} A{f(r)},{f(r)} 0 0 1 {f(x + r)},{f(y)}Z")


def arch_path(x, y, w, h, rb):
    R = w / 2
    return (f"M{f(x)},{f(y + R)} A{f(R)},{f(R)} 0 0 1 {f(x + w)},{f(y + R)} "
            f"V{f(y + h - rb)} A{f(rb)},{f(rb)} 0 0 1 {f(x + w - rb)},{f(y + h)} "
            f"H{f(x + rb)} A{f(rb)},{f(rb)} 0 0 1 {f(x)},{f(y + h - rb)} Z")


def circle_path(cx, cy, r):
    return (f"M{f(cx - r)},{f(cy)} A{f(r)},{f(r)} 0 1 1 {f(cx + r)},{f(cy)} "
            f"A{f(r)},{f(r)} 0 1 1 {f(cx - r)},{f(cy)}Z")


def stroke_path(d, w, color=GOLD, extra=""):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{f(w)}" {extra}/>'


def double_frame_rrect(W, H, r, i1=3.0, i2=4.1, color=GOLD):
    return (stroke_path(rrect_path(i1, i1, W - 2*i1, H - 2*i1, max(r - i1 + 1.2, 0.8)), 0.32, color)
            + stroke_path(rrect_path(i2, i2, W - 2*i2, H - 2*i2, max(r - i2 + 1.2, 0.6)), 0.16, color))


def instagram(cx, y, size, color=GOLD, handle=INSTAGRAM, ls=0.35):
    """Ícono + usuario, centrado en cx (y = línea base)."""
    s = size * 1.05
    approx_w = len(handle) * size * 0.56 + s + size * 0.6
    x0 = cx - approx_w / 2
    icon_y = y - s * 0.86
    ico = (f'<g fill="none" stroke="{color}" stroke-width="{f(size*0.085)}">'
           f'<rect x="{f(x0)}" y="{f(icon_y)}" width="{f(s)}" height="{f(s)}" rx="{f(s*0.28)}"/>'
           f'<circle cx="{f(x0 + s/2)}" cy="{f(icon_y + s/2)}" r="{f(s*0.23)}"/></g>'
           f'<circle cx="{f(x0 + s*0.77)}" cy="{f(icon_y + s*0.23)}" r="{f(s*0.055)}" fill="{color}"/>')
    return ico + text(x0 + s + size * 0.6, y, handle, size, "sans", color, 300, ls=ls, anchor="start")


def arc_text(cx, cy, r, s, size, top=True, color=GOLD, ls=0.5, weight=400, pid="arc"):
    if top:
        d = f"M{f(cx - r)},{f(cy)} A{f(r)},{f(r)} 0 0 1 {f(cx + r)},{f(cy)}"
    else:
        d = f"M{f(cx - r)},{f(cy)} A{f(r)},{f(r)} 0 0 0 {f(cx + r)},{f(cy)}"
    return (f'<path id="{pid}" d="{d}" fill="none"/>'
            f'<text class="sans" font-size="{f(size)}" font-weight="{weight}" fill="{color}" '
            f'letter-spacing="{f(ls)}" text-anchor="middle">'
            f'<textPath href="#{pid}" startOffset="50%">{s}</textPath></text>')


def bg(W, H, color=NAVY):
    return (f'<rect x="{-BLEED}" y="{-BLEED}" width="{f(W + 2*BLEED)}" '
            f'height="{f(H + 2*BLEED)}" fill="{color}"/>')


def subtle_stars(W, H, seed=7, n=12, color=GOLD, opacity=0.85, avoid=None, inset=7.0):
    """Destellos dorados pequeños y dispersos (textura navideña).
    Se colocan dentro del marco interior y lejos del contenido (cajas `avoid`)."""
    import random
    rnd = random.Random(seed)
    out, placed = [], []
    tries = 0
    while len(out) < n and tries < 4000:
        tries += 1
        x, y = rnd.uniform(inset, W - inset), rnd.uniform(inset, H - inset)
        if avoid and any(ax0 <= x <= ax1 and ay0 <= y <= ay1 for ax0, ay0, ax1, ay1 in avoid):
            continue
        if any((x - px) ** 2 + (y - py) ** 2 < 49 for px, py in placed):
            continue
        placed.append((x, y))
        if rnd.random() < 0.3:
            out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="0.22" fill="{color}"/>')
        else:
            out.append(sparkle(x, y, rnd.uniform(0.45, 1.0), color))
    return f'<g opacity="{opacity}">{"".join(out)}</g>'


# ───────────────────────── PIEZAS ─────────────────────────
PIECES = []


def add_piece(pid, title, W, H, shape, art, material, notes, fold=None, pages=None,
              safe=3.0, preview_bg=None):
    PIECES.append(dict(id=pid, title=title, W=W, H=H, shape=shape, art=art,
                       material=material, notes=notes, fold=fold, pages=pages,
                       safe=safe))


def envase_label(name):
    W, H, r = 110.0, 70.0, 4.0
    cx = W / 2
    size = 10.5 if len(name) <= 12 else 8.8
    a = [bg(W, H), subtle_stars(W, H, seed=len(name) + 2, n=10, avoid=[(22, 5, 88, 65)]),
         double_frame_rrect(W, H, r)]
    # logo enmarcado por ramitas
    a.append(logo(cx, 8.2, 17.5))
    a.append(sprig(cx - 13.5, 24.8, 13, -62, mirror=True))
    a.append(sprig(cx + 13.5, 24.8, 13, 62))
    a.append(text(cx, 39.6, name, size, "serif", IVORY, 500, italic=True))
    a.append(divider(cx, 45.2, 17))
    a.append(text(cx, 52.0, f"{KIT.upper()} · {ANIO}", 2.55, "sans", GOLD, 300, ls=0.95))
    a.append(instagram(cx, 61.2, 2.05, GOLD))
    return W, H, rrect_path(0, 0, W, H, r), "".join(a)


for pid, name in PRODUCTOS_ENVASE:
    W, H, shape, art = envase_label(name)
    add_piece(f"etiqueta-{pid}", f"Etiqueta envase · {name}", W, H, shape, art,
              "Vinil autoadhesivo blanco, impresión full color, laminado mate. Troquel rectangular con esquinas redondeadas (r = 4 mm).",
              "Va centrada sobre la zona plana de la tapa del envase Safe-T-Fresh, un poco hacia la bisagra para no tocar la pestaña frontal.")


def hallacas_label():
    W, H, r = 130.0, 80.0, 4.0
    cx = W / 2
    a = [bg(W, H), subtle_stars(W, H, seed=4, n=12, avoid=[(26, 5, 104, 75)]),
         double_frame_rrect(W, H, r)]
    a.append(logo(cx, 8.0, 20.5))
    a.append(text(cx, 46.0, "Hallacas", 15.5, "serif", IVORY, 500, italic=True))
    a.append(sprig(cx - 31, 44.5, 17, -70, mirror=True))
    a.append(sprig(cx + 31, 44.5, 17, 70))
    a.append(divider(cx, 52.4, 21))
    a.append(text(cx, 60.0, f"{KIT.upper()} · {ANIO}", 2.9, "sans", GOLD, 300, ls=1.1))
    a.append(instagram(cx, 70.0, 2.3, GOLD))
    return W, H, rrect_path(0, 0, W, H, r), "".join(a)


W, H, shape, art = hallacas_label()
add_piece("etiqueta-hallacas", "Etiqueta bolsa de hallacas", W, H, shape, art,
          "Vinil autoadhesivo blanco, impresión full color, laminado mate. Troquel rectangular con esquinas redondeadas (r = 4 mm).",
          "Va en el centro del frente de la bolsa al vacío, sobre el cruce de las 4 hallacas. Pegar presionando del centro hacia afuera para que copie el relieve del pabilo.")


def pan_label():
    """Etiqueta de cierre que se dobla sobre la boca de la bolsa kraft."""
    W, H, r = 80.0, 120.0, 4.0
    P = H / 2              # alto de cada panel
    cx = W / 2

    def panel_frame(y0):
        return (stroke_path(rrect_path(3, y0 + 3, W - 6, P - 6, 2.2), 0.32)
                + stroke_path(rrect_path(4.1, y0 + 4.1, W - 8.2, P - 8.2, 1.4), 0.16))

    front = [panel_frame(P),
             logo(cx, P + 7.5, 16.5),
             sprig(cx - 13.0, P + 23.6, 11.5, -62, mirror=True),
             sprig(cx + 13.0, P + 23.6, 11.5, 62),
             text(cx, P + 36.4, "Pan de Jamón", 8.6, "serif", IVORY, 500, italic=True),
             divider(cx, P + 41.6, 13),
             text(cx, P + 48.2, f"{KIT.upper()} · {ANIO}", 2.3, "sans", GOLD, 300, ls=0.8)]
    # panel trasero: se diseña derecho y se gira 180° (queda legible al doblar)
    back_inner = [panel_frame(0),
                  sparkle_cluster(cx, 13.5, 3.2),
                  text(cx, 30.5, "Feliz Navidad", 9.6, "script", IVORY, 400),
                  divider(cx, 37.0, 12),
                  logo(cx, 40.6, 7.0, kind="mono"),
                  instagram(cx, 54.0, 2.1, GOLD)]
    back = f'<g transform="rotate(180 {f(cx)} {f(P / 2)})">{"".join(back_inner)}</g>'
    a = [bg(W, H), subtle_stars(W, H, seed=11, n=0),
         back, "".join(front)]
    return W, H, rrect_path(0, 0, W, H, r), "".join(a), P


W, H, shape, art, P = pan_label()
add_piece("etiqueta-pan-de-jamon", "Etiqueta de cierre · Pan de Jamón", W, H, shape, art,
          "Vinil autoadhesivo blanco, impresión full color, laminado mate. Troquel rectangular con esquinas redondeadas (r = 4 mm).",
          "Cierra la bolsa kraft y reemplaza la cinta adhesiva. Doblar la boca de la bolsa 2 cm, pegar la mitad inferior (Pan de Jamón) en el frente con la línea de doblez justo en el borde, y doblar la mitad superior hacia atrás. El texto trasero queda derecho al voltear la bolsa.",
          fold=P)


def round_label(D, pid, center_art, top_txt, bottom_txt, size=2.15, ls=0.55):
    R = D / 2
    c = R
    a = [bg(D, D),
         f'<circle cx="{f(c)}" cy="{f(c)}" r="{f(R - 2.4)}" fill="none" stroke="{GOLD}" stroke-width="0.32"/>',
         f'<circle cx="{f(c)}" cy="{f(c)}" r="{f(R - 3.4)}" fill="none" stroke="{GOLD}" stroke-width="0.16"/>',
         arc_text(c, c, R - 6.5, top_txt, size, True, GOLD, ls, 400, pid + "-t"),
         arc_text(c, c, R - 4.9, bottom_txt, size, False, GOLD, ls, 400, pid + "-b"),
         sparkle(c - (R - 5.7), c, 0.75), sparkle(c + (R - 5.7), c, 0.75),
         center_art]
    return "".join(a), circle_path(c, c, R)


def torta_label():
    D = 50.0
    c = D / 2
    center = (logo(c, 12.2, 10.5, kind="mono")
              + text(c, 31.0, "Torta Negra", 6.4, "serif", IVORY, 500, italic=True)
              + divider(c, 34.6, 6.2, star=0.9, gap=2.0, sw=0.16))
    art, shape = round_label(D, "torta", center, "OBSEQUIO DE LA CASA", f"NAVIDAD {ANIO}", 2.05, 0.6)
    return D, D, shape, art


W, H, shape, art = torta_label()
add_piece("etiqueta-torta-negra", "Etiqueta redonda · Mini Torta Negra (obsequio)", W, H, shape, art,
          "Vinil autoadhesivo blanco, impresión full color, laminado mate. Troquel circular Ø 50 mm.",
          "Va en el tope del domo. Si el domo es muy curvo, se puede bajar a Ø 45 mm sin cambiar el diseño (se escala).")


def sello_label():
    D = 40.0
    c = D / 2
    center = logo(c, 11.4, 13.0, kind="logo")
    art, shape = round_label(D, "sello", center, "FELIZ NAVIDAD", f"EDICIÓN {ANIO}", 1.85, 0.6)
    return D, D, shape, art


W, H, shape, art = sello_label()
add_piece("sello-cierre", "Sello redondo de cierre (opcional)", W, H, shape, art,
          "Vinil autoadhesivo blanco, impresión full color, laminado mate. Troquel circular Ø 40 mm.",
          "Para cerrar la solapa de la bolsa o el sobre de la tarjeta. Pieza opcional.")


def bolsa_sticker():
    W, H, rb = 130.0, 190.0, 6.0
    cx = W / 2

    def arch_frame(i, sw):
        return stroke_path(arch_path(i, i, W - 2*i, H - 2*i, max(rb - i + 1.5, 1)), sw)

    a = [bg(W, H),
         subtle_stars(W, H, seed=9, n=16, inset=9,
                      avoid=[(22, 8, 108, 180), (0, 0, 130, 40)]),
         arch_frame(3.2, 0.36), arch_frame(4.6, 0.18),
         sparkle_cluster(cx, 17.0, 4.2),
         logo(cx, 27.0, 46.0),
         sprig(cx - 29.5, 70.5, 21, -64, mirror=True, sw=0.25),
         sprig(cx + 29.5, 70.5, 21, 64, sw=0.25),
         text(cx, 96.5, KIT, 13.2, "serif", IVORY, 500, italic=True),
         divider(cx, 104.0, 30, star=2.0, gap=4.2, sw=0.24),
         text(cx, 112.6, f"EDICIÓN ESPECIAL · {ANIO}", 3.15, "sans", GOLD, 300, ls=1.35),
         # menú del kit
         text(cx, 128.5, "Hallacas · Asado Negro", 5.6, "serif", IVORY, 400, italic=True),
         text(cx, 136.8, "Ensalada de Gallina · Pan de Jamón", 5.6, "serif", IVORY, 400, italic=True),
         text(cx, 146.6, "Y UN DULCE OBSEQUIO: TORTA NEGRA", 2.5, "sans", GOLD, 300, ls=0.9),
         divider(cx, 158.0, 9, star=1.2, gap=2.6, sw=0.18),
         instagram(cx, 172.0, 3.0, GOLD)]
    return W, H, arch_path(0, 0, W, H, rb), "".join(a)


W, H, shape, art = bolsa_sticker()
add_piece("sticker-bolsa", "Sticker principal de la bolsa", W, H, shape, art,
          "Vinil autoadhesivo blanco, impresión full color, laminado mate. Troquel en forma de arco (medio punto arriba, esquinas inferiores r = 6 mm).",
          "Va centrado en el frente de la bolsa esmerilada, debajo de la solapa del asa. Sobre el esmerilado el azul noche resalta y el contenido se intuye alrededor.")


def tarjeta():
    W, H = 100.0, 150.0
    cx = W / 2

    def frame(color, i1=5.0, i2=6.3):
        return (stroke_path(rrect_path(i1, i1, W - 2*i1, H - 2*i1, 1.2), 0.36, color)
                + stroke_path(rrect_path(i2, i2, W - 2*i2, H - 2*i2, 0.6), 0.18, color))

    front = "".join([
        bg(W, H),
        subtle_stars(W, H, seed=23, n=14, inset=9, avoid=[(17, 14, 83, 141)]),
        frame(GOLD),
        sparkle_cluster(cx, 24.0, 4.0),
        text(cx - 7, 58.0, "Feliz", 19.5, "script", IVORY, 400),
        text(cx + 2.5, 79.0, "Navidad", 19.5, "script", IVORY, 400),
        divider(cx, 92.0, 22, star=1.8, gap=3.8, sw=0.22),
        logo(cx, 101.0, 25.0),
        text(cx, 136.0, f"{KIT.upper()} · {ANIO}", 2.6, "sans", GOLD, 300, ls=1.0),
    ])
    paras = "".join(f"<p>{p}</p>" for p in MENSAJE_TARJETA)
    back_svg = "".join([
        bg(W, H, IVORY),
        frame(GOLD),
        sparkle_cluster(cx, 16.5, 2.6),
        logo(cx, 121.5, 9.0, color=GOLD, kind="mono"),
        instagram(cx, 137.0, 2.15, "#9C7A3C"),
    ])
    back_html = f"""
<div class="msg">
  {paras}
  <p class="firma">{FIRMA[0]}<br><span>{FIRMA[1]}</span></p>
</div>"""
    return W, H, front, back_svg, back_html


W, H, front, back_svg, back_html = tarjeta()
add_piece("tarjeta", "Tarjeta de mensaje (frente y dorso)", W, H, rrect_path(0, 0, W, H, 0),
          None, "Cartulina de 300–350 g (opalina o hilo), impresión full color a dos caras. Ideal: dorado en hot stamping en el frente. Corte recto.",
          "Va dentro de la bolsa, apoyada sobre los envases. Si se usa sobre, cerrarlo con el sello redondo.",
          pages=[("frente", front, ""), ("dorso", back_svg, back_html)], safe=6.0)


# ───────────────────────── SALIDA ─────────────────────────

CARD_CSS = f"""
.msg{{position:absolute;left:{BLEED + 12}mm;right:{BLEED + 12}mm;top:{BLEED + 24}mm;
  font-family:'Cormorant Garamond',serif;font-size:3.5mm;line-height:1.45;color:{INK};
  text-align:center;font-weight:500;}}
.msg p{{margin:0 0 2.3mm 0;}}
.msg p:first-child{{font-style:italic;font-size:3.9mm;margin-bottom:2.6mm;color:#9C7A3C;}}
.msg p:nth-last-child(2){{font-style:italic;font-weight:600;margin-top:3.2mm;}}
.msg .firma{{font-style:italic;margin-top:3.6mm;}}
.msg .firma span{{font-family:'Pinyon Script',cursive;font-style:normal;font-size:5.6mm;
  line-height:1.3;color:#9C7A3C;}}
"""


def svg_doc(W, H, inner, mode="print", shape=None, pid="x", fold=None, safe=3.0):
    """mode: print (con sangrado) | preview (recortado a la forma) | guide (con guías)."""
    if mode == "preview":
        vb = f"0 0 {f(W)} {f(H)}"
        body = (f'<clipPath id="cut-{pid}"><path d="{shape}"/></clipPath>'
                f'<g clip-path="url(#cut-{pid})">{inner}</g>')
        w, h = W, H
    elif mode == "guide":
        m = 14.0
        vb = f"{-m} {-m} {f(W + 2*m)} {f(H + 2*m + 6)}"
        w, h = W + 2*m, H + 2*m + 6
        body = (f'<rect x="{-m}" y="{-m}" width="{f(W + 2*m)}" height="{f(H + 2*m + 6)}" fill="#ffffff"/>'
                f'<g>{inner}</g>'
                f'<rect x="{-BLEED}" y="{-BLEED}" width="{f(W + 2*BLEED)}" height="{f(H + 2*BLEED)}" '
                f'fill="none" stroke="#00A3E0" stroke-width="0.2"/>'
                f'<path d="{shape}" fill="none" stroke="#FF00FF" stroke-width="0.35"/>')
        if safe:
            body += (f'<rect x="{f(safe)}" y="{f(safe)}" width="{f(W - 2*safe)}" height="{f(H - 2*safe)}" '
                     f'fill="none" stroke="#00C853" stroke-width="0.18" stroke-dasharray="1.2 0.8"/>')
        if fold is not None:
            body += (f'<line x1="-6" y1="{f(fold)}" x2="{f(W + 6)}" y2="{f(fold)}" stroke="#FF00FF" '
                     f'stroke-width="0.25" stroke-dasharray="2 1.2"/>'
                     f'<text x="{f(W + 7)}" y="{f(fold + 1)}" class="sans" font-size="2.6" fill="#FF00FF">doblez</text>')
        body += (f'<text x="{f(W/2)}" y="{f(H + m - 3)}" class="sans" font-size="3.2" fill="#333" '
                 f'text-anchor="middle">{f(W)} × {f(H)} mm (corte) · sangrado 3 mm</text>'
                 f'<text x="{f(W/2)}" y="{f(H + m + 2.5)}" class="sans" font-size="2.4" fill="#666" '
                 f'text-anchor="middle">magenta = línea de corte · azul = sangrado · verde = zona segura</text>')
    else:
        vb = f"{-BLEED} {-BLEED} {f(W + 2*BLEED)} {f(H + 2*BLEED)}"
        w, h = W + 2*BLEED, H + 2*BLEED
        body = inner
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{f(w)}mm" height="{f(h)}mm" viewBox="{vb}">'
            f'<defs><style>{TEXT_CSS}</style>{SYMBOLS}</defs>{body}</svg>'), w, h


def html_page(pages, css_extra=""):
    """pages: lista de (svg, w_mm, h_mm, overlay_html)."""
    W0, H0 = pages[0][1], pages[0][2]
    divs = []
    for svg, w, h, overlay in pages:
        divs.append(f'<div class="pg" style="width:{f(w)}mm;height:{f(h)}mm">{svg}{overlay}</div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{FONT_CSS}
{TEXT_CSS}
@page{{size:{f(W0)}mm {f(H0)}mm;margin:0}}
html,body{{margin:0;padding:0;background:transparent}}
.pg{{position:relative;overflow:hidden;page-break-after:always;break-after:page}}
.pg:last-child{{page-break-after:auto;break-after:auto}}
.pg>svg{{display:block;position:absolute;left:0;top:0}}
{css_extra}
</style></head><body>{''.join(divs)}</body></html>"""


def build():
    OUT_SVG.mkdir(exist_ok=True)
    BUILD.mkdir(exist_ok=True)
    manifest = []
    for p in PIECES:
        pid, W, H = p["id"], p["W"], p["H"]
        pages = p["pages"] or [("", p["art"], "")]
        jobs = {}
        for mode in ("print", "preview", "guide"):
            html_pages = []
            for suffix, inner, overlay in pages:
                svg, w, h = svg_doc(W, H, inner, mode, p["shape"], f"{pid}{suffix}", p["fold"], p["safe"])
                ov = ""
                if overlay:
                    if mode == "print":
                        ov = overlay
                    elif mode == "preview":
                        ov = overlay.replace('class="msg"', 'class="msg" style="left:12mm;right:12mm;top:24mm"')
                    else:
                        ov = overlay.replace('class="msg"', 'class="msg" style="left:26mm;right:26mm;top:38mm"')
                html_pages.append((svg, w, h, ov))
                if mode == "print":
                    name = pid + (f"-{suffix}" if suffix else "")
                    std = svg.replace("<style>", f"<style>{FONT_CSS}", 1)
                    (OUT_SVG / f"{name}.svg").write_text(std)
            if mode == "preview" and len(html_pages) > 1:
                for i, (suffix, _, _) in enumerate(pages):
                    fn = BUILD / f"{pid}-{suffix}_preview.html"
                    fn.write_text(html_page([html_pages[i]], CARD_CSS))
                    jobs[f"preview-{suffix}"] = dict(html=str(fn), w=html_pages[i][1], h=html_pages[i][2])
            else:
                fn = BUILD / f"{pid}_{mode}.html"
                fn.write_text(html_page(html_pages, CARD_CSS))
                jobs[mode] = dict(html=str(fn), w=html_pages[0][1], h=html_pages[0][2],
                                  pages=len(html_pages))
        # contorno de corte
        cut = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(W)}mm" height="{f(H)}mm" '
               f'viewBox="0 0 {f(W)} {f(H)}"><path id="CutContour" d="{p["shape"]}" fill="none" '
               f'stroke="#FF00FF" stroke-width="0.25"/></svg>')
        (OUT_SVG / f"{pid}-corte.svg").write_text(cut)
        manifest.append(dict(id=pid, title=p["title"], W=W, H=H, material=p["material"],
                             notes=p["notes"], jobs=jobs,
                             sides=[s for s, _, _ in pages] if p["pages"] else None))
    (BUILD / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    print(f"{len(manifest)} piezas generadas")


if __name__ == "__main__":
    build()
