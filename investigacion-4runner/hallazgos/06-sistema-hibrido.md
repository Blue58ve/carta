# Agente 6 — Sistema híbrido i-FORCE MAX en Venezuela
**Fecha de investigación:** 2026-11-18

> **Advertencia de cobertura (leer antes de consolidar):** esta investigación quedó **incompleta por límites de herramientas, no por falta de información pública**. (a) WebFetch no pudo abrir ningún sitio externo: la red de la sesión no permite `pressroom.toyota.com` ni `assets.sia.toyota.com`, así que **no se pudo descargar ni leer el PDF del manual del propietario**. (b) El presupuesto de búsquedas web de la sesión (200 consultas compartidas entre los 8 agentes) se agotó cuando este agente llevaba 19 búsquedas, muy por debajo de las 30–40 previstas. Por eso las especificaciones del manual se citan a partir de **reproducciones textuales publicadas en foros y de extractos de buscador**, con número de página, y deben cotejarse con el PDF oficial. Las secciones 6.3 (mercados comparables, Toyota de Venezuela) y 6.4 (servicio y repuestos en Carabobo) quedaron casi enteras **[NO VERIFICADO]**. La sección "Preguntas abiertas" incluye la lista de búsquedas pendientes para una segunda vuelta.

## Resumen ejecutivo (5 líneas)
1. Calificación global: **MEDIO (provisional)**. El combustible es un riesgo **MEDIO** si se usa siempre la gasolina "Súper Premium" de 97 octanos nominales y **ALTO** si solo hay gasolina estándar. El riesgo propio del sistema híbrido es **MEDIO**: la probabilidad de falla es baja, pero el impacto sería alto porque el servicio técnico en Venezuela está sin verificar.
2. Según el manual 2025 (pág. 617, citado en foros), Toyota exige gasolina sin plomo de **87 AKI ("Research Octane Number 91") o más** para la 4Runner. Es un requisito bajo para un turbo: la misma familia de motor T24A-FTS en el Lexus NX 350 exige 91 AKI (RON 96) [3][4][11].
3. En Venezuela (2026), la gasolina regular midió **89 octanos** y la Súper Premium (97 nominal) entre **93 y 96** en mediciones informales [26]. La Súper Premium cumple el mínimo de Toyota (RON 91) incluso midiendo menos de lo prometido. La regular, si de verdad ronda RON 89 (≈85 AKI), queda **por debajo** del mínimo.
4. Desde febrero de 2026 hay Súper Premium en Valencia (estaciones Guaparo y Bohío) a **USD 1,00/L**, solo en efectivo [31][32][30]. El suministro sigue siendo frágil: las refinerías trabajaban al 31–35 % de su capacidad y Cardón sufrió un incendio en octubre de 2026 [42][44][45]. No se pudo verificar si algún concesionario Toyota o taller de Carabobo atiende el i-FORCE MAX.
5. Costo incremental de mitigación estimado frente a EE. UU.: **USD 1.000 / 1.700 / 3.200 al año** (mín/prob/máx). Probabilidad estimada de una falla mayor (batería, inversor o turbo) en 5 años: **4 % / 9 % / 21 %**, con un costo de USD 1.500–10.000 por evento más 2–8 semanas de inmovilización. No se emite 🛑 ALERTA DE ALCANCE, con reservas (ver 6.6).

## Hallazgos detallados (subsecciones 6.1 a 6.6)

### 6.0 Nota de método
- Etiquetas usadas: `[PRIMARIA]` (Toyota, PDVSA, Gobierno), `[PRIMARIA-vía extracto]` (documento oficial leído solo a través del resumen del buscador, sin abrir el original), `[PRENSA]`, `[CONCESIONARIO]` (sitios de concesionarios de EE. UU., secundaria comercial), `[FORO/REDES]`.
- No se citó ninguna cifra técnica de memoria. Las estimaciones van marcadas como **ESTIMACIÓN**, con su supuesto y su rango.

### 6.1 — Cómo funciona y qué exige el sistema

**Arquitectura (4Runner de sexta generación, años modelo 2025–2027)**
- **Trailhunter = solo i-FORCE MAX.** El Toyota Pressroom indica que la Trailhunter "is exclusively powered by the i-FORCE MAX". El motor base i-FORCE (2.4 turbo sin híbrido) rinde 278 hp y 317 lb-ft [1] `[PRIMARIA-vía extracto]`.
- **Potencia combinada del i-FORCE MAX:** 326 hp netos y 465 lb-ft [2] `[PRIMARIA-vía extracto, Toyota Canadá, materiales 2027]`; [19] `[PRENSA]`.
- **Motor T24A-FTS:** 2.393 cm³, diámetro × carrera de 87,5 × 99,5 mm, compresión 11,0:1, turbo *twin-scroll* con intercooler e **inyección dual D-4ST** (directa más puerto). Según la ficha técnica de toyota-club.net, el inyector de alta presión va montado en vertical, por primera vez en un D-4S de Toyota [13][14] `[secundaria técnica]`. Un blog da 10,0:1 de compresión, pero contradice al resto de fuentes y se descarta.
- **Motor-generador:** una sola unidad entre el motor térmico y la caja automática de 8 velocidades, de unos 48 hp, con embrague de desacople [19][22] `[PRENSA, sobre la Tacoma, que comparte el sistema]`. El diseño del embrague no se verificó con documentación Toyota.
- **Batería de tracción:** **níquel-metal hidruro (NiMH), sellada, de 288 V**, ubicada **bajo el piso de carga trasero**. Por eso las 4Runner i-FORCE MAX no tienen tercera fila [15][16] `[CONCESIONARIO]`. La capacidad de **~1,87 kWh** sale de concesionarios y fichas de terceros [16][18], no de Toyota, y queda **[NO VERIFICADO con fuente Toyota]**.
- **Refrigeración:** según un distribuidor de repuestos de concesionario y foros de la Tacoma, el i-FORCE MAX tiene **dos circuitos independientes**: uno para el motor y el turbo, y otro para el inversor, el convertidor, la unidad de control de potencia (PCU) y el motor eléctrico [20][21] `[secundaria/FORO]`. No se pudo confirmar con el manual de la 4Runner ni con el sitio de información técnica de Toyota (TIS).
- **No es enchufable:** es un híbrido autorrecargable que "never needs to be plugged in" [16][17] `[CONCESIONARIO]`. Ver 6.5.
- **Garantía en EE. UU.:** la batería híbrida tiene 10 años o 150.000 millas según las fichas de concesionarios [15] `[CONCESIONARIO]`. Que esa garantía se pierda al exportar el vehículo a Venezuela es probable, pero queda **[NO VERIFICADO]**. Lo resolvería el *Warranty & Maintenance Guide* (alcance territorial de la garantía).
- **Año modelo vigente:** la prensa y los foros describen la 2027 como un año de continuidad (por ejemplo, un color nuevo para la TRD Pro) [23][24] `[PRENSA/FORO]`. No se pudo leer el comunicado oficial 2027 del Pressroom (sitio bloqueado), así que la ausencia de cambios mecánicos en 2027 queda **[NO VERIFICADO]**.

**Combustible exigido por Toyota**
- **Cita del manual 2025 de la 4Runner, pág. 617** (código OM35B85U según [7]), reproducida textualmente en foros [3][4] `[FORO/REDES que reproduce PRIMARIA]`:
  > "You must only use unleaded gasoline. Select octane rating 87 (Research Octane Number 91) or higher. Use of unleaded gasoline with an octane rating lower than 87 may result in engine knocking. Persistent knocking can lead to engine damage."
- **Recomendado frente a mínimo:** el manual 2025, tal como se cita, da **87 AKI (RON 91) "or higher"** como mínimo y no recomienda premium para obtener la potencia nominal. Un concesionario afirma que ninguno de los dos trenes motrices "requires premium fuel to reach its rated output" [17], y KBB lista "Regular" para todas las versiones i-FORCE MAX [18]. Algunos dueños dicen que el motor anda mejor con 91 AKI [4], pero eso es anecdótico.
- **Manual 2026:** existen dos versiones, **OM35C07U** (producción hasta mayo de 2026) y **OM35C28U** (desde junio de 2026). Según los foros, los cambios son legales y de privacidad, y el contenido técnico es casi idéntico [6] `[FORO]`. La cifra de octanaje del manual 2026 y del 2027 queda **[NO VERIFICADO]**. Para resolverlo, el verificador debe leer la sección "Fuel information" (capítulo de especificaciones) del OM35C28U o del manual 2027 en toyota.com/owners.
- **Etanol:** una página oficial de información de combustible de Toyota (manual OM04011U, de otro modelo) limita el etanol a **10 %** y prohíbe expresamente "E15, E30, E50, E85" y cualquier combustible *flex-fuel* [8] `[PRIMARIA-vía extracto]`. Otras fuentes dicen que algunos manuales recientes de Toyota aceptan E15. Para la 4Runner 2025–2027, el límite exacto (E10 o E15) queda **[NO VERIFICADO]**. Lo práctico: Venezuela no comercializa mezclas etanol-gasolina conocidas, aunque esto tampoco se verificó en la sesión, y no se debe usar E85.
- **MMT (manganeso), metanol, plomo:** los manuales de Toyota de EE. UU. de otros modelos (Prius 2016, Tundra, Supra) **no recomiendan gasolina con MMT**. Advierten que puede afectar al sistema de control de emisiones y encender el testigo de falla [9][10] `[PRIMARIA, copias de manuales]`. El texto equivalente del manual de la 4Runner 2025–2027 (incluidos metanol, plomo y azufre) queda **[NO VERIFICADO]**.
- **Misma familia de motor, otra calibración:** según foros que citan el manual y Consumer Reports, el **Lexus NX 350 y el Lexus TX 350** con T24A-FTS exigen **91 AKI (RON 96)** y advierten que con menos octanaje puede dañarse el motor y anularse la garantía [11][12] `[FORO que cita PRIMARIA / PRENSA]`. Que las Toyota (4Runner, Tacoma) acepten 87 AKI indica una calibración con más margen contra la detonación. Es una **ventaja** para Venezuela frente a los Lexus del mismo motor.

**Conversión AKI (EE. UU.) ↔ RON (Venezuela)**
- AKI = (RON + MON)/2. Toyota da su propia equivalencia: **87 AKI ≈ RON 91** para la 4Runner y **91 AKI ≈ RON 96** para Lexus [3][11]. En la práctica, AKI ≈ RON − 4 a 5.
- Aplicado a Venezuela (**ESTIMACIÓN** con la regla RON − 4 a 5):

| Gasolina venezolana | RON | AKI equivalente aprox. | ¿Cumple el mínimo de la 4Runner (87 AKI / RON 91)? |
|---|---|---|---|
| Estándar, nominal | 91 [NO VERIFICADO] | 86–87 | Justo en el límite |
| Estándar, medida [26] | 89 | 84–85 | **No** (2 puntos RON por debajo) |
| Súper Premium, nominal [25] | 97 | 92–93 | Sí, con margen amplio |
| Súper Premium, medida en taller [26] | 93 | 88–89 | Sí (+2 RON) |
| Súper Premium, medida en estación [26] | 95–96 | 90–92 | Sí (+4–5 RON) |

**Componentes sensibles a un combustible deficiente y qué pasa mecánicamente** (explicación técnica general; no se encontraron TSB específicos del T24A-FTS sobre combustible, y su existencia queda **[NO VERIFICADO]**. Fuente que lo resolvería: base de datos de NHTSA, búsqueda por "2025-2027 4Runner hybrid TSB".)
- **Octanaje insuficiente:** el sensor de detonación hace que la ECU **retrase el encendido**. Resultado: menos potencia y torque, más consumo y gases de escape más calientes, lo que aumenta la carga térmica del turbo y del catalizador. Si la detonación persiste, puede dañar pistones y segmentos; el propio manual advierte "persistent knocking can lead to engine damage" [3].
- **LSPI (preignición a baja velocidad):** es típica de los motores turbo de inyección directa a bajas rpm y alta carga. Puede romper pistones o bielas. Influyen sobre todo la química del aceite (por eso conviene usar aceite API SP / ILSAC GF-6 del grado que indica el manual, 0W-20 según [4] `[FORO]`) y, en menor medida, la calidad del combustible.
  - **Inferencia no verificada:** el motor eléctrico entrega torque a bajas rpm, lo que podría reducir el tiempo que el motor térmico pasa en la zona propensa a LSPI. Esto mitigaría el problema, pero no se encontró fuente Toyota que lo confirme.
- **Inyección dual D-4ST:** los inyectores de puerto lavan las válvulas de admisión, lo que reduce los depósitos de carbón típicos de los motores solo de inyección directa [13][14]. Es un **factor mitigante**.
- **Agua o sedimentos:** corroen o tapan los inyectores (de puerto y de alta presión) y la bomba de alta presión, provocan fallos de encendido (códigos P0300–P0304), saturan el filtro de combustible (en el tanque) y pueden dañar la bomba de baja presión. En Venezuela la prensa documenta gasolina "rendida con agua", sin aditivos y sucia [38] y filtros, inyectores y bombas tapados [37].
- **Azufre alto:** envenena el catalizador (de forma parcialmente reversible) y degrada los sensores de oxígeno y de relación aire-combustible (posibles códigos P0420/P0430). El contenido de azufre de la gasolina venezolana de 2025–2026 queda **[NO VERIFICADO]**: no se halló medición pública.
- **Metales (MMT/manganeso, plomo, ferroceno, presentes en algunos elevadores de octanaje):** dañan **de forma permanente** el catalizador, los sensores y las bujías. Toyota no los recomienda [9][10].
- **Filtro de partículas de gasolina (GPF/OPF):** no se pudo verificar si la 4Runner de EE. UU. lo lleva **[NO VERIFICADO]**. Lo resolvería el catálogo de repuestos OEM o el manual de reparación.
- **Interacción con el sistema híbrido:** la batería, el inversor y el motor-generador **no están en contacto con el combustible**, así que la mala gasolina los afecta solo de forma indirecta. Fallos de encendido o testigos del motor pueden limitar la operación del sistema híbrido (modo de emergencia); este comportamiento concreto queda **[NO VERIFICADO]**. Los arranques y paradas frecuentes del motor en un híbrido no agravan la detonación. En el i-FORCE MAX (híbrido paralelo), el motor térmico trabaja la mayor parte del tiempo con el vehículo en marcha.

**Mantenimiento específico del sistema híbrido**
- Un distribuidor de repuestos de un concesionario Toyota de EE. UU. indica para el i-FORCE MAX: **inspección del refrigerante de la PCU y del sistema de enfriamiento de la batería cada 10.000 millas** y **cambio completo a las 100.000 millas o 10 años** [20] `[secundaria]`. El calendario oficial del *Warranty & Maintenance Guide* 2025–2027 queda **[NO VERIFICADO]** (bloqueado).
- Aceite: **0W-20** según el título de un hilo de foro que reproduce el manual 2025 [4] `[FORO]`. La capacidad y el intervalo oficiales quedan **[NO VERIFICADO]**.
- Filtro o rejilla de toma de aire de la batería híbrida, tipo de fluido de la caja automática (ATF), refrigerante del inversor (presumiblemente Toyota Super Long Life Coolant) y actualizaciones de software de la ECU: todo **[NO VERIFICADO]** en esta sesión.
- Diagnóstico: el acceso legal a Toyota Techstream / GTS+ y a una suscripción TIS desde fuera de EE. UU. queda **[NO VERIFICADO]**. Lo resolvería la tienda de techinfo.toyota.com y sus términos de licencia y territorio. Lo mismo la existencia de servicios exclusivos de concesionario (calibraciones o campañas de software).

### 6.2 — Calidad real del combustible en Venezuela (2025–2026)

**Situación de la producción (fechas de cada fuente)**
- **Feb-2026:** el sistema de refinación operaba a **~35 % de su capacidad instalada de 1,29 millones de barriles diarios** (frente al 20–25 % un año antes). Amuay, Cardón, El Palito y Puerto La Cruz procesaban juntas unos 450.000 barriles diarios, y Cardón reiniciaba una unidad productora de gasolina [42][43] `[PRENSA: Reuters]`.
- **Abr-2026:** 31 % (399.000 barriles diarios) [44] `[PRENSA]`. **Jul-2026:** Reuters describe las refinerías como "feas y oxidadas" y estima en al menos USD 20.000 millones la rehabilitación de Paraguaná. Sitúa la capacidad de **El Palito (Carabobo) en ~146.000 barriles diarios** [46][47] `[PRENSA]`.
- **6–8 oct-2026:** un **incendio en Cardón** (310.000 barriles diarios), originado en la rotura de una línea de gas, afectó al craqueador catalítico (FCC), la unidad clave para producir gasolina. Las versiones sobre la gravedad difieren: según una cobertura en español citada en [44], el fuego se apagó en menos de una hora; PDVSA afirmó que había inventarios suficientes [44][45][53] `[PRENSA]`. Su estado al 18-nov-2026 queda **[NO VERIFICADO]**.
- **Demanda e importaciones:** la demanda interna ronda **250.000 barriles diarios** (estimación de Reuters) y PDVSA no la cubre de forma constante. Venezuela importa **nafta de EE. UU.** y componentes de gasolina para completar su producción [44][48] `[PRENSA]`. No se halló confirmación de cargamentos de gasolina terminada de EE. UU. en 2026.
- **Contexto político e industrial:** el 29-ene-2026 la presidenta encargada Delcy Rodríguez firmó la reforma de la Ley Orgánica de Hidrocarburos, que abre el sector a empresas privadas. EE. UU. alivió parcialmente las sanciones. El 7-jul-2026 el Ministerio publicó resoluciones reglamentarias [49][50] `[PRENSA/secundaria jurídica]`. A noviembre de 2026, ese cambio todavía no se traduce en refinerías recuperadas.

**Octanaje vendido frente a medido**
- **Feb-2026:** PDVSA lanzó un plan piloto de gasolina **"Súper Premium" de 97 octanos a USD 1/L** en estaciones de Caracas (6–10 según la fuente), frente a unos USD 0,50/L de la estándar [25][28][39] `[PRENSA]`.
- **Mediciones de El Pitazo (aprox. feb-2026):** la mecánica Alejandra Wetter midió **regular = 89** y **Súper Premium = 93**, y advirtió que su medición es "superficial", una aproximación. En otra prueba en una estación de Caracas, la Súper Premium dio **95–96** en cinco mediciones, sin método publicado [26] `[PRENSA]`. **Ninguna es un ensayo de laboratorio ASTM D2699 (RON).**
- El ingeniero Rafael Quiroz atribuye la calidad irregular al deterioro de la refinación, con efectos en el octanaje y la estabilidad. Un mecánico advierte que "se tapan filtros, inyectores y, a la larga, puede generar daños en la bomba de la gasolina" [37] `[PRENSA]` (fecha de la nota **[NO VERIFICADO]**).
- **Mar-2026:** la Cámara Nacional de Talleres Mecánicos (CANATAME) pidió seguir el manual del fabricante y desmintió rumores virales sobre la gasolina de 97 [36] `[PRENSA]`.
- **May-2023:** gasolina "rendida con agua, sin aditivos necesarios y sucia" que causó daños e incendios en vehículos [38] `[PRENSA]`. Es un antecedente; no refleja necesariamente la situación de 2026.
- **Sin fuente para 2025–2026:** no se encontró ninguna medición de laboratorio independiente, estudio universitario (UC, UCV, USB, LUZ), norma COVENIN vigente ni comunicado de PDVSA o del Ministerio sobre octanaje, azufre, oxigenados (MTBE o etanol), metanol o metales. El origen de los componentes elevadores de octanaje tampoco se verificó. Todo esto queda **[NO VERIFICADO]**, al igual que los episodios de la gasolina iraní (2020–2022) y de la gasolina contaminada en Carabobo en 2024–2025. La búsqueda se interrumpió por el límite de presupuesto.

**Disponibilidad y precio en Carabobo**
- **Feb-2026:** la Súper Premium llegó a Carabobo, en la **E/S Guaparo** (redoma de Guaparo, Av. Bolívar, Valencia) y la **E/S Bohío** (Autopista Regional del Centro) [31][32] `[PRENSA local]`. Según la federación de gasolineros (Fenegas), el plan cubría unas 10 estaciones en Caracas y unas dos por estado en Aragua, Carabobo y Lara [35] `[PRENSA]`.
- **Precios (abr-2026):** Súper Premium a **USD 1,00/L, solo en dólares en efectivo**. Estándar a "precio internacional", **USD 0,50–0,80/L**. Subsidiada: cupo de **120 L/mes** vía sistema Patria, por unos USD 3 en total [30][29] `[PRENSA]`.
- Un índice no oficial consultado vía buscador en noviembre de 2026 mantiene la gasolina de 97 en ~USD 1,00/L "en estaciones seleccionadas" [41] `[secundaria no oficial]`.
- **Señales de fragilidad:**
  - Fenegas denunció falta de documentación formal y propuso que todas las estaciones vendan ambos tipos [34][35].
  - El 15-abr-2026, estaciones Súper Premium de Caracas empezaron a vender también gasolina estándar a USD 0,50/L [29].
  - Las ventas de gasolina cayeron tras el plan [33].
  - Un titular indica que la Súper Premium solo representa **~2 % de las ventas** [56] (fuente exacta **[NO VERIFICADO]**).
- La lista de estaciones Súper Premium en Carabobo a **noviembre de 2026** queda **[NO VERIFICADO]**: las fuentes más recientes son de abril de 2026.
- **Aditivos:** no se encontró evidencia sobre productos concretos vendidos en Venezuela **[NO VERIFICADO]**. Criterio técnico basado en los manuales de Toyota [9][10]:
  - Evitar elevadores de octanaje con **MMT/manganeso, plomo o ferroceno**.
  - Los limpiadores con detergente PEA (polieteramina), sin metales, son aceptables y útiles para mantener los inyectores.
  - Ningún aditivo convierte una gasolina de RON 89 en una de RON 91 de forma fiable y segura en dosis normales.
- **Filtros o separadores de agua adicionales:** no se recomienda instalarlos en la línea de alta presión, por riesgo técnico y de garantía (**[NO VERIFICADO]** con Toyota). Si se reposta desde bidones, conviene usar un embudo con filtro separador de agua.

### 6.3 — Evidencia de híbridos y turbos Toyota/Lexus en Venezuela y mercados comparables
- **Toyota de Venezuela (planta de Cumaná):** si vende o vendió híbridos en 2023–2026, qué motores ofrece en Hilux, Fortuner o Land Cruiser y qué recomienda sobre el combustible queda **[NO VERIFICADO]**. No llegó a buscarse. Lo resolverían toyota.com.ve (catálogo y fichas) y la Cámara Automotriz de Venezuela (CAVENEZ).
- **Parque de híbridos Toyota/Lexus en Venezuela y experiencias de dueños** (Corolla Cross Hybrid, RAV4 Hybrid, Land Cruiser 250, Tundra o Sequoia i-FORCE MAX, Lexus): **[NO VERIFICADO]**. No se halló evidencia documentada ni anecdótica en esta sesión.
- **Turbos de inyección directa de otras marcas en Venezuela** (Chery, JAC, Haval, BYD, etc.): **[NO VERIFICADO]**. La prensa general afirma que el octanaje bajo es un problema sobre todo para motores de alta compresión o turboalimentados [26][36][37], pero no aporta casos de un modelo concreto.
- **Mercados comparables (señal clave):**
  - **Verificado, aunque indirecto:** dentro de EE. UU., Toyota calibra el mismo T24A-FTS para **RON 91** en la 4Runner y la Tacoma y para **RON 96** en los Lexus [3][11][12]. El motor es sensible al octanaje, y la calibración Toyota es la tolerante.
  - **Bolivia (28-oct-2026):** el sector transporte alertó sobre una gasolina de **85 octanos con alto contenido de etanol** [51] `[PRENSA]`. Es un ejemplo de mercado regional con combustible deficiente.
  - **Ecuador:** según un laboratorio de la Escuela Politécnica Nacional citado por la prensa, las muestras comerciales suelen estar entre **85 y 92 octanos** [52] `[PRENSA]` (fecha **[NO VERIFICADO]**).
  - **Sin verificar:** si Toyota ofrece o excluye el T24A-FTS o el i-FORCE MAX (Land Cruiser 250/Prado, Hilux, Tacoma o 4Runner, Lexus GX) en Bolivia, Perú, Ecuador, Paraguay, Colombia, Chile, México, el Golfo, Nigeria, Angola, Kenia o Pakistán, y si lo sustituye por el 2.7 L 2TR-FE, el 4.0 L 1GR-FE o el 2.8 L 1GD-FTV. **No se pudo comprobar con fuentes oficiales.** Hipótesis de trabajo, que no debe usarse como hecho: en Latinoamérica Toyota tiende a ofrecer versiones atmosféricas o diésel de estos modelos. Si se confirma que excluye el 2.4 turbo en mercados con gasolina de 85–91 RON, sería una **señal negativa fuerte**. Fuentes que lo resuelven: los configuradores oficiales toyota.com.bo, toyota.com.pe, toyota.com.ec, toyota.com.co, toyota.cl, toyota.com.mx, toyota.com.sa y toyota.ae.

### 6.4 — Servicio técnico y repuestos del sistema híbrido en Venezuela
- **Concesionarios Toyota en Valencia/Carabobo con técnicos certificados en híbridos y Techstream/GTS+, y su política con vehículos importados por particulares (no TDV):** **[NO VERIFICADO]**. No llegó a buscarse. Lo resolverían el localizador de concesionarios de toyota.com.ve y una llamada (ver "Preguntas abiertas").
- **Talleres independientes de híbridos en Valencia, Carabobo o Caracas** (diagnóstico y reacondicionamiento de baterías, inversores): **[NO VERIFICADO]**. Lo resolverían Google Maps, Instagram ("taller híbridos Valencia Venezuela", "baterías híbridas Caracas") y Fundacomercio o directorios locales.
- **Repuestos y precios OEM en EE. UU.** (batería híbrida, inversor/PCU, motor-generador, turbo, bujías, sensores de relación aire-combustible, refrigerante, aceite 0W-20, filtros): **[NO VERIFICADO]**. Lo resolverían toyotapartsdeal.com, parts.olathetoyota.com o autopartsprime con el VIN o el número de pieza.
- **Costo y plazo del courier Miami–Valencia:** **[NO VERIFICADO]**. **ESTIMACIÓN provisional del agente:** 1–3 semanas por vía aérea para piezas pequeñas y 4–8 semanas por vía marítima para piezas voluminosas. Supuesto: operaciones habituales de courier, sin retención en aduana.
  - La batería NiMH, por su clasificación como mercancía peligrosa para transporte (UN3496), puede tener restricciones de envío **[NO VERIFICADO]**. Lo resolverían la regulación IATA DGR/IMDG y la política del courier.
- **Riesgo de inmovilización:** sin un concesionario confirmado, una avería de una pieza no almacenada (inversor, motor-generador, módulo de control, turbo) puede dejar el vehículo parado **2–8 semanas** (**ESTIMACIÓN**; supuesto: diagnóstico disponible + pedido OEM en EE. UU. por la LLC + courier aéreo + aduana). Si además falta diagnóstico oficial, más tiempo.
- **Plan de contingencia propuesto:**
  1. Stock propio de consumibles (filtros, bujías, refrigerante, aceite, pastillas de freno).
  2. Cuenta en un portal OEM de EE. UU. a nombre de la LLC, con el VIN registrado.
  3. Un escáner con cobertura de híbridos Toyota o acceso legal a Techstream.
  4. Un taller identificado **antes** de importar el vehículo.

### 6.5 — Otros factores ambientales
- **Calor (Valencia, 30–35 °C) y tráfico:** las baterías NiMH envejecen más rápido con temperaturas altas. El enfriamiento de la batería de la 4Runner (toma de aire, ventilador, filtro) **no se pudo verificar**. En la Tacoma, los foros describen un sistema de gestión térmica que incluye la batería [21] `[FORO]`. El inversor tiene, según [20], su propio circuito de refrigerante: hay que vigilar el nivel y la limpieza del radiador del inversor. **Inferencia:** el tráfico lento con aire acondicionado al máximo es el escenario térmico más exigente para batería e inversor. No impide el uso, pero acelera el desgaste.
- **Red eléctrica:** **confirmado** que no es enchufable [16][17]. Los apagones de Carabobo **no afectan a la carga** del vehículo. Sí pueden afectar a las **bombas de las estaciones de servicio**, por lo que conviene llevar siempre más de medio tanque; los apagones de 2025–2026 en Carabobo quedan **[NO VERIFICADO]**.
- **Batería auxiliar de 12 V:** el sistema híbrido la necesita para arrancar. Si el vehículo pasa semanas parado, hace falta un mantenedor de carga. Es práctica general, no verificada para este modelo.
- **Polvo y uso todoterreno:** el filtro de aire del motor y el de cabina deben revisarse con más frecuencia (el calendario de condiciones severas de Toyota **[NO VERIFICADO]**). La toma de aire de la batería híbrida debe mantenerse libre de polvo y barro.
- **Vadeo:** la batería está **sellada** y bajo el piso trasero [15]. La profundidad de vadeo oficial y la altura de la toma de aire de la batería quedan **[NO VERIFICADO]**. Lo resolvería el manual del propietario, en la sección de conducción todoterreno.

### 6.6 — Conclusión técnica

**Calificación del riesgo: MEDIO (provisional)**

| Componente del riesgo | Calificación | Justificación |
|---|---|---|
| **Combustible, motor T24A-FTS** (afecta igual a la versión híbrida y a la no híbrida) | **MEDIO** si se usa siempre Súper Premium; **ALTO** si solo hay estándar | Toyota exige solo RON 91 (87 AKI) [3][4], y la Súper Premium medida (93–96) lo supera [26]. La estándar medida (89) queda por debajo. Riesgos residuales: agua y sedimentos [37][38], azufre y metales desconocidos, y un suministro frágil (refinerías al 31–35 %, incendio de Cardón en oct-2026, Súper Premium con ~2 % de las ventas y solo en efectivo) [42][44][45][56]. Mitigan la inyección dual D-4ST y la calibración tolerante. |
| **Sistema híbrido** (batería NiMH, inversor, motor-generador) | **MEDIO** | La química NiMH es una tecnología Toyota madura, sellada y no enchufable, y no toca el combustible. El riesgo es de **impacto**: sin concesionario ni taller verificados en Carabobo, sin garantía de EE. UU. probable y con piezas a 1–8 semanas, cualquier avería puede inmovilizar el vehículo. El calor acelera el desgaste. |
| **Global** | **MEDIO** | Es viable si se cumplen las condiciones C1–C3. Pasaría a **ALTO** si en noviembre de 2026 no hubiera Súper Premium estable en Valencia o no existiera ningún servicio con diagnóstico Toyota accesible. |

**Condiciones para mantener el riesgo en MEDIO:**
- **C1.** Confirmar que en noviembre de 2026 hay Súper Premium regular en Valencia (Guaparo, Bohío u otras estaciones).
- **C2.** Confirmar un concesionario o taller en Carabobo o Caracas que acepte el vehículo y tenga Techstream/GTS+ o un escáner equivalente para el i-FORCE MAX.
- **C3.** Leer el manual oficial 2026/2027 (OM35C28U o el siguiente) y confirmar que el mínimo sigue siendo 87 AKI / RON 91.

**Sobre la 🛑 ALERTA DE ALCANCE:** **no se emite**. Ningún hallazgo verificado hace inviable la operación: el requisito de octanaje es alcanzable con un combustible que se vende hoy en Valencia. **Reserva:** la falta de verificación del servicio híbrido en Venezuela (6.4) y de los mercados comparables (6.3) es una laguna crítica. El orquestador debería tratarla como una condición previa a la decisión, no como un tema resuelto.

**Costo anual estimado (15.000 km/año) — ESTIMACIONES**

Supuestos:
- Consumo real de 10 / 11,5 / 13 L/100 km, con neumáticos todoterreno, tráfico y aire acondicionado. La cifra EPA de la Trailhunter no se pudo verificar; lo resuelve fueleconomy.gov.
- Súper Premium a USD 1,00 / 1,00 / 1,20 por litro [30][41].
- Gasolina regular en EE. UU. a USD 3,00 / 3,30 / 3,60 por galón (**[NO VERIFICADO]**, precio 2026 no consultado).
- Mantenimiento en Venezuela con calendario severo y piezas importadas; en EE. UU., calendario normal.

| Concepto | Venezuela mín / prob / máx (USD/año) | EE. UU. mín / prob / máx (USD/año) |
|---|---|---|
| Combustible (1.500 / 1.725 / 1.950 L) | 1.500 / 1.725 / 2.340 (Súper Premium) | 1.190 / 1.500 / 1.850 (87 AKI) |
| Mantenimiento: 2–3 cambios de aceite y filtros, filtros de aire y cabina, bujías amortizadas | 500 / 900 / 1.500 | 200 / 300 / 400 (posiblemente cubierto por ToyotaCare los primeros años, [NO VERIFICADO]) |
| Aditivo detergente PEA sin metales | 40 / 80 / 120 | 0 |
| Stock de repuestos y courier, amortizados | 200 / 400 / 800 | 0 |
| Herramienta de diagnóstico o suscripción TIS, amortizada en 5 años | 200 / 400 / 600 | 0 |
| **Total** | **2.440 / 3.505 / 5.360** | **1.390 / 1.800 / 2.250** |
| **Incremental Venezuela − EE. UU.** | **≈ 1.000 / 1.700 / 3.200** | — |

Nota: solo el diferencial entre Súper Premium y estándar dentro de Venezuela suma unos USD 600 / 860 / 1.170 al año.

**Probabilidad de falla mayor en 5 años (≈75.000 km) — ESTIMACIONES**

No se encontró ningún dato de flota. Son juicios técnicos con estos supuestos: uso de Súper Premium casi siempre, aceite del grado correcto, calor tropical y sin garantía. Los costos incluyen pieza OEM, courier y mano de obra; los precios OEM son **[NO VERIFICADO]**.

| Falla | Probabilidad mín / prob / máx | Costo por evento (USD) | Costo esperado prob. |
|---|---|---|---|
| Batería híbrida NiMH | 1 % / 3 % / 8 % | 3.000 / 5.000 / 8.000 | ~150 |
| Inversor / PCU | 1 % / 2 % / 5 % | 3.000 / 6.000 / 10.000 | ~120 |
| Turbo (calor, aceite, combustible) | 2 % / 4 % / 10 % | 1.500 / 3.000 / 5.000 | ~120 |
| **Al menos una de las tres** | **≈4 % / 9 % / 21 %** | — | **≈ USD 390 en 5 años (máx. ≈ USD 1.640)**, más 2–8 semanas de inmovilización por evento |
| Motor dañado por detonación o LSPI (solo si se usa estándar de RON 89 de forma habitual) | 1 % / 3 % / 10 % | 8.000 / 12.000 / 15.000 | — |

**Medidas de mitigación**
1. **Repostar solo Súper Premium** en estaciones identificadas (Guaparo y Bohío según [31][32]; confirmar la lista vigente). Mantener el tanque por encima de 1/4 para no aspirar sedimentos. Llevar un bidón con Súper Premium para rutas largas.
2. **Prohibir elevadores de octanaje con MMT, manganeso o plomo.** Usar solo limpiadores PEA sin metales, cada 1–2 cambios de aceite.
3. Aceite **0W-20 API SP / ILSAC GF-6** (o el grado exacto del manual 2026/2027), importado. Cambios cada 5.000–7.500 km (calendario severo). Filtro de aire cada 10.000–15.000 km, o antes tras uso todoterreno.
4. Registrar códigos y datos con un **escáner OBD-II con cobertura de híbridos Toyota**. Vigilar retardo de encendido o *knock*, ajustes de combustible (*fuel trims*), códigos P0300 y P0420, y temperatura de la batería.
5. Comprar **antes del embarque**, vía la LLC: stock de filtros, bujías, refrigerante Toyota, aceite y sensores de relación aire-combustible. Definir un taller y un proveedor OEM en EE. UU. con el VIN registrado.
6. Mantener libre la toma de aire de la batería híbrida, limpiar el radiador del inversor y no vadear por encima de lo que indique el manual.
7. Exigir al concesionario vendedor en EE. UU. que aplique todas las campañas y actualizaciones de software antes de exportar.

**Alternativa de contingencia**
- **4Runner sin híbrido (i-FORCE 2.4 turbo, por ejemplo TRD Off-Road o TRD Off-Road Premium):** elimina el riesgo específico del híbrido (batería, inversor, motor-generador y su diagnóstico especializado). **El riesgo del combustible persiste**, porque es el **mismo T24A-FTS turbo de inyección directa** (278 hp [1]) y, según el manual citado, con el mismo mínimo de 87 AKI / RON 91; su aplicación idéntica a la versión no híbrida está **[NO VERIFICADO]** en el texto del manual 2026/2027. La Trailhunter no se ofrece sin híbrido [1]. Reduce el riesgo global solo un grado parcial: de MEDIO a MEDIO-bajo.
- **Referencia: Toyota atmosférica o diésel** (Hilux o Fortuner de TDV, Land Cruiser 70 o Prado con 2.7 L 2TR-FE o 2.8 L 1GD-FTV). Por diseño, sin turbo ni inyección directa en el caso del 2TR-FE y con red local de servicio si es TDV, tendrían un perfil de riesgo de combustible y servicio **claramente menor**. La oferta concreta de TDV y la calidad del diésel venezolano quedan **[NO VERIFICADO]**.

## Cifras clave (tabla: concepto | valor | rango mín/prob/máx si es estimación | fuente [n] | fecha de la fuente)

| Concepto | Valor | Rango mín/prob/máx (si es estimación) | Fuente [n] | Fecha de la fuente |
|---|---|---|---|---|
| Tren motriz de la Trailhunter | Solo i-FORCE MAX | — | [1] | 2024–2025 (comunicado del año modelo 2025/2026) |
| Potencia y torque i-FORCE MAX | 326 hp / 465 lb-ft | — | [2][19] | 2026 (Toyota Canadá, materiales 2027) |
| Potencia y torque i-FORCE (no híbrido) | 278 hp / 317 lb-ft | — | [1] | 2024–2025 |
| Motor T24A-FTS | 2.393 cm³; 87,5 × 99,5 mm; 11,0:1; D-4ST; turbo *twin-scroll* | — | [13][14] | 2021 / s.f. |
| Batería híbrida | NiMH sellada, 288 V, bajo el piso de carga | — | [15][16] | 2025–2026 |
| Capacidad de la batería | ~1,87 kWh | [NO VERIFICADO con Toyota] | [16][18] | 2025–2026 |
| Octanaje mínimo, 4Runner (manual 2025, pág. 617) | 87 AKI ("Research Octane Number 91") o más | — | [3][4] | 2024–2025 (manual del año modelo 2025) |
| Octanaje exigido, Lexus NX/TX 350 (mismo motor) | 91 AKI (RON 96) | — | [11][12] | 2022–2025 |
| Etanol máximo (página Toyota de otro modelo) | 10 %; prohíbe E15, E30, E50 y E85 | 4Runner 2025–2027: [NO VERIFICADO] | [8] | s.f. |
| Garantía de la batería híbrida en EE. UU. | 10 años / 150.000 millas | Exportación: [NO VERIFICADO] | [15] | 2025 |
| Súper Premium Venezuela, nominal y precio | 97 RON; USD 1,00/L; solo efectivo en USD | — | [25][30] | Feb–abr 2026 |
| Súper Premium, octanaje medido | 93 (taller); 95–96 (estación en Caracas) | Mediciones informales | [26] | ~Feb 2026 |
| Gasolina regular, octanaje medido | 89 | Medición informal | [26] | ~Feb 2026 |
| Estándar a precio internacional | USD 0,50/L | 0,50–0,80 | [29][30] | Abr 2026 |
| Gasolina subsidiada | 120 L/mes ≈ USD 3 en total (Patria) | — | [30] | Abr 2026 |
| Estaciones Súper Premium en Carabobo | Guaparo (Av. Bolívar, Valencia); Bohío (ARC) | Vigencia en nov-2026 [NO VERIFICADO] | [31][32] | Feb 2026 |
| Peso de la Súper Premium en las ventas | ~2 % | Fuente exacta [NO VERIFICADO] | [56] | 2026 |
| Uso de la capacidad de refinación | 35 % de 1,29 millones de barriles diarios (feb); 31 % = 399.000 b/d (abr) | — | [42][44] | Feb y abr 2026 |
| Capacidad de El Palito (Carabobo) | ~146.000 barriles diarios | 140.000–146.000 | [46] | Jul 2026 |
| Incendio en Cardón (310.000 b/d, FCC afectado) | 6–8 oct 2026 | Estado al 18-nov [NO VERIFICADO] | [44][45][53] | Oct 2026 |
| Demanda interna de gasolina | ~250.000 barriles diarios | — | [44] | 2026 |
| Consumo real supuesto de la Trailhunter | — | 10 / 11,5 / 13 L/100 km (ESTIMACIÓN) | Supuesto del agente | — |
| Costo anual en Venezuela (combustible + mantenimiento + mitigación) | — | USD 2.440 / 3.505 / 5.360 | Estimación (6.6) | 2026-11-18 |
| Costo incremental frente a EE. UU. | — | USD 1.000 / 1.700 / 3.200 al año | Estimación (6.6) | 2026-11-18 |
| Diferencial Súper Premium frente a estándar | — | USD 600 / 860 / 1.170 al año | Estimación con [29][30] | 2026 |
| Probabilidad de falla mayor en 5 años | — | 4 % / 9 % / 21 % | Estimación (6.6) | 2026-11-18 |
| Costo de una falla mayor por evento | — | USD 1.500 – 10.000 | Estimación; precios OEM [NO VERIFICADO] | 2026-11-18 |
| Inmovilización por evento | — | 2 / 4 / 8 semanas | Estimación | 2026-11-18 |

## Riesgos detectados
1. **Octanaje de la gasolina estándar por debajo del mínimo de Toyota.** Una medición informal dio 89 RON frente a un mínimo de 91 [26]. Probabilidad alta si se usa estándar; impacto: retardo del encendido, pérdida de potencia y riesgo de daño por detonación persistente [3]. **Mitigación:** usar solo Súper Premium.
2. **Suministro frágil de la Súper Premium.** Plan piloto con pocas estaciones por estado, solo efectivo en USD, ~2 % de las ventas, estaciones que pasaron a vender estándar en abril de 2026, refinerías al 31–35 % e incendio en Cardón en octubre de 2026 [29][35][42][44][45][56]. Si desaparece en Carabobo, el riesgo del combustible sube a **ALTO**.
3. **Contaminación con agua o sedimentos y calidad inestable** [37][38]. Afecta a inyectores, bomba de alta presión y filtro. No hay mediciones de azufre ni de metales **[NO VERIFICADO]**.
4. **Servicio híbrido y diagnóstico Toyota no confirmados en Carabobo** (6.4, [NO VERIFICADO]). Ante cualquier testigo del sistema híbrido, riesgo de inmovilización prolongada.
5. **Pérdida probable de la garantía de EE. UU. al exportar** **[NO VERIFICADO]**. La batería, el inversor y el turbo quedarían a cargo del cliente.
6. **Calor sostenido en Valencia.** Acelera la degradación de la batería NiMH y exige más a la refrigeración del inversor [20][21].
7. **Logística de repuestos.** Plazos de 1–8 semanas, posibles restricciones de envío de la batería NiMH (UN3496) y aduanas **[NO VERIFICADO]**.
8. **Aditivos inadecuados.** Elevadores de octanaje con MMT o manganeso, comunes en mercados con gasolina mala, dañan el catalizador y los sensores, y Toyota no los recomienda [9][10].
9. **Laguna de evidencia en esta investigación.** Sin fuentes oficiales de mercados comparables ni de Toyota de Venezuela, la "señal clave" de 6.3 está **sin resolver**.

## Preguntas abiertas (incluye preguntas concretas para hacerle al concesionario Toyota de Valencia y a un taller de híbridos)

**Para el concesionario Toyota de Valencia o Carabobo (red de Toyota de Venezuela):**
1. ¿Aceptan dar servicio, garantía local o diagnóstico a una 4Runner 2026/2027 importada por un particular desde EE. UU. (vehículo no TDV)? ¿Con qué condiciones y tarifas?
2. ¿Tienen Techstream / GTS+ con licencia vigente y acceso a TIS para modelos norteamericanos con T24A-FTS e i-FORCE MAX? ¿Pueden aplicar calibraciones o actualizaciones de software?
3. ¿Tienen técnicos certificados en alto voltaje o híbridos? ¿Han atendido Land Cruiser 250, Tundra, Sequoia o Tacoma i-FORCE MAX, o algún RAV4 o Corolla Cross híbrido?
4. ¿Pueden pedir piezas a Toyota Motor North America o Toyota Latinoamérica para un VIN de EE. UU.? ¿Con qué plazos (batería híbrida, inversor, turbo, sensores de relación aire-combustible)?
5. ¿TDV vende algún modelo con motor turbo de gasolina o híbrido en Venezuela? ¿Qué octanaje recomienda y qué adaptaciones hace para el mercado local?
6. ¿Qué gasolina y qué aditivos usan o recomiendan para motores turbo de inyección directa? ¿Han visto casos de detonación o de catalizadores dañados?

**Para un taller independiente de híbridos (Valencia o Caracas):**
1. ¿Diagnostican sistemas híbridos Toyota de segunda y tercera generación (paralelo de un motor con embrague, tipo i-FORCE MAX) o solo del tipo Prius (dos motores eléctricos y engranaje planetario)?
2. ¿Qué escáner usan (Techstream legítimo, Autel o Launch)? ¿Leen datos de bloques de celdas NiMH y del inversor?
3. ¿Reacondicionan baterías NiMH? ¿Prueban y sustituyen inversores? ¿Con qué garantía y precios?
4. ¿Cuántos casos han tenido de daño por combustible en motores turbo de inyección directa (inyectores, bomba de alta presión, LSPI) en 2025–2026? ¿En qué estaciones o zonas?
5. ¿Qué estaciones de Carabobo consideran confiables hoy para Súper Premium?

**Pendientes de verificación (búsquedas que no se pudieron hacer por el límite de presupuesto o el bloqueo de red):**
- Manual del propietario OM35C28U (2026) y del año modelo 2027: sección "Fuel information" (octanaje, etanol, MMT, metanol), profundidad de vadeo, toma de aire de la batería, capacidad y grado del aceite. Además, el *Warranty & Maintenance Guide* (intervalos del refrigerante del inversor, condiciones severas, alcance territorial de la garantía) y TSB y *recalls* de NHTSA para la 4Runner y Tacoma i-FORCE MAX.
- Fichas oficiales de la Land Cruiser 250/Prado, la Hilux y la Tacoma en Bolivia, Perú, Ecuador, Colombia, Chile, México, Arabia Saudí y Emiratos: ¿ofrecen el 2.4 turbo o el i-FORCE MAX?
- toyota.com.ve: catálogo, motores y red de concesionarios en Carabobo. CAVENEZ y CAVEA: híbridos vendidos.
- Norma COVENIN vigente para la gasolina, comunicados de PDVSA sobre la Súper Premium (expansión y estaciones a noviembre de 2026), mediciones de laboratorio (universidades venezolanas, cámaras de talleres), episodios de gasolina iraní o contaminada en 2020–2025 y apagones en Carabobo en 2025–2026.
- Precios OEM en EE. UU. de la batería híbrida, el inversor y el turbo de la 4Runner, y tarifas de courier Miami–Valencia por libra en 2026.
- Precio de la gasolina en EE. UU. en 2026 (EIA) y consumo EPA de la Trailhunter (fueleconomy.gov).

## Fuentes (lista numerada: título — URL — fecha de la fuente — consultada 2026-11-18 — tipo: primaria/secundaria/prensa/foro)
Nota: todas las fuentes se consultaron a través de resúmenes o extractos del motor de búsqueda; WebFetch estuvo bloqueado por la red de la sesión, así que ninguna se abrió completa.

1. The 2026 Toyota 4Runner: Engineered for Exploration (Toyota Pressroom) — https://pressroom.toyota.com/the-2026-toyota-4runner-engineered-for-exploration/ — 2024–2025 (fecha exacta no visible) — consultada 2026-11-18 — primaria (vía extracto; sitio bloqueado para lectura directa)
2. Toyota Canadá — 4Runner, características y beneficios (materiales 2027) — https://www.toyota.ca/en/vehicles/4runner/features-benefits/ — 2026 — consultada 2026-11-18 — primaria (vía extracto)
3. 4Runner6G Forum — "What gas octane level required for iForce Max hybrid 87 or 91" — https://www.4runner6g.com/forum/threads/what-gas-octane-level-required-for-iforce-max-hybrid-87-or-91.3263/ — 2024–2025 — consultada 2026-11-18 — foro (reproduce el texto del manual)
4. 4Runner6G Forum — "Recommended regular fuel gas octane 87 engine oil grade 0W-20 2025 4Runner 6th gen" (cita el manual 2025, pág. 617) — https://www.4runner6g.com/forum/threads/recommended-regular-fuel-gas-octane-87-engine-oil-grade-0w-20-2025-4runner-6th-gen.2056/ — 2024–2025 — consultada 2026-11-18 — foro (reproduce el texto del manual)
5. 6thgen4runner.com — "2025+ (6th Gen) Toyota 4Runner Fuel Type & Tank Capacity" — https://6thgen4runner.com/threads/2025-6th-gen-toyota-4runner-fuel-type-tank-capacity.648/ — 2024–2025 — consultada 2026-11-18 — foro
6. 4Runner6G Forum — "Different owners manual starting 2026 June production 4Runner" (OM35C07U / OM35C28U) — https://www.4runner6g.com/forum/threads/different-owners-manual-starting-2026-june-production-4runner.10728/ — 2026 — consultada 2026-11-18 — foro
7. manuals.plus — Toyota 4Runner 2025 (OM35B85U) — https://manuals.plus/hmn/m/b9266332aeec716c7f1e26a4b7aab797d1e7ed7ca98e3dc923f7314d8363fe1a — 2025 — consultada 2026-11-18 — secundaria (copia del manual)
8. Toyota — Fuel information (manual OM04011U, capítulo 8, de otro modelo) — https://assets.sia.toyota.com/publications/en/om-x/OM04011U/topics/chapter8/ch08se010402.html — s.f. — consultada 2026-11-18 — primaria (vía extracto)
9. 2016 Prius Owner's Manual (EE. UU.), sección de combustible (MMT) — https://attachments.priuschat.com/attachment-files/2019/06/168344_2016_Prius_Owners_Manual_-_US_-_fuel_info.pdf — 2016 (subido en 2019) — consultada 2026-11-18 — primaria (copia en foro)
10. Toyota Tundra Owner's Manual, pág. 612 (MMT), en ManualsLib — https://www.manualslib.com/manual/1407350/Toyota-Tundra.html?page=612 — s.f. — consultada 2026-11-18 — secundaria (copia del manual)
11. ClubLexus — "Fuel 87 or 91" (NX de segunda generación, 2022 en adelante; cita el manual del NX 350) — https://www.clublexus.com/forums/nx-2nd-gen-2022-current/980704-fuel-87-or-91-a.html — 2022–2025 — consultada 2026-11-18 — foro (cita fuente primaria)
12. Consumer Reports — "Cars that require premium fuel do not always benefit from it" — https://www.consumerreports.org/cars/fuel-economy-efficiency/cars-that-require-premium-fuel-do-not-always-benefit-from-it-a1099718013/ — s.f. (menciona el Lexus TX) — consultada 2026-11-18 — prensa
13. Toyota-club.net — FAQ del motor T24 — https://www.toyota-club.net/files/faq/21-09-20_faq_t24-engine_en.htm — 2021-09-20 — consultada 2026-11-18 — secundaria técnica
14. MotorReviewer — ficha del T24A-FTS — https://www.motorreviewer.com/engine.php?engine_id=216 — s.f. — consultada 2026-11-18 — secundaria
15. Reliable Toyota (concesionario) — showroom 2025 4Runner i-FORCE MAX — https://www.reliabletoyotamo.com/showroom/2025/Toyota/4Runner+i-FORCE+MAX/SUV.htm — 2025 — consultada 2026-11-18 — secundaria (concesionario)
16. North Hollywood Toyota — "2026 Toyota 4Runner Hybrid vs. 4Runner" — https://www.northhollywoodtoyota.com/blog/2026-toyota-4runner-hybrid-vs-gas — 2025–2026 — consultada 2026-11-18 — secundaria (concesionario)
17. Tustin Toyota — "2026 Toyota 4Runner i-FORCE MAX: Specs, MPG and Features" — https://www.tustintoyota.com/research/2026-toyota-4runner-hybrid-specs/ — 2025–2026 — consultada 2026-11-18 — secundaria (concesionario)
18. Kelley Blue Book — 2026 Toyota 4Runner i-FORCE MAX Specs — https://www.kbb.com/toyota/4runner-i-force-max/2026/specs/ — 2025–2026 — consultada 2026-11-18 — secundaria
19. Motor1 — "Toyota's Hybrid Truck System Will Be a Game-Changer. Here's How It Works" — https://www.motor1.com/features/717505/toyota-i-force-max-hybrid-truck-explainer/ — 2023–2024 — consultada 2026-11-18 — prensa
20. Olathe Toyota Parts — "i-FORCE MAX hybrid maintenance: OEM care" — https://parts.olathetoyota.com/blog/i-force-max-hybrid-maintenance-oem-care — 2025–2026 — consultada 2026-11-18 — secundaria (distribuidor de repuestos de concesionario)
21. Tacoma4G Forum — "Hybrid automated thermal management system" — https://www.tacoma4g.com/forum/threads/hybrid-automated-thermal-management-system.22761/ — 2025–2026 — consultada 2026-11-18 — foro
22. Top Gear — "Toyota's new Tacoma truck gets hybrid tech…" — https://www.topgear.com/car-news/electric/toyotas-new-tacoma-truck-gets-hybrid-tech-and-shock-absorbers-seats — 2023 — consultada 2026-11-18 — prensa
23. 4Runner6G — "2027 4Runner changes" — https://www.4runner6g.com/2027-4runner-changes/ — 2026 — consultada 2026-11-18 — foro/blog
24. TFLcar — "2027 Toyota TRD Pro Models Get Honey-Hued Signature Color" — https://tflcar.com/2026/07/2027-toyota-4runner-trd-pro-new-color-update/ — jul-2026 — consultada 2026-11-18 — prensa
25. Efecto Cocuyo — "Pdvsa inicia plan piloto con gasolina Súper Premium de 97 octanos a $1 por litro en Caracas" — https://efectococuyo.com/economia/pdvsainicia-plan-piloto-con-gasolina-super-premium-de-97-octanos-a-1-por-litro-en-caracas/ — feb-2026 — consultada 2026-11-18 — prensa
26. El Pitazo — "Gasolina Súper Premium: ¿tiene realmente el octanaje que prometió Pdvsa?" — https://elpitazo.net/economia/gasolina-super-premium-tiene-realmente-el-octanaje-que-prometio-pdvsa/ — ~feb-2026 (unos 266 días de antigüedad según el buscador) — consultada 2026-11-18 — prensa
27. El Diario — "Gasolina 'Súper Premium' en Venezuela: ¿en qué se diferencia de los otros octanajes?" — https://eldiario.com/2026/02/19/gasolina-super-premium-venezuela-en-que-se-diferencia-otros-octanajes/ — 2026-02-19 — consultada 2026-11-18 — prensa
28. El Diario — "Reportaron plan piloto de distribución de gasolina 'Súper Premium' en Caracas" — https://eldiario.com/2026/02/18/plan-piloto-de-distribucion-de-gasolina-super-premium-en-caracas/ — 2026-02-18 — consultada 2026-11-18 — prensa
29. El Diario — "Estaciones de gasolina 'Súper Premium' en Caracas se preparan para ofrecer combustible estándar" — https://eldiario.com/2026/04/15/estaciones-super-premium-gasolina-estandar-caracas/ — 2026-04-15 — consultada 2026-11-18 — prensa
30. CNN en Español — "El precio del combustible premium en Venezuela, más caro y solo en dólares" — https://cnnespanol.cnn.com/2026/04/15/venezuela/venezuela-sistema-combustibles-subsidiado-premium-verde-rojo-orix — 2026-04-15 — consultada 2026-11-18 — prensa
31. Noticias24 Carabobo — "Gasolina Súper Premium en Carabobo ya se vende en estas estaciones" — https://noticias24carabobo.com/gasolina-super-premium-en-carabobo-ya-se-vende-en-estas-estaciones/ — feb-2026 — consultada 2026-11-18 — prensa local
32. Sandy Aveledo — "Ya llegó la gasolina premium a Carabobo" — https://sandyaveledo.net/ya-llego-la-gasolina-premium-a-carabobo/ — feb-2026 — consultada 2026-11-18 — prensa local/blog
33. El Carabobeño — "Venta de gasolina cayó tras plan Súper Premium" — https://www.el-carabobeno.com/venta-de-gasolina-cayo-tras-plan-super-premium/ — 2026 — consultada 2026-11-18 — prensa
34. El Impulso — "Fedengas propone homogeneizar las estaciones de servicios para la venta de gasolina Súper Premium" — https://www.elimpulso.com/2026/03/11/fedengas-propone-homogeneizar-las-estaciones-de-servicios-para-la-venta-de-gasolina-super-premium-11mar/ — 2026-03-11 — consultada 2026-11-18 — prensa
35. Valora Analitik — "Gasolineras de Venezuela, en alerta tras nuevo esquema de gasolina premium" — https://www.valoraanalitik.com/gasolineras-de-venezuela-en-alerta-tras-nuevo-esquema-de-gasolina-premium/ — 2026 — consultada 2026-11-18 — prensa
36. MSC Noticias — "¿Gasolina de 97 octanos? Lo que tu motor de verdad necesita" (posición de CANATAME) — https://www.mscnoticias.com.ve/2026/03/gasolina-de-97-octanos-lo-que-tu-motor-de-verdad-necesita/ — mar-2026 — consultada 2026-11-18 — prensa
37. El Tequeño — "Mala calidad de gasolina en Venezuela provoca averías en motores de vehículos: 'no trae el octanaje suficiente'" — https://xn--eltequeo-j3a.com/mala-calidad-de-gasolina-en-venezuela-provoca-averias-en-motores-de-vehiculos-no-trae-el-octanaje-suficiente/ — fecha [NO VERIFICADO] — consultada 2026-11-18 — prensa
38. El Nacional — "Problemas en el combustible: gasolina rendida con agua, sin aditivos necesarios y sucia, causa daños e incendios en vehículos" — https://www.elnacional.com/2023/05/problemas-en-el-combustible-gasolina-rendida-con-agua-sin-aditivos-necesarios-y-sucia-causa-danos-e-incendios-en-vehiculos/ — may-2023 — consultada 2026-11-18 — prensa
39. Impacto VE — "Gasolina de 97 octanos: lo que se sabe del plan piloto de PDVSA" — https://impactove.com/gasolina-de-97-octanos-lo-que-se-sabe-del-plan-piloto-de-pdvsa — 2026 — consultada 2026-11-18 — prensa
40. El Estímulo — "El petróleo venezolano se reinventa… ¿el precio de la gasolina también?" — https://elestimulo.com/elinteres/energia/2026-02-19/petroleo-precio-gasolina/ — 2026-02-19 — consultada 2026-11-18 — prensa
41. Índice Gasolina Venezuela — https://gasolina.com.ve/ — sin fecha (visto vía buscador, nov-2026) — consultada 2026-11-18 — secundaria no oficial
42. Reuters (vía TradingView) — "Venezuela's refineries working at about 35% of capacity, sources say" — https://www.tradingview.com/news/reuters.com,2026:newsml_L1N3ZF19E:0-venezuela-s-refineries-working-at-about-35-of-capacity-sources-say/ — feb-2026 — consultada 2026-11-18 — prensa
43. Inspectioneering — "Venezuela's Refineries Boost Processing to 35% of Capacity" — https://inspectioneering.com/news/2026-02-23/11952/venezuelas-refineries-boost-processing-to-35-of-capacity — 2026-02-23 — consultada 2026-11-18 — prensa
44. Energy News Beat — "Venezuela's Cardón Refinery Halted After Fire, Taking 310,000 bpd Offline" — https://energynewsbeat.co/downstream/venezuelas-cardon-refinery-halted-after-fire-taking-310000-bpd-offline/ — oct-2026 — consultada 2026-11-18 — prensa
45. Democracy Now — "Venezuela's Second-Largest Refinery Idles as Natural Gas Line Rupture Triggers Fire" — https://www.democracynow.org/2026/10/8/headlines/venezuelas_second_largest_refinery_idles_as_natural_gas_line_rupture_triggers_fire — 2026-10-08 — consultada 2026-11-18 — prensa
46. Reuters (vía KWSN) — "'Ugly and rusty,' Venezuela's refineries are relics that will be hard to revive" — https://kwsn.com/2026/07/29/ugly-and-rusty-venezuelas-refineries-are-relics-that-will-be-hard-to-revive/ — 2026-07-29 — consultada 2026-11-18 — prensa
47. Pipeline & Gas Journal — "Venezuela's Refineries Crumble Despite Oil Export Rebound" — https://pgjonline.com/news/2026/july/venezuelas-refineries-crumble-despite-oil-export-rebound — jul-2026 — consultada 2026-11-18 — prensa
48. Devdiscourse (Reuters) — "Venezuela's Refining Struggles Amid Recovery Efforts" — https://www.devdiscourse.com/article/headlines/3811263-venezuelas-refining-struggles-amid-recovery-efforts — 2026 — consultada 2026-11-18 — prensa
49. AP (vía Anchorage Daily News) — "Venezuela's acting president signs oil industry overhaul easing state control to lure investors" — https://www.adn.com/nation-world/2026/01/29/venezuelas-acting-president-signs-oil-industry-overhaul-easing-state-control-to-lure-investors/ — 2026-01-29 — consultada 2026-11-18 — prensa
50. Cleary Gottlieb — "Venezuela's oil reform: new opportunities, unanswered questions, investor considerations" — https://www.clearygottlieb.com/-/media/files/alert-memos-2026/venezuelas-oil-reform-new-opportunities-unanswered-questions-investor-considerations.pdf — 2026-07-14 — consultada 2026-11-18 — secundaria (jurídica)
51. La Razón (Bolivia) — "Transporte alerta sobre una gasolina de 85 octanos con alto contenido de etanol" — https://larazon.bo/economia-y-empresa/2026/10/28/transporte-alerta-sobre-una-gasolina-de-85-octanos-con-alto-contenido-de-etanol/ — 2026-10-28 — consultada 2026-11-18 — prensa
52. Ecuavisa — "¿Cómo se mide el octanaje y azufre en las gasolinas?" — https://www.ecuavisa.com/noticias/ecuador/como-se-mide-el-octanaje-y-azufre-en-las-gasolinas-LJ1469519 — fecha [NO VERIFICADO] — consultada 2026-11-18 — prensa
53. Reuters (vía Roic.ai) — "Flames, Smoke Seen at Venezuela's Cardón Refinery, Four Sources Say" — https://www.roic.ai/news/flames-smoke-seen-at-venezuelas-cardn-refinery-four-sources-say-10-06-2026 — 2026-10-06 — consultada 2026-11-18 — prensa
54. BNN Bloomberg — "Venezuelan lawmakers approve easing state control of oil industry" — https://www.bnnbloomberg.ca/markets/oil/2026/01/29/venezuelan-lawmakers-approve-easing-state-control-of-oil-industry/ — 2026-01-29 — consultada 2026-11-18 — prensa
55. Wikipedia — "Fuel shortages in Venezuela" (solo contexto, no se usa como evidencia) — https://en.wikipedia.org/wiki/Fuel_shortages_in_Venezuela — s.f. — consultada 2026-11-18 — secundaria
56. Finanzas Digital — "Fenegas: modelo único de gasolina 2026" (probable origen del dato de ~2 % de ventas; atribución [NO VERIFICADO]) — https://finanzasdigital.com/fenegas-modelo-unico-gasolina-2026/ — 2026 — consultada 2026-11-18 — prensa
