# Fase 0 — Levantamiento de datos faltantes

**Proyecto:** cocina central de Grupo BS 2000 (Blue58 · Desayunos · BS Catering · Producción centralizada)
**Ubicación:** Hotel Guaparo Inn, Naguanagua / Valencia, Carabobo
**Fecha:** 26 de octubre de 2026
**Estado:** Fase 0 entregada. **En pausa: espero tus datos y tu visto bueno para pasar a la Fase 1.**
**Equipo consultor:** arquitecto de interiores gastronómicos · ingeniero de instalaciones (MEP) · chef consultor de operaciones · coordinador

Archivos de esta fase:

| Archivo | Para qué sirve |
|---|---|
| `entregables/00-fase-0-levantamiento-de-datos.md` | Este documento: qué entendí, qué falta y cómo medirlo |
| `entregables/00-planilla-levantamiento.xlsx` | Planilla para anotar cada medida y respuesta (celdas amarillas) |
| `entregables/registro-supuestos-y-riesgos.md` | Entregable 10, abierto desde hoy y vivo hasta el final |
| `insumos/README.md` | Qué subir a `insumos/`, con qué nombre y cómo hacerlo |

---

## 1. Qué encontré en los insumos

| Insumo esperado | Estado | Consecuencia |
|---|---|---|
| `insumos/plano-planta-baja.png` | **No está en el repositorio** | No puedo validar el polígono, las colindancias ni el área de ~145 m². |
| `insumos/fotos/` | **No está** | El diagnóstico de la sección 4 del encargo queda **sin validar**: lo trato como tu descripción, no como observación propia. |
| `insumos/equipos-a-comprar.png` | **No está** | Trabajo con la tabla 8.2 del encargo, que transcribiste tú. |
| Mediciones, facturas, fichas técnicas | **No hay** | — |
| `blue58-menu-en.pdf` (raíz del repositorio) | **Encontrado** | Es la carta de Blue58 en inglés (comida y bebidas). La usé para afinar las preguntas sobre la línea (sección 3). |

El repositorio `Blue58ve/carta` solo contiene el README y la carta. Dejé creada la carpeta `insumos/`, con instrucciones, para que subas el resto.

---

## 2. Lo que entendí

- **Alcance.** Se rediseña solo el polígono rojo de la cocina dentro de los 743 m² arrendados: unos 145 m² **[SUPUESTO]**, en un rango de 120–170 m², con una huella aproximada de 20 × 7,5 m. El resto del local no se toca.
- **Una cocina sectorizada en dos alas:**
  - **Ala Blue58 (pequeña).** Línea de restaurante y desayunos, pegada a la puerta del restaurante, con ventana totalmente abierta (pase) hacia el salón y presencia de marca.
  - **Ala de Producción y Catering (grande).** Producción a granel, pastelería, pasapalos, ensamble, holding y despacho por una salida propia.
- **Cuatro operaciones comparten la cocina:**
  - Desayunos (60–120 diarios).
  - Blue58 à la carte: volumen bajo, pero con retrasos en las comandas.
  - BS Catering: 2–3 eventos por semana de 150–250 pax, con capacidad de diseño de **600 pax**.
  - Producción centralizada.
- **El escenario que dimensiona el diseño:** restaurante con mesas + evento de hasta 600 pax + desayunos al día siguiente, todo en simultáneo y sin cruces de personas ni de carros.
- **Lo que no se toca:**
  - Las cavas, incluida la de vegetales.
  - La campana central con sus ductos.
  - Fregaderos, dishwasher, hornos, rebanadora y refrigeración.
  - La batería caliente se queda sobre el gas y los desagües actuales, salvo que se justifique moverla.
  - La columna bajo la campana se integra al diseño.
- **La cocina no cierra.** La obra va por fases, con la operación funcionando en paralelo.
- **El flujo es lineal:** entrada de mercancía → recepción → lavado → almacenamiento → preparación → cocción → holding → ensamble → despacho por la salida de catering.
- **Los siete problemas a resolver:**
  1. Retrasos en las comandas.
  2. Mise en place lejos de las estaciones.
  3. Flujos cruzados.
  4. Recepción sin un punto definido.
  5. Agua empozada.
  6. Plagas en los paneles de PVC.
  7. Piso roto.
- **Equipos nuevos.** Son 17 partidas (18 unidades) de WebstaurantStore. Varias vienen a gas natural, y el iVario a 208/240 V. Antes de comprar hay que verificar el tipo de gas, el voltaje, las fases, la planta eléctrica y la capacidad de la campana.
- **Forma de trabajo:**
  - Por fases, preguntando antes de asumir.
  - Todo valor no confirmado se marca **[SUPUESTO]**.
  - Presupuestos en USD.
  - Todo lo producido va a `entregables/`.

---

## 3. Lo que la carta de Blue58 le exige a la línea

La carta tiene **57 referencias de comida** repartidas en 11 secciones y al menos 7 técnicas de cocción. Esto define las estaciones del ala Blue58.

| Técnica o estación | Platos de la carta | Equipo que implica | Pregunta abierta |
|---|---|---|---|
| **Fritura** | Tequeños, croquetas, arancini, mini empanadas, chicken tenders (×2), alitas BBQ\*, milanesas de res y de pollo\*, chicken crispy burger, papas fritas, papas trufadas y tajadas. Además, papas rústicas\* en todas las hamburguesas y milanesas | Al menos 2 freidoras con aceites separados: empanizados y proteínas por un lado, papas y plátano por otro | ¿Cuántas freidoras hay hoy, de qué capacidad y a qué energía? |
| **Parrilla (charbroiler)** | Rib eye 300 g, baby beef 250 g, pechuga, churrasco, chateaubriand y entrecôte | Charbroiler con refrigeración bajo mesón para las proteínas | ¿Cuál de las dos parrillas nuevas va a la línea y cuál a producción? |
| **Plancha** | 5 hamburguesas, kids burger, club house (huevo frito) y salmón glaseado\* | Plancha de 48" | — |
| **Salamandra** | Lasaña y ½ lasaña gratinadas, gratín de puerro y sopa de cebolla\* | Salamandra sobre la línea | ¿Qué modelo de salamandra Vulcan es? |
| **Pasta** | Ravioloni, 4 linguine y ½ boloñesa | Cuece-pastas u olla dedicada en una hornilla | ¿La pasta se cuece al momento o se precuece? |
| **Pizzettas** | 4 sabores y toppings | Horno de pizza o de piso, o combi o convección | **No hay horno de pizza en la lista de compras. ¿Dónde se hornean hoy?** |
| **Sopas y salsas** | 4 sopas o cremas. Salsas: bearnesa, café de París, chimichurri, BBQ, salsa del día, ragú, carbonara y cuatro quesos | Baño de María con más de 2 pozos y holding controlado para la bearnesa | — |
| **Frío (garde manger)** | Carpaccio, 4 ensaladas y side Caesar | Mesa refrigerada de preparación, con la rebanadora cerca | — |
| **Postres** | Brownie con helado, lemon pie, tres leches, tiramisú y helado | Congelador para helado y refrigerador para postres | ¿Quién emplata los postres: la línea, pastelería o la barra? |

\* Técnica inferida de la descripción del plato **[SUPUESTO]**. El chef debe confirmarla.

**Lectura preliminar del chef consultor (se valida en la Fase 1):**

1. **La freidora será el cuello de botella de la línea.**
   - Hasta 13 referencias pasan por aceite, y papas o tajadas acompañan a 16 platos.
   - La freidora de la lista (Avantco F202) tiene 2 tanques de 15 lb (≈6,8 kg de aceite cada uno), 2 × 2,7/3,6 kW a 208–240 V y es de gama media.
   - Parece corta como freidora principal **[SUPUESTO — se calcula en la Fase 2]**.
2. **Pizzettas y pasta no tienen equipo dedicado** en la lista de compras.
3. **La amplitud de la carta también explica los retrasos, no solo el layout.** Con 57 referencias y 7 técnicas, el cocinero cambia de técnica a cada comanda. Lo evaluaremos en la Fase 1, sin dar por hecho que haya que recortar la carta.
4. **Faltan documentos:** la carta en español (si difiere), la de desayunos y los menús de eventos.

---

## 4. Lista priorizada de datos que necesito

**Prioridades:**

- **P1 · Bloqueante.** Sin esto no puedo empezar el diagnóstico ni el programa de áreas.
- **P2 · Programa y layout.** Lo necesito para las Fases 2 a 4.
- **P3 · Ingeniería, obra y presupuesto.** Lo necesito para las Fases 5 a 8 y puede llegar después.

Cada dato tiene su fila en `00-planilla-levantamiento.xlsx`, con el mismo código. Los procedimientos de medición (§6.x) están en la sección 6.

### P1 · Bloqueante

| # | Qué necesito | Por qué | Cómo obtenerlo |
|---|---|---|---|
| **P1-01** | **Subir los insumos:** plano, todas las fotos y captura del listado de equipos | Hoy no tengo ninguna base visual | `insumos/README.md` |
| **P1-02** | **¿Ya compraste o pagaste algún equipo de la lista? ¿Cuáles?** | ≈USD 70.400 en equipos dependen del tipo de gas y de que haya trifásico (ver pregunta urgente 1) | Respuesta directa |
| **P1-03** | **Contrato y permisos del hotel:** qué obras permite el arrendamiento (abrir el muro hacia el restaurante, cambiar el piso, abrir desagües, tocar la campana o las acometidas), quién aprueba y en qué plazo | Si el hotel no autoriza, cambia el alcance completo | Contrato y conversación con el hotel |
| **P1-04** | **Medidas del polígono:** largo de cada tramo de pared y dos diagonales por cada rectángulo principal | El área de 145 m² es una estimación por píxeles | §6.2 · hoja 2 |
| **P1-05** | **Alturas libres:** del piso a la placa, al fondo de las vigas, al fondo de ductos y tuberías y al borde inferior de la campana | Definen cielo raso, recorridos de ductos, campanas y equipos altos (racks, combi sobre base) | §6.3 · hoja 2 |
| **P1-06** | **Columnas:** ubicación (distancia a dos paredes) y sección de cada una, sobre todo la que está bajo la campana | Condicionan pasillos y estaciones | §6.4 · hoja 3 |
| **P1-07** | **Puertas y vanos:** ancho libre, alto, sentido de apertura y qué conectan. Incluye restaurante, Salón Privado 1, mercancía, salida de catering, escalera y **cada cava** | Flujos, paso de carros GN y espacio que barren las puertas de las cavas | §6.5 · hoja 4 |
| **P1-08** | **Muro hacia el restaurante** (donde iría el pase): material, espesor, si lleva columnas o tuberías por dentro, y fotos desde ambos lados | Abrir un vano puede requerir ingeniero estructural y permiso del hotel | §6.6 |
| **P1-09** | **Campana central:** largo × ancho, altura del borde inferior, cantidad y medida de los filtros, placas y ubicación de los motores de extracción e inyección, y si tiene sistema de supresión | Define qué equipos caben debajo y si la extracción alcanza. Los equipos nuevos con BTU conocido suman ≈532.000 BTU/h (≈156 kW) | §6.7 |
| **P1-10** | **Gas:** ¿gas natural por tubería o GLP (bombonas o tanque)? Fotos del medidor o regulador, de las válvulas y del recorrido visible, y diámetro de la tubería | Combi, plancha, hornillas de olla y charbroilers vienen cotizados a **gas natural** | Mantenimiento del hotel y fotos |
| **P1-11** | **Electricidad:** fotos de los tableros de la cocina con la puerta abierta (sin quitar la tapa interna), del breaker principal, del medidor y de la placa de la planta eléctrica. ¿Qué cargas respalda hoy la planta? ¿La cocina tiene medidor propio o depende del hotel? | El iVario Pro 2-S pide **208–240 V trifásico, ~23 kW (≈64 A a 208 V)** según la ficha de un revendedor | Electricista del hotel |
| **P1-12** | **Desagües:** ubicación y medidas de canaletas y rejillas, sumideros y trampa de grasa (dónde está, tamaño, cada cuánto se limpia), y **mapa de dónde se empoza el agua** | Las pendientes nuevas parten de estos puntos | §6.8 |
| **P1-13** | **¿Quién hará las mediciones?** ¿Puede ayudar el personal de mantenimiento o el electricista del hotel? | Gas, electricidad y azotea requieren a alguien autorizado | Respuesta directa |

### P2 · Programa de áreas y layout

| # | Qué necesito | Por qué |
|---|---|---|
| **P2-01** | **Menús de eventos tipo** (los 3–5 más vendidos), **estilo de servicio** (emplatado, buffet, cóctel o pasapalos, estaciones) y proporción on-premise / off-premise. **Para 600 pax, ¿qué estilo?** | Cambia todo el cálculo de capacidad: 600 emplatados a la vez no se parecen a 600 en buffet |
| **P2-02** | **Salones atendidos:** capacidad de cada salón del hotel, distancia y ruta desde la cocina (rampas, ascensor, escalones) y cómo se transporta lo que va off-premise (vehículo, cajas térmicas) | Holding, despacho y carros |
| **P2-03** | **Ventas del restaurante:** reporte de 3 meses del sistema de ventas con platos por servicio, los 20 más vendidos, hora pico y comandas en esa hora. Tiempo actual de salida de platos según el chef. Carta en español, si difiere de la inglesa | Secuencia y dimensionamiento de la línea |
| **P2-04** | **Desayunos:** formato (buffet o a la carta), carta, horario, dónde se sirven y si son para huéspedes del hotel | Define si basta la línea Blue58 o hace falta una estación de desayunos |
| **P2-05** | **Personal:** horario exacto de cada turno, cocineros por estación y turno, y máximo de personas a la vez en la cocina | Espacio por persona, lavamanos y pasillos |
| **P2-06** | **Pastelería y pasapalos:** productos, volumen semanal y horas de uso del horno | Decide si pastelería tiene horno propio o compartido |
| **P2-07** | **Cavas:** uso, temperatura, medidas internas, puerta, estado y ubicación del condensador de cada una | Integración con el almacenamiento · hoja 5 |
| **P2-08** | **Equipos existentes:** foto de la placa y foto de frente con cinta métrica; ancho × fondo × alto, estado y **si se queda, se reubica o se retira** | Cuadro maestro de equipos · §6.9 · hoja 6 |
| **P2-09** | **Equipos nuevos:** ¿la lista es definitiva? Precio de la amasadora Estella SM50, modelo de la salamandra Vulcan, y si se considera un horno de pizza o un cuece-pastas | Cuadro de equipos y cargas |
| **P2-10** | **Recepción:** días y horas de entrega, volumen típico por entrega (carritos), principales proveedores y dónde se guardan hoy los secos | Zona de recepción |
| **P2-11** | **Residuos y aceite usado:** dónde se acumulan hoy, cada cuánto se retiran y por dónde salen | Ruta de sucio sin cruzar zonas limpias |
| **P2-12** | **Lavado:** marca y modelo del dishwasher, volumen de vajilla por servicio, y quién y dónde lava el equipo que vuelve de los eventos off-premise | Zona de lavado |
| **P2-13** | **Espacios contiguos** (restaurante secundario, almacén, cristalería): ¿están en el arrendamiento y podrían usarse para producción, holding o almacenamiento? | Plan B si el área no alcanza para 600 pax |
| **P2-14** | **Pizzettas y pasta:** cómo y con qué equipo se hacen hoy | Hoy no tienen equipo dedicado en el plan |
| **P2-15** | **Comandas:** cómo llegan hoy a la cocina (papel, impresora, pantalla) y qué sistema de ventas usan | Decidir entre KDS o impresora |

### P3 · Ingeniería, obra y presupuesto

| # | Qué necesito | Por qué |
|---|---|---|
| **P3-01** | **Agua:** calentador (tipo, capacidad, ubicación), presión aproximada, tanque o cisterna, frecuencia de cortes y **dureza del agua** (con kit de prueba o análisis) | El combi y el iVario exigen calidad de agua; además, agua caliente por estación |
| **P3-02** | **Energía:** frecuencia y duración típicas de los apagones, y facturas eléctricas de 6–12 meses | Planta eléctrica y cuadro de cargas |
| **P3-03** | **Climatización:** equipos actuales (área de pasapalos, restaurante), capacidad en BTU y estado. Temperatura en la línea en hora pico, con termómetro | Confort y presión de aire hacia el salón |
| **P3-04** | **Iluminación:** cantidad y tipo de lámparas. Opcional: lectura de lux con una app del teléfono en 5 puntos | Diagnóstico de iluminación |
| **P3-05** | **Incendio:** ¿la tubería roja es de rociadores? Extintores existentes (tipo y fecha) y última inspección de bomberos | Protección contra incendio |
| **P3-06** | **Permisos sanitarios:** permiso vigente y actas de inspección con observaciones | Cumplimiento normativo |
| **P3-07** | **Calendario** de eventos de los próximos 3–6 meses y días de menor demanda | Plan de obra por fases |
| **P3-08** | **Presupuesto disponible** (rango en USD) y fecha objetivo. ¿Prefieres ejecutar por etapas según el flujo de caja? | Prioridad de las partidas |
| **P3-09** | **Marca Blue58:** logo en vector, colores y tipografías | Diseño del pase hacia el restaurante |
| **P3-10** | **Proveedores locales de confianza:** contratistas, electricistas, herreros de acero inoxidable y distribuidores de equipos en Venezuela | Cotizaciones de referencia y comparación con la compra en EE. UU. |

---

## 5. Preguntas urgentes (se responden sin medir)

1. **¿Ya compraste o pagaste algún equipo de la lista?** (P1-02)
   - Si todavía no, recomiendo **no comprar aún**:
     - Los equipos a gas: combi, plancha, hornillas de olla, charbroilers y salamandra. Suman ≈USD 39.400 a precios de referencia, sin contar la salamandra.
     - El iVario: ≈USD 31.000.
   - Primero hay que confirmar el tipo de gas y si hay trifásico. Un equipo de gas natural conectado a GLP sin su conversión de fábrica es inseguro, y el iVario no funciona sin trifásico.
2. **¿El gas de la cocina es natural (tubería) o GLP (bombonas o tanque)?** (P1-10)
3. **¿La cocina tiene medidor y tablero propios o depende del hotel? ¿Sabes si llega trifásico?** (P1-11)
4. **¿El hotel permite obra civil?** Sobre todo abrir el muro para el pase hacia el restaurante. (P1-03)
5. **Para un evento de 600 pax, ¿qué estilo de servicio?** Emplatado, buffet, cóctel o mixto. (P2-01)
6. **Desayunos: ¿buffet o a la carta?** (P2-04)
7. **¿Dónde y cómo se hacen hoy las pizzettas y la pasta?** (P2-14)
8. **¿Quién puede hacer las mediciones?** (P1-13)

---

## 6. Protocolo de medición

### 6.1 Herramientas

- Medidor láser (ideal) o cinta métrica de 8 m.
- Teléfono con cámara.
- Plano impreso (A3 si es posible) o un croquis a mano, y un marcador.
- Un balde, para la prueba de desagües.
- Opcional: termómetro y una app de luxómetro.

### 6.2 Polígono de la cocina (P1-04)

1. Imprime el plano o dibuja un croquis de la cocina vista desde arriba. No tiene que estar a escala.
2. Marca con una letra cada esquina. Empieza por la puerta de mercancía como **A** y sigue en el sentido de las agujas del reloj: A, B, C…
3. Mide cada tramo de pared (A–B, B–C…) **a 1 m de altura**, de pared a pared. Anota en metros con dos decimales, por ejemplo 7,52 m.
4. Si la pared tiene un saliente (columna adosada, ducto), cuenta cada quiebre como una esquina más.
5. En cada zona rectangular grande, mide las **dos diagonales**. Si salen iguales, el rectángulo está a escuadra; si no, ajusto el dibujo.
6. Mide también la cava de vegetales por fuera (largo y ancho), porque está dentro del polígono.

### 6.3 Alturas libres (P1-05)

Mide en al menos 4 puntos: junto a la campana, en el centro del ala Blue58, en la zona de producción y junto a la entrada de mercancía.

```
 ═══════════ placa ═══════════   h1: piso → placa
     ▓▓▓ viga ▓▓▓                h2: piso → fondo de la viga
 ─── ducto / tubería ───         h3: piso → fondo del ducto o la tubería más baja
   [====== campana ======]       h4: piso → borde inferior de la campana
 _________ piso __________
```

### 6.4 Columnas (P1-06)

- Numera cada columna en el croquis: C1, C2…
- Mide la distancia de la columna a las dos paredes más cercanas que sean perpendiculares entre sí.
- Mide la sección: ancho × fondo en cm, o el diámetro si es redonda.

### 6.5 Puertas y vanos (P1-07)

- Mide el ancho libre (de marco a marco, por dentro) y el alto libre.
- Dibuja en el croquis hacia dónde abre la hoja. Anota si es batiente, de vaivén, corrediza o cortina de PVC.
- Anota qué conecta y si hoy pasan carros por ella.
- **Incluye las puertas de todas las cavas** y su sentido de apertura.

### 6.6 Muro hacia el restaurante (P1-08)

- Toma fotos de frente desde la cocina y desde el restaurante.
- Golpea suavemente: ¿suena hueco (drywall o tabique) o macizo (bloque o concreto)?
- Mide el espesor en el marco de la puerta de servicio.
- Anota las tuberías, tomas o tableros que haya en ese muro.
- **No perfores nada** para averiguarlo.

### 6.7 Campana (P1-09)

- Mide largo × ancho de la campana y la altura de su borde inferior al piso (h4).
- Cuenta los filtros y mide uno (ancho × alto).
- Fotografía la placa de los motores de extracción e inyección. Suelen estar en el techo o la azotea: ve acompañado de mantenimiento.
- Busca **cilindros rojos o plateados** cerca de la campana, **boquillas** en los ductos o una **palanca manual**. Si los hay, existe un sistema de supresión: fotografía su etiqueta (con la fecha de la última recarga).
- Fotografía lo que hay debajo hoy: de frente y desde los dos lados.

### 6.8 Desagües y agua empozada (P1-12)

1. Marca en el croquis cada canaleta (largo y ancho de la rejilla) y cada sumidero puntual.
2. Levanta una rejilla, mide la profundidad de la canaleta y anota hacia qué extremo corre el agua.
3. **Después de la limpieza de cierre**, espera 15 minutos y fotografía los charcos. Márcalos en el croquis con su tamaño aproximado.
4. Vacía un balde en 3 o 4 puntos sin desagüe cercano y anota hacia dónde corre el agua.
5. Trampa de grasa: ubicación, medidas de la tapa, profundidad (si mantenimiento la abre) y frecuencia de limpieza.

### 6.9 Equipos existentes (P2-08)

Para cada equipo:

- Foto de frente con la cinta métrica extendida a lo ancho.
- Foto de la **placa de datos**, que suele estar atrás, a un costado o dentro de la puerta. Debe verse: marca, modelo, serie, voltaje, amperios o kW, o BTU y tipo de gas.
- Ancho × fondo × alto.
- Estado (bueno, regular o malo) y si se queda, se reubica o se retira.

### 6.10 Nombres de las fotos

Empieza el nombre con el código de la planilla, para que sepa a qué dato corresponde. Por ejemplo:

- `P1-09_campana_frente.jpg`
- `P1-11_tablero-cocina_abierto.jpg`
- `P2-08_EX07_placa.jpg`

### 6.11 Seguridad

- **No abras tableros eléctricos ni quites tapas internas.** Basta una foto con la puerta abierta. Si hay que medir voltaje, que lo haga un electricista.
- **No manipules válvulas ni conexiones de gas.**
- Sube a la azotea o a los motores de la campana solo con personal de mantenimiento.

---

## 7. Cómo enviármelo

1. Llena la planilla `entregables/00-planilla-levantamiento.xlsx` (las celdas amarillas).
2. Sube la planilla llena y las fotos a `insumos/`, siguiendo `insumos/README.md`. También puedes adjuntar las fotos directamente en esta conversación.
3. Puede llegar por partes: **con el bloque P1 completo arranco la Fase 1 (diagnóstico)**.

---

## 8. Alertas tempranas

Son señales para tomar en cuenta, todavía no decisiones. El detalle está en `registro-supuestos-y-riesgos.md`.

| Código | Alerta | Qué la resuelve |
|---|---|---|
| R-02 | Equipos cotizados a **gas natural** sin saber si el edificio tiene gas natural o GLP (≈USD 39.400 en equipos) | P1-02, P1-10 |
| R-03 | El **iVario Pro 2-S** pide 208–240 V **trifásico**, ~23 kW (≈64 A a 208 V) en un circuito dedicado. Sin trifásico o sin esa capacidad libre en el tablero no se puede instalar | P1-11 |
| R-08 | Los equipos nuevos con BTU conocido suman **≈532.000 BTU/h (≈156 kW)** solo bajo la campana, sin contar el combi, la salamandra ni los equipos existentes que se queden. Hay que verificar el caudal de la campana | P1-09 |
| R-05 | **600 pax en ~145 m² compartidos con el restaurante** es exigente. Si el servicio es emplatado, lo más probable es que haga falta producción escalonada con abatidor (cook-chill) **[hipótesis a calcular en la Fase 2]** | P2-01, P2-13 |
| R-04 | El **pase abierto** depende del tipo de muro y de la autorización del hotel. Además, la cocina debe quedar en presión negativa respecto al salón para que no pasen olores | P1-03, P1-08 |
| R-12 | La **freidora** de la lista parece corta para una carta con 13 referencias fritas **[SUPUESTO]** | P2-03, P2-08 |

---

## 9. Siguiente paso

- **Al recibir el bloque P1** ejecuto la **Fase 1 — Diagnóstico**: estado actual por disciplina, con hallazgos priorizados (crítico, alto, medio, bajo).
- **Mientras tanto**, puedo adelantar dos tareas que no dependen de tus datos. ¿Quieres que las haga en paralelo?
  - Descargar y tabular las fichas técnicas oficiales de los 17 equipos nuevos: energía, agua, desagüe y dimensiones.
  - Investigar la normativa venezolana aplicable: Código Eléctrico Nacional (COVENIN 200), normas sanitarias del MPPS y normas de bomberos.

---

### Fuentes consultadas en esta fase

- Carta Blue58 (inglés): `blue58-menu-en.pdf`, en este repositorio.
- Rational iVario Pro 2-S, 208/240 V, 3 fases, 23 kW, 64/53 A (listado de revendedor; **pendiente confirmar con la ficha oficial de Rational USA**): <https://shop.canadianrestaurantsupply.com/rat-wy9enra.0002213.html>
- Rational iVario Pro 2-S, versión europea, 21 kW, 3 N AC 400 V (referencia de mercado): <https://www.ig-groupuk.com/product/kitchen-appliances/ivario-pro-2-s/>
- Estella SM50 (348SM50), 220–240 V, 60 Hz, 1 fase, 4 hp (listado de equipo usado; **pendiente confirmar con la ficha oficial**): <https://sigmaequipment.com/equipment/used/estella-spiral-mixer-313508>
- Avantco F202, 2 × 15 lb, 208–240 V, 5.400/7.200 W, enchufe NEMA 6-20P: <https://www.webstaurantstore.com/outlet/177F202/88889.html>
