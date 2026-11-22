#!/usr/bin/env python3
"""Ajusta los PDF de impresión a la medida exacta y añade TrimBox/BleedBox.

Chromium redondea el tamaño de página a píxeles (~0,1 mm de más). Este paso
recorta la MediaBox a la medida exacta (corte + 3 mm de sangrado por lado) y
declara la TrimBox (línea de corte), que es lo que leen los RIP de imprenta.
"""
import json
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

ROOT = Path(__file__).resolve().parent
PT = 72 / 25.4
BLEED = 3.0

manifest = json.loads((ROOT / "_build" / "manifest.json").read_text())
for i, p in enumerate(manifest, 1):
    fn = ROOT.parent / "impresion" / f"{i:02d}-{p['id']}.pdf"
    r = PdfReader(fn)
    w = PdfWriter()
    W = (p["W"] + 2 * BLEED) * PT
    H = (p["H"] + 2 * BLEED) * PT
    for page in r.pages:
        top = float(page.mediabox.top)          # el contenido arranca arriba a la izquierda
        box = RectangleObject([0, top - H, W, top])
        trim = RectangleObject([BLEED * PT, top - H + BLEED * PT, W - BLEED * PT, top - BLEED * PT])
        page.mediabox = box
        page.cropbox = box
        page.bleedbox = box
        page.trimbox = trim
        w.add_page(page)
    w.add_metadata({"/Title": p["title"], "/Author": "BS Catering", "/Subject": "Kit Navideño"})
    with open(fn, "wb") as fh:
        w.write(fh)
    print("ok", fn.name, f"{p['W']}×{p['H']} mm + sangrado")
