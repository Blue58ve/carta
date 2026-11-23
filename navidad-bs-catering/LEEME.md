# Kit Navideño BS Catering · «Navidad en casa» 2026

Etiquetas, cinta, sticker de bolsa y tarjeta para el kit navideño (4 hallacas, asado negro o pernil, ensalada de gallina, pan de jamón y mini torta negra de obsequio).
Estilo **elegante**: azul noche, dorado y marfil, con el logo de BS Catering vectorizado.

> **Versión final.** Medidas confirmadas: tapa de los envases **14 × 8 cm** y domo **Ø 11 cm × 8,5 cm de alto**. Nombre «Navidad en casa» e Instagram **@bscateringve**.

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
| 01 | Etiqueta Asado Negro | 90 × 56 mm, esquinas r 3,5 mm | Vinil autoadhesivo | Tapa del envase (14 × 8 cm) |
| 02 | Etiqueta Ensalada de Gallina | 90 × 56 mm, esquinas r 3,5 mm | Vinil autoadhesivo | Tapa del envase (14 × 8 cm) |
| 03 | Etiqueta Hallacas | 130 × 80 mm, esquinas r 4 mm | Vinil autoadhesivo | Centro de la bolsa al vacío |
| 04 | Etiqueta de cierre Pan de Jamón | 80 × 120 mm (se dobla a la mitad) | Vinil autoadhesivo | Cierra la boca de la bolsa kraft |
| 05 | Cinta de regalo Torta Negra (obsequio) | 255 × 25 mm, colas en V de 7 mm | Vinil autoadhesivo | Por encima del domo Ø 11 × 8,5 cm, de base a base (también lo sella) |
| 06 | Sello de cierre (opcional) | Ø 40 mm | Vinil autoadhesivo | Solapa de la bolsa o sobre |
| 07 | Sticker principal de la bolsa | 130 × 190 mm, arco | Vinil autoadhesivo | Frente de la bolsa esmerilada |
| 08 | Tarjeta (frente y dorso) | 100 × 150 mm | Cartulina 300–350 g | Dentro de la bolsa |
| 09 | Etiqueta Pernil (variante) | 90 × 56 mm, esquinas r 3,5 mm | Vinil autoadhesivo | Tapa del envase, cuando el kit lleva pernil en vez de asado |
| 10 | Sticker de la bolsa · versión Pernil | 130 × 190 mm, arco | Vinil autoadhesivo | Igual que el 07; su menú dice «Hallacas · Pernil» |

Cantidades por kit de 4 personas: 1 de cada etiqueta y la cinta (01–05), 1 sticker de bolsa, 1 tarjeta y 1–2 sellos. En los kits con pernil se usan la 09 y el 10 en lugar de la 01 y el 07.
Como el kit siempre va en múltiplos de 4, un kit de 8 lleva el doble de unidades (2 bolsas de hallacas, 2 envases de cada plato, etc.) con las mismas etiquetas. Por eso ninguna etiqueta indica cantidades.

### Cómo se coloca la cinta de la torta negra
1. Pegar una punta en la base negra del domo, de un lado.
2. Subir por la pared del domo, cruzar el tope (ahí queda «Torta Negra · Obsequio de la casa») y bajar por el otro lado.
3. Pegar la otra punta en la base. La cinta queda como un listón de regalo y sella el domo.
4. Largo calculado para el domo de Ø 11 cm × 8,5 cm: 2 paredes de 3 cm + media vuelta del tope (π × 5,5 cm ≈ 17,3 cm) + 1,1 cm pegado en la base de cada lado = **25,5 cm**.

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

## Antes del tiraje
1. **Prueba de la cinta:** imprimir 1 cinta y probarla en el domo. Si sobra o falta largo, se cambia `DOMO` en `fuente/build.py` y se regenera.
2. **Medidas estimadas desde las fotos** (no confirmadas): etiqueta de hallacas 13 × 8 cm sobre la bolsa al vacío, etiqueta del pan de jamón de 8 cm de ancho sobre la bolsa kraft y sticker de 13 × 19 cm en la bolsa esmerilada. Conviene presentarlas sobre el empaque real con una prueba en papel.
3. **Prueba de color** del azul noche y el dorado sobre el vinil elegido.

## Editar y regenerar
Los textos (nombre del kit, año, Instagram, productos, medidas de la tapa y del domo, y mensaje de la tarjeta) están al inicio de `fuente/build.py`.

```bash
python3 fuente/build.py      # genera SVG y páginas
node fuente/render.js        # PDF y PNG (requiere Playwright + Chromium)
python3 fuente/pdf_boxes.py  # medida exacta + TrimBox en los PDF
python3 fuente/mockups.py    # maquetas sobre las fotos
```
