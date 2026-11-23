# Kit Navideño BS Catering · «Navidad en casa» 2026

Etiquetas, cinta, sello, sticker de bolsa y tarjeta para el kit navideño (4 hallacas, asado negro o pernil, ensalada de gallina, pan de jamón y mini torta negra de obsequio).
Estilo **elegante**: azul noche, dorado y marfil, con el logo de BS Catering vectorizado. Instagram **@bscateringve**.

> **Versión final para imprenta.** Medidas confirmadas: tapa de los envases **14 × 8 cm** y domo **Ø 11 cm × 8,5 cm de alto**.
> Lo que va a la imprenta está en **`imprenta/`** (con su orden de impresión en PDF).

## Para la imprenta: `imprenta/`

| Archivo / carpeta | Qué es |
|---|---|
| `00-ORDEN-DE-IMPRESION.pdf` | Instrucciones completas: archivos, materiales, acabados, color, piezas con medidas, cantidades de prueba y de producción |
| `01-PRUEBA/P0-prueba-vinil.pdf` | Pliego de prueba 33 × 48 cm: una de cada pieza y la cinta en 3 largos (245 / 255 / 265 mm) |
| `02-PRODUCCION/` | Pliegos 33 × 48 cm: PA envases, PB hallacas, PC pan de jamón, PD cintas, PE sticker de bolsa + sellos, PF tarjetas (frente y dorso) |
| `03-PIEZAS-INDIVIDUALES/` | Cada pieza por separado, para montar en rollo u otro formato |
| `04-REFERENCIA/` | Vistas de los pliegos y guías con medidas (no se imprimen) |

Todos los PDF van en **CMYK**, con **textos en curvas**, **3 mm de sangrado** y la línea de corte en tinta plana **CutContour** (magenta, sobreimpresión). La tarjeta se corta con guillotina en las marcas.

## Piezas

| # | Pieza | Medida de corte | Material | Por kit | Dónde va |
|---|---|---|---|---|---|
| 01 | Asado Negro | 90 × 56 mm, r 3,5 mm | Vinil | 1 (o Pernil) | Tapa del envase |
| 02 | Ensalada de Gallina | 90 × 56 mm, r 3,5 mm | Vinil | 1 | Tapa del envase |
| 03 | Hallacas | 130 × 80 mm, r 4 mm | Vinil | 1 | Centro de la bolsa al vacío |
| 04 | Pan de Jamón (frontal) | 80 × 60 mm, r 4 mm | Vinil | 1 | Frente de la bolsa kraft, a 2 cm de la boca |
| 05 | Cinta Torta Negra | 255 × 25 mm, colas en V | Vinil | 1 | Cruza el domo de base a base |
| 06 | Sello redondo | Ø 30 mm | Vinil | 1 + 1 opcional | Cierra la bolsa del pan por detrás · solapa de la bolsa |
| 07 | Sticker de la bolsa | 130 × 190 mm, arco | Vinil | 1 | Frente de la bolsa esmerilada (menú: «Asado Negro o Pernil») |
| 08 | Tarjeta | 100 × 150 mm, 2 caras | Cartulina 300–350 g | 1 | Dentro de la bolsa |
| 09 | Pernil | 90 × 56 mm, r 3,5 mm | Vinil | 1 (en lugar del 01) | Tapa del envase |

## Cantidades

Previsión: **50 kits + 10 % de reposición = 55 juegos**. Un kit de 8 personas cuenta como 2 kits.

**Fase 1 · Prueba:** 2 pliegos P0 (vinil) + 1 pliego PF (9 tarjetas). Se arman 2 kits y se revisa color, adhesión (24 h en nevera), medidas y el largo de la cinta.

**Fase 2 · Producción:**

| Pliego | Contenido por pliego | Pliegos | Total |
|---|---|---|---|
| PA | 7 Asado Negro · 7 Pernil · 7 Ensalada | 8 | 56 de cada una |
| PB | 10 Hallacas | 6 | 60 |
| PC | 20 Pan de Jamón | 3 | 60 |
| PD | 14 Cintas (255 mm) | 4 | 56 |
| PE | 4 Stickers de bolsa · 8 Sellos | 14 | 56 stickers · 112 sellos |
| PF | 9 Tarjetas (frente y dorso) | 7 | 63 |

Total: **35 pliegos de vinil + 7 de cartulina** (33 × 48 cm). Asado y Pernil se imprimen en igual cantidad para cubrir cualquier combinación.

## Armado (para el equipo de BS Catering)
- **Envases:** etiqueta centrada en la tapa; quedan 2,5 cm a cada lado y 1,2 cm arriba y abajo.
- **Hallacas:** al centro de la bolsa al vacío; presionar del centro hacia afuera para que copie el relieve del pabilo.
- **Pan de jamón:** etiqueta al frente, a 2 cm de la boca. Doblar la boca hacia atrás y cerrar con el sello redondo.
- **Torta negra:** pegar una punta de la cinta en la base negra, cruzar el domo por arriba y pegar la otra punta en la base del otro lado.
- **Bolsa:** sticker centrado en el frente, debajo de la solapa del asa. Opcional: un sello en la solapa.

## Color de referencia

| Color | Pantalla | CMYK aprox. | Pantone de referencia |
|---|---|---|---|
| Azul noche | `#0F1C30` | C100 M85 Y45 K55 | 2767 C (aprox.) |
| Dorado | `#C9A45C` | C20 M35 Y75 K5 | 7562 C · metálico 871 C |
| Marfil | `#F4EDE0` | C3 M6 Y12 K0 | — |

## Otras carpetas
`impresion/` y `guias/` (PDF de trabajo en RGB y guías), `vista-previa/` (PNG), `maquetas/` y `fuente/fotos/` (no se suben al repositorio), `fuente/logo/` (logo vectorizado), `fuente/` (generadores y tipografías: Cormorant Garamond, Josefin Sans, Pinyon Script e Inter, licencia OFL).

## Regenerar
Textos, medidas (tapa, domo) y productos están al inicio de `fuente/build.py`; pliegos y cantidades en `fuente/imprenta.py`.

```bash
python3 fuente/build.py       # SVG y páginas
node fuente/render.js         # PDF de trabajo y PNG
python3 fuente/pdf_boxes.py   # medida exacta + TrimBox
python3 fuente/imprenta.py    # paquete para la imprenta (CMYK, curvas, CutContour, pliegos)
python3 fuente/orden.py       # orden de impresión
python3 fuente/mockups.py     # maquetas sobre las fotos
```
