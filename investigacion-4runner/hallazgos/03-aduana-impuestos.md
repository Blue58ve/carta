# Agente 3 — Aduana venezolana, aranceles e impuestos
**Fecha de investigación:** 2026-11-18 (ronda 1 y ronda 2)

> **No hay 🛑 ALERTA DE ALCANCE confirmada.** No encontré ninguna norma que prohíba a un particular importar un vehículo nuevo.
>
> **(ronda 2) Régimen Legal 20.** Ya no lo trato como posible prohibición. Las fuentes lo describen de dos formas: como "licencia previa o restricción especial" [10], o como la **Constancia de Registro de Norma COVENIN / Reglamento Técnico de SENCAMER** [48]. Es un requisito técnico que se tramita por producto, no una prohibición. Tampoco está confirmado que alcance a la 8703.40.
>
> **Presupuesto (no es 🛑, porque no es un problema legal).** Con IVA 16 % + 15 % de lujo, ya verificados en la ronda 2, el presupuesto de USD 80.000 **no alcanza en ningún escenario**. Aun con arancel 0 %, el vehículo puesto en puerto costaría ≥ USD 92.600 antes de logística, almacenaje y agente.
>
> **Límite de método.** WebFetch y la red de la sesión estuvieron bloqueados en las dos rondas. Todo lo "verificado" sale de los **extractos del buscador** sobre las URL citadas; no leí ninguna Gaceta completa. En la ronda 2 usé 30 búsquedas, el máximo asignado. Lo que no quedó respaldado en un extracto sigue marcado **[NO VERIFICADO]**.

## Resumen ejecutivo (5 líneas)
1. **Clasificación y arancel:**
   - La 4Runner, híbrida de gasolina no enchufable, va en la **8703.40**, no en la 8703.23, que es solo para motor de émbolo [22][23].
   - El Arancel vigente es el Decreto 4.944 (G.O. 6.804 Ext., 25-04-2024) con reformas hasta la Res. 007-2026 [1][14].
   - La **tarifa exacta de la 8703.40 sigue [NO VERIFICADO]**. Lo único que encontré: el Decreto 5.103 (G.O. 6.890 Ext., 06-03-2025) subió del **20 % al 40 %** los vehículos de gasolina de mayor cilindrada [7][8].
   - Tomo como rango de planificación **20 % / 40 % / 40 %** (mín. / probable / máx.).
2. **Beneficio para híbridos:** no encontré ninguno aplicable a un particular.
   - La subpartida 9801.00.00.23 del Decreto 5.103 menciona vehículos "con motor de encendido por chispa y con motor eléctrico" [50], pero parece ser **material de ensamblaje para ensambladoras (MEIV)**. Es una inferencia.
   - En 2025 se eliminaron la exoneración de IVA de las partidas 98.01–98.07 y la partida 98.08 de vehículos ensamblados (CBU) [11].
3. **(ronda 2) Tributos verificados:**
   - **IVA general 16 %** [28][29][33].
   - **IVA adicional de lujo 15 %**, que la ley permite subir hasta 20 %. Se aplica a vehículos con valor en aduanas ≥ **US$ 40.000**, umbral expresado **en dólares**, así que la 4Runner lo supera. Base legal: art. 61 de la Ley de IVA, G.O. 6.396 Ext. (21-08-2018), ratificado por la G.O. 6.507 Ext. (29-01-2020) [32][33][34].
   - **Tasa por determinación del régimen aduanero: 1 % del valor en aduanas** según el Reglamento de Tasas [37]. La LOA reformada (G.O. 6.507 Ext., 29-01-2020) admite un rango de 0,5 % a 2 % [36].
   - **IGTF: 3 % sobre pagos en divisas** (G.O. 6.687 Ext., 25-02-2022). El Decreto 4.972 (G.O. 6.821 Ext., 12-07-2024) solo llevó a 0 % ciertos pagos en bolívares [39][40].
4. **Carga tributaria total sobre el CIF** (fórmula a + t + (1 + a + t) × 31 %, donde a = arancel y t = tasa aduanera):
   - **57,9 %** como mínimo (arancel 20 %, tasa 0,5 %).
   - **84,7 %** en el escenario probable (arancel 40 %, tasa 1 %).
   - **88,6 %** como máximo (arancel 40 %, tasa 2 % e IGTF 3 % si los tributos se pagaran en divisas).
   - En dinero: con CIF de USD 70.000, entre **USD 40.500 y 62.000** de tributos; con CIF de USD 75.000, entre **USD 43.400 y 66.450**.
5. **Persona natural frente a la C.A.:** la carga aduanera es **idéntica**. La C.A. solo bajaría a ~62 % (o ~41 % si también recuperara el IVA de lujo) si el SENIAT le admitiera el crédito fiscal. Con uso personal del accionista eso es improbable, y además abre riesgos de ISLR y de dividendo encubierto. **Siguen [NO VERIFICADO]:**
   - la tarifa de la 8703.40;
   - si la Res. 022-2025 la incluye;
   - si el IGTF se aplica al pago de tributos aduaneros en divisas;
   - la fecha de tipo de cambio que usa la aduana;
   - la existencia de valores de referencia del SENIAT.

## Hallazgos detallados

### 1. Arancel de Aduanas vigente y cadena de reformas (2024–2026)
| # | Instrumento | Gaceta Oficial | Contenido relevante | Estado de verificación |
|---|---|---|---|---|
| a | **Decreto N° 4.944** (24-04-2024), Arancel de Aduanas | **G.O. N° 6.804 Ext., 25-04-2024** [1][2][27] | Arancel base, con códigos de **10 dígitos** [1]. Según un bufete, se aplica desde el 25-05-2024 [3] | Número y fecha coinciden en varias fuentes. Texto no leído |
| b | **Decreto N° 5.103** | **G.O. N° 6.890 Ext., 06-03-2025** [4][5] | Modifica nomenclatura y tarifas del art. 37 [6]. Exige 50 % de valor agregado nacional para las calificaciones MEIV [6][54]. Según fuentes comerciales, sube del 20 % al 40 % la tarifa de turismos y camionetas de gasolina de hasta 9 puestos de > 2.100 cm³ [7] (otra fuente dice > 1.500 cc [8]). Limita la antigüedad a 5 años (art. 13 [8]). **(ronda 2)** Su tabla incluye la subpartida **9801.00.00.23** "con motor de encendido por chispa y con motor eléctrico", junto a tractores de carretera; la columna de tarifa es ilegible en el extracto [50]. AB Group dice que el decreto da a híbridos y eléctricos "partida propia y tratamiento diferenciado", sin cifras, y que la regla de 5 años no les aplica [8] | Gaceta: consistente. El 40 % y la referencia a híbridos vienen de **[BUFETE/GESTOR]**; no confirmados en la Gaceta |
| c | **Decreto N° 5.122** | **G.O. N° 43.111, 21-04-2025** [9] | Reforma parcial; contenido no revisado | [NO VERIFICADO] |
| d | Reforma de mayo de 2025 | s/d [12b] | Contenido no revisado | [NO VERIFICADO] |
| e | **Decreto N° 5.147** (30-06-2025) | **G.O. N° 6.918 Ext.** [11] | Elimina la partida **98.08 (vehículos CBU)** y la posibilidad de exonerar el IVA en las partidas **98.01 a 98.07** [11]. **(ronda 2)** Según un resumen, también dispensa temporalmente el Régimen Legal 20 de SENCAMER en ciertas subpartidas [48] | [BUFETE/GESTOR]; la dispensa está [NO VERIFICADO] en cuanto a qué subpartidas cubre |
| f | **Resolución N° 022-2025** (03-07-2025), MPPEF | **G.O. N° 43.166, 09-07-2025** [10][49] | Modifica las columnas 5 y 6 del art. 37 en **29 subpartidas** de vehículos y autopartes, con **Régimen Legal 20** en importación. Códigos citados: 8701.21.00.00, 8703.22.10.10, 8703.90.90.00 y 8711.20.20.00 [10]. Las exportaciones siguen mayormente con régimen general (8716.31.00.10 con RL 11 y 20) [49] | **(ronda 2)** En 30 búsquedas ningún extracto menciona 8703.23, 8703.24, 8703.40 ni 8704. Su inclusión sigue [NO VERIFICADO] |
| g | Reforma de agosto de 2025 | s/d [12] | Contenido no revisado | [NO VERIFICADO] |
| h | Resolución N° 010-2025 | s/d [14] | Elimina la Nota Complementaria 3 del Capítulo 87 (certificado de emisiones) | [NO VERIFICADO] |
| i | **Decreto N° 5.198** (31-12-2025) | **G.O. N° 6.952 Ext.**; vigente desde el 05-01-2026 [13] | Modifica 1.371 subpartidas y 2 anexos; 753 con aplicación preferente [13]. No hallé cambios en el Capítulo 87 | [NO VERIFICADO] respecto al Capítulo 87 |
| j | **Decreto N° 5.376** | **G.O. N° 43.409, 06-07-2026** [17] | Suspende exportaciones de materiales de construcción. **No afecta al caso** | [BUFETE] |
| k | **Resolución N° 007-2026** (agosto de 2026), 11.ª reforma | s/d [14][18] | Contenido desconocido | **[NO VERIFICADO], prioridad alta** |

La LOA establece que se aplican **el régimen jurídico y el Arancel vigentes a la fecha de registro de la declaración de aduanas** (ronda 2) [36]. Por eso cualquier reforma publicada antes de registrar la declaración afecta a la operación.

### 2. Clasificación arancelaria
- **8703.40** (SA 2022): vehículos con motor de émbolo de encendido por chispa **y** motor eléctrico, excepto los que se pueden cargar desde una fuente externa. Los híbridos enchufables van en 8703.60 y los eléctricos en 8703.80 [22][55].
- **8703.21–8703.24:** cubren vehículos con **solo** motor de émbolo de encendido por chispa. El SA divide esas subpartidas en 1.000, 1.500 y 3.000 cm³; el corte de 2.100 cm³ es una regla **nacional** (ronda 2) [55].
- La 8703.40 no exige que la propulsión sea simultánea o en paralelo [22]. Costa Rica clasifica los híbridos de la misma forma [23].
- **Código nacional de 10 dígitos:** **[NO VERIFICADO]**. El Arancel venezolano abre la 8703 por cilindrada; por ejemplo, existe la 8703.22.10.10 para 1.000–1.500 cm³ [10].
- **(ronda 2) Capítulo 98:** por el contexto, la 9801.00.00.23 parece ser el **material de ensamblaje (CKD/MEIV)** para vehículos híbridos, destinado a ensambladoras calificadas, y no la importación de un vehículo ensamblado (CBU) por un particular. Es una **inferencia** del agente [50][6]. Además, la exoneración de IVA de las partidas 98.01–98.07 se eliminó en junio de 2025 [11].
- **Riesgo de reclasificación:** si la aduana no acepta la condición de híbrido, aplicaría la tarifa de gasolina > 2.100 cm³, que sería del 40 % según [7].

### 3. Tarifa ad valorem (AEC) aplicable
- **(ronda 2)** Busqué la tarifa de la 8703.40 con 6 consultas específicas. **Ninguna dio un extracto con el porcentaje.**
- Lo que hay son fuentes secundarias que no coinciden:
  - 20 % → 40 % para gasolina > 2.100 cm³ [7];
  - 40 % para > 1.500 cc [8];
  - 40 % "para vehículos" en una guía de 2026 [52];
  - 35–70 % y una supuesta "reducción de hasta 20 puntos para híbridos" en el sitio de un vendedor de Toyota, **sin cita normativa y poco fiable** [52];
  - un análisis colombiano de hace unos dos años según el cual Venezuela **no estipula tratamientos diferenciales para híbridos** [51].
- **Rango de trabajo (sin cambios):** mín. **20 %**, probable **40 %**, máx. **40 %**.
- **Origen:** no conozco preferencias arancelarias con Japón ni con EE. UU. [NO VERIFICADO].

### 4. Tratamiento especial para híbridos o eléctricos
- **No encontré ninguna exoneración, rebaja ni régimen vigente** para híbridos aplicable a un particular. En la ronda 2 hice 4 búsquedas adicionales y salieron solo regímenes de Argentina y Colombia, que no aplican.
- **(ronda 2) Decreto N° 5.197, "Decreto de Exoneraciones en Materia Aduanera"** (G.O. 6.952 Ext., 31-12-2025, vigente hasta el 31-12-2026) [47]:
  - Según un resumen, el Apéndice I exonera el **90 % del impuesto de importación y el 90 % del IVA**. Otra fuente habla del Apéndice IV.
  - Los bienes del Apéndice I necesitan permiso del **COMEX (Régimen Legal 9)**.
  - El MPPEF puede incluir o excluir bienes por resolución.
  - **No se encontró que cubra vehículos de pasajeros CBU [NO VERIFICADO].** Un decreto anterior mencionaba "vehículos… totalmente ensamblados, partidas 87.01 a 87.16" en un contexto que no está claro [47].
  - Fuente que lo resuelve: Apéndice I de la G.O. 6.952, que el SENIAT tiene indexada en seniatenlinea.seniat.gob.ve/wp-content/uploads/2026/01/GORBV-6952.pdf [47].
- **(ronda 2) Decreto N° 5.196** (misma Gaceta): suspende exenciones de IVA a importaciones de alimentos e insumos [47]. Reduce beneficios.
- **(ronda 2) Decreto N° 5.207** (G.O. 43.292, 09-01-2026): exonera IVA, impuesto de importación, tasa e IGTF **solo a combustibles y aditivos** [46]. No aplica.
- **Conclusión:** no hay beneficio para híbridos con el que se pueda contar.

### 5. Base imponible y valoración
- **Valor en aduana CIF.** Venezuela aplica el **Acuerdo de Valoración de la OMC (GATT 1994) desde el 29-12-1994**, según jurisprudencia del TSJ (ronda 2) [54].
- **Base del IVA en importación:** valor en aduanas **más el arancel** (ronda 2, según fuentes de gestores [38]). Que también incluya la tasa aduanera está [NO VERIFICADO], pero el efecto es mínimo: 0,31 puntos del CIF.
- **Momento del pago (ronda 2):** el impuesto de importación, la tasa y los demás gravámenes se pagan **antes o en el momento del registro de la declaración** [36].
- **Valores de referencia del SENIAT para vehículos:** **[NO VERIFICADO]**, no encontré ninguna lista vigente (ronda 2). La **Gerencia del Valor (División de Precios)** del SENIAT atiende consultas de valor de vehículos [54] y ha aplicado ajustes de valor en otros casos, por ejemplo Pirelli [54]. Recomendación: factura real del concesionario y pago bancario trazable.

### 6. IVA, IVA de lujo, tasa aduanera, IGTF y otras cargas (ronda 2)
| Concepto | Valor verificado | Base legal / fuente | Comentario |
|---|---|---|---|
| **IVA, alícuota general** | **16 %** | Rango legal 8 %–16,5 %. Fijado en 16 % por el Decreto 3.584 (ago-2018) [29] y mantenido en la reforma de la Ley de IVA, **G.O. 6.507 Ext., 29-01-2020** [30][33]. Vigencia en 2026: PwC Tax Summaries [28] | No encontré reforma de la Ley de IVA en 2025–2026 (búsqueda específica [33]) |
| **IVA adicional por consumo suntuario (vehículos)** | **15 %** adicional, sobre la misma base → **31 % en total** | **Art. 61 de la Ley de IVA**: vehículos con **valor en aduanas (o precio de fábrica en el país) ≥ US$ 40.000** (G.O. 6.396 Ext., 21-08-2018 [32]). La reforma de 2020 (G.O. 6.507 Ext.) mantiene el 15 % "hasta tanto el Ejecutivo establezca una alícuota distinta" (rango 15–20 %, art. 27) [33][34][35] | **Unidad: USD.** La reforma de 2018 dejó de usar unidades tributarias [33]. **La 4Runner lo supera** (CIF 70.000–75.000 > 40.000). No encontré ningún decreto que haya subido la alícuota por encima del 15 % [NO VERIFICADO para 2026] |
| IVA adicional por pagos en divisas o criptoactivos | 5 %–25 % en la ley, **sin alícuota fijada** según fuentes de 2020 [42] | Ley de IVA 2020 | No encontré decreto que la active. Estado en 2026 y aplicación en aduana: [NO VERIFICADO]. No la incluyo en el cálculo |
| **Tasa por determinación del régimen aduanero** | **1 % del valor en aduanas** (rango legal 0,5 %–2 %) | Reglamento de la LOA sobre Tasas Aduaneras (Decreto N° 1.505, fecha s/d): "uno por ciento (1 %) del valor en aduanas" [37]. La LOA reformada (G.O. 6.507 Ext., 29-01-2020) fija la tasa entre 0,5 % y 2 % [36]. Gestores reportan ~1 % [38] | Es posible que el reglamento sea anterior a 2020; el 1 % que se aplica en la práctica no lo confirmé en el portal del SENIAT |
| **IGTF** | **3 %** sobre pagos en divisas o criptoactivos | Ley de IGTF reformada, **G.O. 6.687 Ext., 25-02-2022** [39]. **Decreto 4.972, G.O. 6.821 Ext., 12-07-2024** (vigente desde el 15-07-2024): 0 % en ciertas operaciones en bolívares; no cambia el 3 % en divisas [40]. Guías de 2026 confirman el 3 % [41] | Lo cobran los **contribuyentes especiales** [39]. **No encontré si se aplica al pago de tributos aduaneros en divisas [NO VERIFICADO].** Si los tributos se pagan en Bs, el IGTF en divisas no se aplica. El pago del vehículo en EE. UU. desde una cuenta extranjera está fuera del sistema venezolano; que no cause IGTF es una inferencia del agente |
| **Moneda y tipo de cambio** | Los tributos se pagan **antes o al registrar la declaración** [36]. Las cantidades fijas de la LOA se expresan en múltiplos de la tasa oficial BCV de la moneda de mayor valor (reforma de 2020) [36][45] | LOA, G.O. 6.507 Ext. (2020); Acceso a la Justicia [45] | **La regla exacta de qué fecha de tasa se usa para convertir el CIF a Bs sigue [NO VERIFICADO].** Como el pago coincide con el registro, la diferencia práctica es mínima |
| **Tasa oficial BCV** | **911,62 Bs/USD** (fijada el 12-11-2026, vigente desde el 13-11-2026) | [PRENSA] que cita al BCV [43]. Referencias: 891,10 (03-11) y 896,12 (06-11) [43] | No encontré la tasa del 18-11-2026. Hay depreciación continua (unos 2,3 % en 9 días) |
| Unidad Tributaria | **Bs 43** | Providencia SNAT/2025/000048, G.O. 43.140, 02-06-2025 [44] | Ya casi no se usa como referencia aduanera; la LOA usa la tasa BCV [45] |
| Ley de Protección de Pensiones, timbre fiscal estadal | Sin cambios respecto a la ronda 1 | — | [NO VERIFICADO]. En principio no gravan la importación |

### 7. Restricciones y requisitos para importar
- **Prohibición para particulares:** no encontré ninguna. El Decreto 5.103 no limita la importación a fines comerciales [7].
- **Antigüedad:** máximo 5 años [7][8]. No afecta a un vehículo nuevo.
- **(ronda 2) Régimen Legal 20 (Res. 022-2025):**
  - Finanzas Digital lo describe como "licencia previa o restricciones especiales" expedida por el "órgano competente" [10].
  - SENCAMER lo identifica con la **Constancia de Registro de Norma Venezolana COVENIN / Reglamento Técnico**. El RL 21 se fusionó con el RL 20 por el Decreto N° 4.111. El Decreto N° 3.679 (30-05-2005) exige presentar la constancia de SENCAMER junto con la declaración de aduanas [48].
  - Se tramita en SENCAMER en línea, por producto [48].
  - **No sé si una persona natural puede pedirla ni cuánto tarda [NO VERIFICADO]**, ni si la 8703.40 está en la lista.
  - **No es una prohibición**, por eso no hay 🛑. Si la 8703.40 estuviera incluida, añadiría un trámite técnico y tiempo.
  - El Decreto 5.147 habría dispensado temporalmente el RL 20 en ciertas subpartidas [48] [NO VERIFICADO].
- **Agente de aduanas:** según una guía de gestor (ronda 2), "en ambas vías [ordinaria y equipaje] es obligatorio gestionar el trámite con un agente aduanal autorizado por el SENIAT" [53]. Es una fuente [BUFETE/GESTOR]; el artículo de la LOA sigue [NO VERIFICADO].
- **RIF y registro de usuario aduanero de la persona natural o de la C.A.:** [NO VERIFICADO].
- **(ronda 2) Régimen de equipaje** [53]:
  - El vehículo, valorado como nuevo, no puede superar **US$ 20.000**.
  - Exige **al menos 1 año de residencia fuera del país** y tener el vehículo a nombre del viajero **≥ 11 meses** antes del ingreso.
  - Requiere un certificado de uso emitido por un consulado venezolano.
  - Un vehículo por persona, de hasta 9 puestos; no se puede vender en Venezuela durante 3 años.
  - **El cliente no califica por dos motivos:** es residente en Venezuela y el valor de la 4Runner supera los US$ 20.000. Fuentes de gestores y prensa; el texto normativo actual está [NO VERIFICADO].

### 8. Persona natural frente a la C.A.: diferencias tributarias
- **Tributos de aduana:** **iguales** para los dos titulares. No hay alícuotas distintas según el tipo de importador.
- **Crédito fiscal de IVA (solo la C.A.):**
  - Un vehículo para uso personal del accionista difícilmente cumple el requisito de estar vinculado a la actividad gravada, así que el crédito probablemente se rechazaría [artículo exacto NO VERIFICADO].
  - Una C.A. recién constituida sin ventas solo acumularía el crédito, sin poder usarlo.
  - Si se admitiera el crédito del IVA general, la carga probable bajaría de 84,7 % a **62,2 %**; si también se admitiera el IVA de lujo, a **41,0 %**. No sé si el IVA de lujo da derecho a crédito [NO VERIFICADO].
- **ISLR, dividendo encubierto, transferencia posterior al accionista e impuesto a los grandes patrimonios:** sin cambios respecto a la ronda 1 [NO VERIFICADO].
- **Valoración del agente:** para uso personal, importar como persona natural es lo más simple y lo menos arriesgado.

## Cifras clave (tabla: concepto | valor | rango mín/prob/máx si es estimación | fuente [n] | fecha de la fuente / Gaceta)

| Concepto | Valor | Rango mín / prob / máx (si es estimación) | Fuente [n] | Fecha fuente / Gaceta |
|---|---|---|---|---|
| Arancel de Aduanas base | Decreto N° 4.944 (24-04-2024) | — | [1][2][27] | G.O. N° 6.804 Ext., 25-04-2024 |
| Subpartida SA | 8703.40 | — | [22][23][55] | SA 2022 |
| Código nacional de 10 dígitos | [NO VERIFICADO] | — | resolver con [1][4][10] | — |
| AEC gasolina > 2.100 cm³ (Decreto 5.103) | 40 % (antes 20 %) [BUFETE/GESTOR] | — | [7] ([8]: > 1.500 cc) | G.O. N° 6.890 Ext., 06-03-2025 |
| AEC de la 8703.40 de 2.393 cm³ | [NO VERIFICADO] | 20 % / 40 % / 40 % | inferido de [7][8][52] | — |
| Régimen Legal 20 en 29 subpartidas de vehículos y autopartes | Sí; la 8703.40 [NO VERIFICADO] | — | [10][48][49] | Res. 022-2025, G.O. N° 43.166, 09-07-2025 |
| Partida 98.08 (CBU) y exoneración de IVA de las partidas 98.01–98.07 | Eliminadas | — | [11] | Decreto 5.147, G.O. N° 6.918 Ext., 30-06-2025 |
| Exoneraciones aduaneras generales (Decreto 5.197) | 90 % del arancel y 90 % del IVA en el Apéndice I, hasta el 31-12-2026; **cobertura de vehículos no hallada** | — | [47] | G.O. N° 6.952 Ext., 31-12-2025 |
| Beneficio para híbridos | No encontrado | — | [51][50][11] | — |
| **IVA, alícuota general** (ronda 2) | **16 %** | — | [28][29][30][33] | Decreto 3.584 (2018); Ley IVA, G.O. N° 6.507 Ext., 29-01-2020 |
| **IVA adicional de lujo** (ronda 2) | **15 %** (rango legal 15–20 %) | — | [32][33][34][35] | Art. 61 Ley IVA; G.O. N° 6.396 Ext., 21-08-2018; G.O. N° 6.507 Ext., 29-01-2020 |
| **Umbral de lujo para vehículos** (ronda 2) | Valor en aduanas ≥ **US$ 40.000** (en USD). **La 4Runner lo supera** | — | [32][33][35] | Ídem |
| **Tasa por determinación del régimen aduanero** (ronda 2) | **1 % del valor en aduanas** | 0,5 % / 1 % / 2 % (rango de la LOA) | [36][37][38] | Reglamento de Tasas (Decreto 1.505); LOA, G.O. N° 6.507 Ext., 29-01-2020 |
| **IGTF** (ronda 2) | **3 %** sobre pagos en divisas | 0 % (tributos en Bs) / 0 % / 3 % | [39][40][41] | G.O. N° 6.687 Ext., 25-02-2022; Decreto 4.972, G.O. N° 6.821 Ext., 12-07-2024 |
| IVA adicional por pago en divisas | 5–25 % en la ley; sin decreto que la fije (2020) | — | [42] | Ley IVA 2020; vigencia en 2026 [NO VERIFICADO] |
| **Tasa oficial BCV** (ronda 2) | **911,62 Bs/USD** | — | [43] [PRENSA] | Fijada el 12-11-2026, vigente desde el 13-11-2026 |
| Unidad Tributaria (ronda 2) | Bs 43 | — | [44] | Prov. SNAT/2025/000048, G.O. N° 43.140, 02-06-2025 |
| Tope de valor del régimen de equipaje (ronda 2) | US$ 20.000 (valor como nuevo) | — | [53] [BUFETE/GESTOR] | s/f |

**Fórmulas (ronda 2):**
- Arancel = CIF × a
- Tasa = CIF × t
- Base del IVA = CIF + Arancel + Tasa (la inclusión de la tasa es un supuesto)
- IVA = Base × 16 %
- IVA de lujo = Base × 15 % (aplica porque el valor en aduanas ≥ US$ 40.000)
- IGTF = Tributos × 3 %, solo si se pagan en divisas y el impuesto aplica [NO VERIFICADO]
- **Carga (% del CIF) = a + t + (1 + a + t) × 31 %**

**Escenarios recalculados (ronda 2), en USD:**

| Escenario | a | t | Carga % del CIF | CIF 70.000: Arancel / Tasa / IVA 16 % / Lujo 15 % / **Total tributos** / CIF + tributos | CIF 75.000: Arancel / Tasa / IVA 16 % / Lujo 15 % / **Total tributos** / CIF + tributos |
|---|---|---|---|---|---|
| **Mínimo** | 20 % | 0,5 % | **57,9 %** | 14.000 / 350 / 13.496 / 12.652,50 / **40.498,50** / 110.498,50 | 15.000 / 375 / 14.460 / 13.556,25 / **43.391,25** / 118.391,25 |
| Arancel 20 %, tasa 1 % | 20 % | 1 % | 58,5 % | 14.000 / 700 / 13.552 / 12.705 / **40.957** / 110.957 | 15.000 / 750 / 14.520 / 13.612,50 / **43.882,50** / 118.882,50 |
| **Probable** | 40 % | 1 % | **84,7 %** | 28.000 / 700 / 15.792 / 14.805 / **59.297** / 129.297 | 30.000 / 750 / 16.920 / 15.862,50 / **63.532,50** / 138.532,50 |
| Arancel 40 %, tasa 2 % | 40 % | 2 % | 86,0 % | 28.000 / 1.400 / 15.904 / 14.910 / **60.214** / 130.214 | 30.000 / 1.500 / 17.040 / 15.975 / **64.515** / 139.515 |
| **Máximo** (40 %, tasa 2 % + IGTF 3 % sobre tributos) | 40 % | 2 % | **88,6 %** | Tributos + IGTF ≈ **62.020** / ≈ 132.020 | Tributos + IGTF ≈ **66.450** / ≈ 141.450 |
| Referencia: arancel 0 % | 0 % | 1 % | 32,3 % | 0 / 700 / 11.312 / 10.605 / **22.617** / 92.617 | 0 / 750 / 12.120 / 11.362,50 / **24.232,50** / 99.232,50 |

En bolívares, a la tasa BCV de 911,62 (vigente desde el 13-11-2026) [43], el escenario probable equivale a **≈ Bs 54,06 millones** (CIF 70.000) y **≈ Bs 57,92 millones** (CIF 75.000). Es solo ilustrativo: la tasa aplicable será la de la fecha que fije la aduana.

**Por titular (ronda 2):**

| Titular | Carga aduanera | Carga efectiva si se admite crédito del IVA general | Carga efectiva si se admite también el crédito del IVA de lujo | Comentario |
|---|---|---|---|---|
| Persona natural | Mín. 57,9 % · Prob. 84,7 % · Máx. 88,6 % | No aplica | No aplica | La opción más simple |
| La C.A. venezolana | Igual: 57,9 % · 84,7 % · 88,6 % | Mín. ≈ 38,6 % · Prob. ≈ 62,2 % | Mín. ≈ 20,5 % · Prob. ≈ 41,0 % | **Improbable** con uso personal: posible rechazo del crédito, crédito sin usar por falta de ventas, riesgo de ISLR y de dividendo encubierto. Que el IVA de lujo dé crédito está [NO VERIFICADO] |

*Los importes no incluyen flete interno, almacenaje, servicios portuarios ni honorarios del agente de aduanas, que llevan otros agentes.*

## Riesgos detectados
1. **Tarifa de la 8703.40 sin confirmar.** La diferencia entre 20 % y 40 % es de unos **26 puntos del CIF**: alrededor de USD 18.300 con CIF de 70.000 y USD 19.650 con CIF de 75.000.
2. **El presupuesto no alcanza (ronda 2, ya con IVA verificado).** Escenario mínimo: USD 110.500–118.400 antes de logística. Escenario probable: USD 129.300–138.500. Ni con arancel 0 % (USD 92.600–99.200) se llega a USD 80.000.
3. **Régimen Legal 20:** si la 8703.40 estuviera en la Res. 022-2025, habría que tramitar la constancia COVENIN o reglamento técnico de SENCAMER, o la "licencia previa", con plazo desconocido. No está confirmado que la incluya ni que sea una prohibición.
4. **Resolución 007-2026** (agosto de 2026) con contenido desconocido. Se aplica el Arancel vigente a la fecha de registro de la declaración [36].
5. **Normativa muy cambiante:** al menos 11 reformas del Arancel entre 2024 y 2026. El Decreto 5.197 vence el 31-12-2026. El Ejecutivo puede subir el IVA de lujo hasta el 20 % y la tasa aduanera hasta el 2 % sin reformar la ley [33][36].
6. **Reclasificación** a 8703.23 si no se acredita la condición de híbrido.
7. **Ajuste del valor** por la Gerencia del Valor del SENIAT [54].
8. **La C.A.:** registro aduanero incompleto, rechazo de crédito y de depreciación, posible dividendo encubierto.
9. **Tipo de cambio:** depreciación del bolívar de unos 2,3 % en 9 días en noviembre de 2026 [43]. Conviene registrar la declaración y pagar el mismo día.
10. **IGTF** sobre tributos pagados en divisas o sobre honorarios en divisas del agente: no está aclarado.
11. **Verificación limitada:** todas las cifras salen de extractos del buscador; no leí ninguna Gaceta completa.

## Preguntas abiertas
1. ¿Cuál es el código de 10 dígitos y la tarifa de la 8703.40 de 2.393 cm³ en el art. 37 del Decreto 4.944 con sus reformas, en especial el Decreto 5.103 y la Res. 007-2026? Lo resuelve el texto de las Gacetas 6.804 y 6.890 Ext., por ejemplo los PDF de Tradex o Travieso Evans [1][4][50].
2. ¿Incluye la Res. 022-2025 alguna 8703.40? ¿El RL 20 equivale aquí a la constancia de SENCAMER o a una licencia ministerial? ¿Puede pedirla una persona natural y cuánto tarda?
3. ¿Qué cambió la Res. 007-2026?
4. ¿Se aplica el IGTF al pago de tributos aduaneros en divisas? ¿Acepta el SENIAT pagos de aduana en divisas?
5. ¿Qué fecha de tasa BCV se usa para convertir el CIF: la del registro de la declaración o la del pago?
6. ¿El 1 % del Reglamento de Tasas sigue siendo la tasa aplicada tras la reforma de la LOA de 2020?
7. ¿La base del IVA de importación incluye la tasa aduanera? ¿El IVA de lujo da derecho a crédito fiscal?
8. ¿Cubre el Apéndice I del Decreto 5.197 algún vehículo de la partida 87.03? Hay que revisar el PDF GORBV-6952 [47].
9. ¿Existen listas de valores de referencia del SENIAT para vehículos nuevos?
10. ¿Es obligatorio por ley el agente de aduanas para una persona natural (artículo de la LOA)? ¿Qué registros se exigen (RIF, registro de usuario aduanero)?
11. ¿Se ha activado la alícuota adicional de IVA por pagos en divisas (5–25 %)?
12. ¿Cuál es el umbral vigente en 2026 del impuesto a los grandes patrimonios?

## Fuentes (lista numerada: título — URL — fecha de la fuente — consultada 2026-11-18 — tipo: primaria/secundaria/prensa/foro)
*Todas se consultaron el 2026-11-18 **a través de los extractos del buscador**; no se abrió ninguna URL directamente. "Primaria (copia)" significa una copia de la Gaceta u otra norma alojada por un tercero, que no se leyó completa.*

1. Gaceta Oficial N° 6.804 Extraordinario (Decreto N° 4.944, Arancel de Aduanas) — https://www.traviesoevans.com/travieso/wp-content/uploads/gacetas/2024/04-abril/2024-04-25-6804-extraordinario.pdf ; copia de Tradex: https://www.tradex.com.ve/wp-content/uploads/Tradex-Arancel-de-Aduanas-Decreto-4.944-GOE-6.804.pdf — 25-04-2024 — consultada 2026-11-18 — primaria (copia)
2. FEDEAGRO, "Se dicta el Arancel de Aduanas" — https://fedeagro.org/se-dicta-el-arancel-de-aduanas/ — 2024 — consultada 2026-11-18 — secundaria
3. Stanzione, "Actualización en el Arancel de Aduanas en Venezuela a partir del pasado 25 de mayo de 2024" — https://stanzione.com/actualizacion-en-el-arancel-de-aduanas-en-venezuela-a-partir-del-pasado-25-de-mayo-de-2024/ — 2024 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
4. Gaceta Oficial N° 6.890 Extraordinario (Decreto N° 5.103) — https://assets.kpmg.com/content/dam/kpmg/ve/pdf/2025/3/g.e_6.890.pdf ; https://traviesoevans.com/travieso/wp-content/uploads/gacetas/2025/03-marzo/2025-03-06-6890-extraordinario.pdf — 06-03-2025 — consultada 2026-11-18 — primaria (copia)
5. Legis, "Reforma Parcial del Arancel de Aduanas" — https://www.legis.com.ve/BancoConocimiento/N/nota_20-03-2025-01/nota_20-03-2025-01.asp?Miga=1&CodSeccion=25 — 20-03-2025 — consultada 2026-11-18 — secundaria
6. PwC Venezuela, "Decreto N° 5.103, que modifica parcialmente el Decreto N° 4.944" — https://www.pwc.com/ve/es/assets/documentos/stl/NAC-Exoneraciones-IVA-e-Impuestos-de-Importacion-FY25-Rev-AAP-1.pdf — 2025 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
7. Continental Suppliers, "SENIAT autoriza importación de vehículos nuevos y usados" — https://continentalsuppliers.com/seniat-autoriza-importacion-de-vehiculos-nuevos-y-usados/ — s/f (posterior a mar-2025) — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
8. AB Group Shipping, "Calculadora envío carro a Venezuela 2026" — https://www.abgroupshipping.com/blogs/es/calculadora-envio-carro-a-venezuela-2026-desde-1-450 — 2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
9. Decreto N° 5.122 / G.O. N° 43.111 — https://vlexvenezuela.com/vid/decreto-n-5-122-1080119490 ; https://www.bancaynegocios.com/wp-content/uploads/2025/05/GO-43.111-2-4.pdf — 21-04-2025 — consultada 2026-11-18 — primaria (copia)
10. Resolución N° 022-2025, G.O. N° 43.166: Badell & Grau — https://badellgrau.com/gaceta-oficial-n-o-43-166-del-09-de-julio-de-2025/ ; Ámbito Aduanero (X) — https://x.com/ambitoaduanero/status/1945213683782893594 ; Finanzas Digital — https://finanzasdigital.com/regimen-legal-20-importacion-vehiculos-venezuela-2025/ y https://finanzasdigital.com/resolucion-gaceta-oficial-43-166-importacion-vehiculos-venezuela/ ; Fedecámaras Radio — https://fedecamarasradio.com/gobierno-ajusta-aranceles-de-importacion-para-vehiculos-y-autopartes-en-gaceta-oficial-n-43-166/ ; Sumarium — https://sumarium.info/2025/07/15/gobierno-venezolano-refuerza-control-de-comercio-exterior-sobre-vehiculos-y-autopartes-con-nueva-resolucion/ — 09/15-07-2025 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR] / [PRENSA]
11. LEĜA Abogados, "Reforma del Arancel de Aduanas de fecha 30 de junio de 2025" (Decreto 5.147, G.O. 6.918 Ext.) — https://lega.law/reform-of-the-customs-tariff-dated-june-30-2025/ — 2025 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
12. Legis, "Reforman parcialmente el decreto que establece el Arancel de Aduanas" — https://www.legis.com.ve/BancoConocimiento/N/nota_27-08-2025-07/nota_27-08-2025-07.asp?Miga=1&CodSeccion=25 — 27-08-2025 — secundaria. 12b. Legis, "Dictan decreto que reforma el Arancel de Aduanas" — https://www.legis.com.ve/BancoConocimiento/N/nota_13-05-2025-n2/nota_13-05-2025-n2.asp?Miga=1&CodSeccion=25 — 13-05-2025 — consultada 2026-11-18 — secundaria
13. Baker McKenzie, "Venezuela: Nueva reforma parcial del Arancel de Aduanas" (Decreto 5.198) — https://www.bakermckenzie.com/en/insight/publications/2026/01/venezuela-new-partial-amendment-to-the-customs-tariff-schedule — ene-2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
14. Tradex, "Normativa Arancelaria / Exoneración de Gravámenes y Tributos" y "SUMARIO – Reforma Arancel – Decreto de Exoneración G.O. 6.952" — https://www.tradex.com.ve/normativa-arancelaria/ ; https://www.tradex.com.ve/wp-content/uploads/Tradex-Reforma-Arancel-de-Aduanas-Decreto-de-Exoneracion-GO.-6.952.pdf — 2025–2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
15. Acceso a la Justicia, "Suspensión de la aplicación de las exenciones a la importación…" y "Exoneraciones de Impuestos de Importación e IVA a la importación" — https://accesoalajusticia.org/suspension-de-la-aplicacion-de-las-exenciones-a-la-importacion/ ; https://accesoalajusticia.org/exoneraciones-de-impuestos-de-importacion-e-impuesto-al-valor-agregado-a-la-importacion/ — 2025–2026 — consultada 2026-11-18 — secundaria
16. LEĜA, "Exoneraciones en materia aduanera vigentes hasta el 31 de diciembre de 2026" — https://lega.law/en/exoneraciones-en-materia-aduanera-vigentes-hasta-el-31-de-diciembre-de-2026/ ; https://lega.law/lega-informa/exoneraciones-aduanas-2026/ — ene-2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
17. TTPN, "Decreto Nro. 5.376…" (G.O. 43.409) — https://ttpn.com.ve/?p=5604 — jul-2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
18. Ámbito Aduanero, "Arancel de Aduanas de Venezuela…" (y aviso de la Res. 007-2026) — https://www.ambitoaduanero.com/home-mainmenu-1/21-jurisprudenciassecciona/87-aranceladuanasvenezuela — s/f — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
19. Holland & Knight, exoneraciones 2023 y 2024 — https://www.hklaw.com/-/media/files/insights/publications/2023/07/venezueladecreeprovidesexemptionsaffectingimporttaxeses.pdf ; https://www.hklaw.com/-/media/files/insights/publications/2024/09/venezuelaextendsvatexemptiones.pdf — 2023/2024 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
20. Acceso a la Justicia y Legiscomex, régimen de equipaje (jurisprudencia) — https://accesoalajusticia.org/requisitos-para-la-importacion-de-vehiculos-bajo-regimen-de-equipaje/ ; https://accesoalajusticia.org/importacion-de-vehiculo-usado-bajo-regimen-aduanero-especial-de-equipaje/ ; https://www.legiscomex.com/BancoMedios/Documentos%20PDF/régimen%20de%20equipaje%20de%20pasajeros.pdf — s/f — consultada 2026-11-18 — secundaria
21. TSJ / Tribunal Superior Contencioso Tributario, sentencia de 2014 sobre vehículos nuevos (vLex) — https://vlexvenezuela.com/vid/tribunal-superior-contencioso-tributario-593348022 — 02-07-2014 — consultada 2026-11-18 — primaria (jurisprudencia)
22. MINCIT Colombia, proyecto de decreto sobre híbridos (análisis de la 8703.40) — https://abcrepecev.com/hubfs/21-04-21-pd-vehiculos-hibridos.pdf — abr-2021 — secundaria (referencia comparada); Studocu (UCV Perú) — https://www.studocu.com/pe/document/universidad-cesar-vallejo/nomenclatura-arancelaria-y-valoracion-aduanera/vehiculo-hibrido-y-electricos/95358829 — [FORO/REDES] — consultada 2026-11-18
23. Ministerio de Hacienda de Costa Rica, Res. MH-DGA-RES-0535-2024 — https://www.hacienda.go.cr/docs/MH-DGA-RES-0535-2024.pdf — 2024 — consultada 2026-11-18 — secundaria (referencia comparada)
24. Easyship, calculadora de aranceles de Venezuela (método CIF) — https://www.easyship.com/es-es/duties-and-taxes-calculator/venezuela — s/f — consultada 2026-11-18 — secundaria comercial
25. Somerset Escargot, "Nuevas tasas de importación en Venezuela 2026…" — https://somersetescargot.co.uk/nuevas-tasas-de-importacion-en-venezuela-2026-cambios-en-aranceles-aduaneros-desde-marzo/ — 2026 — consultada 2026-11-18 — [FORO/REDES] (poco fiable; no se usó)
26. Times Brasil, ACE 69 — https://timesbrasil.com.br/brasil/venezuela-quer-elevar-tarifa-sobre-carros-brasileiros/ — 2025 — consultada 2026-11-18 — [PRENSA] (contexto)
27. Pandectas Digital, "Arancel de Aduanas [Vigente]" — https://pandectasdigital.blogspot.com/2024/04/arancel-de-aduanas.html — abr-2024 — consultada 2026-11-18 — [FORO/REDES]
28. (ronda 2) PwC Worldwide Tax Summaries, "Venezuela – Corporate – Other taxes" (IVA general 16 %, rango 8–16,5 %) — https://taxsummaries.pwc.com/venezuela/corporate/other-taxes — 2026 (s/f) — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
29. (ronda 2) KPMG Venezuela, Síntesis Legal 35/2018 (Decreto 3.584, alícuota general 16 %) — https://kpmg.com/ve/es/home/insights/2018/08/sintesislegal35-2018.html — ago-2018 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
30. (ronda 2) vLex, "Sobre la reforma de la Ley que establece el IVA" (16 % mantenido) — https://vlexvenezuela.com/vid/reforma-ley-establece-iva-929608712 — 2020 — consultada 2026-11-18 — secundaria; JETRO (16 % desde el 01-01-2020) — https://www.jetro.go.jp/world/cs_america/ve/invest_04.html — s/f — secundaria
31. (ronda 2) KPMG, Síntesis Legal 1-2026 — https://assets.kpmg.com/content/dam/kpmg/ve/pdf/2026/1/S%C3%ADntesis%20Legal%201-2026.pdf — ene-2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR] (contexto; no se extrajeron cifras)
32. (ronda 2) Travieso Evans, memo de la reforma de la Ley de IVA y G.O. Ext. N° 6.396 (art. 61: vehículos ≥ US$ 40.000; lujo 15 %) — http://www.traviesoevans.com/memos/memo-reforma-ley-iva.pdf ; http://www.traviesoevans.com/memos/Gaceta-Ext-6396-21082018-ReformaLey-IVA.pdf — 21-08-2018 — consultada 2026-11-18 — primaria (copia) / [BUFETE/GESTOR]
33. (ronda 2) G.O. N° 6.507 Ext., Decreto Constituyente de reforma de la Ley de IVA (y comparativos) — https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-parcial-del-decreto-con-rango-valor-y-fuerza-de-ley-que-establece-el-impuesto-al-valor-agregado-20220204234747.pdf ; https://www.venamcham.org/wp-content/uploads/2021/11/Reforma-COT-IVA-G.O.-Ext-No-6507-29-ENE-2020.pdf ; Moore, comparativo 2020 frente a 2018 — https://www.moore-venezuela.com/MediaLibsAndFiles/media/venezuelaweb.moorestephens.com/Documents/Comparativo-Ley-del-IVA-2020-vs-2018-pdfDEFINITIVO.pdf ; transcripción — https://docs.cachicamo.app/fiscal/ley-iva-2020 — 29-01-2020 — consultada 2026-11-18 — primaria (copia)
34. (ronda 2) Banca y Negocios, "Impuesto al lujo…" y "Alícuota del IVA al consumo suntuario será de 15 %"; Tal Cual, "Bienes suntuarios pagarán en total 31 %…" — https://www.bancaynegocios.com/impuesto-al-lujo-vehiculos-aviones-armas-y-otros-productos-pagaran-iva-de-15-en-venezuela/ ; https://www.bancaynegocios.com/alicuota-del-iva-al-consumo-suntuario-sera-de-15/ ; https://talcualdigital.com/bienes-suntuarios-pagaran-en-total-31-de-impuesto-al-valor-agregado/ — ago-2018 — consultada 2026-11-18 — [PRENSA]
35. (ronda 2) Rodríguez C., "6 claves sobre tarifas y exenciones del IVA en Venezuela" (vehículos ≥ US$ 40.000 → 31 %) — https://rodriguezc.com/6-claves-sobre-tarifas-y-exencioness-del-iva-en-venezuela/ — s/f — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
36. (ronda 2) G.O. N° 6.507 Ext., Decreto Constituyente de reforma de la Ley Orgánica de Aduanas (tasa del 0,5 % al 2 %; pago antes o al registro; régimen y Arancel vigentes a la fecha de registro) — https://www.venamcham.org/wp-content/uploads/2021/11/G.O.-Ext-6507-Ene-2020-Reforma-de-la-Ley-Orga%CC%81nica-de-Aduanas-MAYO-2020-comprimido.pdf ; https://www.asambleanacional.gob.ve/storage/documentos/leyes/decreto-constituyente-de-reforma-del-decreto-con-rango-valor-y-fuerza-de-ley-organica-de-aduanas-20220204223809.pdf ; Acceso a la Justicia (comparación) — https://accesoalajusticia.org/wp-content/uploads/2020/02/Ley-Org%C3%A1nica-de-Aduanas.-Comparaci%C3%B3n-vis-a-vis.pdf ; Travieso Evans (alerta) — https://www.traviesoevans.com/wp-content/uploads/2020/11/Alerta-Reforma-Decreto-LOAduanas-espanol-enero-29-2020.pdf — 29-01-2020 — consultada 2026-11-18 — primaria (copia)
37. (ronda 2) Reglamento de la LOA sobre las Tasas Aduaneras (Decreto N° 1.505; tasa del 1 % del valor en aduanas) — https://vlexvenezuela.com/vid/decreto-n-1-505-547479754 ; https://irp-cdn.multiscreensite.com/d92a6498/files/uploaded/REGLAMENTO%20LEY%20ORG%C3%81NICA%20DE%20ADUANAS.pdf — fecha s/d (probablemente anterior a 2020) — consultada 2026-11-18 — primaria (copia)
38. (ronda 2) Bitácora Económica, "Automotrices prefieren pagar impuestos a ensamblar en Venezuela"; Maxiautos, "Importar un vehículo a Venezuela en 2026"; ByMotorCar, "How to import Chinese cars to Venezuela" — https://bitacoraeconomica.com/automotrices-prefieren-pagar-impuestos-a-ensamblar-en-venezuela/ ; https://maxiautosve.com/importar-un-vehiculo-a-venezuela-en-2025-2026-plazos-costos-y-documentos-clave/ ; https://bymotorcar.com/import-chinese-cars-to-venezuela/ — 2025–2026 — consultada 2026-11-18 — [PRENSA] / [BUFETE/GESTOR]
39. (ronda 2) IGTF 3 % en divisas (G.O. 6.687 Ext.; percepción por contribuyentes especiales): Moore Venezuela — https://www.moore-venezuela.com/wp-content/uploads/sites/15/2025/12/156-IGTF.pdf ; Crónica Uno — https://cronica.uno/igtf-de-3-a-transacciones-en-divisas-debe-reflejarse-en-las-facturas-a-partir-del-lunes/ ; Gerencia y Tributos — https://gerenciaytributos.blogspot.com/2022/03/regimen-percepcion-IGTF-contribuyentes-especiales-divisas.html — 2022/2025 — consultada 2026-11-18 — secundaria / [PRENSA]
40. (ronda 2) Decreto N° 4.972, G.O. N° 6.821 Ext. (IGTF del 2 % al 0 % en ciertas operaciones en Bs): PwC — https://www.pwc.com/ve/es/publicaciones/assets/PublicacionesNew/Boletines/Modificación%20de%20la%20Alícuota%20de%20IGTF%202%20al%200%20(Julio%202024).pdf ; Forvis Mazars — https://www.forvismazars.com/ve/es/insights/forvis-mazars-insights/se-fija-en-0-la-alicuota-del-igtf ; Acceso a la Justicia — https://accesoalajusticia.org/fue-eliminado-impuesto-grandes-transacciones-financieras/ — 12-07-2024 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
41. (ronda 2) Guías de IGTF 2026 (3 % vigente): Nompli — https://www.nompli.com/blog/igtf-venezuela-como-calcular-3-porciento-2026 ; Alegra — https://blog.alegra.com/venezuela/como-calcular-el-igtf-en-una-factura/ — 2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
42. (ronda 2) IVA adicional por pagos en divisas (5–25 %, sin decreto que lo fije): Nayma Consultores — https://naymaconsultores.com/claves-iva-adicional-a-los-pagos-en-dolares-venezuela/ ; Infobae — https://www.infobae.com/america/venezuela/2020/02/10/venezuela-el-regimen-de-nicolas-maduro-impondra-altos-impuestos-extras-a-las-compras-en-dolares/ ; El Carabobeño — https://www.el-carabobeno.com/en-claves-que-dice-la-ley-del-iva-sobre-los-consumos-en-divisas/ — 2020 — consultada 2026-11-18 — secundaria / [PRENSA]
43. (ronda 2) Tasa BCV de noviembre de 2026: Finanzas Digital — https://finanzasdigital.com/tasa-de-cambio-bcv-12-noviembre-2026/ , https://finanzasdigital.com/tasa-de-cambio-bcv-03-noviembre-2026/ , https://finanzasdigital.com/tasa-de-cambio-bcv-06-noviembre-2026/ ; El Caribe — https://www.elcaribe.com.do/panorama/dolar-venezuela-hoy-4-noviembre-2026/ ; La Patilla — https://lapatilla.com/2026/11/12/el-dolar-bcv-sigue-sin-encontrar-techo-y-ya-amenaza-otra-barrera-historica/ — 03/12-11-2026 — consultada 2026-11-18 — [PRENSA] (cita al BCV)
44. (ronda 2) UT de Bs 43 (Prov. SNAT/2025/000048, G.O. 43.140): IUSDATA — https://iusdata.com/seniat-ut-unidad-tributaria-bs-43/ ; FOGADE — https://www.fogade.gob.ve/2025/06/04/seniat-ajusta-unidad-tributaria-a-43-bolivares/ — 02/04-06-2025 — consultada 2026-11-18 — secundaria / organismo oficial
45. (ronda 2) Acceso a la Justicia, "Sustitución progresiva de la Unidad Tributaria como referencia fiscal en Venezuela" — https://accesoalajusticia.org/sustitucion-progresiva-unidad-tributaria-referencia-fiscal-venezuela/ — 2025 — consultada 2026-11-18 — secundaria
46. (ronda 2) Decreto N° 5.207, G.O. N° 43.292 (exoneración para combustibles): PwC — https://www.pwc.com/ve/es/assets/documentos/stl/NAC-Exoneracion-IVA-Decreto-5207-Ene2026.pdf ; LEĜA — https://lega.law/lega-informa/exoneracion-iva-importacion-hidrocarburos/ ; Torres Plaz & Araujo — https://www.torresplazaraujo.com/alerta-legal-decreto-no-5-207/ ; Finanzas Digital — https://finanzasdigital.com/exoneracion-impuestos-combustibles-venezuela-2026/ — 09-01-2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
47. (ronda 2) Decretos N° 5.197 (exoneraciones aduaneras) y N° 5.196 (suspensión de exenciones de IVA), G.O. N° 6.952 Ext.: TTPN — https://ttpn.com.ve/?p=5409 ; LEĜA — https://lega.law/lega-informa/exoneraciones-aduanas-2026/ ; Grant Thornton — https://www.grantthornton.com.ve/globalassets/1.-member-firms/venezuela/2026/ni-resumen-decreto-de-suspension-de-exenciones-del-iva.pdf ; Acceso a la Justicia — https://accesoalajusticia.org/nuevas-regulaciones-sobre-el-pago-del-i-v-a/ ; Cavefar (decreto anterior) — https://cavefar.org.ve/wp-content/uploads/2025/07/Decreto-de-Exoneracion-y-Exenciones.pdf ; G.O. 6.952 en el SENIAT (indexada) — seniatenlinea.seniat.gob.ve/wp-content/uploads/2026/01/GORBV-6952.pdf — 31-12-2025 — consultada 2026-11-18 — primaria (copia) / secundaria [BUFETE/GESTOR]
48. (ronda 2) Régimen Legal 20 / SENCAMER: SENCAMER, "Tres nuevos productos deben cumplir Régimen Legal 20" — https://www.sencamer.gob.ve/?p=7316 ; Decreto N° 3.679 (30-05-2005) — https://ine.gob.ve/wp-content/uploads/2024/09/Decreto-No.pdf ; SENCAMER en línea — https://enlinea.sencamer.gob.ve/action/registro/intro ; Aduaneros.net, Decreto 5.147 / G.O. 6.918 Ext. — https://aduaneros.net/wp-content/uploads/2025/07/2025_Reforma_5_AA_Decreto_5147_GOE_6918.pdf ; Unica Customs — https://www.unicacustoms.com/en/blog/how-to-import-a-car-to-venezuela/ — 2005–2025 — consultada 2026-11-18 — primaria (organismo y decreto) / secundaria
49. (ronda 2) Finanzas Digital, "Gaceta Oficial N° 43.166: Sumario"; Hexa Legal (entrevista a Marisol Mujica) — https://finanzasdigital.com/gaceta-oficial-43166/ ; https://hexa-legal.com/marisol-mujica-ajuste-arancelario-eleva-costos-y-complica-importacion-de-vehiculos/ — jul-2025 — consultada 2026-11-18 — [PRENSA] / [BUFETE/GESTOR]
50. (ronda 2) Tradex, PDF del Decreto 5.103 (extracto con la subpartida 9801.00.00.23) — https://www.tradex.com.ve/wp-content/uploads/Tradex-Decreto-5.103-Reforma-del-Arancel-de-Aduanas.pdf — 06-03-2025 — consultada 2026-11-18 — primaria (copia)
51. (ronda 2) Asuntos Legales (Colombia), "La paradoja de los vehículos híbridos" (Venezuela sin trato diferencial) — https://www.asuntoslegales.com.co/analisis/camilo-castrillon-2955163/la-paradoja-de-los-vehiculos-hibridos-3962501 — ~2024 — consultada 2026-11-18 — [PRENSA]
52. (ronda 2) Toyove, "Aranceles para importar un Toyota a Venezuela 2026" (poco fiable); Landeed, "Cómo importar a Venezuela en 2026" — https://toyove.com/aranceles-importar-toyota-venezuela/ ; https://landeed-ve.netlify.app/guide/importar-a-venezuela/ — 2026 — consultada 2026-11-18 — [FORO/REDES]
53. (ronda 2) Régimen de equipaje para vehículos (US$ 20.000, 1 año fuera, agente obligatorio): Diario El Regional del Zulia — https://diarioelregionaldelzulia.com/seniat-reactiva-importacion-de-vehiculos-por-regimen-de-equipaje/ ; La Nación — https://lanacionweb.com/frontera/como-importar-un-vehiculo-usado-bajo-el-regimen-de-equipaje/ ; Cedrizuela — https://cedrizuela.com/blogs/migracion/importacion-de-vehiculos-a-venezuela-regimen-de-equipaje-vs-via-comun-seniat-e-intt ; Venezuela Productiva Automotriz — https://venezuelaproductivaautomotriz.com/42695-importar-carro-venezuela-aranceles/ ; Embajada de Venezuela en Polonia — https://www.venez.pl/certificado-de-uso-de-vehiculo/ ; Scribd — https://www.scribd.com/document/526465502/La-Importacion-de-Vehiculos-Bajo-Regimen-de-Equipaje-de-Pasajeros-1 — s/f a 2026 — consultada 2026-11-18 — [PRENSA] / [BUFETE/GESTOR] / [FORO/REDES]
54. (ronda 2) Valoración: Pirelli Venezuela vs. SENIAT (vLex) — https://vlexvenezuela.com/vid/pirelli-venezuela-c-vs-seniat-407618458 ; TSJ-SPA N° 01428, 03-12-2015 — https://vlexvenezuela.com/vid/servicio-nacional-integrado-administracion-593081778 — 2010–2015 — consultada 2026-11-18 — primaria (jurisprudencia)
55. (ronda 2) Duane Morris, "Navigating the Charge" (códigos SA 8703.40–8703.80) y aperturas SA del Capítulo 87 (MH El Salvador) — https://www.duanemorris.com/site/static/dms-ev-latin-america-us.pdf ; https://transparencia.mh.gob.sv/downloads/pdf/DC5710_cap_tulo87.pdf — s/f — consultada 2026-11-18 — secundaria (referencia de nomenclatura)
