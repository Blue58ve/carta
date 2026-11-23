#!/usr/bin/env python3
"""Paquete para la imprenta — Kit Navideño BS Catering «Navidad en casa» 2026.

Genera en ../imprenta/:
  03-PIEZAS-INDIVIDUALES/  cada pieza en PDF: CMYK, textos en curvas, 3 mm de sangrado,
                           línea de corte en tinta plana «CutContour» (sobreimpresión)
  02-PRODUCCION/           pliegos montados de 33 × 48 cm para el tiraje (~50 kits + 10 %)
  01-PRUEBA/               pliego de prueba (todas las piezas + cinta en 3 largos)
  04-REFERENCIA/           vistas previas de los pliegos y guías con medidas
  00-ORDEN-DE-IMPRESION.pdf

Requiere haber corrido antes: build.py, render.js y pdf_boxes.py.
Uso: python3 fuente/imprenta.py
"""
import json
import math
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
OUT = ROOT / "imprenta"
TMP = B.BUILD / "imprenta"
PT = 72 / 25.4

SHEET_W, SHEET_H = 330.0, 480.0          # pliego 33 × 48 cm (13 × 19 in)
MARGIN = 15.0                            # margen libre (pinzas, marcas del plotter)
GAP = 6.0                                # separación entre cortes (los sangrados se tocan)
ASADO, PERNIL = 30, 30                   # kits con asado negro / con pernil (confirmado)
KITS = ASADO + PERNIL                    # 60 kits: el resto de piezas se imprime para 60 o más
META = KITS

P = {p["id"]: p for p in B.PIECES}
NUM = {p["id"]: i for i, p in enumerate(B.PIECES, 1)}


def variante_cinta(largo):
    W, H, shape, art = B.torta_cinta(largo)
    return dict(id=f"cinta-{int(largo)}", W=W, H=H, shape=shape, art=art, cut=("ribbon", 7.0),
                fold=None, safe=3.0, pages=None, title=f"Cinta {int(largo)} mm")


# ───────────────────────── montaje ─────────────────────────

def grid(piece, cols, rows, x0, y0, rot=0, gap=GAP):
    W, H = piece["W"], piece["H"]
    fw, fh = (H, W) if rot else (W, H)
    return [dict(piece=piece, x=x0 + c * (fw + gap), y=y0 + r * (fh + gap), rot=rot)
            for r in range(rows) for c in range(cols)]


def centered_x(total):
    return MARGIN + (SHEET_W - 2 * MARGIN - total) / 2


def centered_y(total):
    return MARGIN + (SHEET_H - 2 * MARGIN - total) / 2


def span(n, size, gap=GAP):
    return n * size + (n - 1) * gap


def sheet_production():
    sheets = []
    # A · envases: 5 Asado + 5 Pernil + 11 Ensalada por pliego  ×6  →  30 · 30 · 66
    asado, pernil, ens = P["etiqueta-asado-negro"], P["etiqueta-pernil"], P["etiqueta-ensalada-de-gallina"]
    x0, y0 = centered_x(span(3, 90)), centered_y(span(7, 56))
    pl = []
    for r in range(7):
        fila = [asado, pernil, ens] if r < 5 else [ens, ens, ens]
        for c, piece in enumerate(fila):
            pl.append(dict(piece=piece, x=x0 + c * (90 + GAP), y=y0 + r * (56 + GAP), rot=0))
    sheets.append(dict(id="PA", nombre="Envases: Asado Negro, Pernil y Ensalada de Gallina",
                       archivo="PA-envases", copias=6, placements=pl))
    # B · hallacas 2 × 5
    h = P["etiqueta-hallacas"]
    sheets.append(dict(id="PB", nombre="Hallacas", archivo="PB-hallacas", copias=6,
                       placements=grid(h, 2, 5, centered_x(span(2, 130)), centered_y(span(5, 80)))))
    # C · pan de jamón girado 4 × 5
    pan = P["etiqueta-pan-de-jamon"]
    sheets.append(dict(id="PC", nombre="Pan de Jamón (frontal)", archivo="PC-pan-de-jamon", copias=3,
                       placements=grid(pan, 4, 5, centered_x(span(4, 60)), centered_y(span(5, 80)), rot=1)))
    # D · cintas 1 × 14
    ci = P["cinta-torta-negra"]
    sheets.append(dict(id="PD", nombre=f"Cintas Torta Negra ({int(ci['W'])} mm)", archivo="PD-cintas", copias=5,
                       placements=grid(ci, 1, 14, centered_x(ci["W"]), centered_y(span(14, 25)))))
    # E · sticker de bolsa 2 × 2 + fila de 8 sellos
    bo, se = P["sticker-bolsa"], P["sello-cierre"]
    total_h = span(2, 190) + GAP + 30
    y0 = centered_y(total_h)
    pl = grid(bo, 2, 2, centered_x(span(2, 130)), y0)
    pl += grid(se, 8, 1, centered_x(span(8, 30)), y0 + span(2, 190) + GAP)
    sheets.append(dict(id="PE", nombre="Sticker de la bolsa + sellos de cierre", archivo="PE-bolsa-y-sellos",
                       copias=15, placements=pl))
    for i, sh in enumerate(sheets, 1):
        sh["pagina"], sh["de"] = i, len(sheets)
    return sheets


def sheet_test():
    pl = []
    x = MARGIN + 5
    pl.append(dict(piece=P["sticker-bolsa"], x=x, y=MARGIN + 5, rot=0))
    xr = x + 130 + GAP + 4
    pl.append(dict(piece=P["etiqueta-hallacas"], x=xr, y=MARGIN + 5, rot=0))
    y = MARGIN + 5 + 80 + GAP
    for i, pid in enumerate(["etiqueta-asado-negro", "etiqueta-pernil", "etiqueta-ensalada-de-gallina"]):
        pl.append(dict(piece=P[pid], x=xr, y=y + i * (56 + GAP), rot=0))
    for i in range(4):
        pl.append(dict(piece=P["sello-cierre"], x=xr + 90 + GAP + 3, y=y + i * (30 + GAP), rot=0))
    yp = MARGIN + 5 + 190 + GAP
    for i in range(2):
        pl.append(dict(piece=P["etiqueta-pan-de-jamon"], x=x, y=yp + i * (60 + GAP), rot=0))
    labels = []
    yc = SHEET_H - MARGIN - 25
    variantes = [("C", variante_cinta(265)), ("B", P["cinta-torta-negra"]), ("A", variante_cinta(245))]
    for i, (letra, piece) in enumerate(variantes):
        yy = yc - i * (25 + GAP)
        pl.append(dict(piece=piece, x=x, y=yy, rot=0))
        extra = " ✓" if letra == "B" else ""
        labels.append((x + piece["W"] + 5, yy + 14.5, f"{letra} · {int(piece['W'])} mm{extra}"))
    return dict(id="P0", nombre="PRUEBA: una de cada pieza + cinta en 3 largos", archivo="P0-prueba-vinil",
                copias=2, placements=pl, labels=labels)


def card_sheet():
    t = P["tarjeta"]
    front, back = t["pages"][0], t["pages"][1]
    pl = [dict(x=MARGIN + c * 100, y=MARGIN + r * 150) for r in range(3) for c in range(3)]
    return dict(id="PF", nombre="Tarjetas (frente y dorso)", archivo="PF-tarjetas", copias=7,
                placements=pl, front=front, back=back)


# ───────────────────────── HTML de los pliegos ─────────────────────────

PAGE_CSS = """
@page{size:%(w)smm %(h)smm;margin:0}
html,body{margin:0;padding:0;background:#fff}
.sheet{position:relative;width:%(w)smm;height:%(h)smm;overflow:hidden;page-break-after:always}
.sheet:last-child{page-break-after:auto}
.pc{position:absolute}
.pc>svg{display:block}
.cap2{position:absolute;left:0;right:0;bottom:7.6mm;text-align:center;font:600 3mm 'Josefin Sans',sans-serif;letter-spacing:.1mm;color:#1B2333}
.cap{position:absolute;left:0;right:0;bottom:3.4mm;text-align:center;font:400 2.3mm 'Josefin Sans',sans-serif;
  letter-spacing:.12mm;color:#777}
.lab{position:absolute;font:400 2.4mm 'Josefin Sans',sans-serif;color:#555;white-space:nowrap}
"""


def piece_div(pl):
    p = pl["piece"]
    W, H = p["W"], p["H"]
    svg, w, h = B.svg_doc(W, H, p["art"], "print", p["shape"], p["id"], None, 3.0)
    if pl["rot"]:
        style = (f"left:{B.f(pl['x'] + H + 3)}mm;top:{B.f(pl['y'] - 3)}mm;"
                 "transform-origin:0 0;transform:rotate(90deg);")
    else:
        style = f"left:{B.f(pl['x'] - 3)}mm;top:{B.f(pl['y'] - 3)}mm;"
    return f'<div class="pc" style="{style}width:{B.f(w)}mm;height:{B.f(h)}mm">{svg}</div>'


def caption(sh, extra=""):
    line = (f'<div class="cap">BS CATERING · NAVIDAD EN CASA {B.ANIO} · PLIEGO {sh["id"]} — {sh["nombre"].upper()}'
            f' · {int(SHEET_W / 10)} × {int(SHEET_H / 10)} CM{extra}</div>')
    if "pagina" in sh:
        cont = {}
        for pl in sh["placements"]:
            nm = NOMBRE_CORTO[pl["piece"]["id"]]
            cont[nm] = cont.get(nm, 0) + 1
        det = " · ".join(f"{n} {k}" for k, n in cont.items())
        line = (f'<div class="cap2">PÁGINA {sh["pagina"]} DE {sh["de"]} · IMPRIMIR {sh["copias"]} COPIAS'
                f' &nbsp;—&nbsp; {det} por pliego</div>') + line
    return line


NOMBRE_CORTO = {"etiqueta-asado-negro": "Asado Negro", "etiqueta-pernil": "Pernil",
                "etiqueta-ensalada-de-gallina": "Ensalada de Gallina", "etiqueta-hallacas": "Hallacas",
                "etiqueta-pan-de-jamon": "Pan de Jamón", "cinta-torta-negra": "Cintas",
                "sticker-bolsa": "Stickers de bolsa", "sello-cierre": "Sellos"}


def sheet_html(sh):
    divs = [piece_div(pl) for pl in sh["placements"]]
    for x, y, txt in sh.get("labels", []):
        divs.append(f'<div class="lab" style="left:{B.f(x)}mm;top:{B.f(y - 2.4)}mm">{txt}</div>')
    body = f'<div class="sheet">{"".join(divs)}{caption(sh)}</div>'
    css = PAGE_CSS % dict(w=B.f(SHEET_W), h=B.f(SHEET_H))
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{B.FONT_CSS}{B.TEXT_CSS}{css}'
            f'</style></head><body>{body}</body></html>')


def crop_marks():
    xs = [MARGIN + i * 100 for i in range(4)]
    ys = [MARGIN + i * 150 for i in range(4)]
    L, off = 6.0, 2.0
    lines = []
    for x in xs:
        lines.append((x, MARGIN - off - L, x, MARGIN - off))
        lines.append((x, SHEET_H - MARGIN + off, x, SHEET_H - MARGIN + off + L))
    for y in ys:
        lines.append((MARGIN - off - L, y, MARGIN - off, y))
        lines.append((SHEET_W - MARGIN + off, y, SHEET_W - MARGIN + off + L, y))
    seg = "".join(f'<line x1="{B.f(a)}" y1="{B.f(b)}" x2="{B.f(c)}" y2="{B.f(d)}"/>' for a, b, c, d in lines)
    return (f'<svg style="position:absolute;left:0;top:0" width="{B.f(SHEET_W)}mm" height="{B.f(SHEET_H)}mm" '
            f'viewBox="0 0 {B.f(SHEET_W)} {B.f(SHEET_H)}"><g stroke="#000" stroke-width="0.15">{seg}</g></svg>')


def card_sheet_html(sh):
    t = P["tarjeta"]
    pages = []
    for side, (suffix, inner, overlay), fill in [("FRENTE", sh["front"], B.NAVY), ("DORSO", sh["back"], B.IVORY)]:
        divs = [f'<div style="position:absolute;left:{B.f(MARGIN - 3)}mm;top:{B.f(MARGIN - 3)}mm;'
                f'width:{B.f(306)}mm;height:{B.f(456)}mm;background:{fill}"></div>']
        for pl in sh["placements"]:
            svg, w, h = B.svg_doc(t["W"], t["H"], inner, "preview", t["shape"], f"card{suffix}", None, 6)
            ov = overlay.replace('class="msg"', 'class="msg" style="left:12mm;right:12mm;top:24mm"') if overlay else ""
            divs.append(f'<div class="pc" style="left:{B.f(pl["x"])}mm;top:{B.f(pl["y"])}mm;width:100mm;'
                        f'height:150mm;overflow:hidden">{svg}{ov}</div>')
        cap = caption(dict(id=sh["id"], nombre=f"Tarjetas · {side}"),
                      " · CORTE CON GUILLOTINA EN LAS MARCAS")
        pages.append(f'<div class="sheet">{"".join(divs)}{crop_marks()}{cap}</div>')
    css = PAGE_CSS % dict(w=B.f(SHEET_W), h=B.f(SHEET_H))
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{B.FONT_CSS}{B.TEXT_CSS}{css}{B.CARD_CSS}'
            f'</style></head><body>{"".join(pages)}</body></html>')


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
    elif kind == "ribbon":
        N = cut[1]
        p = c.beginPath()
        for i, (x, y) in enumerate([(0, 0), (W, 0), (W - N, H / 2), (W, H), (0, H), (N, H / 2)]):
            (p.moveTo if i == 0 else p.lineTo)(x, y)
        p.close()
        c.drawPath(p, stroke=1, fill=0)
    else:
        c.rect(0, 0, W, H, stroke=1, fill=0)


def cut_overlay(cuts, page_w_pt, page_h_pt, path):
    """cuts: lista de (corte, x, y, W, H, rot) en mm, origen arriba a la izquierda del pliego."""
    c = canvas.Canvas(str(path), pagesize=(page_w_pt, page_h_pt))
    spot = CMYKColorSep(0, 1, 0, 0, spotName="CutContour", density=1)
    k = PT
    for cut, x, y, W, H, rot in cuts:
        c.saveState()
        if rot:
            c.transform(0, -k, -k, 0, k * (x + H), page_h_pt - k * y)
        else:
            c.transform(k, 0, 0, -k, k * x, page_h_pt - k * y)
        c.setStrokeColor(spot)
        c.setStrokeOverprint(1)
        c.setLineWidth(0.25 / k)
        draw_shape(c, cut, W, H)
        c.restoreState()
    c.showPage()
    c.save()


def to_cmyk_curves(src, dst):
    subprocess.run(["gs", "-q", "-dBATCH", "-dNOPAUSE", "-dSAFER", "-sDEVICE=pdfwrite", "-dNoOutputFonts",
                    "-sColorConversionStrategy=CMYK", "-sProcessColorModel=DeviceCMYK",
                    "-dCompatibilityLevel=1.6", "-dAutoRotatePages=/None", "-o", str(dst), str(src)], check=True)


def finalize(src, dst, w_mm, h_mm, cuts_per_page=None, trim_inset=0.0, title=""):
    TMP.mkdir(parents=True, exist_ok=True)
    cm = TMP / (dst.stem + "-cmyk.pdf")
    to_cmyk_curves(src, cm)
    r = PdfReader(cm)
    w = PdfWriter()
    for i, page in enumerate(r.pages):
        top = float(page.mediabox.top)
        cuts = cuts_per_page[i] if cuts_per_page else None
        if cuts:
            ov = TMP / f"{dst.stem}-corte-{i}.pdf"
            cut_overlay(cuts, float(page.mediabox.width), float(page.mediabox.height), ov)
            page.merge_page(PdfReader(ov).pages[0])
            # reportlab declara Helvetica aunque el corte no lleva texto: se quita para que
            # el preflight no reporte una fuente sin incrustar (todo el texto ya está en curvas)
            res = page["/Resources"].get_object()
            if "/Font" in res:
                del res["/Font"]
        box = RectangleObject([0, top - h_mm * PT, w_mm * PT, top])
        page.mediabox = box
        page.cropbox = box
        page.bleedbox = box
        t = trim_inset * PT
        page.trimbox = RectangleObject([t, top - h_mm * PT + t, w_mm * PT - t, top - t])
        w.add_page(page)
    w.add_metadata({"/Title": title, "/Author": "BS Catering", "/Subject": "Kit Navideño 2026 — imprenta"})
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(dst, "wb") as fh:
        w.write(fh)


def preview_png(pdf, png, dpi=60, page=1):
    subprocess.run(["gs", "-q", "-dBATCH", "-dNOPAUSE", "-dSAFER", "-sDEVICE=png16m", f"-r{dpi}",
                    f"-dFirstPage={page}", f"-dLastPage={page}", "-dTextAlphaBits=4", "-dGraphicsAlphaBits=4",
                    "-o", str(png), str(pdf)], check=True)


# ───────────────────────── principal ─────────────────────────

def main():
    TMP.mkdir(parents=True, exist_ok=True)
    d_ind = OUT / "03-PIEZAS-INDIVIDUALES"
    d_prod = OUT / "02-PRODUCCION"
    d_test = OUT / "01-PRUEBA"
    d_ref = OUT / "04-REFERENCIA"
    for d in (d_ind, d_prod, d_test, d_ref):
        d.mkdir(parents=True, exist_ok=True)

    # 1 · piezas individuales
    piezas = []
    for p in B.PIECES:
        n = NUM[p["id"]]
        src = ROOT / "impresion" / f"{n:02d}-{p['id']}.pdf"
        dst = d_ind / f"{n:02d}-{p['id']}.pdf"
        pages = len(PdfReader(src).pages)
        guillotina = p["id"] == "tarjeta"
        cuts = None if guillotina else [[(tuple(p["cut"]), 3.0, 3.0, p["W"], p["H"], 0)]] * pages
        finalize(src, dst, p["W"] + 6, p["H"] + 6, cuts, trim_inset=3.0, title=p["title"])
        piezas.append(dict(n=n, id=p["id"], title=p["title"], W=p["W"], H=p["H"], file=dst.name,
                           material=p["material"], notes=p["notes"], cut=p["cut"]))
        print("pieza", dst.name)

    # 2 · pliegos
    jobs, sheets = [], []
    for sh in [sheet_test()] + sheet_production():
        html = TMP / f"{sh['archivo']}.html"
        html.write_text(sheet_html(sh))
        raw = TMP / f"{sh['archivo']}-rgb.pdf"
        jobs.append(dict(html=str(html), pdf=str(raw), w=SHEET_W, h=SHEET_H))
        sheets.append(sh)
    cs = card_sheet()
    html = TMP / f"{cs['archivo']}.html"
    html.write_text(card_sheet_html(cs))
    jobs.append(dict(html=str(html), pdf=str(TMP / f"{cs['archivo']}-rgb.pdf"), w=SHEET_W, h=SHEET_H))
    jf = TMP / "trabajos.json"
    jf.write_text(json.dumps(jobs))
    subprocess.run(["node", str(B.ROOT / "render_html.js"), str(jf)], check=True)

    resumen = []
    for sh in sheets:
        raw = TMP / f"{sh['archivo']}-rgb.pdf"
        dst = (d_test if sh["id"] == "P0" else d_prod) / f"{sh['archivo']}.pdf"
        cuts = [[(tuple(pl["piece"]["cut"]), pl["x"], pl["y"], pl["piece"]["W"], pl["piece"]["H"], pl["rot"])
                 for pl in sh["placements"]]]
        finalize(raw, dst, SHEET_W, SHEET_H, cuts, 0.0, f"Pliego {sh['id']} — {sh['nombre']}")
        png = d_ref / f"{sh['archivo']}.png"
        preview_png(dst, png)
        cont = {}
        for pl in sh["placements"]:
            cont[pl["piece"]["id"]] = cont.get(pl["piece"]["id"], 0) + 1
        resumen.append(dict(id=sh["id"], nombre=sh["nombre"], archivo=dst.name, copias=sh["copias"],
                            contenido=cont, png=png.name, prueba=sh["id"] == "P0"))
        print("pliego", dst.name)
    raw = TMP / f"{cs['archivo']}-rgb.pdf"
    dst = d_prod / f"{cs['archivo']}.pdf"
    finalize(raw, dst, SHEET_W, SHEET_H, None, 0.0, "Pliego PF — Tarjetas (frente y dorso)")
    preview_png(dst, d_ref / f"{cs['archivo']}-frente.png", page=1)
    preview_png(dst, d_ref / f"{cs['archivo']}-dorso.png", page=2)
    resumen.append(dict(id="PF", nombre=cs["nombre"], archivo=dst.name, copias=cs["copias"],
                        contenido={"tarjeta": 9}, png=f"{cs['archivo']}-frente.png", prueba=False))
    print("pliego", dst.name)

    # guías con medidas como referencia
    for g in sorted((ROOT / "guias").glob("*-guia.pdf")):
        shutil.copy2(g, d_ref / g.name)

    # archivo único con todas las etiquetas: lo más sencillo para la imprenta
    d_env = ROOT / "etiquetas-imprenta"
    d_env.mkdir(exist_ok=True)
    wr = PdfWriter()
    for sh in sheets:
        if sh["id"] != "P0":
            for pg in PdfReader(d_prod / f"{sh['archivo']}.pdf").pages:
                wr.add_page(pg)
    wr.add_metadata({"/Title": f"BS Catering · Etiquetas Navidad en casa {B.ANIO}", "/Author": "BS Catering",
                     "/Subject": "Etiquetas autoadhesivas — pliegos 33 × 48 cm con CutContour"})
    with open(d_env / f"BS-Catering-Etiquetas-Navidad-{B.ANIO}.pdf", "wb") as fh:
        wr.write(fh)
    print("archivo único", d_env)

    (TMP / "resumen.json").write_text(json.dumps(dict(piezas=piezas, pliegos=resumen, meta=META, kits=KITS),
                                                 ensure_ascii=False, indent=1))
    print("listo:", OUT)


if __name__ == "__main__":
    main()
