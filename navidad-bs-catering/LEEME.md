# Kit Navideño BS Catering · «Navidad en casa» 2026

Etiquetas, sellos, sticker de bolsa y tarjeta para el kit navideño (4 hallacas, asado negro o pernil, ensalada de gallina, pan de jamón y mini torta negra de obsequio). Instagram **@bscateringve**.

> **Versión 2 (25/11/2026), tras la prueba impresa.** En la primera prueba el azul noche salió casi negro y los textos dorados, finos y pequeños, no se leían. Cambios:
> - Fondo **azul más claro** (`#2B568A`) y **todos los textos y el logo en blanco** (el blanco del vinil, sin tinta).
> - Dorado **solo en marcos, ramitas y destellos**, con trazos más gruesos.
> - Tipografías más firmes y más grandes: **Lora seminegrita** (nombres) y **Montserrat seminegrita** (información). Nada por debajo de 2,6 mm de alto.
> - **Torta negra:** sello redondo de Ø 5 cm en el tope del domo (reemplaza a la cinta).
> - **Sticker de la bolsa:** más pequeño, 10 × 14 cm.
> - **Sello de cierre Ø 3 cm:** solo el logo, sin texto pequeño.

## Para enviar a la imprenta: `etiquetas-imprenta/`

8 PDF, uno por etiqueta, a tamaño real. El nombre del archivo dice la medida y **la cantidad**. Se acompaña con `00-Instrucciones-para-la-imprenta.pdf` (1 página).
Formato: CMYK, textos en curvas, 3 mm de sangrado y línea de corte en tinta plana **CutContour** (magenta, sobreimpresión, no se imprime).

| # | Etiqueta | Medida de corte | Cantidad |
|---|---|---|---|
| 01 | Asado Negro | 90 × 56 mm, esquinas r 3,5 | **30** |
| 02 | Pernil | 90 × 56 mm, esquinas r 3,5 | **30** |
| 03 | Ensalada de Gallina | 90 × 56 mm, esquinas r 3,5 | **60** |
| 04 | Hallacas | 130 × 80 mm, esquinas r 4 | **60** |
| 05 | Pan de Jamón | 80 × 60 mm, esquinas r 4 | **60** |
| 06 | Sello Torta Negra | Ø 50 mm | **60** |
| 07 | Sello de cierre | Ø 30 mm | **120** (60 pan + 60 solapa de la bolsa) |
| 08 | Sticker de la bolsa | 100 × 140 mm, arco | **60** |
| | **Total** | | **480** |

Material: vinil blanco autoadhesivo, impresión full color, **laminado mate**. Recomendación: pedir 1 muestra de cada una antes del tiraje.

La **tarjeta** (frente y dorso, 100 × 150 mm, cartulina 300–350 g, 60 unidades) está aparte en `tarjeta-imprenta/`.

## Armado
- **Envases (tapa 14 × 8 cm):** etiqueta centrada; quedan 2,5 cm a cada lado y 1,2 cm arriba y abajo.
- **Hallacas:** al centro de la bolsa al vacío; presionar del centro hacia afuera.
- **Pan de jamón:** etiqueta al frente, a 2 cm de la boca; la boca se dobla hacia atrás y se cierra con el sello de Ø 3 cm.
- **Torta negra:** sello de Ø 5 cm en el tope del domo (Ø 11 cm).
- **Bolsa:** sticker centrado en el frente, debajo de la solapa del asa. Opcional: un sello en la solapa.

## Color de referencia (valores CMYK de los archivos)

| Color | Pantalla | CMYK | Uso |
|---|---|---|---|
| Azul | `#2B568A` | C90 M70 Y21 K5 | Fondo de las etiquetas |
| Blanco | `#FFFFFF` | sin tinta | Textos y logo |
| Dorado | `#D9B66F` | C15 M27 Y67 K0 | Marcos y adornos |

## Carpetas
`etiquetas-imprenta/` y `tarjeta-imprenta/` (lo que se envía), `impresion/` (PDF de trabajo en RGB), `guias/` (medidas, zona segura y corte), `vista-previa/` (PNG), `maquetas/` y `fuente/fotos/` (no se suben al repositorio), `fuente/logo/` (logo vectorizado), `fuente/` (generadores y tipografías: Lora, Montserrat, Pinyon Script, Inter y, para documentos, Cormorant Garamond y Josefin Sans; todas OFL).

## Regenerar
Textos, medidas y productos al inicio de `fuente/build.py`; cantidades en `fuente/imprenta.py`.

```bash
python3 fuente/build.py         # SVG y páginas
node fuente/render.js           # PDF de trabajo y PNG
python3 fuente/pdf_boxes.py     # medida exacta + TrimBox
python3 fuente/imprenta.py      # PDF para la imprenta (CMYK, curvas, CutContour)
python3 fuente/instrucciones.py # hoja de instrucciones
python3 fuente/mockups.py       # maquetas sobre las fotos
```
