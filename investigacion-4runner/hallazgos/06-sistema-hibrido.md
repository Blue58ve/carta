# Agente 6 — Sistema híbrido i-FORCE MAX en Venezuela
**Fecha de investigación:** 2026-11-18 (ronda 1 y ronda 2 el mismo día)

> **Advertencia de cobertura (actualizada en la ronda 2):**
> - **WebFetch no funcionó en ninguna ronda.** La red de la sesión no permite pressroom.toyota.com ni assets.sia.toyota.com, y el usuario decidió no ampliarla. Por eso **no se pudo leer el PDF del manual del propietario ni el Warranty & Maintenance Guide**.
> - Todas las fuentes se consultaron **a través de los resúmenes y extractos de WebSearch**: 19 búsquedas en la ronda 1 y 40 en la ronda 2.
> - Las especificaciones del manual se citan a partir de **reproducciones textuales en foros, de datos de la EPA tomados de agregadores y de fichas oficiales de distribuidores Toyota de otros países**. El verificador debe cotejarlas con el PDF oficial.
> - La ronda 2 cerró la señal de mercados comparables (6.3), la política de Toyota de Venezuela y parte de los repuestos. **El servicio híbrido en Carabobo sigue sin evidencia pública.**

## Resumen ejecutivo (5 líneas)
1. **Calificación global: MEDIO** (sin cambio en la ronda 2, pero el componente híbrido sube). El combustible es **MEDIO** y la señal de mercados comparables lo respalda. El componente propio del sistema híbrido **sube de MEDIO a ALTO (ronda 2)** en su dimensión de servicio: Toyota de Venezuela confirmó que los vehículos importados por particulares "prácticamente pierden" la garantía, no vende híbridos y no apareció ningún taller con capacidad i-FORCE MAX. Solo baja a MEDIO si el cliente se equipa con diagnóstico propio y una cadena de repuestos desde EE. UU.
2. Toyota exige **87 AKI ("Research Octane Number 91") o más** (manual 2025, pág. 617, citado en foros) [3][4]. **(ronda 2)** La EPA clasifica la 4Runner Hybrid 4WD 2026 como vehículo de **gasolina regular** (23 mpg en ciudad / 24 en carretera) [57][58]. No se encontró el texto del manual 2026/2027 **[NO VERIFICADO]**.
3. En Venezuela se venden gasolinas de **91 y 95 RON a precio internacional** (≈USD 0,50/L) y la **Súper Premium de 97 RON a USD 1/L**, que sigue a la venta en noviembre de 2026 [95][92][30]. Las mediciones informales dieron regular = 89 y Súper Premium = 93–96 [26]. La Súper Premium (y probablemente la de 95) cumple el mínimo de RON 91; una gasolina de RON 89 no lo cumple.
4. **Señal de mercados (ronda 2): no es negativa para el motor.**
   - Toyota vende oficialmente el 2.4 turbo T24A-FTS (sin híbrido) en Colombia, Perú, Bolivia, Arabia Saudí, Emiratos y Filipinas. En Colombia exige gasolina "extra" **RON 95 o superior** [62][65][68][71][76][77].
   - Lo excluye en Chile, Sudáfrica y Kenia, que son mercados diésel [70][79][81].
   - El **i-FORCE MAX híbrido no se vende oficialmente en Sudamérica**; solo apareció en México (Tacoma) [83][84].
5. Costo incremental estimado frente a EE. UU.: **USD 1.000 / 1.700 / 3.200 al año** (mín/prob/máx). Probabilidad de una falla mayor en 5 años: **4 % / 9 % / 21 %**, a USD 2.500–10.000 por evento más 2–8 semanas de inmovilización. **No se emite 🛑 ALERTA DE ALCANCE.**

## Hallazgos detallados (subsecciones 6.1 a 6.6)

### 6.0 Nota de método
- Etiquetas usadas:
  - `[PRIMARIA]`: Toyota o distribuidores oficiales Toyota de otros países, PDVSA, Gobierno.
  - `[PRIMARIA-vía extracto]`: documento oficial leído solo a través del resumen del buscador.
  - `[PRENSA]`.
  - `[CONCESIONARIO]`: concesionarios de EE. UU., secundaria comercial.
  - `[FORO/REDES]`.
- No se citó ninguna cifra técnica de memoria. Las estimaciones van marcadas como **ESTIMACIÓN**, con su supuesto y su rango. Lo nuevo o corregido en la segunda vuelta lleva **(ronda 2)**.

### 6.1 — Cómo funciona y qué exige el sistema

**Arquitectura (4Runner de sexta generación, años modelo 2025–2027)**
- **Trailhunter = solo i-FORCE MAX** ("exclusively powered by the i-FORCE MAX"). El motor base i-FORCE (2.4 turbo sin híbrido) rinde 278 hp y 317 lb-ft [1] `[PRIMARIA-vía extracto]`.
- **Potencia combinada del i-FORCE MAX:** 326 hp netos y 465 lb-ft [2][19] `[PRIMARIA-vía extracto / PRENSA]`.
- **Motor T24A-FTS:** 2.393 cm³, 87,5 × 99,5 mm, compresión 11,0:1 y turbo *twin-scroll* con intercooler [13][14] `[secundaria técnica]`.
- **(ronda 2) Inyección dual D-4ST confirmada con documento de distribuidor oficial:** la ficha técnica de la Land Cruiser Prado 2026 de Yokomotor (distribuidor Toyota en Colombia) describe el 2.4 turbo como "2.393 c.c… 16 válvulas, turbo, DOHC, VVT-i dual, transmisión por cadena e inyección D-4ST (directa e indirecta)", con compresión 11,0:1 [62] `[PRIMARIA, distribuidor oficial]`.
- **(ronda 2) Documento técnico de Toyota:** existe el paper SAE 2024-01-2089, "The New Toyota 2.4L L4 Turbo Engine with 8AT and 1-Motor Hybrid Electric Powertrains for Midsize Pickup Trucks" [61] `[PRIMARIA técnica, solo título]`. Su contenido no se pudo leer.
- **Motor-generador:** una sola unidad entre el motor y la caja automática de 8 velocidades, de unos 48 hp, con embrague de desacople [19][22] `[PRENSA, Tacoma]`. **(ronda 2)** Los datos de la EPA confirman "automatic (S8)" y 4WD *part-time* para la 4Runner Hybrid 4WD 2026 [57].
- **Batería de tracción:** NiMH sellada de 288 V, bajo el piso de carga trasero [15][16] `[CONCESIONARIO]`. La capacidad de ~1,87 kWh sigue **[NO VERIFICADO con fuente Toyota]** [16][18].
- **Refrigeración:** dos circuitos independientes, uno para el motor y el turbo y otro para el inversor, el convertidor, la PCU y el motor eléctrico, según fuentes secundarias [20][21]. **(ronda 2)** Un repuesto OEM, el "Inverter Assembly HEV" G92A0-60021 para Tacoma y Land Cruiser, incluye el convertidor DC [104]. No se pudo confirmar con el manual.
- **No es enchufable** [16][17].
- **Garantía en EE. UU.:** la batería híbrida tiene 10 años o 150.000 millas [15]. Para el efecto de exportar el vehículo, ver 6.4 (ronda 2).
- **Año modelo vigente:** la 2027 es de continuidad según prensa y foros [23][24]. **[NO VERIFICADO]** con el Pressroom.
- **(ronda 2) Contexto a largo plazo:** Toyota anunció en septiembre de 2024 un nuevo 2.0 turbo que sustituirá al 2.4 turbo en el futuro [64] `[PRENSA especializada]`. No afecta al vehículo nuevo. Supone que el T24A-FTS no tendrá una vida de producción tan larga como los motores atmosféricos clásicos; el soporte de repuestos en EE. UU. no debería verse afectado a medio plazo **[inferencia]**.

**Combustible exigido por Toyota**
- **Cita del manual 2025 de la 4Runner, pág. 617** (código OM35B85U [7]), reproducida en foros [3][4] `[FORO/REDES que reproduce PRIMARIA]`:
  > "You must only use unleaded gasoline. Select octane rating 87 (Research Octane Number 91) or higher. Use of unleaded gasoline with an octane rating lower than 87 may result in engine knocking. Persistent knocking can lead to engine damage."
- **(ronda 2) Datos EPA del año modelo 2026:** la 4Runner Hybrid 4WD 2026 figura como vehículo de **gasolina regular**, con 23 mpg en ciudad y 24 en carretera ("The EPA lists the 2026 Toyota 4Runner Hybrid 4WD as running on regular gasoline") [57] `[secundaria, agregador de datos EPA; fueleconomy.gov no se abrió]`. Cars.com da **23 mpg combinados** para la Hybrid Trailhunter 4WD [58], y Tustin Toyota da un tanque de **19,0 galones** [59] `[CONCESIONARIO]`. Si la etiqueta fuera "Premium Recommended" o "Premium Required", la EPA lo indicaría. Este dato respalda que el requisito para el año modelo 2026 es 87 AKI.
- **(ronda 2) Coherencia con la Tacoma i-FORCE MAX, mismo tren motriz:** según foros que citan su manual, "Octane Rating 87 or higher… research octane number 91" (pág. 615), y ante detonación persistente con 87 hay que llevarla a Toyota (pág. 621) [60] `[FORO]`.
- **Manual 2026 y 2027:** existen las versiones OM35C07U y OM35C28U [6]. **(ronda 2)** No se halló ninguna cita textual de la sección de combustible del manual 2026 ni del 2027 **[NO VERIFICADO]**. Lo resolvería toyota.com/owners, sección "Fuel information".
- **Etanol (ronda 2: sigue sin resolver):** en el foro de la 4Runner de sexta generación, un usuario afirma que el manual 2025 permite "up to 15%" (pág. 624) y otro cree que dice 10 % [4] `[FORO]`. Otro sitio indica que el vehículo "is not designed to run on ethanol-based fuels (e.g., E85)" [5]. Una página oficial de Toyota de otro modelo limita el etanol al 10 % y prohíbe E15–E85 [8]. **Límite exacto (E10 o E15): [NO VERIFICADO].** Lo seguro es no usar E85.
- **MMT y metales:** los manuales de Toyota de EE. UU. de otros modelos no recomiendan el MMT, porque afecta a las emisiones y puede encender el testigo de falla [9][10]. **(ronda 2)** No se encontró el texto equivalente para la 4Runner 2025–2027 **[NO VERIFICADO]**.
- **La misma familia de motor admite otra calibración:**
  - El Lexus NX/TX 350 exige 91 AKI (RON 96) [11][12].
  - **(ronda 2)** Para la Land Cruiser 250 i-FORCE MAX de EE. UU., los foros se contradicen: 87 como mínimo y 91 recomendado, con una tapa de combustible que dice "Premium Fuel" [63] `[FORO]`. Queda **[NO VERIFICADO]**.
  - La Sequoia i-FORCE MAX 2024 aparece como "premium recommended but not required" [63] `[FORO]`.
  - La 4Runner y la Tacoma son las calibraciones más tolerantes de la familia.

**Conversión AKI (EE. UU.) ↔ RON (Venezuela)**
- AKI = (RON + MON)/2. Toyota da su propia equivalencia: **87 AKI ≈ RON 91** (4Runner) y 91 AKI ≈ RON 96 (Lexus) [3][11]. En la práctica, AKI ≈ RON − 4 a 5. **(ronda 2)** Ecopetrol, citado por La República y El Tiempo, equipara 91 IAD (índice antidetonante) con ~94–95 RON [85][87], lo que es coherente con esa regla.
- Aplicado a Venezuela (**ESTIMACIÓN** con la regla RON − 4 a 5; grados nominales confirmados en la ronda 2 [95][96]):

| Gasolina venezolana | RON | AKI equivalente aprox. | ¿Cumple el mínimo de la 4Runner (87 AKI / RON 91)? |
|---|---|---|---|
| "91", nominal (precio internacional) | 91 | 86–87 | Justo en el límite, sin margen |
| "95", nominal (precio internacional) | 95 | 90–91 | Sí, con +4 RON, si el octanaje real se cumple |
| "Regular", medida [26] (no se sabe si 91 o 95) | 89 | 84–85 | **No** |
| Súper Premium, nominal [25] | 97 | 92–93 | Sí, con margen amplio |
| Súper Premium, medida [26] | 93 / 95–96 | 88–92 | Sí, con +2 a +5 RON |

**Componentes sensibles y efectos mecánicos** (explicación técnica general, sin cambios de fondo en la ronda 2; los TSB específicos del T24A-FTS sobre combustible quedan **[NO VERIFICADO]**)
- **Octanaje insuficiente:** la ECU retrasa el encendido. Resultado: menos potencia, más consumo y gases de escape más calientes, con más carga térmica para el turbo y el catalizador. La detonación persistente puede dañar el motor [3].
- **LSPI (preignición a baja velocidad):** el riesgo depende sobre todo de la química del aceite. Conviene usar aceite API SP / ILSAC GF-6 del grado del manual (0W-20 según [4]). La posible mitigación por el torque eléctrico a bajas rpm es una **inferencia no verificada**.
- **Inyección dual D-4ST** (confirmada en [62]): los inyectores de puerto limpian las válvulas de admisión. Es un **factor mitigante** frente a los motores solo de inyección directa.
- **Agua y sedimentos:** dañan inyectores, bomba de alta presión, filtro y bomba de baja presión. Provocan fallos de encendido (P0300–P0304) [37][38].
- **Azufre alto:** degrada el catalizador y los sensores de oxígeno y de relación aire-combustible (P0420). **(ronda 2)** En 2023, especialistas citados por LaPatilla y Voz de América atribuyeron a la gasolina venezolana "una alta concentración de azufre" que corroe las bombas de combustible, en una ola de incendios de vehículos en el Zulia. PDVSA lo negó [98][99] `[PRENSA, 2023]`. No hay mediciones de azufre de 2025–2026 **[NO VERIFICADO]**.
- **Metales (MMT, plomo, ferroceno):** producen daño permanente en el catalizador y los sensores [9][10].
- **GPF/OPF** en la versión de EE. UU.: **[NO VERIFICADO]**.
- **Interacción con el sistema híbrido:** la batería, el inversor y el motor-generador no tocan el combustible. Un fallo del motor térmico puede limitar el sistema híbrido (modo de emergencia) **[NO VERIFICADO]**.

**Mantenimiento específico del sistema híbrido**
- Refrigerante de la PCU y del sistema de la batería: inspección cada 10.000 millas y cambio a las 100.000 millas o 10 años [20] `[secundaria]`. El calendario oficial del Warranty & Maintenance Guide queda **[NO VERIFICADO]**.
- Aceite 0W-20 [4] `[FORO]`. La capacidad, el tipo de fluido de la caja y el filtro de la toma de aire de la batería quedan **[NO VERIFICADO]**.
- **(ronda 2) Diagnóstico:** un escáner OBD-II genérico solo lee la ECU del motor; **no accede** al control de la batería (BMS), al inversor ni a la unidad de control híbrida (HCU) [113] `[secundaria, taller colombiano]`. Para talleres independientes existe **Techstream Lite**, descrito como una alternativa económica con soporte de nivel de fábrica [112] `[secundaria]`. El precio, la disponibilidad y la licencia de uso en Venezuela quedan **[NO VERIFICADO]**.

### 6.2 — Calidad real del combustible en Venezuela (2025–2026)

**Producción (fechas de cada fuente)**
- Feb-2026: ~35 % de 1,29 millones de barriles diarios [42][43]. Abr-2026: 31 % (399.000 b/d) [44]. Jul-2026: refinerías "feas y oxidadas"; El Palito, unos 146.000 b/d [46][47].
- 6–8 oct-2026: incendio en Cardón (310.000 b/d) que afectó al craqueador catalítico (FCC) [44][45][53]. Su estado al 18-nov queda **[NO VERIFICADO]**.
- Demanda de unos 250.000 b/d. Se importan nafta y componentes de EE. UU. [44][48].
- **(ronda 2) Antecedente:** durante la pandemia Venezuela dejó de producir gasolina e importó parte de Irán [97]. La calidad de la gasolina iraní se cuestionó en 2020 [100] `[PRENSA]`.
- **Contexto político:** reforma de la Ley de Hidrocarburos del 29-ene-2026, firmada por la presidenta encargada Delcy Rodríguez; resoluciones del 7-jul-2026 [49][50][54].

**Grados, octanaje y calidad**
- **(ronda 2) Grados vigentes:** Venezuela vende gasolina **subsidiada** (cupo Patria) y gasolina **"de 91 y 95 octanos" a precio internacional**. Desde 2026 se suma la **Súper Premium de 97** [95] `[PRENSA, mar-2026, citando a El Estímulo]`. Históricamente, la de 95 suponía ~70 % de las ventas de PDVSA y la de 91 ~30 % [96] `[PRENSA, Argus]`.
- **Mediciones de feb-2026** (informales, no ensayos ASTM D2699): regular 89; Súper Premium 93 en taller y 95–96 en una estación de Caracas [26].
- Calidad irregular atribuida al deterioro de la refinación; filtros, inyectores y bombas tapados [37]. CANATAME recomienda seguir el manual [36].
- **2023:** gasolina "rendida con agua… y sucia" [38]. **(ronda 2)** Además, una ola de incendios de vehículos en el Zulia (al menos 9 en abril de 2023) se atribuyó a la gasolina: combustible muy corrosivo, con mucho azufre y falta de solventes, que alcanzó 65 °C en algunos tanques. PDVSA negó la relación, y un experto la atribuyó también a repuestos chinos de baja calidad [98][99] `[PRENSA]`.
- **Sin fuente para 2025–2026:** mediciones de laboratorio, estudios universitarios, norma COVENIN vigente, azufre, oxigenados y metales **[NO VERIFICADO]**. En la ronda 2 no hubo cupo de búsquedas para estos puntos.

**Disponibilidad y precio**
- **Súper Premium en Carabobo (feb-2026):** E/S Guaparo (Av. Bolívar, Valencia) y E/S Bohío (ARC) [31][32]. Fenegas hablaba de unas dos estaciones por estado en Aragua, Carabobo y Lara [35].
- **Precios (abr-2026):** Súper Premium a USD 1,00/L, solo en efectivo y en dólares. Estándar a precio internacional, USD 0,50–0,80/L. Subsidiada: 120 L/mes, unos USD 3 en total [30][29].
- **(ronda 2) Noviembre de 2026:** El Diario confirma que "algunas estaciones de servicio del país ofrecen gasolina Súper Premium de 97 octanos". El cronograma del 16 al 22 de noviembre la lista en estaciones de Caracas (PDV Las Mercedes, Altamira, La Floresta, El Hatillo), pagada solo en efectivo en divisas [92][93] `[PRENSA, 7 y 14 de noviembre de 2026]`.
  - Por las ventas bajas, **PDVSA cambió la estrategia**: las bombas pueden vender los dos tipos de combustible a la vez [94][101] `[PRENSA]`.
  - **La disponibilidad en Carabobo en noviembre de 2026 sigue sin confirmarse** [NO VERIFICADO].
- **Aditivos:** sin evidencia de productos concretos en Venezuela. Criterio técnico: evitar MMT, manganeso, plomo y ferroceno; usar solo detergentes PEA sin metales [9][10].
- **Filtros adicionales:** no instalarlos en la línea de alta presión. Usar un embudo con separador de agua si se reposta desde bidones.

### 6.3 — Evidencia de híbridos y turbos Toyota/Lexus en Venezuela y mercados comparables

**Toyota de Venezuela (ronda 2)**
- **Ya no ensambla en Venezuela.** Descartó reabrir la planta de Cumaná, que necesitaría al menos 170.000 unidades al año para ser rentable. **Importa sus vehículos, principalmente de Indonesia.** Toyota tiene cerca del 10 % de un parque de unos 4 millones de vehículos [91] `[PRENSA, Bloomberg Línea; fecha exacta NO VERIFICADO, probablemente 2024–2025]`.
- **Gama en marzo de 2024:** 8 modelos y 17 versiones (Yaris, Corolla, Fortuner, Hilux, Land Cruiser 300, Land Cruiser 70, Prado, Hiace) [89] `[PRENSA]`. En 2025 destacó la demanda del Agya, Hino regresó al país y se amplió la logística de repuestos originales [90] `[PRENSA]`.
- El Corolla Cross se lanzó en Venezuela hacia 2021 en versión convencional, a USD 38.000 [88]. **No se encontró ningún híbrido vendido oficialmente por Toyota de Venezuela entre 2021 y 2026**: ni Corolla Cross Hybrid, ni RAV4 Hybrid, ni Land Cruiser 250. Ausencia de evidencia, no prueba.
- Los motores de los modelos de Toyota de Venezuela (por ejemplo, si la Land Cruiser 300 llega con el V6 biturbo de inyección directa o la Prado 250 con el 2.4 turbo o el 2.7) quedan **[NO VERIFICADO]**. No apareció ninguna ficha venezolana. Si Toyota de Venezuela vendiera la Land Cruiser 300 con el V35A biturbo de inyección directa, sería un precedente favorable. Lo resolvería toyota.com.ve.
- **Parque de híbridos y experiencias de dueños en Venezuela:** **[NO VERIFICADO]**. No se halló evidencia.

**Mercados comparables, la señal clave (ronda 2: ahora documentada)**

| País | Modelo con T24A-FTS | Oferta oficial | Combustible indicado / contexto | Fuente |
|---|---|---|---|---|
| **Colombia** | Land Cruiser Prado 250 | **2.4 turbo gasolina** (TX, TX-L, First Edition; 276–278 hp) desde 2024; 2.8 diésel después | **Gasolina "extra", RON 95 o superior** (ficha del distribuidor 2026). La "corriente" ronda 81 IAD (~84 RON) [86][87] | [62][73][74] |
| **Perú** | Prado | **2.7 TX-L (atmosférico, 164 hp) + 2.4T VX y VX-L** | Grados locales **[NO VERIFICADO]** | [71][72] |
| **Bolivia** | Land Cruiser 250 Prado | Toyosa la lanzó con **2.4 turbo**; versiones 2.7 (TX, BX) después | Gasolina de 85 octanos con etanol en la alerta de oct-2026 [51] | [76] (sin fecha) |
| **Arabia Saudí** | Prado | **2.4 turbo gasolina, 267 hp / 430 Nm** + 2.8 diésel | Calibración de 267 hp, frente a los 278 hp de Colombia y EE. UU. Combustible **[NO VERIFICADO]** | [65][66][67] |
| **Emiratos** | Prado | **Solo 2.4 turbo gasolina** (sin diésel) | — | [68][69] |
| **Filipinas** | Prado | **2.4 turbo gasolina, en lugar del diésel** | — | [77][78] |
| **México** | Tacoma (fabricada en México) | 2.4 turbo e **i-FORCE MAX híbrida** (TRD Pro HEV 2025; "décimo híbrido de Toyota en México") | — | [83][84] |
| **Chile** | Prado 250 | **Solo 2.8 diésel** | — | [70] |
| **Sudáfrica** | Prado 250 | **Solo 2.8 diésel** | — | [79][80] |
| **Kenia** | Prado 250 | 2.8 diésel (anuncios de concesionarios); una reseña menciona un 2.7 de gasolina | — | [81] |
| Ecuador, Paraguay, Nigeria, Brasil | — | **[NO VERIFICADO]**, sin resultados | — | — |

- **4Runner de sexta generación en Latinoamérica:** llegó primero a Chile. El Carro Colombiano afirma que las versiones híbridas "aún no llegarán a América Latina". En Colombia aparecen anuncios de 4Runner i-FORCE MAX, probablemente de importación particular [75] `[PRENSA / anuncios]`.
- **Land Cruiser 250 con el 2.4 turbo híbrido:** prevista para Norteamérica y China [82]. No se halló venta oficial en Sudamérica.

**Lectura de la señal (ronda 2)**
1. **Toyota no excluye el T24A-FTS de los mercados latinoamericanos con gasolina mediocre** (Colombia, Perú, Bolivia) ni del Golfo. Lo ofrece como motor de gasolina principal de la Prado. Donde lo excluye (Chile, Sudáfrica, Kenia), la razón aparente es la preferencia por el diésel, no una incompatibilidad con el combustible; esa razón queda **[NO VERIFICADO]**.
2. En el mercado con la gasolina base más pobre de los documentados, Colombia (corriente ~84 RON), **Toyota exige la gasolina premium local (RON 95+)**. Esto es coherente con el mínimo estadounidense de RON 91: la corriente no lo alcanza y la siguiente opción disponible es la extra (inferencia).
   - Para Venezuela, la regla práctica es **usar la gasolina de 95 o la Súper Premium, nunca la de 91 ni la subsidiada**.
   - Con la de 95 o la Súper Premium medida en 93, el margen sobre RON 91 es positivo. Sobre el RON 95 "colombiano", el margen es **nulo o negativo** si la Súper Premium solo da 93. Esto no impide el uso, pero eleva la importancia de repostar en estaciones fiables.
3. **El híbrido i-FORCE MAX no tiene presencia oficial en Sudamérica.** No hay red regional de técnicos ni stock de repuestos de esta plataforma en países vecinos. Todo depende de EE. UU. (o de México). **Esta es la señal negativa real, y afecta al servicio, no al combustible.**

### 6.4 — Servicio técnico y repuestos del sistema híbrido en Venezuela

**Política de Toyota de Venezuela (ronda 2)**
- Sobre los vehículos importados por particulares, el gerente de Ventas, Flotilla y Postventa dijo que "la garantía prácticamente se pierde" [89] `[PRENSA, El Diario, mar-2024]`.
- Según su vicepresidente de operaciones, Matteo D'Abrizzio:
  - Los repuestos genuinos se distribuyen **solo a través de sus 47 concesionarios autorizados**.
  - Lo que se instala fuera de la red no tiene garantía; dentro de ella, la garantía del servicio es de un año [90] `[PRENSA, 2025]`.
- **Implicación:** que un concesionario de Toyota de Venezuela acepte servicio pagado (no en garantía) para una 4Runner de EE. UU. **no está descartado ni confirmado** [NO VERIFICADO]. Es improbable que tenga repuestos o software de una plataforma que Toyota de Venezuela no vende.

**Concesionarios en Valencia y Carabobo**
- **[NO VERIFICADO] (ronda 2).** Tres búsquedas no devolvieron nombres de concesionarios oficiales de Carabobo; los resultados eran de Valencia, España.
- Solo apareció Viera Motors (Av. Bolívar, La Ceiba, Valencia), un vendedor de usados, sin confirmación de que sea concesionario oficial [114].
- Lo resolvería el localizador de toyota.com.ve o una llamada a Toyota de Venezuela.

**Talleres de híbridos en Valencia y Caracas**
- **[NO VERIFICADO] (ronda 2).** Dos búsquedas específicas no hallaron ningún taller con evidencia pública. Solo aparecieron talleres de Colombia, como C3 Care Car Center en Bogotá [113].
- **Lectura:** la ausencia de presencia web no prueba que no existan talleres (en Venezuela muchos operan por Instagram o WhatsApp). Sí indica que **no hay un proveedor reconocido y verificable**.

**Techstream en Venezuela**
- **[NO VERIFICADO].** No hubo resultados venezolanos.
- Existe Techstream Lite para independientes [112]. La compra legal de una suscripción TIS por la LLC en EE. UU. y su uso en Venezuela están por confirmar (términos de licencia y territorio).

**Repuestos y precios OEM en EE. UU. (ronda 2: referencias parciales, ninguna confirmada para la 4Runner con su VIN)**

| Pieza | Referencia encontrada | Precio | Estado |
|---|---|---|---|
| Batería híbrida | G9510-60011 "Drive Motor Battery Pack" listada para Tacoma, Tundra y Sequoia [103]. KBB: "No Pricing Data Available" para la 4Runner i-FORCE MAX [102] | Sin precio. Referencia genérica: los packs Toyota se venden por internet en concesionarios a **más de USD 3.000** (por ejemplo, Camry Hybrid G9510-33101, USD 3.366) [107]. Instalada, USD 3.000–8.000 [108] | [NO VERIFICADO para la 4Runner] |
| Inversor con convertidor | G92A0-60021 "Inverter Assembly HEV" (Tacoma y Land Cruiser, incluye convertidor DC) [104] | Sin precio. Referencia de otro vehículo: el inversor de la Grand Highlander (G92A0-48393) se vende a **USD 4.262** [105] | [NO VERIFICADO para la 4Runner] |
| Turbo T24A-FTS | Pieza 17201-25010 (Crown, Grand Highlander) [106] | **USD 2.458 (MSRP USD 3.618)** | Encaje en la 4Runner [NO VERIFICADO] |

**Courier Miami–Venezuela (ronda 2)**
- No se encontró una tarifa verificada por kilo.
- Plazos publicados:
  - Aéreo de 3–5 días hábiles según un operador (salidas los viernes) [110], o de 7–15 días con Tealca según una guía [109].
  - Marítimo de 15–21 días hábiles [110].
  - Valencia está entre los destinos de entrega más rápida [109].
- Avisos:
  - USPS suspendió el servicio a Venezuela en julio de 2026, pero otra fuente indica que no había suspensión al 22 de octubre de 2026 [109][111]. Hay que verificarlo.
  - Conviene verificar a los destinatarios contra el programa de sanciones de OFAC para Venezuela [109].
  - **[NO VERIFICADO]:** la tarifa por kilo y las restricciones para enviar la batería NiMH (UN3496).

**Riesgo de inmovilización y contingencia**
- **ESTIMACIÓN:** 2 / 4 / 8 semanas por evento.
- Plan propuesto:
  1. Diagnóstico propio (Techstream Lite o TIS, comprado por la LLC).
  2. Stock de consumibles.
  3. Cuenta en un portal OEM de EE. UU. con el VIN.
  4. Un técnico de alto voltaje identificado **antes** de importar.

### 6.5 — Otros factores ambientales
Sin cambios de fondo en la ronda 2.
- **Calor:** acelera la degradación de la batería NiMH y exige más a la refrigeración del inversor [20][21]. **(ronda 2)** Un taller colombiano atribuye la mayoría de las fallas prematuras de baterías híbridas a un mantenimiento deficiente de su refrigeración (ventiladores y conductos) [113] `[secundaria]`.
- **No enchufable:** los apagones no afectan a la carga, pero pueden dejar sin servicio las bombas de las estaciones [16][17]. Los apagones de Carabobo en 2025–2026 quedan **[NO VERIFICADO]**.
- **Batería de 12 V:** usar un mantenedor de carga si el vehículo pasa mucho tiempo parado.
- **Polvo, vadeo y toma de aire de la batería:** **[NO VERIFICADO]** con el manual. La batería está sellada y bajo el piso [15].

### 6.6 — Conclusión técnica

**Calificación del riesgo: MEDIO (global, sin cambio en la ronda 2)**

| Componente | Ronda 1 | **Ronda 2** | Por qué cambió o se mantuvo |
|---|---|---|---|
| **Combustible, motor T24A-FTS** (igual en la versión híbrida y en la no híbrida) | MEDIO (ALTO solo con estándar) | **MEDIO, se mantiene y se refuerza** | La EPA confirma "regular" en el año modelo 2026 [57]. Venezuela vende 95 RON y 97 RON, y la Súper Premium sigue en noviembre de 2026 [92][95]. Toyota vende este mismo motor en Colombia, Perú, Bolivia y el Golfo, exigiendo la premium local [62]. Riesgos residuales: calidad irregular (agua, azufre [98]), refinerías al 31–35 % e incendio en Cardón. Sería ALTO si solo se pudiera usar gasolina de 91 o subsidiada. |
| **Sistema híbrido** (batería NiMH, inversor, motor-generador, servicio) | MEDIO | **ALTO, sube** (sin mitigación) / **MEDIO** (con mitigación) | La probabilidad de falla sigue siendo baja: NiMH madura, sellada, sin contacto con el combustible. Pero ahora está **documentado** que: (a) Toyota de Venezuela considera perdida la garantía de los vehículos importados por particulares [89]; (b) sus repuestos genuinos solo salen de su red de 47 concesionarios, que no vende esta plataforma [90]; (c) no vende híbridos [88][89][91]; (d) el i-FORCE MAX no tiene presencia oficial en Sudamérica [75][82]; (e) no apareció ningún taller híbrido ni Techstream en Venezuela; (f) un escáner genérico no accede a la batería, el inversor ni la unidad de control híbrida [113]. Cualquier testigo del sistema híbrido puede inmovilizar el vehículo durante semanas. |
| **Global** | MEDIO | **MEDIO** | El riesgo que más preocupa al cliente, el combustible, es manejable. El riesgo híbrido es de logística y servicio, **mitigable** con medidas conocidas (diagnóstico propio, repuestos vía la LLC, técnico identificado). Pasa a **ALTO** si no se cumple C2. |

**Condiciones para mantener el riesgo en MEDIO**
- **C1 (ronda 2: parcialmente cumplida):** que haya gasolina de 95 RON o Súper Premium fiable en Valencia. La Súper Premium está confirmada en Caracas en noviembre de 2026 [92]; Carabobo sigue sin confirmar.
- **C2 (sin cumplir):** contar con diagnóstico Techstream propio o de un taller, y con un técnico de alto voltaje identificado, antes de comprar.
- **C3 (parcialmente cumplida):** la EPA confirma "regular" para el año modelo 2026. Falta leer el texto del manual 2026/2027.

**Sobre la 🛑 ALERTA DE ALCANCE:** **no se emite**. La ronda 2 eliminó la principal duda pendiente de que Toyota excluyera este motor en mercados con mal combustible: no lo hace. Ningún hallazgo verificado hace inviable la operación.

**Costo anual estimado (15.000 km/año) — ESTIMACIONES** (ronda 2: supuestos de consumo y repuestos revisados)

Supuestos:
- Consumo de 10 / 11,5 / 13 L/100 km. El piso es la cifra EPA de **23 mpg combinados ≈ 10,2 L/100 km** [57][58]; el resto se añade por tráfico, aire acondicionado y neumáticos todoterreno.
- Combustible en Venezuela a USD 1,00 / 1,00 / 1,20 por litro (Súper Premium). Con gasolina de 95 a USD 0,50 el costo bajaría, pero con más riesgo de calidad.
- Gasolina regular en EE. UU. a USD 3,00 / 3,30 / 3,60 por galón **[NO VERIFICADO]**.

| Concepto | Venezuela mín / prob / máx (USD/año) | EE. UU. mín / prob / máx (USD/año) |
|---|---|---|
| Combustible (1.500 / 1.725 / 1.950 L) | 1.500 / 1.725 / 2.340 | 1.190 / 1.500 / 1.850 |
| Mantenimiento con calendario severo y piezas importadas | 500 / 900 / 1.500 | 200 / 300 / 400 |
| Aditivo PEA sin metales | 40 / 80 / 120 | 0 |
| Stock y courier, amortizados | 200 / 400 / 800 | 0 |
| Diagnóstico (Techstream Lite o TIS más interfaz), amortizado en 5 años | 200 / 400 / 600 | 0 |
| **Total** | **2.440 / 3.505 / 5.360** | **1.390 / 1.800 / 2.250** |
| **Incremental** | **≈ 1.000 / 1.700 / 3.200** | — |

**Falla mayor en 5 años — ESTIMACIONES** (sin datos de flota; ronda 2: los costos se apoyan en las referencias OEM de 6.4)

| Falla | Probabilidad mín / prob / máx | Costo por evento (pieza + courier + mano de obra, USD) | Costo esperado prob. |
|---|---|---|---|
| Batería híbrida NiMH | 1 % / 3 % / 8 % | 3.500 / 5.000 / 8.000 (pack de concesionario >3.000 [107][108]) | ~150 |
| Inversor / PCU | 1 % / 2 % / 5 % | 5.000 / 6.500 / 10.000 (referencia de USD 4.262 de otro modelo [105]) | ~130 |
| Turbo | 2 % / 4 % / 10 % | 2.500 / 3.500 / 5.000 (pieza de USD 2.458–3.618 [106]) | ~140 |
| **Al menos una** | **≈4 % / 9 % / 21 %** | — | **≈ USD 420 en 5 años (máx. ≈ USD 1.700)**, más 2–8 semanas de inmovilización |
| Motor dañado por detonación o LSPI (solo con uso habitual de gasolina de RON ≤ 91 o de calidad dudosa) | 1 % / 3 % / 10 % | 8.000 / 12.000 / 15.000 | — |
| **(ronda 2)** Falla menor del sistema híbrido que inmoviliza sin diagnóstico (sensor, software, 12 V, relé) | 5 % / 12 % / 25 % | 200 / 800 / 2.500 + días o semanas de espera | ~100 |

**Medidas de mitigación** (ronda 2: se añaden 1b, 4b y 8)
1. Repostar solo Súper Premium o, como respaldo, gasolina de 95 en estaciones fiables. **Nunca** la de 91 ni la subsidiada. Mantener el tanque por encima de 1/4 y llevar un bidón con Súper Premium para rutas largas.
   - **1b.** Registrar en un cuaderno o una app la estación de cada repostaje, para detectar cuál causa testigos o detonación.
2. Nada de MMT, manganeso ni plomo. Usar solo limpiadores PEA sin metales.
3. Aceite 0W-20 API SP / ILSAC GF-6 importado, cada 5.000–7.500 km. Filtro de aire cada 10.000–15.000 km, o antes tras uso todoterreno.
4. Llevar un escáner OBD-II para el motor.
   - **4b.** Comprar, vía la LLC, **Techstream Lite o una suscripción TIS con interfaz J2534** [112]: es el único acceso a la batería, el inversor y la unidad de control híbrida [113]. Confirmar la licencia antes de comprar.
5. Comprar stock antes del embarque, vía la LLC: filtros, bujías, refrigerante Toyota, aceite y sensores de relación aire-combustible. Mantener una cuenta OEM con el VIN.
6. Mantener libre la toma de aire de la batería y limpio el radiador del inversor. No vadear por encima de lo que indique el manual.
7. Aplicar todas las campañas y actualizaciones de software en EE. UU. antes de exportar.
8. **(ronda 2)** Antes de comprar, contactar al menos con un concesionario de Toyota de Venezuela en Carabobo y con un taller de alto voltaje (ver "Preguntas abiertas"). Si ninguno puede diagnosticar el i-FORCE MAX, aplicar la contingencia.

**Alternativa de contingencia**
- **4Runner sin híbrido (i-FORCE 2.4 turbo, por ejemplo TRD Off-Road o TRD Off-Road Premium):**
  - Elimina el componente que la ronda 2 subió a ALTO: batería, inversor, motor-generador y diagnóstico híbrido.
  - **El riesgo del combustible persiste igual**, porque el motor es el mismo T24A-FTS turbo de inyección D-4ST.
  - **(ronda 2)** Es justamente la configuración que Toyota vende oficialmente en Colombia, Perú, Bolivia, el Golfo y Filipinas (en la Prado), lo que facilita encontrar técnicos con experiencia en ese motor en la región; su disponibilidad en Venezuela queda **[NO VERIFICADO]**.
  - La Trailhunter no existe sin híbrido [1].
  - Con esta versión, el riesgo global bajaría de MEDIO a **MEDIO-BAJO**.
- **Referencia: Toyota atmosférica o diésel** (Hilux o Fortuner de Toyota de Venezuela importadas de Indonesia [91]; Land Cruiser 70; Prado con 2.7 L 2TR-FE de 164 hp como la de Perú [72]). Su perfil de riesgo de combustible y servicio es claramente menor y tiene garantía y repuestos en la red de 47 concesionarios. Los motores concretos que ofrece Toyota de Venezuela quedan **[NO VERIFICADO]**.

## Cifras clave (tabla: concepto | valor | rango mín/prob/máx si es estimación | fuente [n] | fecha de la fuente)

| Concepto | Valor | Rango mín/prob/máx (si es estimación) | Fuente [n] | Fecha de la fuente |
|---|---|---|---|---|
| Tren motriz de la Trailhunter | Solo i-FORCE MAX | — | [1] | 2024–2025 |
| Potencia y torque i-FORCE MAX | 326 hp / 465 lb-ft | — | [2][19] | 2026 |
| Potencia y torque i-FORCE (no híbrido) | 278 hp / 317 lb-ft | — | [1] | 2024–2025 |
| Motor T24A-FTS (ronda 2: D-4ST confirmada por distribuidor) | 2.393 cm³; 11,0:1; D-4ST directa e indirecta; turbo | — | [13][62] | 2021; mar-2026 |
| Batería híbrida | NiMH sellada, 288 V, bajo el piso | ~1,87 kWh [NO VERIFICADO con Toyota] | [15][16] | 2025–2026 |
| Octanaje mínimo, 4Runner (manual 2025, pág. 617) | 87 AKI (RON 91) o más | — | [3][4] | 2024–2025 |
| **(ronda 2)** Combustible según la EPA, 4Runner Hybrid 4WD 2026 | Regular; 23 / 24 mpg (ciudad / carretera) | — | [57] | 2026 |
| **(ronda 2)** Consumo EPA de la Hybrid Trailhunter 2026 | 23 mpg combinados (≈10,2 L/100 km) | — | [58] | 2026 |
| **(ronda 2)** Tanque | 19,0 galones (≈72 L) | — | [59] | 2026 |
| Etanol máximo | E10 o E15, en conflicto | [NO VERIFICADO] | [4][8] | — |
| Lexus NX/TX 350 (mismo motor) | 91 AKI (RON 96) | — | [11][12] | 2022–2025 |
| **(ronda 2)** Prado 2.4T en Colombia: combustible | Extra, RON 95 o superior | — | [62] | mar-2026 |
| **(ronda 2)** Gasolina corriente en Colombia | 81 IAD (~84 RON) | Vigencia [NO VERIFICADO] | [86][87] | 2006 / s.f. |
| **(ronda 2)** Mercados con Prado 2.4T oficial | Colombia, Perú, Bolivia, Arabia Saudí (267 hp), Emiratos, Filipinas | — | [62][65][68][71][76][77] | 2024–2026 |
| **(ronda 2)** Mercados sin 2.4T (solo diésel) | Chile, Sudáfrica, Kenia | — | [70][79][81] | 2024 |
| **(ronda 2)** i-FORCE MAX con presencia oficial en Latinoamérica | Solo México (Tacoma HEV) | — | [83][84] | 2024–2025 |
| **(ronda 2)** Grados en Venezuela | Subsidiada; 91 y 95 a precio internacional; Súper Premium 97 | — | [95][96] | mar-2026 |
| Súper Premium: precio | USD 1,00/L, efectivo en USD | — | [25][30] | Feb–abr 2026 |
| **(ronda 2)** Súper Premium a la venta en noviembre de 2026 | Sí (estaciones de Caracas listadas) | Carabobo [NO VERIFICADO] | [92][93] | 7 y 14 nov 2026 |
| Octanaje medido | Regular 89; Súper Premium 93 y 95–96 | Informal | [26] | ~Feb 2026 |
| Estándar a precio internacional | USD 0,50/L | 0,50–0,80 | [29][30] | Abr 2026 |
| Uso de la capacidad de refinación | 35 % (feb); 31 % (abr) | — | [42][44] | 2026 |
| Incendio en Cardón (FCC afectado) | 6–8 oct 2026 | Estado actual [NO VERIFICADO] | [44][45][53] | Oct 2026 |
| **(ronda 2)** Toyota de Venezuela: garantía de vehículos importados por particulares | "Prácticamente se pierde" | — | [89] | Mar 2024 |
| **(ronda 2)** Toyota de Venezuela: canal de repuestos genuinos | Solo 47 concesionarios autorizados | — | [90] | 2025 |
| **(ronda 2)** Toyota de Venezuela: producción local | No ensambla; importa sobre todo de Indonesia | — | [91] | 2024–2025 (s.f.) |
| **(ronda 2)** Precio de referencia de una batería HV Toyota (concesionario) | > USD 3.000 (Camry: USD 3.366) | Instalada, 3.000–8.000 | [107][108] | 2025–2026 |
| **(ronda 2)** Precio de referencia de un inversor (Grand Highlander) | USD 4.262 | Para la 4Runner [NO VERIFICADO] | [105] | 2025–2026 |
| **(ronda 2)** Turbo 17201-25010 (Crown, Grand Highlander) | USD 2.458 (MSRP 3.618) | Encaje [NO VERIFICADO] | [106] | 2026 |
| **(ronda 2)** Plazo del courier Miami–Venezuela | Aéreo 3–15 días; marítimo 15–21 días hábiles | Tarifa por kilo [NO VERIFICADO] | [109][110] | 2026 |
| Costo anual en Venezuela | — | USD 2.440 / 3.505 / 5.360 | Estimación (6.6) | 2026-11-18 |
| Costo incremental frente a EE. UU. | — | USD 1.000 / 1.700 / 3.200 al año | Estimación (6.6) | 2026-11-18 |
| Probabilidad de falla mayor en 5 años | — | 4 % / 9 % / 21 % | Estimación (6.6) | 2026-11-18 |
| Costo por evento de falla mayor | — | USD 2.500 – 10.000 | Estimación con [105]–[108] | 2026-11-18 |
| Inmovilización por evento | — | 2 / 4 / 8 semanas | Estimación | 2026-11-18 |

## Riesgos detectados
1. **Gasolina de 91 o subsidiada por debajo del mínimo efectivo.** La de 91 nominal no deja margen y la medida dio 89 [26][95]. **Mitigación:** usar solo 95 o Súper Premium.
2. **Suministro de Súper Premium.** Sigue en noviembre de 2026, confirmado en Caracas; Carabobo está por confirmar [92]. Ventas bajas [101], refinerías al 31–35 % e incendio en Cardón [42][44][45].
3. **Calidad irregular** (agua, sedimentos, azufre). Hay antecedentes de corrosión e incendios en 2023 [38][98][99] y no hay datos de laboratorio de 2025–2026.
4. **(ronda 2, sube) Servicio híbrido inexistente o no verificable en Venezuela.** Toyota de Venezuela no vende híbridos; la garantía de los vehículos importados por particulares "prácticamente se pierde" [89]; los repuestos genuinos solo salen de su red, que no tiene esta plataforma [90]; no apareció ningún taller híbrido ni Techstream; el i-FORCE MAX no tiene presencia oficial en Sudamérica [75][82]. **Es el riesgo principal del proyecto.**
5. **Sin garantía efectiva.** La batería, el inversor y el turbo quedan a cargo del cliente, con costos de USD 2.500–10.000 por evento [105]–[108].
6. **Calor.** Degrada la batería NiMH y exige más a la refrigeración del inversor [20][113].
7. **Logística.** Plazos de 1–8 semanas. El estado de USPS es contradictorio, hay que verificar contra OFAC y las restricciones para enviar baterías NiMH están por confirmar [109][111].
8. **Aditivos con MMT o metales** [9][10].
9. **(ronda 2)** Margen de octanaje estrecho si se toma como referencia el criterio de Toyota en Colombia (RON 95+) y la Súper Premium solo da 93 [26][62].

## Preguntas abiertas (incluye preguntas concretas para hacerle al concesionario Toyota de Valencia y a un taller de híbridos)

**Para el concesionario Toyota de Valencia o Carabobo (red de Toyota de Venezuela):**
1. ¿Dan servicio pagado (fuera de garantía) a una 4Runner 2026/2027 i-FORCE MAX importada de EE. UU. por un particular? Toyota de Venezuela dijo en 2024 que la garantía "prácticamente se pierde" [89]: ¿atienden igualmente el mantenimiento y el diagnóstico?
2. ¿Tienen Techstream / GTS+ con licencia que cubra modelos norteamericanos con T24A-FTS e híbrido de un motor? ¿Pueden aplicar actualizaciones de software?
3. ¿Tienen técnicos certificados en alto voltaje? ¿Han atendido alguna Tundra, Sequoia, Tacoma o Land Cruiser i-FORCE MAX, o cualquier híbrido Toyota?
4. ¿Pueden pedir piezas para un VIN de EE. UU. (batería, inversor, turbo, sensores de relación aire-combustible)? ¿Con qué plazos?
5. ¿Qué motor llevan las Land Cruiser 300 y Prado que venden hoy (V6 biturbo, 2.4 turbo, 2.7, diésel)? ¿Qué gasolina recomiendan para ellas?
6. ¿Han visto detonación, catalizadores dañados o inyectores tapados en motores turbo de inyección directa por la gasolina local?

**Para un taller independiente de híbridos (Valencia o Caracas):**
1. ¿Diagnostican híbridos Toyota de un solo motor con embrague (i-FORCE MAX) o solo del tipo Prius?
2. ¿Qué escáner usan (Techstream legítimo o Lite, Autel, Launch)? ¿Leen los bloques de celdas NiMH y el inversor?
3. ¿Reacondicionan baterías NiMH y prueban inversores? ¿Con qué garantía y precios?
4. ¿Cuántos casos han tenido de daño por combustible en turbos de inyección directa en 2025–2026? ¿En qué estaciones o zonas?
5. ¿Qué estaciones de Carabobo venden hoy Súper Premium o gasolina de 95 fiables?

**Pendientes de verificación tras la ronda 2:**
- Texto de la sección "Fuel information" del manual 2026 (OM35C28U) y del 2027 (octanaje, etanol E10/E15, MMT, metanol); vadeo; toma de aire de la batería; capacidad y grado del aceite.
- Warranty & Maintenance Guide 2026/2027 y TSB o *recalls* de NHTSA.
- Toyota de Venezuela: motores de sus modelos, lista de concesionarios en Carabobo, política escrita sobre vehículos importados.
- Ecuador, Paraguay, Nigeria y Brasil (oferta de la Prado y la Tacoma). Combustible indicado para la Prado 2.4T en Arabia Saudí y Perú.
- Norma COVENIN, mediciones de laboratorio, azufre y estado de Cardón al 18 de noviembre de 2026.
- Precios OEM de la 4Runner por VIN (batería, inversor, turbo), tarifa del courier por kilo y restricciones para enviar baterías NiMH.
- Talleres de híbridos en Venezuela (Instagram o WhatsApp, fuera del alcance de WebSearch).

## Fuentes (lista numerada: título — URL — fecha de la fuente — consultada 2026-11-18 — tipo: primaria/secundaria/prensa/foro)
Nota: todas se consultaron a través de resúmenes y extractos del buscador; WebFetch estuvo bloqueado en ambas rondas.

1. The 2026 Toyota 4Runner: Engineered for Exploration (Toyota Pressroom) — https://pressroom.toyota.com/the-2026-toyota-4runner-engineered-for-exploration/ — 2024–2025 — consultada 2026-11-18 — primaria (vía extracto)
2. Toyota Canadá — 4Runner, características y beneficios (materiales 2027) — https://www.toyota.ca/en/vehicles/4runner/features-benefits/ — 2026 — consultada 2026-11-18 — primaria (vía extracto)
3. 4Runner6G Forum — "What gas octane level required for iForce Max hybrid 87 or 91" — https://www.4runner6g.com/forum/threads/what-gas-octane-level-required-for-iforce-max-hybrid-87-or-91.3263/ — 2024–2025 — consultada 2026-11-18 — foro (reproduce el manual)
4. 4Runner6G Forum — "Recommended regular fuel gas octane 87 engine oil grade 0W-20 2025 4Runner 6th gen" (manual 2025, págs. 617 y 624) — https://www.4runner6g.com/forum/threads/recommended-regular-fuel-gas-octane-87-engine-oil-grade-0w-20-2025-4runner-6th-gen.2056/ — 2024–2025 — consultada 2026-11-18 — foro (reproduce el manual)
5. 6thgen4runner.com — "2025+ (6th Gen) Toyota 4Runner Fuel Type & Tank Capacity" — https://6thgen4runner.com/threads/2025-6th-gen-toyota-4runner-fuel-type-tank-capacity.648/ — 2024–2025 — consultada 2026-11-18 — foro
6. 4Runner6G — "Different owners manual starting 2026 June production 4Runner" — https://www.4runner6g.com/forum/threads/different-owners-manual-starting-2026-june-production-4runner.10728/ — 2026 — consultada 2026-11-18 — foro
7. manuals.plus — Toyota 4Runner 2025 (OM35B85U) — https://manuals.plus/hmn/m/b9266332aeec716c7f1e26a4b7aab797d1e7ed7ca98e3dc923f7314d8363fe1a — 2025 — consultada 2026-11-18 — secundaria
8. Toyota — Fuel information (manual OM04011U, otro modelo) — https://assets.sia.toyota.com/publications/en/om-x/OM04011U/topics/chapter8/ch08se010402.html — s.f. — consultada 2026-11-18 — primaria (vía extracto)
9. 2016 Prius Owner's Manual (EE. UU.), sección de combustible — https://attachments.priuschat.com/attachment-files/2019/06/168344_2016_Prius_Owners_Manual_-_US_-_fuel_info.pdf — 2016 — consultada 2026-11-18 — primaria (copia)
10. Toyota Tundra Owner's Manual, pág. 612, en ManualsLib — https://www.manualslib.com/manual/1407350/Toyota-Tundra.html?page=612 — s.f. — consultada 2026-11-18 — secundaria (copia)
11. ClubLexus — "Fuel 87 or 91" (NX de segunda generación) — https://www.clublexus.com/forums/nx-2nd-gen-2022-current/980704-fuel-87-or-91-a.html — 2022–2025 — consultada 2026-11-18 — foro
12. Consumer Reports — "Cars that require premium fuel do not always benefit from it" — https://www.consumerreports.org/cars/fuel-economy-efficiency/cars-that-require-premium-fuel-do-not-always-benefit-from-it-a1099718013/ — s.f. — consultada 2026-11-18 — prensa
13. Toyota-club.net — FAQ del motor T24 — https://www.toyota-club.net/files/faq/21-09-20_faq_t24-engine_en.htm — 2021-09-20 — consultada 2026-11-18 — secundaria técnica
14. MotorReviewer — T24A-FTS — https://www.motorreviewer.com/engine.php?engine_id=216 — s.f. — consultada 2026-11-18 — secundaria
15. Reliable Toyota — showroom 2025 4Runner i-FORCE MAX — https://www.reliabletoyotamo.com/showroom/2025/Toyota/4Runner+i-FORCE+MAX/SUV.htm — 2025 — consultada 2026-11-18 — secundaria (concesionario)
16. North Hollywood Toyota — "2026 Toyota 4Runner Hybrid vs. 4Runner" — https://www.northhollywoodtoyota.com/blog/2026-toyota-4runner-hybrid-vs-gas — 2025–2026 — consultada 2026-11-18 — secundaria (concesionario)
17. Tustin Toyota — 2026 Toyota 4Runner i-FORCE MAX Specs — https://www.tustintoyota.com/research/2026-toyota-4runner-hybrid-specs/ — 2025–2026 — consultada 2026-11-18 — secundaria (concesionario)
18. Kelley Blue Book — 2026 Toyota 4Runner i-FORCE MAX Specs — https://www.kbb.com/toyota/4runner-i-force-max/2026/specs/ — 2025–2026 — consultada 2026-11-18 — secundaria
19. Motor1 — "Toyota's Hybrid Truck System Will Be a Game-Changer…" — https://www.motor1.com/features/717505/toyota-i-force-max-hybrid-truck-explainer/ — 2023–2024 — consultada 2026-11-18 — prensa
20. Olathe Toyota Parts — "i-FORCE MAX hybrid maintenance: OEM care" — https://parts.olathetoyota.com/blog/i-force-max-hybrid-maintenance-oem-care — 2025–2026 — consultada 2026-11-18 — secundaria
21. Tacoma4G Forum — "Hybrid automated thermal management system" — https://www.tacoma4g.com/forum/threads/hybrid-automated-thermal-management-system.22761/ — 2025–2026 — consultada 2026-11-18 — foro
22. Top Gear — Tacoma hybrid tech — https://www.topgear.com/car-news/electric/toyotas-new-tacoma-truck-gets-hybrid-tech-and-shock-absorbers-seats — 2023 — consultada 2026-11-18 — prensa
23. 4Runner6G — "2027 4Runner changes" — https://www.4runner6g.com/2027-4runner-changes/ — 2026 — consultada 2026-11-18 — foro/blog
24. TFLcar — "2027 Toyota TRD Pro Models Get Honey-Hued Signature Color" — https://tflcar.com/2026/07/2027-toyota-4runner-trd-pro-new-color-update/ — jul-2026 — consultada 2026-11-18 — prensa
25. Efecto Cocuyo — "Pdvsa inicia plan piloto con gasolina Súper Premium de 97 octanos a $1 por litro en Caracas" — https://efectococuyo.com/economia/pdvsainicia-plan-piloto-con-gasolina-super-premium-de-97-octanos-a-1-por-litro-en-caracas/ — feb-2026 — consultada 2026-11-18 — prensa
26. El Pitazo — "Gasolina Súper Premium: ¿tiene realmente el octanaje que prometió Pdvsa?" — https://elpitazo.net/economia/gasolina-super-premium-tiene-realmente-el-octanaje-que-prometio-pdvsa/ — ~feb-2026 — consultada 2026-11-18 — prensa
27. El Diario — "Gasolina 'Súper Premium' en Venezuela: ¿en qué se diferencia de los otros octanajes?" — https://eldiario.com/2026/02/19/gasolina-super-premium-venezuela-en-que-se-diferencia-otros-octanajes/ — 2026-02-19 — consultada 2026-11-18 — prensa
28. El Diario — "Reportaron plan piloto de distribución de gasolina 'Súper Premium' en Caracas" — https://eldiario.com/2026/02/18/plan-piloto-de-distribucion-de-gasolina-super-premium-en-caracas/ — 2026-02-18 — consultada 2026-11-18 — prensa
29. El Diario — "Estaciones de gasolina 'Súper Premium' en Caracas se preparan para ofrecer combustible estándar" — https://eldiario.com/2026/04/15/estaciones-super-premium-gasolina-estandar-caracas/ — 2026-04-15 — consultada 2026-11-18 — prensa
30. CNN en Español — "El precio del combustible premium en Venezuela, más caro y solo en dólares" — https://cnnespanol.cnn.com/2026/04/15/venezuela/venezuela-sistema-combustibles-subsidiado-premium-verde-rojo-orix — 2026-04-15 — consultada 2026-11-18 — prensa
31. Noticias24 Carabobo — "Gasolina Súper Premium en Carabobo ya se vende en estas estaciones" — https://noticias24carabobo.com/gasolina-super-premium-en-carabobo-ya-se-vende-en-estas-estaciones/ — feb-2026 — consultada 2026-11-18 — prensa local
32. Sandy Aveledo — "Ya llegó la gasolina premium a Carabobo" — https://sandyaveledo.net/ya-llego-la-gasolina-premium-a-carabobo/ — feb-2026 — consultada 2026-11-18 — prensa local/blog
33. El Carabobeño — "Venta de gasolina cayó tras plan Súper Premium" — https://www.el-carabobeno.com/venta-de-gasolina-cayo-tras-plan-super-premium/ — 2026 — consultada 2026-11-18 — prensa
34. El Impulso — "Fedengas propone homogeneizar las estaciones de servicios…" — https://www.elimpulso.com/2026/03/11/fedengas-propone-homogeneizar-las-estaciones-de-servicios-para-la-venta-de-gasolina-super-premium-11mar/ — 2026-03-11 — consultada 2026-11-18 — prensa
35. Valora Analitik — "Gasolineras de Venezuela, en alerta tras nuevo esquema de gasolina premium" — https://www.valoraanalitik.com/gasolineras-de-venezuela-en-alerta-tras-nuevo-esquema-de-gasolina-premium/ — 2026 — consultada 2026-11-18 — prensa
36. MSC Noticias — "¿Gasolina de 97 octanos? Lo que tu motor de verdad necesita" — https://www.mscnoticias.com.ve/2026/03/gasolina-de-97-octanos-lo-que-tu-motor-de-verdad-necesita/ — mar-2026 — consultada 2026-11-18 — prensa
37. El Tequeño — "Mala calidad de gasolina en Venezuela provoca averías en motores de vehículos" — https://xn--eltequeo-j3a.com/mala-calidad-de-gasolina-en-venezuela-provoca-averias-en-motores-de-vehiculos-no-trae-el-octanaje-suficiente/ — fecha [NO VERIFICADO] — consultada 2026-11-18 — prensa
38. El Nacional — "Problemas en el combustible: gasolina rendida con agua…" — https://www.elnacional.com/2023/05/problemas-en-el-combustible-gasolina-rendida-con-agua-sin-aditivos-necesarios-y-sucia-causa-danos-e-incendios-en-vehiculos/ — may-2023 — consultada 2026-11-18 — prensa
39. Impacto VE — "Gasolina de 97 octanos: lo que se sabe del plan piloto de PDVSA" — https://impactove.com/gasolina-de-97-octanos-lo-que-se-sabe-del-plan-piloto-de-pdvsa — 2026 — consultada 2026-11-18 — prensa
40. El Estímulo — "El petróleo venezolano se reinventa… ¿el precio de la gasolina también?" — https://elestimulo.com/elinteres/energia/2026-02-19/petroleo-precio-gasolina/ — 2026-02-19 — consultada 2026-11-18 — prensa
41. Índice Gasolina Venezuela — https://gasolina.com.ve/ — s.f. (nov-2026) — consultada 2026-11-18 — secundaria no oficial
42. Reuters (vía TradingView) — "Venezuela's refineries working at about 35% of capacity" — https://www.tradingview.com/news/reuters.com,2026:newsml_L1N3ZF19E:0-venezuela-s-refineries-working-at-about-35-of-capacity-sources-say/ — feb-2026 — consultada 2026-11-18 — prensa
43. Inspectioneering — "Venezuela's Refineries Boost Processing to 35% of Capacity" — https://inspectioneering.com/news/2026-02-23/11952/venezuelas-refineries-boost-processing-to-35-of-capacity — 2026-02-23 — consultada 2026-11-18 — prensa
44. Energy News Beat — "Venezuela's Cardón Refinery Halted After Fire…" — https://energynewsbeat.co/downstream/venezuelas-cardon-refinery-halted-after-fire-taking-310000-bpd-offline/ — oct-2026 — consultada 2026-11-18 — prensa
45. Democracy Now — "Venezuela's Second-Largest Refinery Idles…" — https://www.democracynow.org/2026/10/8/headlines/venezuelas_second_largest_refinery_idles_as_natural_gas_line_rupture_triggers_fire — 2026-10-08 — consultada 2026-11-18 — prensa
46. Reuters (vía KWSN) — "'Ugly and rusty,' Venezuela's refineries are relics…" — https://kwsn.com/2026/07/29/ugly-and-rusty-venezuelas-refineries-are-relics-that-will-be-hard-to-revive/ — 2026-07-29 — consultada 2026-11-18 — prensa
47. Pipeline & Gas Journal — "Venezuela's Refineries Crumble Despite Oil Export Rebound" — https://pgjonline.com/news/2026/july/venezuelas-refineries-crumble-despite-oil-export-rebound — jul-2026 — consultada 2026-11-18 — prensa
48. Devdiscourse (Reuters) — "Venezuela's Refining Struggles Amid Recovery Efforts" — https://www.devdiscourse.com/article/headlines/3811263-venezuelas-refining-struggles-amid-recovery-efforts — 2026 — consultada 2026-11-18 — prensa
49. AP (vía ADN) — "Venezuela's acting president signs oil industry overhaul…" — https://www.adn.com/nation-world/2026/01/29/venezuelas-acting-president-signs-oil-industry-overhaul-easing-state-control-to-lure-investors/ — 2026-01-29 — consultada 2026-11-18 — prensa
50. Cleary Gottlieb — "Venezuela's oil reform…" — https://www.clearygottlieb.com/-/media/files/alert-memos-2026/venezuelas-oil-reform-new-opportunities-unanswered-questions-investor-considerations.pdf — 2026-07-14 — consultada 2026-11-18 — secundaria (jurídica)
51. La Razón (Bolivia) — "Transporte alerta sobre una gasolina de 85 octanos con alto contenido de etanol" — https://larazon.bo/economia-y-empresa/2026/10/28/transporte-alerta-sobre-una-gasolina-de-85-octanos-con-alto-contenido-de-etanol/ — 2026-10-28 — consultada 2026-11-18 — prensa
52. Ecuavisa — "¿Cómo se mide el octanaje y azufre en las gasolinas?" — https://www.ecuavisa.com/noticias/ecuador/como-se-mide-el-octanaje-y-azufre-en-las-gasolinas-LJ1469519 — fecha [NO VERIFICADO] — consultada 2026-11-18 — prensa
53. Reuters (vía Roic.ai) — "Flames, Smoke Seen at Venezuela's Cardón Refinery" — https://www.roic.ai/news/flames-smoke-seen-at-venezuelas-cardn-refinery-four-sources-say-10-06-2026 — 2026-10-06 — consultada 2026-11-18 — prensa
54. BNN Bloomberg — "Venezuelan lawmakers approve easing state control of oil industry" — https://www.bnnbloomberg.ca/markets/oil/2026/01/29/venezuelan-lawmakers-approve-easing-state-control-of-oil-industry/ — 2026-01-29 — consultada 2026-11-18 — prensa
55. Wikipedia — "Fuel shortages in Venezuela" (solo contexto) — https://en.wikipedia.org/wiki/Fuel_shortages_in_Venezuela — s.f. — consultada 2026-11-18 — secundaria
56. Finanzas Digital — "Fenegas: modelo único de gasolina 2026" — https://finanzasdigital.com/fenegas-modelo-unico-gasolina-2026/ — 2026 — consultada 2026-11-18 — prensa
57. **(ronda 2)** mpgbuddy — "2026 Toyota 4Runner Hybrid 4WD: MPG and fuel economy" (cita la EPA) — https://mpgbuddy.com/cars/toyota/4runner-hybrid-4wd/2026 — 2026 — consultada 2026-11-18 — secundaria (agregador de datos EPA)
58. **(ronda 2)** Cars.com — Toyota 4Runner Hybrid 2026, versiones — https://www.cars.com/research/toyota-4runner_hybrid-2026/trims — 2026 — consultada 2026-11-18 — secundaria
59. **(ronda 2)** Tustin Toyota — "2026 Toyota 4Runner MPG: Fuel Economy by Trim" — https://www.tustintoyota.com/research/2026-toyota-4runner-mpg/ — 2026 — consultada 2026-11-18 — secundaria (concesionario)
60. **(ronda 2)** Tacoma4G Forum — "Premium fuel or regular" (cita el manual de la Tacoma, págs. 615 y 621) — https://www.tacoma4g.com/forum/threads/premium-fuel-or-regular.12665/ — 2024 — consultada 2026-11-18 — foro
61. **(ronda 2)** SAE Technical Paper 2024-01-2089 — "The New Toyota 2.4L L4 Turbo Engine with 8AT and 1-Motor Hybrid Electric Powertrains for Midsize Pickup Trucks" — https://saemobilus.sae.org/papers/new-toyota-24l-l4-turbo-engine-8at-1-motor-hybrid-electric-powertrains-midsize-pickup-trucks-2024-01-2089 — 2024 — consultada 2026-11-18 — primaria técnica (solo título)
62. **(ronda 2)** Yokomotor (distribuidor Toyota en Colombia) — Ficha técnica Land Cruiser Prado 2026 — https://yokomotor.com.co/wp-content/uploads/sites/2/2026/03/yokomotor-toyota-ficha-tecnica-land-cruiser-prado-2026.pdf — mar-2026 — consultada 2026-11-18 — primaria (distribuidor oficial, vía extracto)
63. **(ronda 2)** LandCruiserForum — "2024 Land Cruiser require Premium Fuel?" — https://landcruiserforum.com/posts/3903 — 2024 — consultada 2026-11-18 — foro
64. **(ronda 2)** Lexus Enthusiast — "New turbocharged high-output engines announced" — https://lexusenthusiast.com/2024/09/16/new-turbocharged-high-output-engines-announced/ — 2024-09-16 — consultada 2026-11-18 — prensa especializada
65. **(ronda 2)** Abdul Latif Jameel Motors — "A Legend Reborn: ALJ Motors Saudi Arabia unveils all-new Land Cruiser Prado" — https://jameelmotors.com/en/quick-reads/a-legend-reborn-abdul-latif-jameel-motors-saudi-arabia-unveils-all-new-land-cruiser-prado — 2024 — consultada 2026-11-18 — primaria (distribuidor oficial)
66. **(ronda 2)** Arab News — "A 'game changer': ALJ Motors unveils new Land Cruiser Prado" — https://arab.news/ps5m8 — 2024 — consultada 2026-11-18 — prensa
67. **(ronda 2)** Toyota Arabia Saudí — Prado 2024, especificaciones completas (dominio de pruebas UAT; usar con cautela) — https://toyota-owners-uat-567050-cm.azurewebsites.net/en/vehicles/suv/Prado/Full-Specs — 2024 — consultada 2026-11-18 — primaria (vía extracto)
68. **(ronda 2)** Toyota UAE (Al-Futtaim) — Land Cruiser Prado 2.4 L — https://www.toyota.ae/en/new-cars/land-cruiser-prado/2.4-l — 2025 — consultada 2026-11-18 — primaria (vía extracto)
69. **(ronda 2)** Drive Arabia — "Exploring the 2024 Toyota Land Cruiser Prado" — https://www.drivearabia.com/news/2024/08/05/exploring-the-2024-toyota-land-cruiser-prado/ — 2024-08-05 — consultada 2026-11-18 — prensa
70. **(ronda 2)** 24horas.cl — "Toyota Land Cruiser Prado 2024 se estrena en Chile y llega en dos versiones" — https://www.24horas.cl/motores-24/lanzamientos/toyota-land-cruiser-prado-2024-se-estrena-en-chile-y-llega-en-dos-versiones — 2024 — consultada 2026-11-18 — prensa
71. **(ronda 2)** Toyota Perú — Catálogo Land Cruiser Prado 2025 — https://www.toyotaperu.com.pe/sites/default/files/2025-10/catalogo-lcprado-2025.pdf — oct-2025 — consultada 2026-11-18 — primaria (vía extracto)
72. **(ronda 2)** Autocosmos Perú — Land Cruiser Prado 2.7L TX-L Aut (2026) — https://www.autocosmos.com.pe/catalogo/2026/toyota/land-cruiser-prado/27l-tx-l-aut/169846 — 2026 — consultada 2026-11-18 — secundaria
73. **(ronda 2)** El Carro Colombiano — "Toyota Land Cruiser Prado 250: Colombia, precios, versiones, datos" — https://www.elcarrocolombiano.com/lanzamientos/toyota-land-cruiser-prado-250-colombia-precios-versiones-datos/ — 2024 — consultada 2026-11-18 — prensa
74. **(ronda 2)** El Carro Colombiano — "Toyota Land Cruiser Prado 2025 diésel en Colombia" — https://www.elcarrocolombiano.com/novedades/toyota-land-cruiser-prado-2025-diesel-colombia-precios-versiones-datos/ — 2024–2025 — consultada 2026-11-18 — prensa
75. **(ronda 2)** El Carro Colombiano — "Toyota 4Runner 2025 ya está en América Latina" — https://www.elcarrocolombiano.com/autos-del-mundo/toyota-4runner-2025-ya-esta-en-america-latina-que-trae-y-cuanto-cuesta/ — 2025 — consultada 2026-11-18 — prensa
76. **(ronda 2)** EJU.tv (Bolivia) — "La nueva Land Cruiser 250 Prado: La evolución no para" — https://eju.tv/?p=4114760 — fecha [NO VERIFICADO] — consultada 2026-11-18 — prensa
77. **(ronda 2)** Autodeal (Filipinas) — "Coming soon: Toyota Land Cruiser Prado new turbocharged engine" — https://www.autodeal.com.ph/articles/car-news-philippines/coming-soon-toyota-land-cruiser-prado-new-turbocharged-engine — 2024–2025 — consultada 2026-11-18 — prensa
78. **(ronda 2)** AutoIndustriya — "2024 Toyota Land Cruiser Prado: Why no turbo diesel for PH?" — https://www.autoindustriya.com/auto-industry-news/2024-toyota-land-cruiser-prado-why-no-turbo-diesel-for-ph.html — 2024 — consultada 2026-11-18 — prensa
79. **(ronda 2)** Cars.co.za — "New Toyota Land Cruiser Prado: full SA line-up uncovered" — https://www.cars.co.za/motoring-news/New-Toyota-Land-Cruiser-Prado-Full-SA-Line-Up-Uncovered/201199/ — 2024 — consultada 2026-11-18 — prensa
80. **(ronda 2)** BusinessTech — "Toyota reveals new Land Cruiser Prado for South Africa – pricing" — https://businesstech.co.za/news/motoring/455726/toyota-reveals-new-land-cruiser-prado-for-south-africa-pricing/ — 2024 — consultada 2026-11-18 — prensa
81. **(ronda 2)** Carimports.co.ke — "2024 Toyota Land Cruiser 250 review" (Kenia) — https://www.carimports.co.ke/reviews/2024-toyota-land-cruiser-250-review-prices-specs/ — 2024 — consultada 2026-11-18 — secundaria
82. **(ronda 2)** The Citizen (Sudáfrica) — "Wait over: say hello to the new Toyota Land Cruiser Prado" — https://citizen.co.za/motoring/all-new-toyota-land-cruiser-prado-becomes-reality — 2023 — consultada 2026-11-18 — prensa
83. **(ronda 2)** Xataka México — "Toyota Tacoma TRD Pro HEV 2025 llega a México" — https://www.xataka.com.mx/automovil/toyota-tacoma-trd-pro-hev-2025-llega-a-mexico-pick-up-hibrida-326-hp-4x4-amortiguadores-asientos-para-caminos-extremos — 2025 — consultada 2026-11-18 — prensa
84. **(ronda 2)** TechRadar México — "Tacoma HEV 2024: el décimo híbrido eléctrico de Toyota en México" — https://global.techradar.com/es-mx/vehicle-tech/hybrid-electric-vehicles/tacoma-hev-2024-el-decimo-hibrido-electrico-hev-de-toyota-en-mexico — 2024 — consultada 2026-11-18 — prensa
85. **(ronda 2)** El Tiempo — "Gasolinas premium de mejor calidad y más amigables con el medioambiente" (Colombia) — https://www.eltiempo.com/economia/sectores/gasolinas-premium-de-mejor-calidad-y-mas-amigables-con-el-medioambiente-607322 — fecha [NO VERIFICADO] — consultada 2026-11-18 — prensa
86. **(ronda 2)** Resolución MinAmbiente 1180 de 2006 (Colombia; corriente 81 IAD, extra 87 IAD) — https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_minambientevdt_1180_2006.htm — 2006 — consultada 2026-11-18 — primaria (vigencia actual NO VERIFICADA)
87. **(ronda 2)** El Carro Colombiano — "El problema del octanaje en la gasolina colombiana" — https://elcarrocolombiano.com/notas-de-interes/el-problema-del-octanaje-en-la-gasolina-colombiana/ — s.f. — consultada 2026-11-18 — prensa
88. **(ronda 2)** El Carro Colombiano — "Toyota Corolla Cross ya se vende en Venezuela…" — https://www.elcarrocolombiano.com/industria/toyota-corolla-cross-ya-se-vende-en-venezuela-y-es-mucho-mas-cara-que-en-colombia/ — ~nov-2021 — consultada 2026-11-18 — prensa
89. **(ronda 2)** El Diario — "Toyota Venezuela estima vender más de 6.000 vehículos en 2024: ¿cómo y dónde se pueden adquirir?" — https://eldiario.com/2024/03/19/toyota-venezuela-como-y-donde-se-pueden-adquirir-los-vehiculos/ — 2024-03-19 — consultada 2026-11-18 — prensa
90. **(ronda 2)** Finanzas Digital — "Toyota Venezuela: Agya 2025" (repuestos, 47 concesionarios, Hino) — https://finanzasdigital.com/toyota-venezuela-agya-2025/ — 2025 — consultada 2026-11-18 — prensa
91. **(ronda 2)** Bloomberg Línea — "Toyota descarta reabrir planta en Venezuela, pese a 'renacimiento' del mercado automotor" — https://www.bloomberglinea.com/latinoamerica/venezuela/toyota-descarta-reabrir-planta-en-venezuela-pese-a-renacimiento-del-mercado-automotor/ — fecha [NO VERIFICADO] (2024–2025) — consultada 2026-11-18 — prensa
92. **(ronda 2)** El Diario — "Cronograma de distribución de gasolina: del 16 al 22 de noviembre" — https://eldiario.com/2026/11/14/cronograma-distribucion-gasolina-16-al-22-noviembre/ — 2026-11-14 — consultada 2026-11-18 — prensa
93. **(ronda 2)** El Diario — "Cronograma de distribución de gasolina del 9 al 15 de noviembre" — https://eldiario.com/2026/11/07/distribucion-gasolina-noviembre/ — 2026-11-07 — consultada 2026-11-18 — prensa
94. **(ronda 2)** Caraota Digital — "El anuncio que hizo PDVSA sobre la venta de gasolina súper premium y la regular en el país" — https://caraotadigital.net/venezuela/el-anuncio-que-hizo-pdvsa-sobre-la-venta-de-gasolina-super-premium-y-la-regular-en-el-pais/ — abr-2026 — consultada 2026-11-18 — prensa
95. **(ronda 2)** El Imparcial — "…Venezuela cuenta con tres tipos de gasolina…" — https://www.elimparcial.com/mexico/2026/03/31/mientras-venezuela-busca-aumentar-las-inversiones-petroleras-actualmente-el-pais-cuenta-con-tres-tipos-de-gasolina-para-surtir-los-vehiculos-una-de-ellas-subsidiada-pero-los-venezolanos-deben-someterse-a-largas-filas-ademas-de-registrarse-en-una-aplicacion-para-poner-obtener-el-beneficio/ — 2026-03-31 — consultada 2026-11-18 — prensa
96. **(ronda 2)** Argus Media — "Venezuela shifting gasoline consumption trends" — https://www.argusmedia.com/pt/news-and-insights/latest-market-news/1192825-venezuela-shifting-gasoline-consumption-trends — fecha [NO VERIFICADO] — consultada 2026-11-18 — prensa
97. **(ronda 2)** Argus Media — "PdV defends gasoline quality amid output pressure" — https://argusmedia.com/en/news/2443924-pdv-defends-gasoline-quality-amid-output-pressure — 2023 — consultada 2026-11-18 — prensa
98. **(ronda 2)** Finanzas Digital — "La calidad de la gasolina en Venezuela, un riesgo de incendio para los vehículos" — https://finanzasdigital.com/la-calidad-de-la-gasolina-en-venezuela-un-riesgo-de-incendio-para-los-vehiculos/ — abr/may-2023 — consultada 2026-11-18 — prensa
99. **(ronda 2)** Voz de América — "Mala calidad de la gasolina: averías e incendios de vehículos en Venezuela" — https://www.vozdeamerica.com/a/mala-calidad-de-la-gasolina--averías-incendios-vehiculos-venezuela-pdvsa/7064925.html — 2023 — consultada 2026-11-18 — prensa
100. **(ronda 2)** LaPatilla — "Calidad de la gasolina iraní está en duda" — https://www.lapatilla.com/2020/06/08/calidad-de-la-gasolina-irani-esta-en-duda/ — 2020-06-08 — consultada 2026-11-18 — prensa
101. **(ronda 2)** Finanzas Digital — "Gasolina súper premium: derrumbe de ventas en Venezuela" — https://finanzasdigital.com/gasolina-super-premium-derrumbe-ventas-venezuela/ — 2026 — consultada 2026-11-18 — prensa
102. **(ronda 2)** KBB — "2025 Toyota 4Runner i-FORCE MAX battery replacement" — https://www.kbb.com/toyota/4runner-i-force-max/2025/battery-replacement — 2025 — consultada 2026-11-18 — secundaria
103. **(ronda 2)** North Park Toyota Parts — Drive Motor Battery Pack G9510-60011 — https://parts.northparktoyota.com/oem-parts/toyota-drive-motor-battery-pack-g951060011 — 2025–2026 — consultada 2026-11-18 — secundaria (concesionario)
104. **(ronda 2)** North Park Toyota Parts — Inverter Assembly HEV M G92A0-60021 — https://parts.northparktoyota.com/oem-parts/toyota-inverter-assembly-hev-m-g92a060021 — 2025–2026 — consultada 2026-11-18 — secundaria (concesionario)
105. **(ronda 2)** North Park Toyota Parts — Drive Motor Inverter G92A0-48393 (Grand Highlander) — https://parts.northparktoyota.com/oem-parts/toyota-drive-motor-inverter-g92a048393 — 2025–2026 — consultada 2026-11-18 — secundaria (concesionario)
106. **(ronda 2)** Toyota Parts Deal — Genuine Toyota Crown Turbocharger (17201-25010) — https://toyotapartsdeal.com/oem-toyota-crown-turbocharger.html — 2026 — consultada 2026-11-18 — secundaria (concesionario)
107. **(ronda 2)** CarWhere — "Hybrid Battery Replacement Cost (2026)" — https://www.carwhere.com/car-repair-cost/hybrid-battery-replacement — 2026 — consultada 2026-11-18 — secundaria
108. **(ronda 2)** SlashGear — "How much it costs to replace a Toyota RAV4 Hybrid battery" — https://www.slashgear.com/2270747/toyota-rav4-hybrid-battery-replacement-cost/ — 2025–2026 — consultada 2026-11-18 — prensa
109. **(ronda 2)** Venezuela Investment Journal — "Shipping & Logistics Guide 2026" — https://venezuela-investment-journal.onrender.com/best-shipping-companies-venezuela — 2026 — consultada 2026-11-18 — secundaria no oficial
110. **(ronda 2)** OneWay Cargo — Servicios de reempaque (horarios aéreo y marítimo) — https://onewaycargo.net/files/servicios/reempaque.pdf — s.f. — consultada 2026-11-18 — secundaria (operador)
111. **(ronda 2)** ParcelPath — "Shipping to Venezuela from the USA" — https://parcelpath.com/shipping-to-venezuela/ — 2026 — consultada 2026-11-18 — secundaria
112. **(ronda 2)** IATN — Toyota (Techstream Lite) — https://iatn.net/reviews/toyota — s.f. — consultada 2026-11-18 — secundaria
113. **(ronda 2)** C3 Care Car Center (Colombia) — "Diagnóstico automotriz para vehículos híbridos" — https://www.c3carecarcenter.com/blog/diagnostico-automotriz-para-vehiculos-hibridos/ — 2025 — consultada 2026-11-18 — secundaria (taller)
114. **(ronda 2)** Klapty — anuncio de Viera Motors, Valencia — https://www.klapty.com/p/cercademy/t/toyota-fortuner-trd-sportivo-viera-motors-153651 — s.f. — consultada 2026-11-18 — anuncio/foro
