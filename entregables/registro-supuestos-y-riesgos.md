# Registro de supuestos y riesgos

**Proyecto:** cocina central de Grupo BS 2000
**Abierto:** 26-10-2026, en la Fase 0
**Última actualización:** 26-10-2026, Fase 0

Es un documento vivo y se actualiza al cierre de cada fase.

- Un **supuesto** es un valor o un hecho que uso para avanzar sin haberlo confirmado. En los demás entregables aparece marcado **[SUPUESTO]**.
- Un **riesgo** es algo que puede salir mal y afectar el costo, el plazo, la inocuidad o la operación.

Cada supuesto indica qué dato lo confirma, con el código de la planilla `00-planilla-levantamiento.xlsx`.

---

## 1. Supuestos

| ID | Supuesto | Fuente o razonamiento | Dato que lo confirma | Fases afectadas | Estado |
|---|---|---|---|---|---|
| S-01 | El área de la cocina es de **~145 m²**, en un rango de 120–170 m² | Proporción de píxeles contra los 743 m² del plano, que no tiene escala ni cotas (dato del encargo) | P1-04: medición de tramos y diagonales | 2 a 8 | Abierto |
| S-02 | La huella es de **~20 × 7,5 m** | Misma estimación por píxeles (encargo) | P1-04 | 2 a 4 | Abierto |
| S-03 | El estado actual descrito en la sección 4 del encargo (piso, paredes, techo, iluminación, campana, equipos) es correcto | Descripción del dueño. Las fotos **no están** en el repositorio | P1-01: fotos | 1 | Abierto |
| S-04 | El listado de equipos nuevos y sus precios son los de la tabla 8.2 del encargo | Transcripción del dueño (WebstaurantStore). La captura **no está** en el repositorio | P1-01, P2-09 | 5, 8 | Abierto |
| S-05 | El combi, la plancha y las hornillas de olla están cotizados en versión **gas natural**. Los charbroilers y la salamandra, a gas de tipo no especificado | Tabla 8.2 del encargo | P1-02, P2-09 | 5, 8 | Abierto |
| S-06 | El tipo de gas del edificio (natural o GLP) es **desconocido** | Sin datos | P1-10 | 3 a 5, 8 | Abierto |
| S-07 | La acometida eléctrica (voltaje, fases, capacidad) es **desconocida**. Hipótesis de trabajo: 60 Hz con 120 V y 208/240 V disponibles; no sé si hay trifásico | Encargo, sección 8.2, alerta 2 | P1-11 | 3 a 5, 8 | Abierto |
| S-08 | iVario Pro 2-S: **208–240 V, 3 fases, ~23 kW, 64/53 A** | Listado de un revendedor (Canadian Restaurant Supply). La versión europea es de 21 kW a 400 V | Ficha oficial de Rational USA | 5, 8 | Abierto |
| S-09 | Estella SM50: **220–240 V, 1 fase, 4 hp** | Listado de equipo usado (SIGMA Equipment). WebstaurantStore indica 220 V y 4 hp sin decir las fases | Ficha oficial de Estella o placa del equipo | 5 | Abierto |
| S-10 | Avantco F202: **2 tanques de 15 lb**, 2 circuitos de 208–240 V de 2,7/3,6 kW cada uno, enchufe NEMA 6-20P | Listados de WebstaurantStore | Ficha oficial | 5 | Abierto |
| S-11 | La carta vigente de Blue58 es `blue58-menu-en.pdf` (57 referencias de comida) | Único documento del repositorio | P2-03: carta en español y reporte de ventas | 2 a 4 | Abierto |
| S-12 | Alitas BBQ, milanesas y papas rústicas **se fríen**. El salmón glaseado va a la plancha y la sopa de cebolla se gratina | Inferido de la descripción de cada plato | Confirmación del chef (P2-03) | 2 a 4 | Abierto |
| S-13 | El muro entre la cocina y el restaurante **admite abrir un vano** para el pase | Sin datos. Es condición para una decisión ya tomada por el dueño | P1-03, P1-08 y revisión estructural | 3 a 5, 7 | Abierto |
| S-14 | Los desayunos se producen en la misma línea del ala Blue58 y terminan antes del almuerzo | Encargo, secciones 2 y 5 | P2-04 | 2 a 4 | Abierto |

---

## 2. Riesgos

Escala: **A** = alta, **M** = media, **B** = baja.

| ID | Riesgo | Prob. | Impacto | Mitigación propuesta | Responsable | Estado |
|---|---|---|---|---|---|---|
| R-01 | **Faltan los insumos** (plano, fotos, listado de equipos): el diseño arrancaría sin base visual | A (situación actual) | A | Subirlos a `insumos/` antes de la Fase 1 | Dueño | Abierto |
| R-02 | Comprar equipos para un **tipo de gas equivocado**: ≈USD 39.400 entre combi, plancha, hornillas de olla y charbroilers, más la salamandra | M | A | No comprar los equipos a gas hasta confirmar el tipo de gas (P1-10). Si es GLP, pedirlos en versión GLP de fábrica y verificar la presión | Dueño + MEP | Abierto |
| R-03 | **No hay trifásico, o no hay capacidad** para el iVario (~23 kW) más el resto de las cargas nuevas | M | A | Verificar la acometida y el tablero (P1-11). Alternativas a evaluar: ampliar la acometida, un modelo menor (iVario Pro 2-XS, también trifásico pero de menor carga [por verificar]) o un basculante a gas | MEP | Abierto |
| R-04 | El hotel **no autoriza** la obra: abrir el muro para el pase, cambiar el piso, rehacer desagües | M | A | Revisar el contrato (P1-03) y presentar un anteproyecto al hotel apenas haya layout (Fase 3) | Dueño | Abierto |
| R-05 | El **área no alcanza** para 600 pax con el restaurante operando en paralelo | M-A (hipótesis) | A | Cálculo en la Fase 2. Opciones: producción escalonada, abatidor y cook-chill, espacios contiguos (P2-13) | Chef consultor | Abierto |
| R-06 | La obra **interrumpe el servicio** | A | A | Plan por fases (Fase 7): trabajo nocturno, estaciones temporales, días de baja demanda (P3-07) | Coordinador | Abierto |
| R-07 | **Cortes eléctricos o de agua** frecuentes afectan la cadena de frío, el combi y el iVario | M (por confirmar) | A | Dimensionar la planta y el respaldo de agua (P3-01, P3-02) | MEP | Abierto |
| R-08 | La campana existente **no tiene caudal suficiente** para la nueva carga térmica: ≈532.000 BTU/h (≈156 kW) solo en los equipos nuevos con BTU conocido | M | A | Medir el caudal real (P1-09), hacer el balance de extracción e inyección (Fase 5) y decidir qué equipos van bajo la campana | MEP | Abierto |
| R-09 | Equipos importados **sin servicio técnico ni repuestos** locales; la garantía de compra en EE. UU. podría no cubrir Venezuela | M | M | Comparar con distribuidores locales (P3-10) y confirmar la cobertura de garantía por marca | Coordinador | Abierto |
| R-10 | **Agua dura** sin tratamiento daña el combi y el iVario | M | M-A | Análisis de dureza (P3-01) y ablandador o filtro según el resultado y lo que pida el fabricante | MEP | Abierto |
| R-11 | Las **plagas se dispersan** al desmontar los paneles de PVC | A | M | Control de plagas antes, durante y después del desmontaje, y sellado inmediato | Arquitecto | Abierto |
| R-12 | La **freidora** de la lista (Avantco F202, gama media) es insuficiente para 13 referencias fritas y acompañantes fritos en 16 platos | M (hipótesis) | M | Calcular la demanda de fritura con el reporte de ventas (P2-03) y evaluar freidoras de piso o más tanques | Chef + MEP | Abierto |
| R-13 | **No hay equipo dedicado** para pizzettas ni pasta en el plan de compras | M | M | Confirmar cómo se hacen hoy (P2-14) y decidir equipo o regeneración en la Fase 4 | Chef | Abierto |

---

## 3. Historial

| Fecha | Fase | Cambio |
|---|---|---|
| 26-10-2026 | 0 | Registro creado: supuestos S-01 a S-14 y riesgos R-01 a R-13 |
