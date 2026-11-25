#!/usr/bin/env python3
"""Hoja de instrucciones (A4, 1 página) que acompaña a las etiquetas sueltas.
Uso: python3 fuente/instrucciones.py   (después de imprenta.py)
"""
import base64
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402
import imprenta as I  # noqa: E402  (cantidades y nombres de archivo)

ROOT = B.ROOT.parent
DEST = ROOT / "etiquetas-imprenta"
TMP = B.BUILD / "imprenta"
FECHA = "25 de noviembre de 2026"


def font_css():
    css = B.FONT_CSS
    for w in (400, 600):
        b64 = base64.b64encode((B.ROOT / "fuentes" / f"Inter-{w}.woff").read_bytes()).decode()
        css += f"@font-face{{font-family:'Inter';font-weight:{w};src:url(data:font/woff;base64,{b64}) format('woff');}}"
    return css


def img(path):
    return "file://" + str(path)


FORMA = {"etiqueta-asado-negro": "Rectángulo, esquinas r 3,5 mm", "etiqueta-pernil": "Rectángulo, esquinas r 3,5 mm",
         "etiqueta-ensalada-de-gallina": "Rectángulo, esquinas r 3,5 mm", "etiqueta-hallacas": "Rectángulo, esquinas r 4 mm",
         "etiqueta-pan-de-jamon": "Rectángulo, esquinas r 4 mm", "sello-torta-negra": "Círculo",
         "sello-cierre": "Círculo", "sticker-bolsa": "Arco, esquinas inferiores r 5 mm"}
MEDIDA = {"etiqueta-asado-negro": "9 × 5,6 cm", "etiqueta-pernil": "9 × 5,6 cm", "etiqueta-ensalada-de-gallina": "9 × 5,6 cm",
          "etiqueta-hallacas": "13 × 8 cm", "etiqueta-pan-de-jamon": "8 × 6 cm", "sello-torta-negra": "Ø 5 cm",
          "sello-cierre": "Ø 3 cm", "sticker-bolsa": "10 × 14 cm"}
NOMBRE = {"etiqueta-asado-negro": "Asado Negro", "etiqueta-pernil": "Pernil", "etiqueta-ensalada-de-gallina": "Ensalada de Gallina",
          "etiqueta-hallacas": "Hallacas", "etiqueta-pan-de-jamon": "Pan de Jamón", "sello-torta-negra": "Sello Torta Negra",
          "sello-cierre": "Sello de cierre", "sticker-bolsa": "Sticker de la bolsa"}

filas, total = [], 0
for i, (pid, (archivo, medida, cant)) in enumerate(I.ETIQUETAS.items(), 1):
    total += cant
    nota = ('<br><span class="mut">60 para cerrar el pan + 60 para la solapa de la bolsa</span>'
            if pid == "sello-cierre" else "")
    filas.append(f"""<tr><td class="pg">{i:02d}</td>
<td class="th"><img src="{img(ROOT / 'vista-previa' / (pid + '.png'))}"></td>
<td><b>{NOMBRE[pid]}</b>{nota}<br><span class="file">{i:02d}-{archivo}_{medida}_{cant}-unidades.pdf</span></td>
<td class="num">{MEDIDA[pid]}<br><span class="mut">{FORMA[pid]}</span></td>
<td class="c big">{cant}</td></tr>""")

HTML = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
{font_css()}
@page {{ size: A4; margin: 10mm 13mm 9mm; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font: 400 9pt/1.42 'Inter', sans-serif; color:#1B2333; }}
.head {{ background:{B.BLUE}; color:#fff; padding: 4.5mm 7mm; display:flex; gap:6mm; align-items:center; border-radius:1.5mm; }}
.head img {{ width: 19mm; }}
.eyebrow {{ font: 600 7pt 'Montserrat'; letter-spacing:.24em; text-transform:uppercase; color:#E8CF98; margin:0 0 1.5mm; }}
h1 {{ font: 600 17pt/1.15 'Lora', serif; margin:0; }}
.head .meta {{ margin-left:auto; text-align:right; font-size:7.8pt; color:#DCE4EF; line-height:1.55; }}
h2 {{ font: 600 11.5pt 'Lora', serif; color:{B.BLUE}; margin: 3.6mm 0 1.6mm; border-bottom:.35mm solid #C9A45C; padding-bottom:1mm; }}
p {{ margin: 0 0 1.6mm; }}
.intro {{ background:#F3F5F9; border-radius:1.5mm; padding: 2.6mm 4mm; margin-top: 3mm; }}
table {{ width:100%; border-collapse:collapse; font-size:8.6pt; }}
th {{ text-align:left; font: 600 7pt 'Inter'; text-transform:uppercase; letter-spacing:.05em; color:#5B6474; border-bottom:.3mm solid #1B2333; padding:1.3mm 1.5mm; }}
td {{ border-bottom:.2mm solid #DADFE7; padding:1.3mm 1.5mm; vertical-align:middle; }}
td.pg {{ font: 600 10pt 'Inter'; color:{B.BLUE}; width: 8mm; }}
td.th {{ width: 24mm; }} td.th img {{ max-width: 22mm; max-height: 14mm; display:block; }}
td.c, th.c {{ text-align:center; }} td.big {{ font: 600 15pt 'Inter'; color:{B.BLUE}; width: 22mm; }}
td.num {{ white-space:nowrap; font-weight:600; }}
.mut {{ color:#5B6474; font-weight:400; font-size:7.8pt; }}
.file {{ font-size: 7.2pt; color:#4A6890; font-feature-settings: 'calt' 0; }}
.tot td {{ border-bottom:0; font-weight:600; }}
.grid {{ display:grid; grid-template-columns: 1fr 1fr; gap: 5mm; }}
ul {{ margin:0; padding-left: 4.2mm; }} li {{ margin: 0 0 1mm; }}
.sw {{ display:flex; gap:2.5mm; margin-top:1mm; }}
.sw div {{ flex:1; font-size:7.4pt; border:.2mm solid #DADFE7; border-radius:1mm; overflow:hidden; }}
.sw i {{ display:block; height:6mm; }} .sw span {{ display:block; padding:1.2mm 1.8mm; }}
.note {{ border-left: .8mm solid #C9A45C; padding: 1.5mm 3mm; background:#FBF6EA; margin-top: 3mm; }}
</style></head><body>
<div class="head"><img src="{img(B.ROOT / 'logo' / 'bs-catering-logo-blanco.svg')}">
<div><p class="eyebrow">Instrucciones para la imprenta · versión 2</p><h1>Etiquetas autoadhesivas · Navidad en casa {B.ANIO}</h1></div>
<div class="meta">BS Catering<br>{B.INSTAGRAM}<br>{FECHA}</div></div>

<div class="intro"><b>8 archivos PDF, uno por etiqueta</b>, a tamaño real (escala 1:1). El nombre de cada archivo dice
la etiqueta, la medida y <b>la cantidad a imprimir</b>. El montaje en pliegos queda a criterio de la imprenta.
Esta versión reemplaza a la anterior: fondo azul más claro y textos en blanco.</div>

<h2>Etiquetas y cantidades</h2>
<table><thead><tr><th>#</th><th></th><th>Etiqueta y archivo</th><th>Medida de corte</th><th class="c">Cantidad</th></tr></thead>
<tbody>{''.join(filas)}
<tr class="tot"><td></td><td></td><td>Total</td><td></td><td class="c big">{total}</td></tr></tbody></table>

<div class="grid">
<div><h2>Material y acabado</h2><ul>
<li><b>Vinil blanco autoadhesivo</b>, impresión full color.</li>
<li><b>Laminado mate</b> (las etiquetas van a nevera).</li>
<li><b>Corte</b> por plotter o troquel siguiendo la línea de corte. Pueden entregarse en planchas con medio corte o sueltas.</li>
<li>Los textos y el logo son <b>blancos</b>: es el blanco del vinil, sin tinta. No imprimir blanco.</li>
</ul></div>
<div><h2>Los archivos</h2><ul>
<li>CMYK, textos convertidos a curvas, <b>3 mm de sangrado</b>.</li>
<li>Línea de corte en tinta plana <b>«CutContour»</b> (magenta, sobreimpresión). <b>No se imprime.</b></li>
</ul>
<h2>Color de referencia</h2>
<div class="sw"><div><i style="background:{B.BLUE}"></i><span><b>Azul</b> C90 M70 Y21 K5</span></div>
<div><i style="background:{B.GOLD}"></i><span><b>Dorado</b> (adornos) C15 M27 Y67 K0</span></div></div>
</div></div>

<div class="note"><b>Antes del tiraje completo:</b> imprimir y cortar <b>1 muestra de cada etiqueta</b> para aprobar el tono del azul, el laminado y el corte.</div>
</body></html>"""

html = TMP / "instrucciones.html"
html.write_text(HTML)
out = DEST / "00-Instrucciones-para-la-imprenta.pdf"
jf = TMP / "instrucciones.json"
jf.write_text(json.dumps([dict(html=str(html), pdf=str(out))]))
subprocess.run(["node", str(B.ROOT / "render_html.js"), str(jf)], check=True)
print("ok", out, "total", total)
