#!/usr/bin/env python3
"""Archivos para la imprenta — Kit Navideño BS Catering «Navidad en casa» 2026.

Cada etiqueta sale en su propio PDF, a tamaño real: CMYK, textos en curvas, 3 mm de
sangrado y línea de corte en tinta plana «CutContour» (sobreimpresión). El nombre del
archivo lleva la medida y la cantidad a imprimir.

  ../etiquetas-imprenta/   las 8 etiquetas (lo que se envía a la imprenta)
  ../tarjeta-imprenta/     la tarjeta (frente y dorso, corte con guillotina)

Requiere haber corrido antes: build.py, render.js y pdf_boxes.py.
Uso: python3 fuente/imprenta.py
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402

from pypdf import PdfReader, PdfWriter  # noqa: E402
from pypdf.generic import RectangleObject  # noqa: E402
from reportlab.lib.colors import CMYKColorSep  # noqa: E402
from reportlab.pdfgen import canvas  # noqa: E402

ROOT = B.ROOT.parent
TMP = B.BUILD / "imprenta"
PT = 72 / 25.4

ASADO, PERNIL = 30, 30                   # kits con asado negro / con pernil (confirmado)
KITS = ASADO + PERNIL                    # 60 kits: el resto de piezas se imprime para 60

# Etiquetas que se mandan a hacer: nombre de archivo, medida y cantidad
ETIQUETAS = {                            # orden de la lista: las proteínas al final
    "etiqueta-hallacas": ("Hallacas", "130x80mm", KITS),
    "etiqueta-ensalada-de-gallina": ("Ensalada-de-Gallina", "90x56mm", KITS),
    "etiqueta-pan-de-jamon": ("Pan-de-Jamon", "80x60mm", KITS),
    "sello-torta-negra": ("Sello-Torta-Negra", "50mm", KITS),
    "sello-cierre": ("Sello-cierre", "30mm", KITS * 2),        # cierre del pan + solapa de la bolsa
    "sticker-bolsa": ("Sticker-bolsa", "100x140mm", KITS),
    "etiqueta-asado-negro": ("Asado-Negro", "90x56mm", ASADO),
    "etiqueta-pernil": ("Pernil", "90x56mm", PERNIL),
}
TARJETA = ("Tarjeta-frente-y-dorso", "100x150mm", KITS)

P = {p["id"]: p for p in B.PIECES}
NUM = {p["id"]: i for i, p in enumerate(B.PIECES, 1)}


# ───────────────────────── corte (CutContour) ─────────────────────────

def draw_shape(c, cut, W, H):
    kind = cut[0]
    if kind == "rrect":
        c.roundRect(0, 0, W, H, cut[1], stroke=1, fill=0)
    elif kind == "circle":
        c.circle(W / 2, H / 2, W / 2, stroke=1, fill=0)
    elif kind == "arch":
        rb, R = cut[1], W / 2
        p = c.beginPath()
        p.moveTo(0, R)
        p.arcTo(0, 0, W, 2 * R, startAng=180, extent=180)
        p.lineTo(W, H - rb)
        p.arcTo(W - 2 * rb, H - 2 * rb, W, H, startAng=0, extent=90)
        p.lineTo(rb, H)
        p.arcTo(0, H - 2 * rb, 2 * rb, H, startAng=90, extent=90)
        p.close()
        c.drawPath(p, stroke=1, fill=0)
    else:
        c.rect(0, 0, W, H, stroke=1, fill=0)


def cut_overlay(cut, W, H, page_w_pt, page_h_pt, path):
    """Trazo de corte en la línea de corte (3 mm adentro del borde con sangrado)."""
    c = canvas.Canvas(str(path), pagesize=(page_w_pt, page_h_pt))
    k = PT
    c.transform(k, 0, 0, -k, k * 3.0, page_h_pt - k * 3.0)    # origen = esquina de corte, y hacia abajo
    c.setStrokeColor(CMYKColorSep(0, 1, 0, 0, spotName="CutContour", density=1))
    c.setStrokeOverprint(1)
    c.setLineWidth(0.25 / k)
    draw_shape(c, cut, W, H)
    c.showPage()
    c.save()


def to_cmyk_curves(src, dst):
    subprocess.run(["gs", "-q", "-dBATCH", "-dNOPAUSE", "-dSAFER", "-sDEVICE=pdfwrite", "-dNoOutputFonts",
                    "-sColorConversionStrategy=CMYK", "-sProcessColorModel=DeviceCMYK",
                    "-dCompatibilityLevel=1.6", "-dAutoRotatePages=/None", "-o", str(dst), str(src)], check=True)


def finalize(piece, src, dst, with_cut=True):
    TMP.mkdir(parents=True, exist_ok=True)
    W, H = piece["W"], piece["H"]
    cm = TMP / (dst.stem + "-cmyk.pdf")
    to_cmyk_curves(src, cm)
    r = PdfReader(cm)
    w = PdfWriter()
    for i, page in enumerate(r.pages):
        top = float(page.mediabox.top)
        if with_cut:
            ov = TMP / f"{dst.stem}-corte.pdf"
            cut_overlay(tuple(piece["cut"]), W, H, float(page.mediabox.width), float(page.mediabox.height), ov)
            page.merge_page(PdfReader(ov).pages[0])
            res = page["/Resources"].get_object()
            if "/Font" in res:          # reportlab declara Helvetica aunque el corte no lleva texto
                del res["/Font"]
        box = RectangleObject([0, top - (H + 6) * PT, (W + 6) * PT, top])
        page.mediabox = page.cropbox = page.bleedbox = box
        page.trimbox = RectangleObject([3 * PT, top - (H + 3) * PT, (W + 3) * PT, top - 3 * PT])
        w.add_page(page)
    w.add_metadata({"/Title": piece["title"], "/Author": "BS Catering", "/Subject": "Kit Navideño 2026"})
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(dst, "wb") as fh:
        w.write(fh)


def main():
    d_et = ROOT / "etiquetas-imprenta"
    d_ta = ROOT / "tarjeta-imprenta"
    resumen = []
    for i, (pid, (nombre, medida, cant)) in enumerate(ETIQUETAS.items(), 1):
        p = P[pid]
        src = ROOT / "impresion" / f"{NUM[pid]:02d}-{pid}.pdf"
        dst = d_et / f"{i:02d}-{nombre}_{medida}_{cant}-unidades.pdf"
        finalize(p, src, dst)
        resumen.append(dict(n=i, id=pid, archivo=dst.name, W=p["W"], H=p["H"], cantidad=cant, cut=p["cut"]))
        print("etiqueta", dst.name)
    t = P["tarjeta"]
    nombre, medida, cant = TARJETA
    dst = d_ta / f"{nombre}_{medida}_{cant}-unidades.pdf"
    finalize(t, ROOT / "impresion" / f"{NUM['tarjeta']:02d}-tarjeta.pdf", dst, with_cut=False)
    print("tarjeta", dst.name)
    (TMP / "resumen.json").write_text(json.dumps(dict(etiquetas=resumen, kits=KITS), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
