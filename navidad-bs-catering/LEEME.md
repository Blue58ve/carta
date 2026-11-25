# Kit Navideño BS Catering · «Navidad en casa» 2026

Etiquetas, sellos, sticker de bolsa y tarjeta para el kit navideño (4 hallacas, asado negro o pernil, ensalada de gallina, pan de jamón y mini torta negra de obsequio). Instagram **@bscateringve**.

> **Versión 3 (25/11/2026): dos propuestas de estilo, pendiente de elegir.**
> La v1 (azul noche + textos dorados finos) no se leía impresa; la v2 (azul medio + textos blancos) se leía pero perdió la elegancia. La v3 recupera la paleta original con letra serif clásica (**Playfair Display**) más gruesa y más grande, y textos informativos en **Josefin Sans** seminegrita (eco del «CATERING» del logo):
> - **A · Azul noche refinado** (`TEMA=noche`, por defecto): fondo azul noche menos oscuro, textos marfil, logo dorado.
> - **B · Marfil clásico** (`TEMA=marfil`): fondo marfil, textos y logo azul noche, detalles dorados.
>
> Se mantienen los cambios de la v2: sello redondo de Ø 5 cm para la torta, sticker de bolsa de 10 × 14 cm y sello de cierre solo con el logo. Las proteínas (Asado Negro / Pernil) van al final en el menú y en la lista de archivos.

## Para enviar a la imprenta: `etiquetas-imprenta/`

8 PDF, uno por etiqueta, a tamaño real. El nombre del archivo dice la medida y **la cantidad**. Se acompaña con `00-Instrucciones-para-la-imprenta.pdf` (1 página).
Formato: CMYK, textos en curvas, 3 mm de sangrado y línea de corte en tinta plana **CutContour** (magenta, sobreimpresión, no se imprime).

| # | Etiqueta | Medida de corte | Cantidad |
|---|---|---|---|
| 01 | Hallacas | 130 × 80 mm, esquinas r 4 | **60** |
| 02 | Ensalada de Gallina | 90 × 56 mm, esquinas r 3,5 | **60** |
| 03 | Pan de Jamón | 80 × 60 mm, esquinas r 4 | **60** |
| 04 | Sello Torta Negra | Ø 50 mm | **60** |
| 05 | Sello de cierre | Ø 30 mm | **120** (60 pan + 60 solapa de la bolsa) |
| 06 | Sticker de la bolsa | 100 × 140 mm, arco | **60** |
| 07 | Asado Negro | 90 × 56 mm, esquinas r 3,5 | **30** |
| 08 | Pernil | 90 × 56 mm, esquinas r 3,5 | **30** |
| | **Total** | | **480** |

Material: vinil blanco autoadhesivo, impresión full color, **laminado mate**. Recomendación: pedir 1 muestra de cada una antes del tiraje.

La **tarjeta** (frente y dorso, 100 × 150 mm, cartulina 300–350 g, 60 unidades) está aparte en `tarjeta-imprenta/`.

## Armado
- **Envases (tapa 14 × 8 cm):** etiqueta centrada; quedan 2,5 cm a cada lado y 1,2 cm arriba y abajo.
- **Hallacas:** al centro de la bolsa al vacío; presionar del centro hacia afuera.
- **Pan de jamón:** etiqueta al frente, a 2 cm de la boca; la boca se dobla hacia atrás y se cierra con el sello de Ø 3 cm.
- **Torta negra:** sello de Ø 5 cm en el tope del domo (Ø 11 cm).
- **Bolsa:** sticker centrado en el frente, debajo de la solapa del asa. Opcional: un sello en la solapa.

## Color de referencia
Los valores CMYK exactos de cada estilo salen en `00-Instrucciones-para-la-imprenta.pdf` (se calculan con la misma conversión de los archivos).

| Estilo | Fondo | Textos | Logo | Adornos |
|---|---|---|---|---|
| A · Azul noche | `#1F3557` | marfil `#F6EEDC` | dorado `#D8B670` | dorado `#D4B06A` |
| B · Marfil | `#F7F1E5` | azul noche `#1F3557` | azul noche | dorado `#B48C42` |

## Carpetas
`etiquetas-imprenta/` y `tarjeta-imprenta/` (lo que se envía), `impresion/` (PDF de trabajo en RGB), `guias/` (medidas, zona segura y corte), `vista-previa/` (PNG), `maquetas/` y `fuente/fotos/` (no se suben al repositorio), `fuente/logo/` (logo vectorizado), `fuente/` (generadores y tipografías: Lora, Montserrat, Pinyon Script, Inter y, para documentos, Cormorant Garamond y Josefin Sans; todas OFL).

## Regenerar
Textos, medidas y productos al inicio de `fuente/build.py`; cantidades en `fuente/imprenta.py`.

```bash
TEMA=noche python3 fuente/build.py   # SVG y páginas (TEMA=noche | marfil)
node fuente/render.js           # PDF de trabajo y PNG
python3 fuente/pdf_boxes.py     # medida exacta + TrimBox
python3 fuente/imprenta.py      # PDF para la imprenta (CMYK, curvas, CutContour)
python3 fuente/instrucciones.py # hoja de instrucciones
python3 fuente/mockups.py       # maquetas sobre las fotos
```
