# Kit Navideño BS Catering · «Navidad en Casa» 2026

Etiquetas, sticker de bolsa y tarjeta para el kit navideño (4 hallacas, asado negro, ensalada de gallina, pan de jamón y mini torta negra de obsequio).
Estilo **elegante**: azul noche, dorado y marfil, con el logo de BS Catering vectorizado.

> **Borrador 1.** Las medidas son estimaciones hechas a partir de las fotos. Ajustar cuando lleguen las medidas reales (ver «Pendientes»).

## Archivos

| Carpeta | Qué contiene | Para quién |
|---|---|---|
| `impresion/` | PDF listos para imprenta: tamaño exacto + **3 mm de sangrado**, fuentes incrustadas, TrimBox definida | Imprenta |
| `guias/` | El mismo arte con la **línea de corte** (magenta), el sangrado (azul), la zona segura (verde) y el doblez | Imprenta / revisión |
| `fuente/svg/*-corte.svg` | Contorno de corte vectorial (trazo `CutContour`) para el plotter de corte | Imprenta |
| `vista-previa/` | PNG de cada pieza (fondo transparente) | Revisión, redes |
| `maquetas/` | Las etiquetas montadas sobre las fotos reales del empaque (no se suben al repositorio, igual que `fuente/fotos/`) | Revisión |
| `fuente/logo/` | Logo vectorizado (completo, monograma y «CATERING») en negro, dorado y blanco | Uso general |
| `fuente/` | Generador (`build.py`), render (`render.js`), maquetas y fuentes tipográficas | Edición |

## Piezas

| # | Pieza | Medida de corte | Material | Dónde va |
|---|---|---|---|---|
| 01 | Etiqueta Asado Negro | 110 × 70 mm, esquinas r 4 mm | Vinil autoadhesivo | Tapa del envase Safe-T-Fresh |
| 02 | Etiqueta Ensalada de Gallina | 110 × 70 mm, esquinas r 4 mm | Vinil autoadhesivo | Tapa del envase Safe-T-Fresh |
| 03 | Etiqueta Hallacas | 130 × 80 mm, esquinas r 4 mm | Vinil autoadhesivo | Centro de la bolsa al vacío |
| 04 | Etiqueta de cierre Pan de Jamón | 80 × 120 mm (se dobla a la mitad) | Vinil autoadhesivo | Cierra la boca de la bolsa kraft |
| 05 | Etiqueta Torta Negra (obsequio) | Ø 50 mm | Vinil autoadhesivo | Tope del domo |
| 06 | Sello de cierre (opcional) | Ø 40 mm | Vinil autoadhesivo | Solapa de la bolsa o sobre |
| 07 | Sticker principal de la bolsa | 130 × 190 mm, arco | Vinil autoadhesivo | Frente de la bolsa esmerilada |
| 08 | Tarjeta (frente y dorso) | 100 × 150 mm | Cartulina 300–350 g | Dentro de la bolsa |

Cantidades por kit de 4 personas: 1 de cada etiqueta (01–05), 1 sticker de bolsa, 1 tarjeta y 1–2 sellos.
Como el kit siempre va en múltiplos de 4, un kit de 8 lleva el doble de unidades (2 bolsas de hallacas, 2 envases de cada plato, etc.) con las mismas etiquetas. Por eso ninguna etiqueta indica cantidades.

### Cómo se coloca la etiqueta del pan de jamón
1. Doblar la boca de la bolsa kraft unos 2 cm.
2. Pegar la mitad inferior (la que dice «Pan de Jamón») en el frente, con la línea de doblez justo en el borde.
3. Doblar la mitad superior hacia atrás. Al voltear la bolsa se lee «Feliz Navidad» derecho (por eso en el archivo está de cabeza).

## Indicaciones para la imprenta

- **Vinil:** blanco brillante o mate, impresión full color y **laminado mate** (da el acabado elegante y protege de la humedad de la nevera).
- **Corte:** troquelado o plotter siguiendo `fuente/svg/*-corte.svg` o la línea magenta de `guias/`.
- **Color de referencia** (pedir prueba de color antes del tiraje):

| Color | Pantalla | CMYK aprox. | Pantone de referencia |
|---|---|---|---|
| Azul noche | `#0F1C30` | C100 M85 Y45 K55 | 2767 C (aprox.) |
| Dorado | `#C9A45C` | C20 M35 Y75 K5 | 7562 C · metálico 871 C |
| Marfil | `#F4EDE0` | C3 M6 Y12 K0 | — |

- **Mejora opcional:** el dorado se puede hacer en **hot stamping** (tarjeta) o con vinil dorado metálico. Los archivos ya separan el dorado como color plano, así que la imprenta lo puede aislar fácilmente.
- Los PDF salen en RGB. La imprenta los convierte a CMYK con su perfil.

## Tipografías
- **Cormorant Garamond** (nombres de producto y textos), **Josefin Sans** (mayúsculas espaciadas, eco de «CATERING») y **Pinyon Script** («Feliz Navidad»). Todas de Google Fonts, licencia libre (OFL). Están en `fuente/fuentes/`.

## Pendientes
1. **Usuario de Instagram:** se usó `@bscatering` provisionalmente. Confirmarlo.
2. **Medidas reales:** tapa del envase (zona plana), bolsa de hallacas, ancho de la bolsa kraft, diámetro del tope del domo y bolsa esmerilada.
3. **Nombre del kit:** se usó «Navidad en Casa». Opciones: «La Mesa del 24», «Nochebuena en Casa», «Sabor a Hogar», «Tradición en Casa».

## Editar y regenerar
Los textos (nombre del kit, año, Instagram, productos y mensaje de la tarjeta) están al inicio de `fuente/build.py`.

```bash
python3 fuente/build.py      # genera SVG y páginas
node fuente/render.js        # PDF y PNG (requiere Playwright + Chromium)
python3 fuente/pdf_boxes.py  # medida exacta + TrimBox en los PDF
python3 fuente/mockups.py    # maquetas sobre las fotos
```
