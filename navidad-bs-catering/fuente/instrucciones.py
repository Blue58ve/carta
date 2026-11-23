#!/usr/bin/env python3
"""Hoja de instrucciones (A4, 1 página) que acompaña a las etiquetas sueltas.
Uso: python3 fuente/instrucciones.py   (después de imprenta.py)
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402
import imprenta as I  # noqa: E402  (cantidades y nombres de archivo)
import orden as O  # noqa: E402  (fuentes y utilidades)

ROOT = B.ROOT.parent
DEST = ROOT / "etiquetas-imprenta"
TMP = B.BUILD / "imprenta"

FORMA = {"etiqueta-asado-negro": "Rectángulo, esquinas r 3,5 mm", "etiqueta-pernil": "Rectángulo, esquinas r 3,5 mm",
         "etiqueta-ensalada-de-gallina": "Rectángulo, esquinas r 3,5 mm", "etiqueta-hallacas": "Rectángulo, esquinas r 4 mm",
         "etiqueta-pan-de-jamon": "Rectángulo, esquinas r 4 mm", "cinta-torta-negra": "Tira con colas en V",
         "sello-cierre": "Círculo", "sticker-bolsa": "Arco, esquinas inferiores r 6 mm"}
MEDIDA = {"etiqueta-asado-negro": "9 × 5,6 cm", "etiqueta-pernil": "9 × 5,6 cm", "etiqueta-ensalada-de-gallina": "9 × 5,6 cm",
          "etiqueta-hallacas": "13 × 8 cm", "etiqueta-pan-de-jamon": "8 × 6 cm", "cinta-torta-negra": "25,5 × 2,5 cm",
          "sello-cierre": "Ø 3 cm", "sticker-bolsa": "13 × 19 cm"}
NOMBRE = {"etiqueta-asado-negro": "Asado Negro", "etiqueta-pernil": "Pernil", "etiqueta-ensalada-de-gallina": "Ensalada de Gallina",
          "etiqueta-hallacas": "Hallacas", "etiqueta-pan-de-jamon": "Pan de Jamón", "cinta-torta-negra": "Cinta Torta Negra",
          "sello-cierre": "Sello redondo", "sticker-bolsa": "Sticker de la bolsa"}

filas, total = [], 0
for i, (pid, (archivo, medida, cant)) in enumerate(I.ETIQUETAS.items(), 1):
    total += cant
    nota = '<br><span class="mut">60 para cerrar el pan + 60 para la solapa de la bolsa</span>' if pid == "sello-cierre" else ""
    filas.append(f"""<tr><td class="pg">{i:02d}</td>
<td class="th"><img src="{O.img(ROOT / 'vista-previa' / (pid + '.png'))}"></td>
<td><b>{NOMBRE[pid]}</b>{nota}<br><span class="file">{i:02d}-{archivo}_{medida}_{cant}-unidades.pdf</span></td>
<td class="num">{MEDIDA[pid]}<br><span class="mut">{FORMA[pid]}</span></td>
<td class="c big">{cant}</td></tr>""")

HTML = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
{O.font_css()}
@page {{ size: A4; margin: 10mm 13mm 9mm; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font: 400 9pt/1.42 'Inter', sans-serif; color:#1B2333; }}
.head {{ background:#0F1C30; color:#fff; padding: 4.5mm 7mm; display:flex; gap:6mm; align-items:center; border-radius:1.5mm; }}
.head img {{ width: 19mm; }}
.eyebrow {{ font: 400 7pt 'Josefin Sans'; letter-spacing:.3em; text-transform:uppercase; color:#C9A45C; margin:0 0 1.5mm; }}
h1 {{ font: italic 500 20pt/1.05 'Cormorant Garamond', serif; margin:0; }}
.head .meta {{ margin-left:auto; text-align:right; font-size:7.8pt; color:#C9C2B3; line-height:1.55; }}
h2 {{ font: 600 12.5pt 'Cormorant Garamond', serif; color:#0F1C30; margin: 3.6mm 0 1.6mm; border-bottom:.35mm solid #A8843E; padding-bottom:1mm; }}
p {{ margin: 0 0 1.6mm; }}
.intro {{ background:#F5F1E8; border-radius:1.5mm; padding: 2.6mm 4mm; margin-top: 3mm; }}
table {{ width:100%; border-collapse:collapse; font-size:8.6pt; }}
th {{ text-align:left; font: 600 7pt 'Inter'; text-transform:uppercase; letter-spacing:.05em; color:#5B6474; border-bottom:.3mm solid #1B2333; padding:1.3mm 1.5mm; }}
td {{ border-bottom:.2mm solid #D9D3C7; padding:1.3mm 1.5mm; vertical-align:middle; }}
td.pg {{ font: 600 10pt 'Inter'; color:#A8843E; width: 8mm; }}
td.th {{ width: 24mm; }} td.th img {{ max-width: 22mm; max-height: 13mm; display:block; }}
td.c, th.c {{ text-align:center; }} td.big {{ font: 600 15pt 'Inter'; color:#0F1C30; width: 22mm; }}
td.num {{ white-space:nowrap; font-weight:600; }}
.mut {{ color:#5B6474; font-weight:400; font-size:7.8pt; }}
.file {{ font-size: 7.2pt; color:#8A7444; font-feature-settings: 'calt' 0; }}
.tot td {{ border-bottom:0; font-weight:600; }}
.grid {{ display:grid; grid-template-columns: 1fr 1fr; gap: 5mm; }}
ul {{ margin:0; padding-left: 4.2mm; }} li {{ margin: 0 0 1mm; }}
.sw {{ display:flex; gap:2.5mm; margin-top:1mm; }}
.sw div {{ flex:1; font-size:7.4pt; border:.2mm solid #D9D3C7; border-radius:1mm; overflow:hidden; }}
.sw i {{ display:block; height:6mm; }} .sw span {{ display:block; padding:1.2mm 1.8mm; }}
.note {{ border-left: .8mm solid #A8843E; padding: 1.5mm 3mm; background:#FBF6EA; margin-top: 3mm; }}
</style></head><body>
<div class="head"><img src="{O.img(B.ROOT / 'logo' / 'bs-catering-logo-dorado.svg')}">
<div><p class="eyebrow">Instrucciones para la imprenta</p><h1>Etiquetas autoadhesivas · Navidad en casa {B.ANIO}</h1></div>
<div class="meta">BS Catering<br>{B.INSTAGRAM}<br>{O.FECHA}</div></div>

<div class="intro"><b>8 archivos PDF, uno por etiqueta</b>, a tamaño real (escala 1:1). El nombre de cada archivo dice
la etiqueta, la medida y <b>la cantidad a imprimir</b>. El montaje en pliegos queda a criterio de la imprenta.</div>

<h2>Etiquetas y cantidades</h2>
<table><thead><tr><th>#</th><th></th><th>Etiqueta y archivo</th><th>Medida de corte</th><th class="c">Cantidad</th></tr></thead>
<tbody>{''.join(filas)}
<tr class="tot"><td></td><td></td><td>Total</td><td></td><td class="c big">{total}</td></tr></tbody></table>

<div class="grid">
<div><h2>Material y acabado</h2><ul>
<li><b>Vinil blanco autoadhesivo</b>, impresión full color.</li>
<li><b>Laminado mate</b> (las etiquetas van a nevera).</li>
<li><b>Corte</b> por plotter o troquel siguiendo la línea de corte. Pueden entregarse en planchas con medio corte o sueltas.</li>
</ul></div>
<div><h2>Los archivos</h2><ul>
<li>CMYK, textos convertidos a curvas, <b>3 mm de sangrado</b>.</li>
<li>Línea de corte en tinta plana <b>«CutContour»</b> (magenta, sobreimpresión). <b>No se imprime.</b></li>
</ul>
<h2>Color de referencia</h2>
<div class="sw"><div><i style="background:#0F1C30"></i><span><b>Azul noche</b> C100 M85 Y45 K55 · Pantone 2767 C</span></div>
<div><i style="background:#C9A45C"></i><span><b>Dorado</b> C20 M35 Y75 K5 · Pantone 7562 C</span></div></div>
</div></div>

<div class="note"><b>Antes del tiraje completo:</b> imprimir y cortar <b>1 muestra de cada etiqueta</b> para aprobar color, laminado y corte.</div>
</body></html>"""

html = TMP / "instrucciones.html"
html.write_text(HTML)
out = DEST / "00-Instrucciones-para-la-imprenta.pdf"
jf = TMP / "instrucciones.json"
jf.write_text(json.dumps([dict(html=str(html), pdf=str(out))]))
subprocess.run(["node", str(B.ROOT / "render_html.js"), str(jf)], check=True)
print("ok", out, "total", total)
