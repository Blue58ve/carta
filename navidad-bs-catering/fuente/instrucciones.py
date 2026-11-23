#!/usr/bin/env python3
"""Hoja de instrucciones (A4, 1 página) que acompaña al archivo único de etiquetas.
Uso: python3 fuente/instrucciones.py   (después de imprenta.py)
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build as B  # noqa: E402
import orden as O  # noqa: E402  (reutiliza fuentes, nombres y cantidades)

ROOT = B.ROOT.parent
DEST = ROOT / "etiquetas-imprenta"
TMP = B.BUILD / "imprenta"
R = json.loads((TMP / "resumen.json").read_text())
ARCHIVO = f"BS-Catering-Etiquetas-Navidad-{B.ANIO}.pdf"

pliegos = [sh for sh in R["pliegos"] if not sh["prueba"] and sh["id"] != "PF"]
filas = []
for i, sh in enumerate(pliegos, 1):
    cont = "<br>".join(f"{n} {O.NOMBRE[pid]}" for pid, n in sh["contenido"].items())
    total = "<br>".join(f"<b>{n * sh['copias']}</b> {O.NOMBRE[pid]}" for pid, n in sh["contenido"].items())
    filas.append(f"""<tr><td class="pg">{i}</td>
<td class="th"><img src="{O.img(ROOT / 'imprenta' / '04-REFERENCIA' / sh['png'])}"></td>
<td>{cont}</td><td class="c big">{sh['copias']}</td><td>{total}</td></tr>""")
n_pliegos = sum(sh["copias"] for sh in pliegos)

medidas = [("Asado Negro · Pernil · Ensalada", "90 × 56 mm", "esquinas r 3,5"),
           ("Hallacas", "130 × 80 mm", "esquinas r 4"),
           ("Pan de Jamón", "80 × 60 mm", "esquinas r 4"),
           ("Cinta Torta Negra", "255 × 25 mm", "tira con colas en V"),
           ("Sello de cierre", "Ø 30 mm", "círculo"),
           ("Sticker de la bolsa", "130 × 190 mm", "arco, esquinas inf. r 6")]
med_rows = "".join(f"<tr><td>{a}</td><td class='num'>{b}</td><td class='mut'>{c}</td></tr>" for a, b, c in medidas)

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
.file {{ background:#F5F1E8; border-radius:1.5mm; padding: 2.6mm 4mm; margin-top: 3mm; }}
.file b.name {{ font: 600 10pt 'Inter'; }}
table {{ width:100%; border-collapse:collapse; font-size:8.4pt; }}
th {{ text-align:left; font: 600 7pt 'Inter'; text-transform:uppercase; letter-spacing:.05em; color:#5B6474; border-bottom:.3mm solid #1B2333; padding:1.3mm 1.5mm; }}
td {{ border-bottom:.2mm solid #D9D3C7; padding:1.1mm 1.5mm; vertical-align:middle; }}
td.pg {{ font: 600 14pt 'Inter'; color:#A8843E; width: 9mm; text-align:center; }}
td.th {{ width: 13mm; }} td.th img {{ width: 10.5mm; display:block; border:.2mm solid #D9D3C7; }}
td.c, th.c {{ text-align:center; }} td.big {{ font: 600 14pt 'Inter'; color:#0F1C30; }}
td.num {{ white-space:nowrap; font-weight:600; }}
.mut {{ color:#5B6474; }}
.tot td {{ border-bottom:0; font-weight:600; }}
.grid {{ display:grid; grid-template-columns: 1fr 1fr; gap: 4mm; }}
ul {{ margin:0; padding-left: 4.2mm; }} li {{ margin: 0 0 1mm; }}
.sw {{ display:flex; gap:2.5mm; margin-top:1mm; }}
.sw div {{ flex:1; font-size:7.4pt; border:.2mm solid #D9D3C7; border-radius:1mm; overflow:hidden; }}
.sw i {{ display:block; height:6mm; }} .sw span {{ display:block; padding:1.2mm 1.8mm; }}
.note {{ border-left: .8mm solid #A8843E; padding: 1.5mm 3mm; background:#FBF6EA; margin-top: 3mm; }}
</style></head><body>
<div class="head"><img src="{O.img(B.ROOT / 'logo' / 'bs-catering-logo-dorado.svg')}">
<div><p class="eyebrow">Instrucciones para la imprenta</p><h1>Etiquetas autoadhesivas · Navidad en casa {B.ANIO}</h1></div>
<div class="meta">BS Catering<br>{B.INSTAGRAM}<br>{O.FECHA}</div></div>

<div class="file"><b class="name">{ARCHIVO}</b><br>
Un solo PDF de <b>{len(pliegos)} páginas</b>. Cada página es un <b>pliego de 33 × 48 cm</b> listo para imprimir y cortar.
En el margen inferior de cada página dice <b>cuántas copias imprimir</b>. Total: <b>{n_pliegos} pliegos</b>.</div>

<h2>Qué imprimir</h2>
<table><thead><tr><th class="c">Pág.</th><th></th><th>Contenido de cada pliego</th><th class="c">Copias</th><th>Total de etiquetas</th></tr></thead>
<tbody>{''.join(filas)}
<tr class="tot"><td></td><td></td><td>Total</td><td class="c big">{n_pliegos}</td><td>pliegos de 33 × 48 cm</td></tr></tbody></table>

<div class="grid">
<div><h2>Material y acabado</h2><ul>
<li><b>Vinil blanco autoadhesivo</b>, impresión full color.</li>
<li><b>Laminado mate</b> (las etiquetas van a nevera).</li>
<li><b>Medio corte</b> (kiss-cut) siguiendo la línea de corte; entregar en planchas.</li>
</ul>
<h2>El archivo</h2><ul>
<li>CMYK, escala 1:1, textos en curvas, 3 mm de sangrado.</li>
<li>Línea de corte en tinta plana <b>«CutContour»</b> (magenta, sobreimpresión). <b>No se imprime.</b></li>
<li>Margen libre de 15 mm para pinzas y marcas de registro del plotter.</li>
</ul></div>
<div><h2>Medidas de corte</h2><table><tbody>{med_rows}</tbody></table>
<h2>Color de referencia</h2>
<div class="sw"><div><i style="background:#0F1C30"></i><span><b>Azul noche</b> C100 M85 Y45 K55 · Pantone 2767 C</span></div>
<div><i style="background:#C9A45C"></i><span><b>Dorado</b> C20 M35 Y75 K5 · Pantone 7562 C</span></div></div>
</div></div>

<div class="note"><b>Antes del tiraje completo:</b> imprimir y cortar <b>1 copia de cada página</b> para aprobar color, laminado y corte.
Luego completar las copias indicadas.</div>
</body></html>"""

html = TMP / "instrucciones.html"
html.write_text(HTML)
out = DEST / "Instrucciones-para-la-imprenta.pdf"
jf = TMP / "instrucciones.json"
jf.write_text(json.dumps([dict(html=str(html), pdf=str(out))]))
subprocess.run(["node", str(B.ROOT / "render_html.js"), str(jf)], check=True)
print("ok", out)
