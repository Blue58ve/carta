#!/usr/bin/env python3
"""Orden de impresión (PDF A4) para la imprenta. Lee el resumen que deja imprenta.py.
Uso: python3 fuente/orden.py
"""
import base64
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402

ROOT = B.ROOT.parent
OUT = ROOT / "imprenta"
TMP = B.BUILD / "imprenta"
R = json.loads((TMP / "resumen.json").read_text())

FECHA = "23 de noviembre de 2026"
NOMBRE = {
    "etiqueta-asado-negro": "Asado Negro", "etiqueta-ensalada-de-gallina": "Ensalada de Gallina",
    "etiqueta-hallacas": "Hallacas", "etiqueta-pan-de-jamon": "Pan de Jamón (frontal)",
    "cinta-torta-negra": "Cinta Torta Negra", "sello-cierre": "Sello redondo de cierre",
    "sticker-bolsa": "Sticker de la bolsa", "tarjeta": "Tarjeta", "etiqueta-pernil": "Pernil",
    "cinta-245": "Cinta A (245 mm)", "cinta-265": "Cinta C (265 mm)",
}
FORMA = {"rrect": "Rectángulo, esquinas r {} mm", "circle": "Círculo", "arch": "Arco (medio punto), esquinas inf. r {} mm",
         "ribbon": "Tira con colas en V de {} mm", "rect": "Rectángulo (guillotina)"}
USO = {
    "etiqueta-asado-negro": ("1*", "Tapa del envase del plato principal (14 × 8 cm)"),
    "etiqueta-pernil": ("1*", "Igual que Asado Negro, cuando el kit lleva pernil"),
    "etiqueta-ensalada-de-gallina": ("1", "Tapa del envase de la ensalada (14 × 8 cm)"),
    "etiqueta-hallacas": ("1", "Centro de la bolsa al vacío de 4 hallacas"),
    "etiqueta-pan-de-jamon": ("1", "Frente de la bolsa kraft, a 2 cm de la boca"),
    "sello-cierre": ("1 + 1 opc.", "Cierra la bolsa del pan por detrás · opcional en la solapa de la bolsa"),
    "cinta-torta-negra": ("1", "Cruza el domo de la torta (Ø 11 × 8,5 cm) de base a base"),
    "sticker-bolsa": ("1", "Frente de la bolsa esmerilada del kit"),
    "tarjeta": ("1", "Dentro de la bolsa"),
}


def font_css():
    css = B.FONT_CSS
    for w in (400, 600):
        b64 = base64.b64encode((B.ROOT / "fuentes" / f"Inter-{w}.woff").read_bytes()).decode()
        css += f"@font-face{{font-family:'Inter';font-weight:{w};src:url(data:font/woff;base64,{b64}) format('woff');}}"
    return css


def img(path):
    return "file://" + str(path)


def fmt_cut(cut):
    k = cut[0]
    t = FORMA[k]
    return t.format(str(cut[1]).replace(".0", "").replace(".", ",")) if "{}" in t else t


def mm(v):
    s = f"{v:g}".replace(".", ",")
    return s


# ── cantidades ──
prod, prueba = {}, {}
for sh in R["pliegos"]:
    tgt = prueba if sh["prueba"] else prod
    for pid, n in sh["contenido"].items():
        tgt[pid] = tgt.get(pid, 0) + n * sh["copias"]
# en la prueba las tarjetas se imprimen aparte (1 pliego PF)
prueba["tarjeta"] = 9

piezas = R["piezas"]
META = R["meta"]

rows = []
for p in piezas:
    uso, donde = USO[p["id"]]
    t_prueba = prueba.get(p["id"], 0)
    if p["id"] == "cinta-torta-negra":
        t_prueba_txt = f'{t_prueba} <small>(+ {prueba.get("cinta-245", 0)} A y {prueba.get("cinta-265", 0)} C)</small>'
    else:
        t_prueba_txt = str(t_prueba)
    rows.append(f"""<tr>
<td class="n">{p['n']:02d}</td>
<td class="th"><img src="{img(ROOT / 'vista-previa' / (p['id'] + ('-frente' if p['id'] == 'tarjeta' else '') + '.png'))}"></td>
<td><b>{NOMBRE[p['id']]}</b><br><span class="mut">{donde}</span></td>
<td class="num">{mm(p['W'])} × {mm(p['H'])} mm<br><span class="mut">{fmt_cut(p['cut'])}</span></td>
<td class="c">{uso}</td>
<td class="c">{t_prueba_txt}</td>
<td class="c"><b>{prod.get(p['id'], 0)}</b></td>
</tr>""")

sheet_rows, sheet_cards = [], []
for sh in R["pliegos"]:
    cont = " · ".join(f"{n} {NOMBRE[pid]}" for pid, n in sh["contenido"].items())
    total = " · ".join(f"{n * sh['copias']} {NOMBRE[pid]}" for pid, n in sh["contenido"].items())
    carpeta = "01-PRUEBA" if sh["prueba"] else "02-PRODUCCION"
    material = "Cartulina 300–350 g, 4/4" if sh["id"] == "PF" else "Vinil + laminado mate"
    sheet_rows.append(f"""<tr class="{'test' if sh['prueba'] else ''}">
<td><b>{sh['id']}</b></td><td>{sh['nombre']}<br><span class="mut">{carpeta}/{sh['archivo']}</span></td>
<td>{cont}</td><td class="mut">{material}</td><td class="c big">{sh['copias']}</td><td class="mut">{total}</td></tr>""")
    sheet_cards.append(f"""<figure><img src="{img(OUT / '04-REFERENCIA' / sh['png'])}"><figcaption><b>{sh['id']}</b> · {sh['nombre']}<br>
<span class="mut">Imprimir {sh['copias']} {'pliego' if sh['copias'] == 1 else 'pliegos'}</span></figcaption></figure>""")

n_vinil_prod = sum(sh["copias"] for sh in R["pliegos"] if not sh["prueba"] and sh["id"] != "PF")
n_card_prod = sum(sh["copias"] for sh in R["pliegos"] if sh["id"] == "PF")
n_test = sum(sh["copias"] for sh in R["pliegos"] if sh["prueba"])
cinta = next(p for p in piezas if p["id"] == "cinta-torta-negra")

HTML = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
{font_css()}
@page {{ size: A4; margin: 14mm 14mm 16mm; }}
:root {{ --navy:#0F1C30; --gold:#A8843E; --ink:#1B2333; --mut:#5B6474; --line:#D9D3C7; --soft:#F5F1E8; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font: 400 9.4pt/1.45 'Inter', sans-serif; color: var(--ink); }}
h1 {{ font: italic 500 25pt/1.05 'Cormorant Garamond', serif; margin: 0; color:#fff; }}
h2 {{ font: 600 15pt/1.15 'Cormorant Garamond', serif; margin: 7mm 0 2.5mm; color: var(--navy); border-bottom: .4mm solid var(--gold); padding-bottom: 1.2mm; }}
h3 {{ font: 600 10pt 'Inter'; margin: 4mm 0 1.5mm; }}
.eyebrow {{ font: 400 7.2pt 'Josefin Sans'; letter-spacing: .3em; text-transform: uppercase; color: #C9A45C; margin: 0 0 2mm; }}
.head {{ background: var(--navy); color:#fff; padding: 7mm 8mm; display:flex; gap: 7mm; align-items:center; border-radius: 1.5mm; }}
.head img {{ width: 24mm; }}
.head .meta {{ margin-left:auto; text-align:right; font-size:8pt; color:#C9C2B3; line-height:1.6; }}
.mut {{ color: var(--mut); font-size: 8.2pt; }}
small {{ font-size: 7.6pt; color: var(--mut); }}
p {{ margin: 0 0 2mm; }}
.grid2 {{ display:grid; grid-template-columns: 1fr 1fr; gap: 4mm; }}
.box {{ background: var(--soft); border-radius: 1.5mm; padding: 3.5mm 4mm; }}
.box h3 {{ margin-top: 0; }}
ul {{ margin: 0; padding-left: 4.5mm; }} li {{ margin: 0 0 1.1mm; }}
table {{ width:100%; border-collapse: collapse; font-size: 8.6pt; }}
th {{ text-align:left; font: 600 7.4pt 'Inter'; text-transform: uppercase; letter-spacing:.05em; color: var(--mut); border-bottom: .3mm solid var(--ink); padding: 1.6mm 1.5mm; }}
td {{ border-bottom: .2mm solid var(--line); padding: 1.8mm 1.5mm; vertical-align: middle; }}
td.n {{ font: 600 9pt 'Inter'; color: var(--gold); width: 7mm; }}
td.th {{ width: 22mm; }} td.th img {{ max-width: 20mm; max-height: 14mm; display:block; }}
td.c, th.c {{ text-align:center; }} td.num {{ white-space: nowrap; }}
td.big {{ font: 600 13pt 'Inter'; color: var(--navy); }}
tr.test td {{ background: #FBF6EA; }}
.tot td {{ font-weight: 600; border-bottom: 0; }}
.sw {{ display:flex; gap: 3mm; }}
.sw div {{ flex:1; border:.2mm solid var(--line); border-radius:1mm; overflow:hidden; font-size:7.8pt; }}
.sw i {{ display:block; height: 9mm; }} .sw span {{ display:block; padding: 1.5mm 2mm; }}
.sheets {{ display:grid; grid-template-columns: repeat(4, 1fr); gap: 3.5mm; }}
.sheets figure {{ margin:0; font-size: 7.6pt; }}
.sheets img {{ width:100%; border: .2mm solid var(--line); display:block; margin-bottom: 1.2mm; }}
.break {{ break-before: page; }}
.check li {{ list-style: none; position: relative; padding-left: 5mm; }}
.check li::before {{ content: ""; position:absolute; left:0; top:.8mm; width: 2.8mm; height: 2.8mm; border: .3mm solid var(--ink); border-radius: .5mm; }}
.pill {{ display:inline-block; font: 600 7.2pt 'Inter'; background: var(--navy); color:#fff; border-radius: 10mm; padding: .6mm 2.4mm; margin-right: 1.5mm; }}
.foot {{ margin-top: 6mm; font-size: 7.6pt; color: var(--mut); border-top: .2mm solid var(--line); padding-top: 2mm; }}
</style></head><body>

<div class="head">
  <img src="{img(B.ROOT / 'logo' / 'bs-catering-logo-dorado.svg')}">
  <div><p class="eyebrow">Orden de impresión</p><h1>Kit Navideño «Navidad en casa» {B.ANIO}</h1></div>
  <div class="meta">BS Catering<br>{B.INSTAGRAM}<br>{FECHA}</div>
</div>

<h2>Resumen del trabajo</h2>
<p>Etiquetas en <b>vinil autoadhesivo impreso y cortado</b> (8 diseños) y una <b>tarjeta en cartulina</b> a dos caras para el kit navideño de BS Catering.
Se trabaja en dos fases: <span class="pill">1</span><b>prueba</b> ({n_test} pliegos de vinil + 1 de tarjetas) y, una vez aprobada,
<span class="pill">2</span><b>producción</b> para <b>{R['kits']} kits + 10 % de reposición</b> ({META} juegos): {n_vinil_prod} pliegos de vinil y {n_card_prod} de cartulina, de 33 × 48 cm.</p>

<div class="grid2">
  <div class="box"><h3>Archivos entregados</h3><ul>
    <li>PDF en <b>CMYK</b>, escala <b>1:1</b> en milímetros, <b>textos convertidos a curvas</b>.</li>
    <li><b>Sangrado de 3 mm</b> por lado en cada pieza; TrimBox definida.</li>
    <li>Línea de corte en tinta plana <b>«CutContour»</b> (magenta 100 %, sobreimpresión, 0,25 pt). <b>No se imprime</b>: es el trazado del plotter o troquel.</li>
    <li>Pliegos de <b>33 × 48 cm</b> con margen libre de 15 mm para pinzas y marcas de registro del plotter (las agrega su software de corte).</li>
    <li>Si trabajan en rollo u otro tamaño de pliego, usen <b>03-PIEZAS-INDIVIDUALES</b> y monten a su medida.</li>
  </ul></div>
  <div class="box"><h3>Materiales y acabados</h3><ul>
    <li><b>Etiquetas:</b> vinil blanco autoadhesivo, impresión full color y <b>laminado mate</b> (va a nevera: debe resistir humedad y frío).</li>
    <li><b>Corte:</b> <b>medio corte</b> (kiss-cut) sobre el CutContour, entregado en planchas para despegar fácil. La cinta también en medio corte.</li>
    <li><b>Tarjeta:</b> cartulina de 300–350 g (opalina o sulfato), 4/4, corte con guillotina en las marcas. Opcional: dorado en hot stamping en el frente.</li>
    <li>Superficies: tapa de PET, bolsa al vacío, bolsa kraft, bolsa esmerilada y domo de PET.</li>
  </ul></div>
</div>

<h3>Color de referencia</h3>
<div class="sw">
  <div><i style="background:#0F1C30"></i><span><b>Azul noche</b> · C100 M85 Y45 K55 · ref. Pantone 2767 C</span></div>
  <div><i style="background:#C9A45C"></i><span><b>Dorado</b> · C20 M35 Y75 K5 · ref. Pantone 7562 C (metálico 871 C)</span></div>
  <div><i style="background:#F4EDE0"></i><span><b>Marfil</b> · C3 M6 Y12 K0</span></div>
</div>
<p class="mut" style="margin-top:2mm">El azul noche cubre casi toda la superficie: pedimos prueba de color sobre el vinil final antes del tiraje.</p>

<div class="break"></div>
<h2 style="margin-top:0">Piezas, medidas y cantidades</h2>
<table>
<thead><tr><th>#</th><th></th><th>Pieza y uso</th><th>Medida de corte</th><th class="c">Por kit</th><th class="c">Prueba</th><th class="c">Producción</th></tr></thead>
<tbody>{''.join(rows)}</tbody>
</table>
<p class="mut" style="margin-top:2mm">* Cada kit lleva <b>Asado Negro o Pernil</b>: se imprimen ambos en igual cantidad para cubrir cualquier combinación. Un kit de 8 personas cuenta como 2 kits.
La tarjeta de la prueba sale de 1 pliego PF (9 tarjetas).</p>

<div class="break"></div>
<h2 style="margin-top:0">Fase 1 · Prueba</h2>
<div class="grid2">
  <div>
    <p><b>Imprimir:</b></p>
    <ul>
      <li><b>P0 · Pliego de prueba</b>, vinil + laminado mate + medio corte: <b>{n_test} pliegos</b>. Cada pliego trae 1 sticker de bolsa, 1 hallacas, 1 Asado Negro, 1 Pernil, 1 Ensalada, 2 Pan de Jamón, 4 sellos y la cinta en <b>3 largos</b> (A 245, B {int(cinta['W'])} y C 265 mm).</li>
      <li><b>PF · Tarjetas</b>: <b>1 pliego</b> (9 tarjetas) en la cartulina elegida.</li>
    </ul>
    <p style="margin-top:3mm"><b>Revisar con el empaque real (2 kits armados):</b></p>
    <ul class="check">
      <li>Tono del azul y del dorado; legibilidad de los textos pequeños (Instagram, «Navidad en casa · 2026»).</li>
      <li>Adhesión en cada superficie y después de <b>24 h en nevera</b>.</li>
      <li>Cinta del domo: elegir el largo que llega justo a la base (A, B o C).</li>
      <li>El sello de Ø 30 mm cierra bien la bolsa del pan doblada hacia atrás.</li>
      <li>Medidas sobre la bolsa al vacío, la bolsa kraft y la bolsa esmerilada.</li>
      <li>Laminado mate y facilidad para despegar (medio corte).</li>
    </ul>
    <p class="mut" style="margin-top:3mm">La producción usa la cinta <b>B ({int(cinta['W'])} mm)</b>. Si en la prueba queda mejor A o C, BS Catering enviará el pliego PD actualizado.</p>
  </div>
  <figure style="margin:0"><img src="{img(OUT / '04-REFERENCIA' / 'P0-prueba-vinil.png')}" style="width:100%;border:.2mm solid var(--line)">
  <figcaption class="mut">P0 · Pliego de prueba (33 × 48 cm)</figcaption></figure>
</div>

<h2>Fase 2 · Producción ({R['kits']} kits + 10 %)</h2>
<table>
<thead><tr><th>Pliego</th><th>Nombre y archivo</th><th>Contenido por pliego</th><th>Material</th><th class="c">Pliegos</th><th>Total</th></tr></thead>
<tbody>{''.join(sheet_rows)}
<tr class="tot"><td></td><td colspan="3">Total producción: {n_vinil_prod} pliegos de vinil + {n_card_prod} de cartulina (33 × 48 cm)</td><td class="c">{n_vinil_prod + n_card_prod}</td><td></td></tr>
</tbody></table>
<p class="mut" style="margin-top:2mm">Las cantidades salen redondeadas a pliegos completos y todas cubren al menos {META} juegos. Los sellos (112) alcanzan para cerrar el pan y la solapa de cada bolsa.</p>

<div class="break"></div>
<h2 style="margin-top:0">Vista de los pliegos</h2>
<div class="sheets">{''.join(sheet_cards)}
<figure><img src="{img(OUT / '04-REFERENCIA' / 'PF-tarjetas-dorso.png')}"><figcaption><b>PF</b> · Tarjetas, dorso<br><span class="mut">Misma posición que el frente (todas las tarjetas son iguales)</span></figcaption></figure>
</div>

<h2>Contenido de la carpeta</h2>
<table>
<tbody>
<tr><td><b>00-ORDEN-DE-IMPRESION.pdf</b></td><td>Este documento.</td></tr>
<tr><td><b>01-PRUEBA/</b></td><td>P0-prueba-vinil.pdf. Para la tarjeta de prueba, usar PF-tarjetas.pdf de 02-PRODUCCION.</td></tr>
<tr><td><b>02-PRODUCCION/</b></td><td>PA a PE (vinil) y PF (tarjetas: página 1 frente, página 2 dorso).</td></tr>
<tr><td><b>03-PIEZAS-INDIVIDUALES/</b></td><td>Cada pieza por separado (01 a 09), con sangrado y CutContour, para montar en otro formato.</td></tr>
<tr><td><b>04-REFERENCIA/</b></td><td>Imágenes de los pliegos y guías de cada pieza con medidas, zona segura y línea de corte. Solo de referencia, no imprimir.</td></tr>
</tbody></table>

<div class="foot">BS Catering · {B.INSTAGRAM} · Kit Navideño «Navidad en casa» {B.ANIO}. Cualquier duda sobre los archivos, consultar antes de imprimir.</div>
</body></html>"""

html = TMP / "orden.html"
html.write_text(HTML)
jobs = [dict(html=str(html), pdf=str(OUT / "00-ORDEN-DE-IMPRESION.pdf"))]
jf = TMP / "orden.json"
jf.write_text(json.dumps(jobs))
subprocess.run(["node", str(B.ROOT / "render_html.js"), str(jf)], check=True)
print("ok", OUT / "00-ORDEN-DE-IMPRESION.pdf")
