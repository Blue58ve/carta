# Kit Navideño BS Catering · «Navidad en casa» 2026

Etiquetas, sellos, sticker de bolsa y tarjeta para el kit navideño (4 hallacas, asado negro o pernil, ensalada de gallina, pan de jamón y mini torta negra de obsequio). Instagram **@bscateringve**.

> **Versión final (26/11/2026): «Marfil clásico» con azul Oxford.**
> Fondo marfil, textos y logo en **azul Oxford** (`#14213D`), detalles dorados en marcos dobles, ramitas y destellos. Nombres en **Playfair Display**, información en **Josefin Sans** seminegrita (eco del «CATERING» del logo), con tamaños grandes: la letra oscura sobre fondo claro no se cierra al imprimir.
>
> Historial: v1 azul noche con textos dorados finos (no se leía impresa) → v2 azul medio con textos blancos (legible, pero sin elegancia) → v3 dos propuestas (A azul noche, B marfil) → **final: B con azul Oxford**. Se mantienen el sello de Ø 5 cm para la torta, el sticker de bolsa de 10 × 14 cm, el sello de cierre solo con el logo y las proteínas (Asado Negro / Pernil) al final del menú y de la lista de archivos.

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

## Color de referencia (valores CMYK de los archivos)

| Color | Pantalla | CMYK | Uso |
|---|---|---|---|
| Marfil | `#F7F1E5` | C2 M4 Y9 K0 | Fondo |
| Azul Oxford | `#14213D` | C93 M84 Y46 K53 | Textos y logo |
| Dorado | `#B48C42` | C27 M42 Y88 K5 | Marcos y adornos |

El tema anterior A («azul noche») sigue disponible con `TEMA=noche`.

## Carpetas
`etiquetas-imprenta/` y `tarjeta-imprenta/` (lo que se envía), `impresion/` (PDF de trabajo en RGB), `guias/` (medidas, zona segura y corte), `vista-previa/` (PNG), `maquetas/` y `fuente/fotos/` (no se suben al repositorio), `fuente/logo/` (logo vectorizado), `fuente/` (generadores y tipografías: Playfair Display, Josefin Sans, Cormorant Garamond, Pinyon Script e Inter; todas OFL).

## Regenerar
Textos, medidas y productos al inicio de `fuente/build.py`; cantidades en `fuente/imprenta.py`.

```bash
python3 fuente/build.py         # SVG y páginas (tema por defecto: marfil)
node fuente/render.js           # PDF de trabajo y PNG
python3 fuente/pdf_boxes.py     # medida exacta + TrimBox
python3 fuente/imprenta.py      # PDF para la imprenta (CMYK, curvas, CutContour)
python3 fuente/instrucciones.py # hoja de instrucciones
python3 fuente/mockups.py       # maquetas sobre las fotos
```
