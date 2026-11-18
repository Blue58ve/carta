# Agente 7 — Otros riesgos de tener esta camioneta en Venezuela
**Fecha de investigación:** 2026-11-18

## Resumen ejecutivo (5 líneas)
1. **Garantía:** los textos de Toyota USA que localicé limitan la cobertura a los vehículos "originally sold by an authorized dealer in the United States and normally operated or touring in the United States, U.S. territories or Canada" [1][2][5]. En Venezuela hay que dar por perdida toda la garantía, incluida la de batería híbrida de 120 meses/150.000 mi [7][8]. En 2024 TDV declaró que en las importaciones de particulares "la garantía prácticamente se pierde" [23]. No encontré ninguna garantía extendida de terceros que cubra Venezuela [NO VERIFICADO].
2. **Recalls:** según agregadores (no pude consultar NHTSA directamente), la 4Runner de sexta generación tiene 3 campañas: 25V595000 (software del cuadro de instrumentos), 26V282000 y 26V571000 (etiquetas de capacidad de carga). Las tres se resuelven fácil, con software o con una etiqueta [17]-[19]. Un recall mecánico futuro no tendría una solución realista desde Venezuela: llevar la camioneta a Miami no es viable salvo en un caso grave.
3. **Seguro:** el RCV obligatorio cuesta ≈ USD 33–43/año (tarifa de 33–114 EUR, Gaceta Oficial 6.835) [27]-[29]. El casco de cobertura amplia, estimado en 3–7 % del valor, saldría en USD 2.250–5.250/año sobre USD 75.000, o hasta ≈ USD 9.000 si se asegura al valor de mercado local. Son cifras sin cotización real de ninguna aseguradora [NO VERIFICADO].
4. **Robo y reventa:** no hay estadística oficial 2024–2026 de robos por modelo ni para Carabobo [NO VERIFICADO]. La prensa documenta un robo de vehículo con exigencia de rescate en Valencia (jul-2026) y redes regionales que roban camionetas Toyota con destino a Venezuela [41][45]. La reventa es muy alta: hay Trailhunter 2025 publicadas en USD 145.000–169.900 y una venta cerrada en USD 128.890 (sep-2026) [54][55], aunque esos precios podrían bajar si se abre la importación.
5. **Aduana y otros:** no encontré casos documentados en 2025–2026 de robo de piezas en Puerto Cabello o La Guaira [NO VERIFICADO]. Los riesgos principales son: cambios normativos en plena transición política, discrecionalidad aduanera, un vehículo sin seguro de casco durante el tránsito, y el riesgo cambiario (BCV 914,02 Bs/USD, brecha ≈ 20 %, inflación 237,7 %) [36]-[38]. Desde este frente no hay ninguna alerta de alcance.

## Hallazgos detallados

### 0. Limitaciones de esta investigación (leer primero)
- **WebFetch no pudo abrir** los hosts `assets.sia.toyota.com`, `assets.sipb.toyota.com` (PDF del Warranty & Maintenance Guide 2026 de la 4Runner y de la 4Runner HV) ni `api.nhtsa.gov` (base de recalls). El error indica que hay que permitirlos en la configuración de red de la sesión. Tras el tercer fallo dejé de intentar con más sitios, como pedía el mensaje de error.
- **Se agotó el presupuesto compartido de WebSearch** (200 búsquedas por turno, compartido por todos los agentes) en mitad de la investigación. Quedaron sin buscar: exigencia y costo de GPS de las aseguradoras, primas reales de casco por aseguradora, garantías extendidas de terceros, robo de autopartes, casos de robo en puerto, servicio pagado de TDV a vehículos no importados por TDV, disponibilidad local del neumático 265/70R18 y el impuesto municipal de Naguanagua. Todo eso figura como [NO VERIFICADO].
- **Todo el contenido web se obtuvo a través de extractos del buscador**, no leyendo las páginas completas. El verificador debe contrastar las citas textuales con el original.

### 1. Garantía de fábrica (Toyota USA) y exportación

**1.1 Plazos vigentes (año modelo 2025–2026; para 2027 se suponen iguales, [NO VERIFICADO])**

| Cobertura | Plazo | Fuente |
|---|---|---|
| Básica (New Vehicle Limited Warranty) | 36 meses / 36.000 mi | [7][8] |
| Tren motriz | 60 meses / 60.000 mi | [7] |
| Perforación por corrosión | 60 meses / millas ilimitadas | [7] |
| Sistema eléctrico de alto voltaje (componentes híbridos) | 96 meses / 100.000 mi (= 8 años) | [7][8] |
| Batería híbrida (traction battery) | 120 meses / 150.000 mi (= 10 años) | [7][8] |
| ToyotaCare (mantenimiento programado) | 2 años / 25.000 mi | [7] |

Las cifras vienen de listados de concesionarios de EE. UU. (fuente secundaria). La guía oficial de la 4Runner 2026 no se pudo abrir [4]. Un blog que habla de "10 años/150.000 mi de garantía básica" contradice todas las demás fuentes y lo descarto.

**1.2 Ámbito geográfico: texto encontrado**
- Formulación de las guías de Toyota USA: *"These warranties apply to all 2021 model-year Tacoma vehicles distributed by Toyota that are originally sold by an authorized dealer in the United States and normally operated or touring in the United States, U.S. territories or Canada."* [1]. Según el extracto del buscador, la misma fórmula aparece en las guías de 2026 de la Grand Highlander [2] y de la Tacoma [3]. Para la **4Runner 2026/2027 no pude confirmar el texto literal** [4] [NO VERIFICADO]. Es muy probable que use la misma plantilla.
- **Matiz:** la frase "registered and normally operated in the United States" que menciona el encargo **no apareció** en las fuentes. La fórmula encontrada es "originally sold by an authorized dealer in the United States and normally operated or touring in the United States, U.S. territories or Canada". El garante es *Toyota Motor Sales, U.S.A., Inc.* [1].
- Servicio de garantía: *"To obtain warranty service in the United States, U.S. territories, Canada or Mexico, take your vehicle to an authorized Toyota dealership."* [1]. Venezuela no figura en ninguna lista.
- La página de soporte de Toyota USA "Which countries is my New Vehicle Limited Warranty valid in?" indica que la garantía de los vehículos vendidos en EE. UU. vale en **EE. UU., Canadá y territorios de EE. UU.** [5]. Lo sé por el extracto del buscador; no leí la página.
- Texto análogo de Toyota (Canadá, año modelo 2026) para quien viaja o se muda fuera de la zona cubierta: *"Warranty service may not be provided by the local dealer because the local Toyota distributor may have no obligation to provide warranty service to your vehicle, and/or your Toyota may not comply with the regulatory and environmental requirements of such country."* [6]. Hay una frase equivalente en manuales antiguos de Toyota USA ("touring or relocating outside the mainland U.S., Alaska, and Canada") [65].
- La guía 2026 de la Tacoma contiene la línea *"Under this policy, you are eligible in the mainland United States and Alaska"* [3]. Parece referirse a un programa concreto (probablemente ToyotaCare o asistencia en carretera) y no a la garantía base. Hay que confirmarlo en la guía de la 4Runner [NO VERIFICADO].
- **Repuestos comprados en EE. UU. y enviados al exterior:** un distribuidor de repuestos Toyota indica que las piezas enviadas o sacadas de EE. UU. no quedan cubiertas por la política de garantía de Toyota [66] (secundaria).

**Conclusión 1:** una vez la camioneta esté registrada y circulando en Venezuela, no aplica ninguna de las garantías de Toyota USA: ni la básica, ni la de tren motriz, ni la híbrida, ni la de batería. La pérdida que más pesa es la de **batería y componentes de alto voltaje (8–10 años)**. El costo de reemplazar la batería híbrida de la 4Runner i-FORCE MAX queda [NO VERIFICADO]; lo resolvería una cotización de la pieza en un concesionario de EE. UU.

**1.3 Política de "no exportación" de los concesionarios de EE. UU.**
- Una plantilla de la asociación de concesionarios de Virginia (VADA) recoge que el franquiciante tiene una política según la cual *sus concesionarios no deben vender vehículos nuevos para exportación*. También señala riesgo de *chargeback* (penalización al concesionario) si el comprador aparece en la lista de exportadores del fabricante, y menciona que algunos estados protegen al concesionario que vendió de buena fe [22]. No es un documento específico de Toyota.
- En foros, propietarios cuentan que hay concesionarios que se niegan a vender si el comprador dice que va a exportar [FORO/REDES] (citado en [22] como contexto).
- No encontré el texto de la política de exportación de Toyota (TMNA), ni montos de penalización, ni constancia de que firmar un "Non-Export Agreement" y luego exportar anule la garantía [NO VERIFICADO]. **Implicación práctica:** el cliente no debe firmar declaraciones de que no exportará si sí piensa exportar (riesgo contractual y de reclamo del concesionario). Conviene comprar a través de la LLC a un concesionario que acepte ventas para exportación. Esto se cruza con el agente de compra/logística.

**1.4 Toyota de Venezuela (TDV)**
- Declaración de TDV en marzo de 2024: *"en los casos de particulares en los que se importan vehículos de otros países, la garantía prácticamente se pierde"* [23] [PRENSA].
- Un directivo de mercadeo de Toyota Venezuela, en una nota antigua (≈ 2022, fecha exacta sin confirmar): *"Si se compra en nuestros concesionarios el carro viene con garantía, servicio técnico, dotación de repuestos», lo cual no lo pueden ofrecer… los «importadores grises»"* [24] [PRENSA].
- Según un importador no oficial (TOYO VE), **la red oficial venezolana no vende la 4Runner 0 km**; entra por importación directa [25] [CLASIFICADOS/comercial]. No pude consultar toyota.com.ve para confirmarlo [NO VERIFICADO].
- **¿TDV da servicio pagado a vehículos que no importó?** No encontré ninguna fuente que lo confirme o lo niegue [NO VERIFICADO]. Se resolvería preguntando a un concesionario TDV del área de Valencia, gestión que debe hacer el cliente porque este estudio no contacta a terceros. Tampoco encontré si la red TDV vende o atiende híbridos: las fuentes sobre el Corolla Cross híbrido en Venezuela se contradicen y son comerciales [63] [NO VERIFICADO].
- Contexto: se estima que ≈ 20 % de las ventas de vehículos pasa por canales no oficiales ("mercado gris"), sin garantía ni posventa formal [26] [PRENSA, cifra no verificada por la propia fuente].

**1.5 Garantías extendidas de terceros**
- No pude investigarlo (presupuesto de búsqueda agotado) [NO VERIFICADO]. Hipótesis a verificar: los Vehicle Service Agreements de Toyota (Toyota Extra Care) y la mayoría de los VSC de terceros en EE. UU. se limitan a EE. UU. y Canadá. Se resolvería leyendo el contrato de Toyota Extra Care y los de aseguradoras internacionales de garantía mecánica.

### 2. Recalls (campañas de seguridad) de la 4Runner de sexta generación (años modelo 2025–2026)

| Campaña NHTSA | Fecha | Modelos | Defecto | Remedio | Fuente |
|---|---|---|---|---|---|
| 25V595000 | 2025-09-10 | Varios Toyota/Lexus, incluida la 4Runner 2025 | Al arrancar, el cuadro de instrumentos puede no mostrar la velocidad ni los testigos de freno y de presión de neumáticos (software) | Actualización de software; en los no híbridos enchufables, por vía remota (OTA). Recall por fases: cartas el 5-dic-2025 y más cartas previstas para mayo de 2026 | [17][19] |
| 26V282000 | ≈ 2026-05-04 | 4Runner 2026 (Gulf States Toyota) | Etiqueta de capacidad de carga errónea (incumple la norma FMVSS 110) | Etiqueta nueva enviada por correo; cartas el 18-jun-2026; ≈ 94 unidades | [18][19] |
| 26V571000 | ≈ sep-2026 | Tacoma Hybrid 2024, Tundra/Tundra Hybrid 2025, RAV4 Hybrid 2026, **4Runner i-FORCE MAX** y 4Runner (TEMA/Toyota; código Toyota 26TA18) | Etiqueta de modificación de capacidad de carga con valores de peso añadido inexactos | El concesionario sustituye la etiqueta; cartas el 27-oct-2026; 135 unidades | [18][19] |

- Los agregadores no coinciden en el total. U.S. News dice que la 2026 no tiene recalls (página desactualizada); Consumer Reports habla de 2 recalls en la 2026 [20]; TheWeeklyDriver cuenta 3 para 2025–2026 [19]. **Ninguna campaña se verificó contra NHTSA** [21] [NO VERIFICADO]. Para el año modelo 2027 no encontré campañas [NO VERIFICADO].
- **Cómo atenderlos desde Venezuela:**
  - Los recalls de etiqueta (26V282000, 26V571000) se resuelven con una etiqueta que puede enviarse por correo a una dirección en EE. UU. (la de la LLC) y luego remitirse.
  - El 25V595000 se resuelve por software. Que la actualización OTA funcione en Venezuela depende de la conectividad del módulo telemático de Toyota fuera de EE. UU. [NO VERIFICADO; hipótesis: probablemente no funcione]. **Recomendación:** antes de exportar, pedir al concesionario de EE. UU. que haga un chequeo de campañas abiertas por VIN y aplique todas las actualizaciones pendientes.
  - **Recalls mecánicos futuros** (piezas que debe instalar un concesionario): no hay vía documentada para hacerlos en Venezuela [NO VERIFICADO si TDV ejecuta campañas de NHTSA en vehículos no distribuidos por ella].
  - **Llevar el vehículo a Miami para un recall no es realista.** Exige sacarlo de Venezuela, transportarlo por mar en ambos sentidos, hacer trámites de reingreso en EE. UU. y de nuevo en Venezuela (con riesgo de una segunda nacionalización si no se usa un régimen de exportación temporal) y esperar semanas. El costo queda [NO VERIFICADO; ver el agente de logística]. Solo tendría sentido ante un recall grave sin alternativa local.
  - Mitigación: registrar el VIN en el portal de propietarios de Toyota con la dirección de la LLC y revisar el VIN en nhtsa.gov/recalls cada trimestre.

### 3. Repuestos no híbridos y equipamiento específico de la Trailhunter
- **Suspensión:** amortiguadores **Old Man Emu (OME, de ARB) monotubo forjados de 2,5"**, con **depósitos remotos externos** (traseros, tipo *piggyback*) [11][12]. Junto con los neumáticos de 33", elevan la camioneta **+2" adelante y +1,5" atrás** [11][12]. ARB USA vende kits BP-51 para la 4Runner 2025 en el mercado de accesorios [16], lo que indica que hay alternativa OME, aunque en EE. UU. y no en Venezuela [NO VERIFICADO distribuidor de ARB/OME en Venezuela].
  - Un medio indica que la Trailhunter 2027 mantiene sus amortiguadores actuales y no recibe los FOX rediseñados [extracto de búsqueda sobre fuentes de concesionarios; NO VERIFICADO en fuente primaria]. La TRD Pro usa FOX QS3 de bypass interno [11].
- **Neumáticos:** Toyota indica **neumáticos Toyo de 33" (Open Country A/T) en rines de 18" color bronce** [11][12]. La medida **265/70R18 (Toyo Open Country A/T III)** solo la confirma un usuario de foro [14] [FORO/REDES]. Un minorista da 245/70R17 para "la 4Runner 2026", pero parece corresponder a otras versiones [15]. La medida exacta queda [NO VERIFICADO en fuente primaria]; se confirma en la etiqueta de la puerta o en el *window sticker*. No investigué la disponibilidad de 265/70R18 en Venezuela [NO VERIFICADO].
- **Frenos, filtros, compatibilidad con Tacoma 4G y Land Cruiser 250:** el grado Trailhunter es común a Tacoma y 4Runner (Toyota los presenta juntos) [13]. No pude verificar números de pieza compartidos ni la oferta local de Tacoma 4G o Land Cruiser 250 en la red TDV [NO VERIFICADO]. Un importador no oficial lista la Land Cruiser Prado 2026 en Venezuela desde USD 80.000 [64] [CLASIFICADOS]. Si fuera la serie 250, podría haber algo de oferta local de piezas comunes, pero no está comprobado. Lo resolvería un catálogo EPC de Toyota (números de pieza) y una consulta a los proveedores locales.
- **Alternativa práctica:** traer con la camioneta un kit de consumibles para 2–3 años (filtros de aceite, aire y habitáculo, pastillas, escobillas) y abastecerse vía courier desde Miami. Costo [NO VERIFICADO].

### 4. Seguridad: robo y modalidades
- **Estadísticas oficiales:** no encontré estadísticas 2024–2026 del CICPC ni del Ministerio de Interior sobre robo de vehículos por marca o modelo, ni para Carabobo [NO VERIFICADO]. Lo último disponible del OVV:
  - Carabobo, tasa de muertes violentas de **25,3 por 100.000** frente a 26,8 nacional (informe anual 2023) [39].
  - Primer semestre de 2022: Carabobo era el 5.º estado en tasa total de nueve delitos (**111**), y el robo de vehículos se denunciaba con más frecuencia que el hurto [40].
  - El informe anual 2025 del OVV no apareció en las búsquedas [NO VERIFICADO].
- **Casos recientes en Valencia [PRENSA]:**
  - Jul-2026: dos detenidos por robar el vehículo a un conductor de aplicación y **exigir USD 2.500 para devolverlo** (robo con rescate o extorsión) [41][42].
  - Jul-2026: el CICPC recupera dos vehículos en la parroquia San José [44].
  - ≈ Oct-2025: detenidos por un hurto frustrado de vehículos en la zona norte de Valencia [43].
  - Ninguno de estos casos se refiere a camionetas Toyota.
- **Demanda criminal regional de camionetas Toyota [PRENSA]:**
  - En Colombia se desarticuló "Los Toyoteros", una red que robaba camionetas de alta gama y las pasaba por trochas a Venezuela [45].
  - Un medio chileno sostiene que camionetas robadas en Chile se "legalizan" en Venezuela al amparo de una resolución que permite regularizar vehículos de hasta 5 años, y que un Toyota usado puede costar hasta 100 % más que uno nuevo [46] (no verificado).
  - Ambas notas indican que el mercado venezolano tiene una demanda alta de estas camionetas, lo que las hace atractivas para robarlas.
- **Contexto de seguridad 2026:** Delcy Rodríguez es presidenta encargada desde el 5-ene-2026, tras la captura de Maduro por EE. UU. Washington reconoce a su gobierno, no hay fecha de elecciones y sigue habiendo presos políticos [48]. El 12-nov-2026 Venezuela y Colombia acordaron coordinarse en seguridad fronteriza tras dos secuestros de alto perfil [47]. No encontré un balance de la delincuencia común en 2026 [NO VERIFICADO].
- **Robo de autopartes y "secuestro express":** no pude investigarlos [NO VERIFICADO]. Por diseño, la Trailhunter expone piezas valiosas y fáciles de desmontar (rines de 18" con neumáticos de 33", faros y luces auxiliares, toma de aire elevada). Es una hipótesis del agente, no un dato.
- **Blindaje:**
  - Datos antiguos (oct-2016): blindar un SUV contra la delincuencia común (nivel 3A) costaba **USD 18.500–23.000**; el mantenimiento anual rondaba los USD 3.000 y un neumático blindado USD 1.000–1.500. La **4Runner era entonces el modelo más demandado para blindar** [49] [PRENSA, desactualizado].
  - Hoy hace falta un **permiso de SUCAMEN** para blindajes de nivel 3 o superior (guía de ago-2025) [50].
  - En MercadoLibre aparece una 4Runner blindada nivel 3 en USD 49.900, sin fecha [51] [CLASIFICADOS].
  - **Advertencia técnica (hipótesis):** el blindaje añade cientos de kilos. Afectaría la suspensión OME, los frenos y la carga útil, y es una modificación que cualquier garantía residual excluiría. No se encontró un costo de blindaje para 2025–2026 [NO VERIFICADO].
- **GPS:** no pude averiguar el costo ni si las aseguradoras lo exigen [NO VERIFICADO]. Lo resolvería una cotización de una aseguradora y de un proveedor de rastreo satelital en Valencia.

### 5. Seguros
- **RCV (obligatorio):**
  - La tarifa vigente sale de la **Gaceta Oficial Extraordinaria N.º 6.835 del 3-sep-2024**: entre **33 y 114 EUR/año** para vehículos particulares. Las primas se anclan a la tasa de referencia más alta del BCV en lugar de la antigua unidad tributaria [27][28][29].
  - En dólares: la versión básica cuesta ≈ **USD 33–40/año**; el plan básico de Mapfre, **USD 38,63**; una cotización de Pirámide de 2025, **USD 43/año** [28][29].
  - A la tasa BCV del 16-nov-2026 (914,0218 Bs/USD) [36], USD 33–43 equivalen a ≈ **Bs 30.163–39.303**.
  - Hay cooperativas que venden "RCV" por USD 5–10, que no cumplen con SUDEASEG [29] (no verificado). La página de 2026 [29] sigue citando la Gaceta de 2024: no encontré una tarifa más reciente.
- **Casco (cobertura amplia):**
  - Referencia de mercado: **3–7 % del valor del vehículo por año** (blog de seguros localizado por el buscador; no puedo atribuir con certeza si es [31] o [32]) [NO VERIFICADO contra una cotización].
  - Ejemplo real publicado: una póliza amplia con prima de **USD 502,85/año**, sin indicar el valor del vehículo [28].
  - El Impulso (25-sep-2026): el parque automotor envejecido encarece las primas y muchos asegurados se quedan solo con RCV o con pérdida total [33].
  - Mercantil Seguros ofrece cobertura amplia con pérdida parcial sin límite, robo, hurto y choque [34].
  - Requisitos de Seguros Miranda: planilla, certificado de registro o carnet de circulación, cédula y RIF [35]. **Implicación:** sin registro venezolano (INTT) no hay casco, así que el tramo de transporte y puerto requiere un seguro de carga aparte.
  - No verifiqué si las aseguradoras exigen GPS o inspección, si aseguran vehículos importados por particulares, ni las primas por aseguradora (Mercantil, Caracas, Mapfre, La Previsora, Pirámide, Universitas, Banesco) [NO VERIFICADO]. Tampoco encontré un listado oficial vigente de aseguradoras autorizadas por SUDEASEG; hay que consultarlo en sudeaseg.gob.ve.
- **Estimación del casco (del agente):**
  - Suma asegurada de USD 75.000 (precio en EE. UU.): mín. USD 2.250, probable USD 3.000–3.750 (4–5 %), máx. USD 5.250 por año.
  - Si la aseguradora asegura al **valor de mercado local** (≈ USD 128.890, la venta cerrada de sep-2026 [55]): USD 3.867–9.022 por año.
  - Supuestos: tasa del 3–7 %, sin deducible especial, cliente sin siniestros. Una suma tan alta puede requerir reaseguro facultativo [NO VERIFICADO].
- **Riesgo de indemnización:** las pólizas se expresan en divisa pero suelen pagarse en bolívares a la tasa BCV [30]. Con una brecha de ≈ 20 % frente al paralelo [37], una indemnización por pérdida total cobrada en bolívares al tipo oficial podría quedarse corta para reponer la camioneta en dólares (análisis del agente).

### 6. Reventa
- **Precios publicados (asking, no de cierre), consultados vía extractos el 2026-11-18 [CLASIFICADOS]:**
  - 4Runner 2024: SR5 USD 75.000–82.900; TRD Pro USD 124.900 [52][53].
  - 4Runner 2025: SR5 USD 92.000; TRD Pro i-FORCE MAX USD 139.900; TRD Sport USD 149.000 [53][54].
  - **Trailhunter 2025 0 km: USD 145.000, 148.700 y 169.900** [54].
  - Autocosmos: SR5 2025 USD 140.000 [57].
  - Una guía de 2026 da un rango de USD 98.000–170.000 para la 2025, con TRD Pro y Trailhunter por encima de USD 160.000 [56] [PRENSA/blog].
- **Venta cerrada:** Conduce registra una **Trailhunter 2025 vendida en USD 128.890 en sep-2026, con 322 km** [55] [CLASIFICADOS; la plataforma dice publicar precios de cierre].
- **Lectura:**
  - Hoy el mercado paga ≈ 1,9 veces el precio de lista en EE. UU. de la Trailhunter 2027 (USD 68.590 + USD 1.595 de destino) [9][10]. La 4Runner tiene demanda y liquidez altas.
  - Riesgos: (a) si en la transición de 2026 se abre la importación y aumenta la oferta, esa prima se comprimiría; (b) un comprador informado descontará la falta de garantía, de respaldo TDV y de servicio híbrido, cuyo efecto no pude cuantificar [NO VERIFICADO].
- **Estimación de reventa (del agente) a 1–2 años:**
  - Mín. ≈ USD 80.000 (la prima desaparece y el precio converge al costo de importación).
  - Probable USD 100.000–115.000 (la prima se mantiene pero con descuento por uso, por ser híbrida sin respaldo y por la liquidez).
  - Máx. ≈ USD 130.000 (el mercado se mantiene como en sep-2026).
  - Supuestos: kilometraje bajo, documentación de nacionalización completa, sin siniestros.

### 7. Riesgos aduaneros (enfoque de riesgo; los costos y el trámite los cubren otros agentes)
- No encontré casos documentados en 2025–2026 de robo de piezas o daños a vehículos en **Puerto Cabello o La Guaira** [NO VERIFICADO]. El SENIAT informó de un segundo circuito de rayos X en la Aduana Principal de Puerto Cabello [62] (fecha sin confirmar, ≈ 2024).
- **Cambio de normativa durante el tránsito:** riesgo real por la transición política de 2026 (gobierno encargado, negociaciones sin fecha electoral, reformas) [48]. No identifiqué una norma concreta en trámite [NO VERIFICADO].
- **Discrecionalidad y solicitudes irregulares:** no encontré casos documentados recientes [NO VERIFICADO]. Advertencia del agente: al ser el comprador o exportador una **LLC estadounidense**, cualquier pago irregular a funcionarios podría caer bajo la ley anticorrupción de EE. UU. (FCPA) además de la venezolana [NO VERIFICADO en esta sesión; consultar abogado].
- **Tránsito sin seguro:** el casco local exige el registro venezolano [35], así que hace falta un seguro de carga marítima "todo riesgo" hasta la nacionalización [costo NO VERIFICADO; ver agente de logística].

### 8. Otros
- **Riesgo cambiario:**
  - Tasa BCV: **914,0218 Bs/USD** el 16-nov-2026 [36]. Subió de 889,58 a 914,02 entre el 2 y el 16 de noviembre (+2,7 % en dos semanas) [36][37].
  - Paralelo: ≈ 1.082,87 Bs/USD frente a 904,45 BCV el 12-nov-2026, una **brecha de ≈ 19,7 %** [37].
  - Inflación interanual estimada por Hanke: **237,7 %** (2-nov-2026; no es una cifra oficial) [38].
  - Los pagos en bolívares indexados al BCV no encarecen el costo en dólares si se convierte justo a tiempo. Sí afectan las obligaciones fijadas en bolívares y las indemnizaciones pagadas en bolívares (ver §5).
- **Confiscación o llamar la atención:** no encontré fuentes 2025–2026 [NO VERIFICADO]. Mitigación de sentido común: llevar siempre la documentación de nacionalización y propiedad, y tener claro quién es el titular (persona natural o la C.A.).
- **Combustible:** solo se menciona aquí, porque lo estudia otro agente. Un comercializador venezolano advierte en redes que la garantía de su Corolla Cross "no cubre daños por combustible nacional" y menciona reprogramaciones o la eliminación de la EGR [63] [FORO/REDES]. Es una señal de que la calidad del combustible preocupa en el mercado local.
- **Impuesto municipal sobre vehículos:**
  - Valencia tiene una ordenanza de impuesto sobre vehículos [58] y aplicó un descuento del 50 % hasta el 31-jul-2025 (decretos DA/0021/2025 y DA/0022/2025) [59].
  - Los topes nacionales los fija la LOCAPTEM [61] y la tabla de valores máximos de la Gaceta Oficial 6.783 Extraordinario [60].
  - **No encontré la ordenanza de vehículos de Naguanagua ni un recargo específico "de lujo"** [NO VERIFICADO]. Se resolvería con la Gaceta Municipal de Naguanagua o con su servicio de tributación.

## Cifras clave (tabla: concepto | valor | rango mín/prob/máx si es estimación | fuente [n] | fecha de la fuente)

| Concepto | Valor | Rango mín/prob/máx (si es estimación) | Fuente [n] | Fecha de la fuente |
|---|---|---|---|---|
| Garantía básica Toyota USA | 36 meses / 36.000 mi | — (hecho) | [7][8] | listados 2025–2026 |
| Garantía de tren motriz | 60 meses / 60.000 mi | — | [7] | 2025 |
| Garantía de corrosión (perforación) | 60 meses / millas ilimitadas | — | [7] | 2025 |
| Garantía del sistema híbrido de alto voltaje | 96 meses / 100.000 mi | — | [7][8] | 2025–2026 |
| Garantía de batería híbrida | 120 meses / 150.000 mi | — | [7][8] | 2025–2026 |
| ToyotaCare | 2 años / 25.000 mi | — | [7] | 2025 |
| Ámbito geográfico de la garantía | EE. UU., territorios de EE. UU., Canadá (servicio también en México) | — | [1][2][5] | MY2021 / MY2026 / s.f. |
| MSRP de la Trailhunter 2027 | USD 68.590 (+ USD 1.595 de destino) | — | [9][10] | 2026 |
| Recalls de la 4Runner 6G encontrados | 3 (25V595000, 26V282000, 26V571000) | — | [17][18][19] | sep-2025 a oct-2026 |
| Unidades afectadas por 26V282000 / 26V571000 | ≈ 94 / 135 | — | [18][19] | may-2026 / sep-2026 |
| Amortiguadores de serie | OME monotubo forjado de 2,5" con depósito remoto externo | — | [11][12] | 2024–2025 |
| Neumáticos de serie | Toyo Open Country A/T de 33", rin de 18" | Medida 265/70R18 según un foro, no en fuente primaria | [11][12][14] | 2024–2025 / s.f. |
| Elevación frente a otras versiones | +2" adelante / +1,5" atrás | — | [11][12] | 2024–2025 |
| Tarifa RCV, vehículos particulares | 33–114 EUR/año | — | [27][28][29] | GO 6.835, 3-sep-2024 |
| RCV básico en USD | USD 33–43/año (Mapfre 38,63; Pirámide 43) | — | [28][29] | 2025–2026 |
| RCV en Bs (a 914,0218 Bs/USD) | ≈ Bs 30.163–39.303 | cálculo del agente | [36] | 16-nov-2026 |
| Casco amplio como % del valor | 3–7 %/año | referencia de un blog | [31]/[32] | 2026 |
| Casco amplio, ejemplo publicado | USD 502,85/año (valor del vehículo no indicado) | — | [28] | 23-may-2025 |
| Casco amplio sobre USD 75.000 (estimación) | — | 2.250 / 3.000–3.750 / 5.250 USD/año | cálculo sobre [31]/[32] | — |
| Casco a valor de mercado local USD 128.890 (estimación) | — | 3.867 / ≈ 5.200–6.400 / 9.022 USD/año | cálculo sobre [31]/[32][55] | — |
| Tasa BCV | 914,0218 Bs/USD | — | [36] | 16-nov-2026 |
| Brecha con el paralelo | ≈ 19,7 % (1.082,87 frente a 904,45) | cálculo del agente | [37] | 12-nov-2026 |
| Inflación interanual (Hanke, no oficial) | 237,7 % | — | [38] | 2-nov-2026 |
| Trailhunter 2025 0 km, precio publicado en Venezuela | USD 145.000 / 148.700 / 169.900 | — | [54] | s.f. (consultado 2026-11-18) |
| Trailhunter 2025, venta cerrada en Venezuela | USD 128.890 (322 km) | — | [55] | sep-2026 |
| 4Runner 2024 SR5 / TRD Pro, precio publicado | USD 75.000–82.900 / 124.900 | — | [52][53] | s.f. |
| Reventa a 1–2 años (estimación) | — | 80.000 / 100.000–115.000 / 130.000 USD | análisis del agente sobre [54][55][56] | — |
| Blindaje de SUV nivel 3A | USD 18.500–23.000 | dato de 2016, desactualizado | [49] | 6-oct-2016 |
| Mantenimiento anual del blindaje / neumático blindado | ≈ USD 3.000 / USD 1.000–1.500 | 2016 | [49] | 6-oct-2016 |
| 4Runner blindada nivel 3 (usada, publicada) | USD 49.900 | — | [51] | s.f. |
| Muertes violentas, Carabobo frente al país | 25,3 frente a 26,8 por 100.000 hab. | — | [39] | 2023 |
| Tasa total de 9 delitos, Carabobo | 111 (5.º estado) | — | [40] | 1.er semestre de 2022 |
| Rescate exigido por vehículo robado (caso Valencia) | USD 2.500 | — | [41] | 17-jul-2026 |
| Ventas por canales no oficiales ("mercado gris") | ≈ 20 % | cifra no verificada por la fuente | [26] | 2026 |
| Descuento del impuesto municipal de vehículos en Valencia | 50 % (hasta el 31-jul-2025) | — | [59] | 2025 |

## Riesgos detectados (incluye la matriz)

**Matriz de riesgos**

| # | Riesgo | Probabilidad | Impacto | Mitigación | Costo de la mitigación |
|---|---|---|---|---|---|
| 1 | Pérdida total de la garantía de Toyota USA (básica, tren motriz, híbrida 8 años, batería 10 años) al operar en Venezuela [1][2][5][23] | Alta (prácticamente cierta) | Alto (falla de batería o del sistema de alto voltaje sin cobertura) | Inspección y chequeo de campañas en un concesionario de EE. UU. antes de exportar; fondo de autoaseguro; documentar el mantenimiento | Fondo [NO VERIFICADO: depende del costo de la batería, que se resuelve con una cotización de concesionario] |
| 2 | Recall futuro con reparación mecánica imposible de atender en Venezuela [17]-[21] | Media (en 5–10 años de vida) | Medio–Alto (riesgo de seguridad) | Registrar el VIN con la dirección de la LLC; revisar nhtsa.gov cada trimestre; aplicar todas las campañas antes de exportar | Bajo (seguimiento); trasladar el vehículo a EE. UU. es inviable o alto [NO VERIFICADO] |
| 3 | Concesionario de EE. UU. que no vende para exportación o penalización (*chargeback*/reclamo) si el comprador firmó un "no export" [22] | Media | Medio | Comprar con transparencia vía la LLC a un concesionario que acepte exportación; no firmar declaraciones falsas; asesoría legal | [NO VERIFICADO] |
| 4 | Falta de repuestos específicos (OME, neumático de 33"/18", piezas TNGA-F) en Venezuela [11][12][16] | Alta (OME e híbridos) / Media (consumibles) | Medio (vehículo inmovilizado durante semanas) | Kit de consumibles para 2–3 años junto con el vehículo; proveedor en Miami + courier; neumático de repuesto de la misma medida | [NO VERIFICADO] |
| 5 | Sin servicio ni diagnóstico híbrido en la red TDV; sin respaldo de TDV [23][24][25] | Media–Alta | Alto | Identificar antes de comprar un taller (importadores que venden 4Runner 6G) con escáner o software Toyota; preguntar a TDV si da servicio pagado | [NO VERIFICADO] |
| 6 | Robo del vehículo, con violencia o con rescate o extorsión [41][45][46] | Media (sin estadística 2024–2026) | Alto (pérdida de ≈ USD 80.000 o más) | Casco amplio con robo; GPS con inmovilizador; garaje; rutinas de bajo perfil | Casco estimado en USD 2.250–5.250/año (hasta ≈ 9.000); GPS [NO VERIFICADO] |
| 7 | Robo de autopartes (rines y neumáticos de 33", luces, toma de aire) | Media [NO VERIFICADO] | Medio | Tuercas de seguridad, alarma, estacionamiento vigilado | [NO VERIFICADO] |
| 8 | "Secuestro express" o riesgo personal por un vehículo muy visible | Baja–Media [NO VERIFICADO] | Alto | Perfil bajo; blindaje opcional (permiso de SUCAMEN) [50] | Blindaje USD 18.500–23.000 (dato de 2016 [49]) + ≈ USD 3.000/año; afecta la suspensión |
| 9 | Seguro de casco insuficiente: suma asegurada baja, aseguradora sin capacidad, indemnización en Bs a tasa BCV [30][37] | Media | Alto | Suma asegurada en divisas a valor de reposición; verificar la aseguradora en SUDEASEG; leer la cláusula de pago | Diferencia de prima (incluida en el #6) |
| 10 | Vehículo sin casco durante el tránsito y en puerto (el casco exige registro venezolano) [35] | Alta (es un vacío de cobertura) | Alto | Seguro de carga marítima "todo riesgo" puerta a puerta hasta la nacionalización | [NO VERIFICADO; ver agente de logística] |
| 11 | Daños o robo de piezas en Puerto Cabello o La Guaira | Media [NO VERIFICADO: sin casos documentados encontrados] | Medio | Contenedor exclusivo y precintado en lugar de RoRo; retirar accesorios removibles; fotos y acta de inspección | [NO VERIFICADO] |
| 12 | Retención aduanera, discrecionalidad, solicitudes irregulares, demoras y almacenaje | Media | Medio–Alto | Agente aduanal reconocido; valoración y documentos impecables; no pagar irregularidades (riesgo bajo la FCPA para la LLC) | Honorarios del agente [ver otro agente] |
| 13 | Cambio de normativa (aranceles, régimen de importación) durante el tránsito, en plena transición política de 2026 [48] | Media | Alto | Embarcar solo con el marco publicado en Gaceta; vigilar la Gaceta y el SENIAT hasta el arribo | Bajo |
| 14 | Riesgo cambiario: pagos e indemnizaciones en Bs; brecha de ≈ 20 %; inflación de 237,7 % [36][37][38] | Alta | Bajo–Medio | Mantener fondos en USD y convertir justo a tiempo; pólizas en divisas | Bajo |
| 15 | Reventa: descuento por ser híbrida importada sin respaldo TDV; caída de la prima si se abre la importación [54][55][56] | Media | Medio (reventa estimada en USD 80.000–130.000) | Documentación completa (factura, título, nacionalización, historial); mantenimiento documentado | Bajo |
| 16 | Confiscación o atención indeseada de autoridades o delincuentes | Baja–Media [NO VERIFICADO] | Alto | Documentos de origen de fondos y de nacionalización siempre a mano; titularidad clara | Bajo |
| 17 | Combustible (calidad o disponibilidad) [63] | Media (ver agente de combustible) | Alto (motor turbo e híbrido) | Ver el agente de combustible | Ver el agente de combustible |
| 18 | Impuesto municipal anual sobre vehículos (Naguanagua) [58]-[61] | Alta (obligatorio) | Bajo [monto NO VERIFICADO] | Consultar la ordenanza local; pagar a tiempo | Monto [NO VERIFICADO] |
| 19 | Servicios conectados y actualizaciones OTA de Toyota (remedio del 25V595000) inoperantes en Venezuela | Alta (hipótesis) [NO VERIFICADO] | Bajo–Medio | Aplicar todas las actualizaciones antes de exportar | Bajo |

**Lectura de la matriz:** ningún riesgo de este frente hace ilegal o imposible la operación. Los riesgos con impacto alto y probabilidad media o alta son el #1 (garantía), el #5 (servicio híbrido), el #6 (robo), el #10 (vacío de seguro en tránsito) y el #13 (cambio normativo). Esos son los que debería pesar el orquestador.

## Preguntas abiertas
1. ¿Qué dice textualmente el Warranty & Maintenance Guide de la 4Runner 2026/2027 (versión HV) sobre el ámbito geográfico y la exportación? Requiere permitir `assets.sia.toyota.com` y `assets.sipb.toyota.com` y releer [4].
2. ¿Qué recalls abiertos tiene la 4Runner 2025/2026/2027 según NHTSA (no según agregadores)? Requiere permitir `api.nhtsa.gov` o revisar nhtsa.gov/recalls con el VIN concreto.
3. ¿TDV o sus concesionarios en el área de Valencia dan servicio pagado, diagnóstico híbrido y repuestos a una 4Runner 6G no importada por TDV? ¿Ejecutan campañas de NHTSA? Debe preguntarlo el cliente.
4. Primas reales de casco amplio para una suma asegurada de USD 75.000–130.000 en Mercantil, Caracas, Mapfre, La Previsora, Pirámide, Universitas y Banesco: exigencia de GPS e inspección, aceptación de vehículos importados por particulares, moneda de la indemnización. Se resuelve con cotizaciones formales.
5. Costo y proveedores de GPS con inmovilizador en Valencia; costo actual de blindaje nivel 3 para un SUV mediano (2025–2026).
6. Estadísticas 2024–2026 de robo y hurto de vehículos por marca y modelo en Carabobo (CICPC, Ministerio de Interior, informe anual 2025 del OVV, aseguradoras).
7. ¿Hay garantías extendidas de terceros con cobertura en Venezuela o internacional para un híbrido Toyota?
8. Disponibilidad y precio en Venezuela del neumático de serie de la Trailhunter (medida a confirmar: 265/70R18) y de los amortiguadores OME; piezas compartidas con Tacoma 4G y Land Cruiser 250.
9. ¿Existe en Naguanagua un impuesto sobre vehículos con tramo o recargo para vehículos de alto valor? ¿Cuál es la alícuota vigente en 2026?
10. ¿Hay casos documentados en 2025–2026 de daños, robo de piezas o solicitudes irregulares en Puerto Cabello y La Guaira? (prensa regional de Carabobo y Vargas, Ministerio Público).
11. ¿Qué políticas de exportación aplican los concesionarios Toyota de EE. UU. en 2026 (cláusula de no exportación, penalizaciones) y cómo afectan a una compra a través de la LLC?

## Fuentes (lista numerada: título — URL — fecha de la fuente — consultada 2026-11-18 — tipo: primaria/secundaria/prensa/foro)
1. Toyota — 2021 Tacoma Warranty & Maintenance Guide — https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-21Tacoma/pdf/T-MMS-21Tacoma.pdf — año modelo 2021 — consultada 2026-11-18 (extracto de buscador) — primaria
2. Toyota — 2026 Grand Highlander Warranty & Maintenance Guide — https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-26GrandHighlander/pdf/T-MMS-26GrandHighlander.pdf — año modelo 2026 — consultada 2026-11-18 (extracto de buscador) — primaria
3. Toyota — 2026 Tacoma Warranty & Maintenance Guide — https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-26Tacoma/pdf/T-MMS-26Tacoma.pdf — año modelo 2026 — consultada 2026-11-18 (extracto de buscador) — primaria
4. Toyota — 2026 4Runner HV y 4Runner Warranty & Maintenance Guide — https://assets.sipb.toyota.com/publications/en/omms-s/T-MMS-264RunnerHV/pdf/T-MMS-264RunnerHV.pdf y https://assets.sia.toyota.com/publications/en/omms-s/T-MMS-264Runner/pdf/T-MMS-264Runner.pdf — año modelo 2026 — consultada 2026-11-18 (NO SE PUDO ABRIR: host bloqueado) — primaria
5. Toyota Support — "Which countries is my New Vehicle Limited Warranty valid in?" — https://support.toyota.com/s/article/Which-countries-is-my-7766?language=en_US — sin fecha — consultada 2026-11-18 (extracto de buscador) — primaria
6. Toyota Canada — 2026 Owner's Supplement — https://www.toyota.ca/content/dam/toyota/pdf/2026_owners_supplement_en.pdf — año modelo 2026 — consultada 2026-11-18 — primaria (Toyota Canadá, análoga)
7. North Park Toyota (concesionario) — New 2025 Toyota 4Runner i-FORCE MAX TRD Off Road Premium 4x4 (datos de garantía) — https://www.northparktoyota.com/new/Toyota/2025-Toyota-4Runner-i-FORCE-MAX-032a1665ac181130ee82a34575977abd.htm — 2025 — consultada 2026-11-18 — secundaria
8. Listados 2026 de concesionarios: North Park Toyota, 2026 4Runner i-FORCE MAX Limited — https://www.northparktoyota.com/new/Toyota/2026-Toyota-4Runner-i-FORCE-MAX-98e14f45ac180cb6fbf5ec49c2acfb0e.htm ; Tustin Toyota, 2026 4Runner i-FORCE MAX specs — https://www.tustintoyota.com/research/2026-toyota-4runner-hybrid-specs/ ; Reliable Toyota, 2026 4Runner i-FORCE MAX Trailhunter — https://www.reliabletoyotamo.com/new/Toyota/2026-Toyota-4Runner-i-FORCE-MAX-56c8325fac1858fe65a8f852eff6086d.htm — 2026 — consultada 2026-11-18 — secundaria
9. Toyota — 2027 Toyota 4Runner — https://www.toyota.com/vehicles/4runner/2027 — 2026 (año modelo 2027) — consultada 2026-11-18 (extracto de buscador) — primaria
10. U.S. News — 2027 Toyota 4Runner Review, Pricing, & Pictures — https://cars.usnews.com/cars-trucks/toyota/4runner — 2026 — consultada 2026-11-18 — secundaria
11. Toyota Pressroom — The 2026 Toyota 4Runner: Engineered for Exploration — https://pressroom.toyota.com/the-2026-toyota-4runner-engineered-for-exploration/ — 2025 (fecha exacta sin confirmar) — consultada 2026-11-18 — primaria
12. Toyota Pressroom — The All-New 2025 Toyota 4Runner: The Icon That Inspires Exploration — https://pressroom.toyota.com/the-all-new-2025-toyota-4runner-the-icon-that-inspires-exploration/ (réplica: https://www.nasdaq.com/press-release/all-new-2025-toyota-4runner-icon-inspires-exploration-2024-12-10) — 2024-12-10 — consultada 2026-11-18 — primaria
13. Toyota Pressroom — Toyota's Trailhunter Grade: Features That Elevate the Tacoma and 4Runner Overlanding Experience — https://pressroom.toyota.com/?p=103756 — fecha sin confirmar — consultada 2026-11-18 — primaria
14. 4Runner6G Forum — Real practical differences between TRD OR and Pro/TH suspensions re: fitting larger tires — https://www.4runner6g.com/forum/threads/real-practical-differences-between-trd-or-and-pro-th-suspensions-re-fitting-larger-tires.6008 — sin fecha — consultada 2026-11-18 — foro
15. Tires-Easy — Best tires for the 2026 Toyota 4Runner — https://www.tires-easy.com/blog/best-tires-for-the-2026-toyota-4runner/ — 2026-01-08 — consultada 2026-11-18 — secundaria (comercial)
16. ARB USA Store — BP-51 kit for Toyota 4Runner 2025 rear (2230K) — https://store.arbusa.com/bp-51-kit-for-toyota-4runner-2025-rear-0-in-0-lb-2230k/ — sin fecha — consultada 2026-11-18 — secundaria (comercial)
17. Cars.com — 2025 Toyota 4Runner Recalls — https://www.cars.com/research/toyota-4runner-2025/recalls/ — 2025–2026 — consultada 2026-11-18 — secundaria
18. ProblemsByVin — 2026 Toyota 4Runner recalls — https://problemsbyvin.com/2026-toyota-4runner/recalls/ — 2026 — consultada 2026-11-18 — secundaria
19. TheWeeklyDriver — 2025-2026 Toyota 4Runner Reliability: 64 Complaints, 3 Recalls — https://theweeklydriver.com/reliability/toyota/4runner/2025-2026/ — 2026 — consultada 2026-11-18 — secundaria
20. Consumer Reports — 2026 Toyota 4Runner Reliability — https://www.consumerreports.org/cars/toyota/4runner/2026/reliability/ — 2026 — consultada 2026-11-18 — secundaria
21. NHTSA — Recalls API (recallsByVehicle, Toyota 4Runner) — https://api.nhtsa.gov/recalls/recallsByVehicle?make=TOYOTA&model=4RUNNER&modelYear=2025 — n/a — consultada 2026-11-18 (NO SE PUDO ABRIR: host bloqueado) — primaria
22. Virginia Automobile Dealers Association — Dealer Export Policy (plantilla) — https://vada.com/wp-content/uploads/2018/04/Dealer_Export_Policy_VA.pdf — 2018 — consultada 2026-11-18 — secundaria
23. El Diario — Toyota Venezuela estima vender más de 6.000 vehículos en 2024: ¿cómo y dónde se pueden adquirir? — https://eldiario.com/2024/03/19/toyota-venezuela-como-y-donde-se-pueden-adquirir-los-vehiculos/ — 2024-03-19 — consultada 2026-11-18 — prensa
24. Banca y Negocios — Toyota Venezuela está incorporando la venta de vehículos usados en sus concesionarios — https://www.bancaynegocios.com/toyota-venezuela-esta-incorporando-la-venta-de-vehiculos-usados-en-sus-concesionarios/ — ≈ 2022 (sin confirmar) — consultada 2026-11-18 — prensa
25. TOYO VE (importador no oficial) — Toyota 4Runner 2026 en Venezuela: precio, nueva generación, versiones y fotos — https://toyove.com/blog/toyota-4runner-2026-venezuela-precio-ficha-fotos/ — 2026 — consultada 2026-11-18 — clasificados/comercial
26. Venezuela Productiva Automotriz — El «mercado gris» de carros en Venezuela: qué es y sus riesgos — https://venezuelaproductivaautomotriz.com/42688-mercado-gris-carros-venezuela/ — 2026 — consultada 2026-11-18 — prensa/blog
27. Efecto Cocuyo — Nuevas normas y tarifas de la póliza RCV en Venezuela — https://efectococuyo.com/la-humanidad/nuevas-normas-y-tarifas-de-la-poliza-rcv-en-venezuela-cambios-costos-y-recomendaciones/ — 2024 (sin confirmar) — consultada 2026-11-18 — prensa
28. El Diario — ¿Cuánto cuesta la póliza de Responsabilidad Civil Vehicular en Venezuela? — https://eldiario.com/2025/05/23/cuanto-cuesta-poliza-responsabilidad-civil-vehicular-venezuela/ — 2025-05-23 — consultada 2026-11-18 — prensa
29. deseguros.com.ve — RCV 2026: tarifa oficial y precio en bolívares — https://deseguros.com.ve/rcv — 2026 — consultada 2026-11-18 — secundaria
30. Venezuela Productiva Automotriz — Póliza de seguro de vehículo de cobertura amplia en Venezuela — https://venezuelaproductivaautomotriz.com/43565-poliza-seguro-vehiculo-cobertura-amplia-venezuela/ — 2026 — consultada 2026-11-18 — prensa/blog
31. Venezuela Productiva Automotriz — Seguro de carro en Venezuela 2026: tipos y coberturas — https://venezuelaproductivaautomotriz.com/42698-seguro-carro-venezuela-tipos/ — 2026 — consultada 2026-11-18 — prensa/blog
32. Despertar (blog) — RCV en Venezuela 2026: qué es, qué cubre y cuánto cuesta — https://blog.despertar.com.ve/rcv-en-venezuela/ — 2026 — consultada 2026-11-18 — secundaria/blog
33. El Impulso — #PulsoEmpresarial ¿Qué considerar al contratar un seguro para vehículos en Venezuela? — https://www.elimpulso.com/2026/09/25/pulsoempresarial-que-considerar-al-contratar-un-seguro-para-vehiculos-en-venezuela/ — 2026-09-25 — consultada 2026-11-18 — prensa
34. Mercantil Seguros — Pólizas de Auto — https://www.mercantilseguros.com/productos/personas/auto — sin fecha — consultada 2026-11-18 — primaria (aseguradora)
35. Seguros Miranda — Automóvil — https://segurosmiranda.com.ve/automovil/ — sin fecha — consultada 2026-11-18 — primaria (aseguradora)
36. Finanzas Digital — Tasa de Cambio BCV 16 de noviembre de 2026: 914,0218 Bs/USD — https://finanzasdigital.com/tasa-de-cambio-bcv-16-noviembre-2026/ — 2026-11-16 — consultada 2026-11-18 — prensa (reproduce el dato del BCV)
37. ElCambio.ve — Tasa BCV hoy 12 de noviembre 2026 / Dólar BCV en noviembre de 2026 — https://elcambiove.com/tasa-bcv-hoy/ ; https://elcambiove.com/tasa-bcv/2026-11/ — 2026-11-12 — consultada 2026-11-18 — secundaria
38. El Diario — Inflación anual de Venezuela se ubicó en 237,7 % al 2 de noviembre, según medición de Steve Hanke — https://eldiario.com/2026/11/02/inflacion-venezuela-noviembre-2026/ — 2026-11-02 — consultada 2026-11-18 — prensa
39. Observatorio Venezolano de Violencia — Informe Anual de Violencia 2023 — https://observatoriodeviolencia.org.ve/news/informe-anual-de-violencia-2023/ — 2023 — consultada 2026-11-18 — secundaria (ONG)
40. Correo del Caroní — OVV registró más de 15 mil delitos durante primer semestre de 2022 — https://correodelcaroni.com/region/sucesos/ovv-registro-mas-de-15-mil-delitos-durante-primer-semestre-de-2022/ — 2022 — consultada 2026-11-18 — prensa
41. Prensa Oriente — Carabobo: capturaron a dos sujetos tras robar un vehículo y pedir $2.500 para devolverlo — https://prensa.prensaoriente.com.ve/2026/07/17/carabobo-capturaron-a-dos-sujetos-tras-robar-un-vehiculo-y-pedir-2-500-para-devolverlo/ — 2026-07-17 — consultada 2026-11-18 — prensa
42. El Clarín — Robo de vehículo y extorsión tras solicitar un viaje por aplicación en Valencia: capturan a dos sujetos — https://elclarinweb.com/actualidad/robo-de-vehiculo-y-extorsion-tras-solicitar-un-viaje-por-aplicacion-en-valencia-capturan-a-dos-sujetos/ — jul-2026 — consultada 2026-11-18 — prensa
43. Notitarde — Capturados sujetos dedicados al hurto de vehículos en la zona norte de Valencia — https://www.notitarde.com.ve/sucesos/86630/capturado-dos-sujetos-dedicados-al-hurto-de-vehiculos-en-la-zona-norte-de-valencia-video — ≈ oct-2025 — consultada 2026-11-18 — prensa
44. La Calle — Cicpc capturó a sujeto solicitado en Valencia y recuperó dos vehículos — https://lacalle.com.ve/cicpc-capturo-a-sujeto-solicitado-en-valencia-y-recupero-dos-vehiculos/ — jul-2026 — consultada 2026-11-18 — prensa
45. El Tiempo (Colombia) — Los Toyoteros, la red de robos a lujosas camionetas que pasaban por trochas a Venezuela — https://www.eltiempo.com/justicia/delitos/los-toyoteros-red-de-robos-a-camionetas-que-pasaban-por-trochas-a-venezuela-848930 — fecha sin confirmar — consultada 2026-11-18 — prensa
46. Vilas Radio (Chile) — De portonazos a Caracas: camionetas robadas en Chile son legalizadas en Venezuela bajo resolución del gobierno de Maduro — https://vilasradio.cl/de-portonazos-a-caracas-camionetas-robadas-en-chile-son-legalizadas-en-venezuela-bajo-resolucion-del-gobierno-de-maduro/ — fecha sin confirmar (≈ 2024–2025) — consultada 2026-11-18 — prensa
47. U.S. News (Reuters) — Venezuela, Colombia to Collaborate on Border Security Following Kidnappings — https://www.usnews.com/news/world/articles/2026-11-12/venezuela-colombia-to-collaborate-on-border-security-following-kidnappings — 2026-11-12 — consultada 2026-11-18 — prensa
48. House of Commons Library — Venezuela: What has happened since Maduro's capture in January 2026? — https://commonslibrary.parliament.uk/research-briefings/cbp-12211/ — 2026 — consultada 2026-11-18 — secundaria (institucional)
49. El Estímulo — ¿Cuánto cuesta blindar un vehículo en Venezuela? — https://elestimulo.com/elinteres/economia/2016-10-06/cuanto-cuesta-blindar-un-vehiculo-en-venezuela/ — 2016-10-06 — consultada 2026-11-18 — prensa
50. Excen — ¿Qué hacer si quiero blindar mi vehículo? — https://excen.com.ve/los-vehiculos-blindados-en-venezuela/ — ago-2025 — consultada 2026-11-18 — secundaria (comercial)
51. MercadoLibre Venezuela — Camionetas blindadas — https://carros.mercadolibre.com.ve/camionetas-blindadas — sin fecha — consultada 2026-11-18 — clasificados
52. tucarro.com.ve — Toyota Runner 2024 — https://carros.tucarro.com.ve/toyota/2024/toyota-runner — sin fecha — consultada 2026-11-18 — clasificados
53. tucarro.com.ve — Runner (listados 2026) — https://carros.tucarro.com.ve/runner_Desde_101_NoIndex_True_fromYear_0 — sin fecha — consultada 2026-11-18 — clasificados
54. MercadoLibre Venezuela — Carros Toyota 4runner 2025 / Toyota 4Runner — https://carros.mercadolibre.com.ve/carros-toyota-4runner-2025 ; https://carros.mercadolibre.com.ve/toyota/4runner/ — sin fecha — consultada 2026-11-18 — clasificados
55. Conduce — Toyota 4Runner 2026 en venta en Venezuela / Real car sale prices in Venezuela — https://conduceapp.com/catalogo/toyota-4runner-2026-en-venezuela ; https://conduceapp.com/en/precios-de-venta — dato de sep-2026 — consultada 2026-11-18 — clasificados
56. Ricardocars — Toyota 4Runner 2025 en Venezuela: Guía 2026 — https://ricardocars.com/toyota-4runner-2025-venezuela-ricardo-severin/ — 2026 — consultada 2026-11-18 — prensa/blog
57. Autocosmos Venezuela — Toyota 4Runner usados en Venezuela — https://www.autocosmos.com.ve/auto/usado/toyota/4runner — sin fecha — consultada 2026-11-18 — clasificados
58. Gaceta Municipal de Valencia — Ordenanza de Impuesto sobre Vehículos del Municipio Valencia — https://valencia.sigat.net/documentos/ordenanzas/ordenanza_impuesto_vehiculos_del_municipio_valencia.pdf — fecha sin confirmar — consultada 2026-11-18 — primaria
59. Últimas Noticias — Anuncian reducción del 50 % en impuestos de vehículos en Valencia — https://en.ultimasnoticias.com.ve/carabobo/anuncian-reduccion-del-50-en-impuestos-de-vehiculos-en-valencia/ — 2025 — consultada 2026-11-18 — prensa
60. Gaceta Oficial N.º 6.783 Extraordinario — Valores máximos tributarios municipales y estadales (LOCAPTEM, Resolución 11-2023) — https://www.grantthornton.com.ve/globalassets/1.-member-firms/venezuela/2024/goe-6.783-maximos-tributarios-municipal-y-estadal-locaptem-resolucion-11-2023.pdf — ≈ 2024 (sin confirmar) — consultada 2026-11-18 — primaria
61. Gaceta Oficial N.º 6.755 Extraordinario — Ley Orgánica de Coordinación y Armonización de las Potestades Tributarias de los Estados y Municipios — https://assets.kpmg.com/content/dam/kpmg/ve/pdf/2023/08/Gaceta-Oficial-6.755.pdf — ago-2023 — consultada 2026-11-18 — primaria
62. MPPEF — Seniat pone en marcha el segundo circuito de Rayos X en la Aduana Principal de Puerto Cabello — https://www.mppef.gob.ve/seniat-pone-en-marcha-el-segundo-circuito-de-rayos-x-en-la-aduana-principal-de-puerto-cabello/ — fecha sin confirmar (≈ 2024) — consultada 2026-11-18 — primaria (gobierno)
63. TikTok @dacarmotors — Toyota Corolla Cross 2026 precio en Venezuela — https://www.tiktok.com/@dacarmotors/video/7619446055859473685 — 2026 — consultada 2026-11-18 — foro/redes
64. TOYO VE — Toyota Land Cruiser Prado Venezuela 2026 — https://toyove.com/prado — 2026 — consultada 2026-11-18 — clasificados/comercial
65. Manualslib — Toyota (EE. UU.) owner's manual, "Obtaining Warranty Service" (texto sobre touring/relocating outside the mainland U.S., Alaska and Canada) — https://www.manualslib.com/manual/562092/Toyota-Prius-C.html?page=34 — modelo antiguo, sin fecha — consultada 2026-11-18 — secundaria (reproduce documento primario)
66. Bernardi Toyota Parts — International Order Policy — https://toyota.bernardiparts.com/InternationalOrderPolicy.aspx — sin fecha — consultada 2026-11-18 — secundaria (comercial)
