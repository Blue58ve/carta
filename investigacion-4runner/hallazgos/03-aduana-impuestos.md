# Agente 3 — Aduana venezolana, aranceles e impuestos
**Fecha de investigación:** 2026-11-18

> **Sin 🛑 ALERTA DE ALCANCE confirmada.** No encontré ninguna norma que prohíba a particulares importar un vehículo nuevo. Quedan abiertos dos riesgos que podrían frenar la operación: (1) que la subpartida del vehículo esté en el **Régimen Legal 20 (licencia previa)** de la Resolución 022-2025 [10]; (2) que el presupuesto de USD 80.000 todo incluido **no alcance en ningún escenario** si se confirma el IVA (ver §6). El punto (2) es un problema de presupuesto, no de legalidad, así que no lo marco como 🛑.
>
> **Límite de método (importante para el verificador).** No pude leer ninguna fuente directamente: WebFetch y la red de la sesión rechazaron todos los dominios que probé (seniat.gob.ve, tradex.com.ve, bakermckenzie.com, finanzasdigital.com, pwc.com, kpmg.com, traviesoevans.com, lega.law, bcv.org.ve, entre otros). Todo lo "verificado" sale de los **resúmenes del buscador (WebSearch)** sobre las URL citadas. Además, el cupo de búsquedas que comparten todos los agentes (200) se agotó a mitad de la investigación, **antes de que pudiera buscar IVA, alícuota de lujo, IGTF, tasa aduanera, tasa BCV, registro de importador y agente de aduanas**. Esos puntos van como **[NO VERIFICADO]**. Cuando muestro un porcentaje para ellos, es un **supuesto de trabajo tomado del conocimiento previo del agente**, no un dato con fuente; sirve solo para el cálculo de sensibilidad.

## Resumen ejecutivo (5 líneas)
1. **Clasificación:** por el texto del Sistema Armonizado, un híbrido de gasolina **no enchufable** (HEV) va en la **subpartida 8703.40**, no en la 8703.23. La 8703.2x cubre vehículos que solo tienen motor de émbolo [22][23]. El código nacional de 10 dígitos dentro de 8703.40 y su tarifa exacta en el Arancel (Decreto 4.944, G.O. 6.804 Ext., 25-04-2024 [1]) quedan **[NO VERIFICADO]**.
2. **Arancel:** el Decreto 5.103 (G.O. 6.890 Ext., 06-03-2025) subió del **20 % al 40 %** el arancel de los automóviles de gasolina por encima de cierta cilindrada: 2.100 cm³ según [7], 1.500 cm³ según [8]. No confirmé si la 8703.40 sigue esa regla. Trabajo con un rango del **20–40 %** y uso **40 %** para planificar.
3. **Híbridos:** no encontré **ninguna exoneración ni rebaja vigente** para vehículos híbridos o eléctricos en Venezuela. Además, en 2025 se **eliminaron** la partida 98.08, que cubría vehículos ensamblados (CBU), y algunas exoneraciones del sector automotor [11][6].
4. **Carga tributaria:** con los supuestos de trabajo (tasa aduanera 1 %, IVA 16 %, IVA adicional de lujo 15 %), los tributos suman entre **40 % y 85 % del CIF**, o hasta **~89 %** con IGTF y una tasa del 2 %. El costo puesto en puerto, antes de logística local, queda entre **USD 98.000 y 130.000** para un CIF de USD 70.000. Aun con arancel 0 %, el IVA solo llevaría el total por encima de USD 82.000. Con estas cifras, **el presupuesto de USD 80.000 no se cumple**.
5. **Titular:** los tributos de aduana **son los mismos** para la persona natural y para la C.A. La C.A. solo ganaría si pudiera usar el IVA de importación como crédito fiscal, y eso es **improbable** si el uso es personal del accionista, además de traer riesgos de ISLR y de que se trate como dividendo encubierto. Todo el marco de IVA, IGTF y tasa aduanera, y la tasa BCV, quedan **[NO VERIFICADO]**.

## Hallazgos detallados

### 1. Arancel de Aduanas vigente y cadena de reformas (2024–2026)
| # | Instrumento | Gaceta Oficial | Contenido relevante | Estado de verificación |
|---|---|---|---|---|
| a | **Decreto N° 4.944** (24-04-2024), que dicta el Arancel de Aduanas | **G.O. N° 6.804 Extraordinario, 25-04-2024** [1][2][27] | Es el Arancel base, con códigos de **10 dígitos** [1]. Un bufete reporta su aplicación "a partir del 25 de mayo de 2024" [3] | Varias fuentes secundarias coinciden en el número y la fecha de la Gaceta. No leí el texto |
| b | **Decreto N° 5.103** | **G.O. N° 6.890 Extraordinario, 06-03-2025** [4][5] | Modifica la nomenclatura y la tarifa (AEC) de subpartidas del art. 37. "Actualiza condiciones para la importación de vehículos" [6]. Permite exonerar el AEC y el IVA en ciertas importaciones del sector automotor y exige 50 % de valor agregado nacional para calificar como material de ensamblaje (MEIV) [6]. Según fuentes no oficiales, sube del 20 % al 40 % la tarifa de turismos y camionetas de gasolina de hasta 9 puestos por encima de 2.100 cm³ [7] (otra fuente dice > 1.500 cc [8]). Limita la antigüedad a **5 años** (art. 13 según [8]) y no limita la importación a fines comerciales [7] | Número y Gaceta: consistentes. El 40 % y el art. 13 salen de **[BUFETE/GESTOR]** comerciales; **no los confirmé en la Gaceta** |
| c | **Decreto N° 5.122** (reforma parcial) | **G.O. N° 43.111, 21-04-2025** [9] | Contenido no revisado. Un PDF de Tradex lo encabeza con "Número 42.439… 21 de abril de 2025", posible errata | Contenido [NO VERIFICADO] |
| d | Reforma del Arancel de mayo de 2025 | s/d [12b] | Legis la reseña el 13-05-2025; contenido no revisado | [NO VERIFICADO] |
| e | **Decreto N° 5.147** (30-06-2025) | **G.O. N° 6.918 Extraordinario** [11] | Elimina la exoneración de IVA de ciertas partes de ensamblaje y **elimina la partida 98.08 (vehículos totalmente ensamblados, CBU)** [11] | Fuente [BUFETE/GESTOR] |
| f | **Resolución N° 022-2025** (03-07-2025), Ministerio de Economía, Finanzas y Comercio Exterior | **G.O. N° 43.166, 09-07-2025** [10] | Modifica las **columnas 5 y 6 del art. 37** en **29 subpartidas** de vehículos y autopartes y les asigna el **Régimen Legal 20**, descrito como "licencia previa o restricciones especiales". Ejemplos citados: 8703.22.10.10 (1.000–1.500 cm³), 8703.90.90.00, 8701.21.00.00, 8711.20.20.00 [10]. Un especialista dice que rubros que pagaban 3 % pasan a pagar hasta 20 % [10] | Número, fecha y alcance general: varias fuentes coinciden. **No sé si alguna subpartida 8703.40 está en la lista** [NO VERIFICADO] |
| g | Reforma parcial de agosto de 2025 | s/d [12] | Legis la reseña el 27-08-2025; contenido no revisado | [NO VERIFICADO] |
| h | Resolución N° 010-2025 | s/d | Según Tradex, elimina la Nota Complementaria 3 del Capítulo 87, que exigía el **certificado de emisiones de fuentes móviles** [14] | [NO VERIFICADO] (solo lo vi en un resumen) |
| i | **Decreto N° 5.198** (31-12-2025) | **G.O. N° 6.952 Extraordinario**; vigente desde el **05-01-2026** [13] | Modifica 1.371 subpartidas y dos anexos técnicos, con aplicación preferente e inmediata en 753 subpartidas [13]. El listado que vi empieza en el Capítulo 52; no constan cambios en el Capítulo 87 [14] | Cambios en el Capítulo 87 [NO VERIFICADO] |
| j | **Decreto N° 5.376** | **G.O. N° 43.409, 06-07-2026** [17] | Suspende la **exportación** de materiales de construcción por el sismo del 24-06-2026 (Régimen Legal 1), hasta el 31-12-2026. **No afecta a vehículos importados** | Fuente [BUFETE] |
| k | **Resolución N° 007-2026** (agosto de 2026), 11.ª reforma | s/d [14][18] | **Contenido desconocido**. Un resumen menciona una vigencia hasta el 31-12-2026 | **[NO VERIFICADO], prioridad alta**: es la reforma más reciente y podría tocar el Capítulo 87 |

**Conclusión:** el Arancel vigente es el **Decreto 4.944 (G.O. 6.804 Ext., 25-04-2024)**, con al menos 11 reformas. Para fijar la tarifa de la 4Runner hay que leer, en este orden: el art. 37 del Decreto 4.944, el Decreto 5.103, la Resolución 022-2025 y la Resolución 007-2026. Ninguno de esos textos se pudo leer en esta sesión. Según Ámbito Aduanero, la LOA permite modificar el Arancel **por resolución** con aprobación previa del Consejo de Ministros y publicación en Gaceta [18]. Por eso la tarifa puede cambiar sin un decreto nuevo.

### 2. Clasificación arancelaria
- **8703.40** (texto SA 2022/NANDINA): "Los demás vehículos, equipados para la propulsión con motor de émbolo alternativo de encendido por chispa y con motor eléctrico, **excepto los que se puedan cargar mediante conexión a una fuente externa de alimentación eléctrica**". Los híbridos enchufables van en 8703.60 y los eléctricos puros en 8703.80 [22].
- **8703.21 a 8703.24:** cubren vehículos con motor de émbolo de encendido por chispa **únicamente**. La palabra "únicamente" viene de la nomenclatura SA desde 2017; la cito por conocimiento previo y debe confirmarse en el texto del Decreto 4.944 [1]. Un HEV con motor eléctrico de tracción, como el i-FORCE MAX, **no puede ir en 8703.23**.
- Un documento técnico del MINCIT de Colombia aclara que **la 8703.40 no exige que la propulsión eléctrica y térmica sea simultánea ni en paralelo** [22]. Costa Rica (Res. MH-DGA-RES-535-2024) trata los híbridos de la misma manera [23]. Las dos son referencias comparadas, no venezolanas.
- **Código nacional de 10 dígitos:** **[NO VERIFICADO]**. El Arancel venezolano divide la 8703 por cilindrada; por ejemplo, la Gaceta 43.166 cita "8703.22.10.10 – 1.000 a 1.500 cm³" [10]. Lo probable es que la 8703.40 tenga aperturas por cilindrada parecidas. El motor de 2.393 cm³ la pondría en el tramo de 1.500 a 3.000 cm³, o por encima de 2.100 cm³ si se usa ese umbral. **Fuente que lo resuelve:** art. 37 del Decreto 4.944 [1], con las modificaciones del Decreto 5.103 [4] y la Resolución 022-2025 [10].
- **Riesgo de reclasificación:** si la aduana considerara que el sistema es un "microhíbrido" sin tracción eléctrica real, o la clasificara en 8703.23, la tarifa sería la de gasolina > 2.100 cm³, es decir, **40 %** según [7]. Conviene llevar la ficha técnica de Toyota que describe el motor-generador integrado en la transmisión.
- La partida **87.04** (pick-ups de carga) mantiene el 20 % según [7], pero la 4Runner es una SUV de pasajeros, así que no aplica.
- **Descartado:** un documento "Arancel Aduanero de Importaciones 2026 – MEFP" en Scribd muestra tarifas de 3 % y 5 % para la 8703.40, pero **no es venezolano** (lo publica un ministerio "MEFP" de otro país). No debe usarse.

### 3. Tarifa ad valorem (AEC) aplicable
- **Hecho de fuente secundaria:** Decreto 5.103: turismos y camionetas de gasolina de hasta 9 puestos con más de 2.100 cm³ pasan del 20 % al 40 %; los de menor cilindrada siguen en 20 % [7]. AB Group Shipping sitúa el umbral del 40 % en 1.500 cc [8]. Con cualquiera de los dos umbrales, un motor de 2.393 cm³ queda en el tramo del 40 % **si las reglas de gasolina se aplican a la 8703.40**.
- **No verificado:** la tarifa propia de la 8703.40 de 2.393 cm³. No encontré fuente, oficial ni secundaria, que la dé.
- **Rango de trabajo:** mín. **20 %** (si los híbridos mantuvieran la tarifa anterior), probable o de planificación **40 %**, máx. **40 %**. No hallé evidencia de una tarifa preferencial para híbridos.
- **Origen:** no conozco ningún acuerdo preferencial entre Venezuela y Japón o EE. UU. que rebaje el AEC [NO VERIFICADO]. Los acuerdos con Brasil (ACE 69) no aplican.

### 4. Tratamiento especial para híbridos o eléctricos
- **No encontré** ningún decreto vigente (2022–2026) que exonere o rebaje el arancel o el IVA de los vehículos híbridos o eléctricos en Venezuela. Hice una búsqueda ampliada específica y solo aparecieron exoneraciones generales [19][6][14]. **No demuestra que no exista**: es **[NO VERIFICADO]**. Se resolvería con el texto del decreto de exoneraciones vigente y del Arancel.
- **Exoneraciones vigentes en general:**
  - En la G.O. 6.952 Ext. (31-12-2025) se publicó, junto con el Decreto 5.198, un decreto de exoneraciones de impuesto de importación e IVA. Su número es 5.196 o 5.197; las fuentes no coinciden. Deroga el Decreto 5.145 (30-06-2025) y rige **hasta el 31-12-2026** [14][15][16].
  - No vi que cubra vehículos de pasajeros CBU para particulares [NO VERIFICADO].
  - Antecedentes: los regímenes automotores anteriores exigían un "Certificado de Exoneración del Sector Automotriz" o el régimen de material de ensamblaje (Decreto 4.412 de 2021; prórroga del Decreto 4.985 hasta el 31-12-2024, con exoneración del 90 %). Estaban dirigidos a ensambladoras o bienes concretos, no a particulares [19].
  - La exoneración que quedaba para la vía CBU desapareció con la **eliminación de la partida 98.08** en junio de 2025 [11].
- **Acceso a la Justicia** reseña una "suspensión de la aplicación de las exenciones a la importación previstas en el Decreto-Ley del IVA" [15]. Eso **reduce** beneficios, no los amplía.
- **Conclusión de trabajo:** el cliente **no debe contar con ningún beneficio por ser híbrido**, ni como persona natural ni como C.A.

### 5. Base imponible y valoración
- **Valor en aduana CIF** (factura + flete + seguro): una fuente comercial secundaria indica que Venezuela calcula los tributos sobre el CIF [24]. La regla legal está en la Ley Orgánica de Aduanas, su Reglamento y el Acuerdo de Valoración de la OMC. Los artículos concretos son **[NO VERIFICADO]**.
- **Valores o precios de referencia del SENIAT para vehículos nuevos:** **[NO VERIFICADO]**. No encontré si existen listas oficiales. **Riesgo práctico:** si el valor declarado queda por debajo de los precios públicos (MSRP o equivalentes), es esperable que la aduana lo ajuste. Recomendación: que la factura del concesionario refleje el precio real de la transacción, con el pago bancario trazable.
- **Base del IVA de importación:** supongo que es **CIF + arancel + tasa aduanera** (y otros recargos). Es la regla habitual de la Ley de IVA para importaciones, pero **no la verifiqué en esta sesión** [NO VERIFICADO; la resuelve el artículo de base imponible en importaciones de la Ley de IVA vigente].

### 6. IVA, alícuota adicional de lujo, tasa aduanera, IGTF y otras cargas
**Todos los datos de esta sección son [NO VERIFICADO]**, porque el cupo de búsquedas se agotó antes de llegar a ellos. Los valores que siguen son **supuestos de trabajo del conocimiento previo del agente**, para que el verificador o un nuevo agente los confirme:

| Concepto | Supuesto de trabajo | Qué falta confirmar | Fuente que lo resolvería |
|---|---|---|---|
| IVA, alícuota general en importación | 16 % | Alícuota vigente en nov-2026 y decreto que la fija | Ley de IVA vigente y decreto de alícuota general (portal SENIAT / G.O.) |
| IVA adicional por bienes suntuarios (vehículos) | 15 % adicional, que se suma al general | La alícuota exacta (la ley fija un rango), el **umbral de valor del vehículo** y la unidad en que se expresa (USD, "moneda de mayor valor" del BCV o UT) | Ley de IVA vigente, artículos sobre consumo suntuario y su reforma más reciente |
| ¿Supera la 4Runner el umbral de lujo? | Probablemente sí, si el umbral está en decenas de miles de USD | Umbral real y si se mide sobre FOB, CIF o valor en aduana | Ídem |
| Tasa por determinación del régimen aduanero | 1 % del valor en aduana (sensibilidad hasta 2 %) | Porcentaje, base y si existe otra "tasa por servicio aduanero" | Ley Orgánica de Aduanas vigente (artículo de tasas) y su Reglamento |
| IGTF | 3 % sobre pagos en divisas, en ciertos supuestos | (a) alícuota vigente en 2026; (b) si se aplica al pago de tributos de aduana en divisas; (c) si se aplica al pago en EE. UU. desde cuenta extranjera (en principio no, por ser una operación fuera del sistema venezolano); (d) si se aplica a los honorarios en divisas del agente de aduanas | Ley de IGTF vigente, decreto de alícuota y providencias del SENIAT |
| Moneda de pago de los tributos | Se liquidan en Bs a la tasa oficial BCV del día que fija la norma (registro de la declaración o llegada) | Fecha de tasa aplicable y si se aceptan pagos en divisas | LOA, Código Orgánico Tributario vigente y providencias del SENIAT |
| Tasa BCV más reciente | — | No se pudo consultar bcv.org.ve (dominio bloqueado) | bcv.org.ve |
| Ley de Protección de Pensiones (contribución especial de empresas) | Grava la nómina de las empresas, **no la importación** | Confirmar que no grava importaciones | G.O. de la ley (2024) |
| Timbre fiscal / tasas estadales | — | Si algún estado cobra timbre sobre trámites de importación o registro | Leyes de timbre fiscal estadal (Carabobo o Vargas/La Guaira) |

### 7. Restricciones y requisitos para importar
- **Prohibición de importar por particulares:** **no encontré ninguna**. Según una fuente comercial, el Decreto 5.103 **no limita la importación a fines comerciales** [7]. Esto respalda que una persona natural puede importar para uso propio. No está confirmado en la Gaceta.
- **Antigüedad:** máximo **5 años** según el Decreto 5.103 [7][8]. Una regla anterior, recogida en jurisprudencia de 2014, solo admitía vehículos nuevos con año modelo igual al de importación o el siguiente [21]. Un vehículo nuevo MY2026/2027 cumple las dos reglas.
- **Licencia previa (Régimen Legal 20):** la Resolución 022-2025 lo exige para 29 subpartidas de vehículos y autopartes [10]. **Hay que comprobar si alguna 8703.40 está en la lista.** Si lo está, se necesitará una licencia del ministerio competente antes del embarque, y una persona natural podría no conseguirla. Es el principal riesgo de alcance pendiente.
- **Certificado de emisiones:** se habría eliminado como requisito de la Nota Complementaria 3 del Capítulo 87 (Resolución 010-2025) [14] [NO VERIFICADO].
- **RIF, registro de usuario aduanero del SENIAT y agente de aduanas obligatorio:** **[NO VERIFICADO]**. Hay que confirmar si una persona natural puede actuar como consignatario de una importación única sin estar inscrita como importador habitual, y si la LOA obliga a usar un agente de aduanas o permite actuar directamente. En la práctica se espera que intervenga un agente [suposición]. **Fuente:** LOA vigente (auxiliares de la administración aduanera) y providencias del SENIAT sobre el registro de usuarios.
- **Régimen de equipaje o menaje:** existe un régimen de equipaje de pasajeros que ha permitido ingresar vehículos usados de uso personal en ciertos supuestos, con jurisprudencia sobre sus requisitos [20]. Está pensado para viajeros o personas que se mudan, no para residentes. **El cliente, residente en Venezuela, muy probablemente no califica** [suposición basada en [20]; requisitos actuales NO VERIFICADOS].
- **La C.A. recién constituida:** si aún no tiene completo el registro de usuario aduanero o de importador, **no podrá figurar como consignataria** hasta tenerlo [requisito exacto NO VERIFICADO].

### 8. Persona natural frente a la C.A.: diferencias tributarias
- **Tributos de aduana** (arancel, tasa, IVA, IVA adicional): **iguales** con cualquier titular. No hay alícuotas diferenciadas por tipo de importador en las fuentes revisadas.
- **Crédito fiscal de IVA (solo la C.A.):**
  - La Ley de IVA solo permite deducir los créditos fiscales de bienes ligados a la actividad gravada. Un vehículo para uso personal o familiar del accionista **no cumpliría esa condición** y es probable que el SENIAT rechazara el crédito en una fiscalización [regla general; artículo exacto NO VERIFICADO].
  - Una C.A. recién constituida sin ventas no tendría débitos contra los que compensar el crédito, así que el beneficio sería solo diferido.
  - Tampoco sé si la alícuota adicional de lujo da derecho a crédito [NO VERIFICADO].
  - Si el crédito del IVA general (16 %) se admitiera, que es improbable, la carga efectiva bajaría unos 19–23 puntos del CIF (ver §Cifras).
- **ISLR (C.A.):** la depreciación del vehículo solo es deducible si el gasto es normal y necesario para producir la renta. Con uso personal, el SENIAT podría rechazarla. Si la C.A. paga el vehículo y lo usa el accionista, existe el riesgo de que se trate como **distribución encubierta de dividendos**, o como renta en especie para el accionista, con ISLR sobre dividendos [régimen exacto y alícuotas NO VERIFICADOS].
- **Salida futura del vehículo de la C.A.:** si después la C.A. lo vende o lo transfiere al accionista, esa operación generaría IVA (débito fiscal) e ISLR sobre la ganancia [NO VERIFICADO].
- **Impuesto a los grandes patrimonios:** solo alcanzaría al cliente o a la C.A. si son sujetos pasivos especiales y superan el umbral legal. El umbral, la unidad en que se expresa y la vigencia en 2026 están **[NO VERIFICADO]**.
- **Valoración de trabajo:** desde el punto de vista aduanero y tributario, **importar a nombre de la persona natural es más simple y menos arriesgado** para un uso personal. La C.A. no reduce los tributos de aduana y añade riesgos de fiscalización. Esto es un análisis del agente, no un dato.

## Cifras clave (tabla: concepto | valor | rango mín/prob/máx si es estimación | fuente [n] | fecha de la fuente / Gaceta)

| Concepto | Valor | Rango mín / prob / máx (si es estimación) | Fuente [n] | Fecha fuente / Gaceta |
|---|---|---|---|---|
| Arancel de Aduanas base | Decreto N° 4.944 (24-04-2024) | — | [1][2][27] | G.O. N° 6.804 Ext., 25-04-2024 |
| Subpartida SA aplicable | 8703.40 (HEV gasolina no enchufable) | — | [22][23] (nomenclatura SA; confirmar en [1]) | SA 2022 |
| Código nacional de 10 dígitos | [NO VERIFICADO] | — | resolverlo con [1][4][10] | — |
| Arancel (AEC) gasolina > 2.100 cm³ tras el Decreto 5.103 | 40 % (antes 20 %) [BUFETE/GESTOR] | — | [7] ([8] dice > 1.500 cc) | Decreto 5.103, G.O. N° 6.890 Ext., 06-03-2025 |
| Arancel (AEC) aplicable a la 8703.40 de 2.393 cm³ | [NO VERIFICADO] (estimación) | 20 % / 40 % / 40 % | inferido de [7][8] | — |
| Licencia previa (Régimen Legal 20) para 29 subpartidas de vehículos y autopartes | Sí, para las subpartidas listadas; **no sé si incluye la 8703.40** | — | [10] | Res. 022-2025, G.O. N° 43.166, 09-07-2025 |
| Antigüedad máxima | 5 años [BUFETE/GESTOR] | — | [7][8] | Decreto 5.103 (06-03-2025) |
| Partida 98.08 (CBU) | Eliminada | — | [11] | Decreto 5.147, G.O. N° 6.918 Ext., 30-06-2025 |
| Exoneraciones aduaneras generales vigentes | Hasta el 31-12-2026; **sin cobertura conocida para este vehículo** | — | [14][15][16] | G.O. N° 6.952 Ext. (31-12-2025) |
| Beneficio para híbridos o eléctricos | No encontrado [NO VERIFICADO] | — | [19][6] | — |
| Reforma más reciente del Arancel | Res. 007-2026 (ago-2026), contenido [NO VERIFICADO] | — | [14][18] | ago-2026 |
| Tasa por determinación del régimen aduanero | [NO VERIFICADO] (supuesto de trabajo) | 1 % / 1 % / 2 % | — (LOA) | — |
| IVA, alícuota general | [NO VERIFICADO] (supuesto de trabajo) | 16 % | — (Ley IVA) | — |
| IVA adicional suntuario | [NO VERIFICADO] (supuesto de trabajo) | 0 % (bajo el umbral) / 15 % / 15 % | — (Ley IVA) | — |
| IGTF | [NO VERIFICADO] (supuesto de trabajo) | 0 % (tributos pagados en Bs) / 0 % / 3 % sobre los tributos | — (Ley IGTF) | — |
| Tasa oficial BCV | [NO VERIFICADO] (bcv.org.ve bloqueado) | — | — | — |

**Fórmulas** (supuesto: el IVA y el IVA adicional se calculan sobre la misma base):
- Arancel = CIF × a
- Tasa aduanera = CIF × t
- Base IVA = CIF + Arancel + Tasa
- IVA general = Base IVA × g
- IVA adicional de lujo = Base IVA × s
- IGTF = (total de tributos pagados en divisas) × i, solo si aplica
- **Carga total (% del CIF) = a + t + (1 + a + t) × (g + s)**, más IGTF si aplica. El porcentaje no depende del CIF salvo por el umbral de lujo.

**Escenarios** (supuestos de trabajo t = 1 %, g = 16 %; arancel a y lujo s según el escenario):

| Escenario | a | s | Carga % CIF | CIF 70.000: Arancel / Tasa / IVA / Lujo / **Total tributos** / CIF + tributos | CIF 75.000: Arancel / Tasa / IVA / Lujo / **Total tributos** / CIF + tributos |
|---|---|---|---|---|---|
| **A, planificación** (40 % + lujo) | 40 % | 15 % | **84,7 %** | 28.000 / 700 / 15.792 / 14.805 / **59.297** / 129.297 | 30.000 / 750 / 16.920 / 15.862,50 / **63.532,50** / 138.532,50 |
| B (40 %, sin lujo) | 40 % | 0 % | **63,6 %** | 28.000 / 700 / 15.792 / 0 / **44.492** / 114.492 | 30.000 / 750 / 16.920 / 0 / **47.670** / 122.670 |
| C (20 % + lujo) | 20 % | 15 % | **58,5 %** | 14.000 / 700 / 13.552 / 12.705 / **40.957** / 110.957 | 15.000 / 750 / 14.520 / 13.612,50 / **43.882,50** / 118.882,50 |
| **D, mínimo** (20 %, sin lujo) | 20 % | 0 % | **40,4 %** | 14.000 / 700 / 13.552 / 0 / **28.252** / 98.252 | 15.000 / 750 / 14.520 / 0 / **30.270** / 105.270 |
| **Máx.** (A con t = 2 % e IGTF 3 % sobre tributos) | 40 % | 15 % | **88,6 %** | total con IGTF ≈ 62.020 / ≈ 132.020 | total con IGTF ≈ 66.450 / ≈ 141.450 |
| Referencia: arancel 0 %, sin lujo | 0 % | 0 % | 17,2 % | 0 / 700 / 11.312 / 0 / **12.012** / 82.012 | 0 / 750 / 12.120 / 0 / **12.870** / 87.870 |

**Por titular** (mismos supuestos):

| Titular | Carga tributaria de aduana | Carga efectiva si se admitiera el crédito del IVA general (16 %) | Comentario |
|---|---|---|---|
| Persona natural | A 84,7 % · B 63,6 % · C 58,5 % · D 40,4 % | No aplica: un consumidor final no recupera el IVA | Opción más simple |
| La C.A. venezolana | Igual: A 84,7 % · B 63,6 % · C 58,5 % · D 40,4 % | A ≈ 62,2 % · B ≈ 41,0 % · C ≈ 39,2 % · D ≈ 21,0 % (resta (1 + a + t) × 16 %) | **Improbable** con uso personal. Además: posible rechazo en fiscalización, crédito sin aprovechar por falta de ventas y riesgo de ISLR y dividendo encubierto. Tampoco sé si el IVA de lujo se acredita |

*Ninguno de estos importes incluye flete interno, almacenaje, servicios portuarios ni honorarios del agente de aduanas, que llevan otros agentes.*

## Riesgos detectados
1. **Tarifa de la 8703.40 sin confirmar.** La diferencia entre 20 % y 40 % de arancel, arrastrada por el IVA, equivale a unos **26 puntos del CIF**: alrededor de USD 18.300 con un CIF de 70.000 y USD 19.700 con uno de 75.000.
2. **Presupuesto inviable con los supuestos actuales.** Aun en el escenario mínimo D, el costo antes de logística local es de USD 98.000–105.000. Con arancel 0 %, solo el IVA lo deja en USD 82.000–88.000. El presupuesto de USD 80.000 todo incluido **no se cumple** salvo que exista una exoneración que no encontré. Depende de confirmar el IVA, que está [NO VERIFICADO].
3. **Licencia previa (Régimen Legal 20)** si la 8703.40 está entre las 29 subpartidas de la Res. 022-2025 [10]. Podría impedir la importación a una persona natural o a una C.A. sin registro. **Riesgo de alcance pendiente.**
4. **Resolución 007-2026** (agosto de 2026) con contenido desconocido: podría haber cambiado tarifas o regímenes del Capítulo 87.
5. **Normativa muy cambiante:** al menos 11 reformas del Arancel entre abril de 2024 y agosto de 2026. La tarifa que se aplica es la vigente en la fecha que fije la LOA (registro de la declaración o llegada). Si el vehículo llega en 2027, el decreto de exoneraciones que vence el 31-12-2026 ya no regirá.
6. **Reclasificación** a 8703.23, o rechazo de la condición de híbrido, si la documentación técnica no es clara.
7. **Ajuste del valor** por la aduana si la factura queda por debajo de los precios de referencia o del precio público; hay que comprobar si existen listas del SENIAT.
8. **La C.A.:** registro de importador incompleto, que impide nacionalizar a su nombre; rechazo del crédito fiscal de IVA y de la depreciación; posible dividendo encubierto; IVA e ISLR adicionales si luego transfiere el vehículo al accionista.
9. **Tipo de cambio:** los tributos se liquidan en Bs [NO VERIFICADO]. Una devaluación entre la liquidación y el pago, o diferencias entre tasas, alteran el costo en USD.
10. **Verificación limitada:** ningún dato de este archivo se leyó en la fuente primaria. Todo sale de resúmenes del buscador o de fuentes secundarias.

## Preguntas abiertas
1. ¿Cuál es el código nacional de 10 dígitos y la tarifa de la 8703.40 para un motor de 2.393 cm³ en el art. 37 del Decreto 4.944, con las modificaciones del Decreto 5.103, la Res. 022-2025 y la Res. 007-2026? Lo resuelve el texto de esas Gacetas.
2. ¿Está alguna subpartida 8703.40 en el Régimen Legal 20 (Res. 022-2025, G.O. 43.166)? ¿Qué ministerio emite la licencia y puede pedirla una persona natural?
3. ¿Qué cambió exactamente la Res. 007-2026 (agosto de 2026)? ¿En qué Gaceta se publicó?
4. IVA: alícuota general vigente, alícuota adicional de lujo, umbral del vehículo (unidad y base de medición) y decreto o Gaceta. ¿Hubo reformas de la Ley de IVA en 2025–2026?
5. Tasa por determinación del régimen aduanero: porcentaje, base y artículo de la LOA vigente.
6. IGTF: alícuota vigente en 2026 y si aplica al pago de tributos de aduana en divisas o a los honorarios del agente.
7. ¿Se pueden pagar los tributos de aduana en divisas? ¿A qué fecha se toma la tasa BCV? ¿Cuál es la tasa BCV de noviembre de 2026?
8. ¿Puede una persona natural con RIF ser consignataria de una importación única sin estar inscrita como importador? ¿Es obligatorio el agente de aduanas?
9. ¿Publica el SENIAT valores de referencia para vehículos nuevos?
10. ¿Cubre el decreto de exoneraciones de la G.O. 6.952 Ext. (5.196 o 5.197) alguna subpartida de vehículos de pasajeros? ¿Hay algún beneficio para híbridos fuera del Arancel, por ejemplo en leyes ambientales o de transición energética?
11. Ley de IVA: ¿la alícuota adicional de lujo da derecho a crédito fiscal? ¿Qué artículo impide deducir los créditos de bienes ajenos a la actividad?
12. Impuesto a los grandes patrimonios: umbral vigente en 2026 y si alcanza al cliente o a la C.A.

**Para el orquestador:** las preguntas 1 a 7 necesitan una ronda nueva con más cupo de búsquedas, o que se permitan en la red de la sesión los dominios seniat.gob.ve, tradex.com.ve, traviesoevans.com, bcv.org.ve, pwc.com, kpmg.com y lega.law.

## Fuentes (lista numerada: título — URL — fecha de la fuente — consultada 2026-11-18 — tipo: primaria/secundaria/prensa/foro)
*Todas se consultaron el 2026-11-18 **a través de los resúmenes del buscador**. No se abrió ninguna URL directamente porque los dominios estaban bloqueados en la sesión.*

1. Gaceta Oficial N° 6.804 Extraordinario (Decreto N° 4.944, Arancel de Aduanas), copia alojada por Travieso Evans — https://www.traviesoevans.com/travieso/wp-content/uploads/gacetas/2024/04-abril/2024-04-25-6804-extraordinario.pdf — 25-04-2024 — consultada 2026-11-18 — primaria (copia de la G.O.; no leída directamente)
2. FEDEAGRO, "Se dicta el Arancel de Aduanas" — https://fedeagro.org/se-dicta-el-arancel-de-aduanas/ — 2024 — consultada 2026-11-18 — secundaria
3. Stanzione, "Actualización en el Arancel de Aduanas en Venezuela a partir del pasado 25 de mayo de 2024" — https://stanzione.com/actualizacion-en-el-arancel-de-aduanas-en-venezuela-a-partir-del-pasado-25-de-mayo-de-2024/ — 2024 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
4. Gaceta Oficial N° 6.890 Extraordinario (Decreto N° 5.103), copias de KPMG y Travieso Evans — https://assets.kpmg.com/content/dam/kpmg/ve/pdf/2025/3/g.e_6.890.pdf ; https://traviesoevans.com/travieso/wp-content/uploads/gacetas/2025/03-marzo/2025-03-06-6890-extraordinario.pdf — 06-03-2025 — consultada 2026-11-18 — primaria (copia; no leída directamente)
5. Legis, "Reforma Parcial del Arancel de Aduanas" — https://www.legis.com.ve/BancoConocimiento/N/nota_20-03-2025-01/nota_20-03-2025-01.asp?Miga=1&CodSeccion=25 — 20-03-2025 — consultada 2026-11-18 — secundaria
6. PwC Venezuela, "Decreto N° 5.103, que modifica parcialmente el Decreto N° 4.944" (Exoneraciones IVA e Impuestos de Importación FY25) — https://www.pwc.com/ve/es/assets/documentos/stl/NAC-Exoneraciones-IVA-e-Impuestos-de-Importacion-FY25-Rev-AAP-1.pdf — 2025 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
7. Continental Suppliers, "SENIAT autoriza importación de vehículos nuevos y usados" — https://continentalsuppliers.com/seniat-autoriza-importacion-de-vehiculos-nuevos-y-usados/ — s/f (posterior a mar-2025) — consultada 2026-11-18 — secundaria [BUFETE/GESTOR] (empresa importadora)
8. AB Group Shipping, "Calculadora envío carro a Venezuela 2026" — https://www.abgroupshipping.com/blogs/es/calculadora-envio-carro-a-venezuela-2026-desde-1-450 — 2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR] (naviera)
9. Decreto N° 5.122 / Gaceta Oficial N° 43.111 — https://vlexvenezuela.com/vid/decreto-n-5-122-1080119490 ; https://www.bancaynegocios.com/wp-content/uploads/2025/05/GO-43.111-2-4.pdf — 21-04-2025 — consultada 2026-11-18 — primaria (copia; no leída)
10. Resolución N° 022-2025, G.O. N° 43.166: Badell & Grau — https://badellgrau.com/gaceta-oficial-n-o-43-166-del-09-de-julio-de-2025/ ; Ámbito Aduanero (X) — https://x.com/ambitoaduanero/status/1945213683782893594 ; Finanzas Digital — https://finanzasdigital.com/regimen-legal-20-importacion-vehiculos-venezuela-2025/ y https://finanzasdigital.com/resolucion-gaceta-oficial-43-166-importacion-vehiculos-venezuela/ ; Fedecámaras Radio — https://fedecamarasradio.com/gobierno-ajusta-aranceles-de-importacion-para-vehiculos-y-autopartes-en-gaceta-oficial-n-43-166/ ; Sumarium — https://sumarium.info/2025/07/15/gobierno-venezolano-refuerza-control-de-comercio-exterior-sobre-vehiculos-y-autopartes-con-nueva-resolucion/ — 09/15-07-2025 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR] y [PRENSA] (resumen de una fuente primaria)
11. LEĜA Abogados, "Reforma del Arancel de Aduanas de fecha 30 de junio de 2025" (Decreto 5.147, G.O. 6.918 Ext.) — https://lega.law/reform-of-the-customs-tariff-dated-june-30-2025/ — 2025 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
12. Legis, "Reforman parcialmente el decreto que establece el Arancel de Aduanas" — https://www.legis.com.ve/BancoConocimiento/N/nota_27-08-2025-07/nota_27-08-2025-07.asp?Miga=1&CodSeccion=25 — 27-08-2025 — consultada 2026-11-18 — secundaria. 12b. Legis, "Dictan decreto que reforma el Arancel de Aduanas" — https://www.legis.com.ve/BancoConocimiento/N/nota_13-05-2025-n2/nota_13-05-2025-n2.asp?Miga=1&CodSeccion=25 — 13-05-2025 — secundaria
13. Baker McKenzie, "Venezuela: Nueva reforma parcial del Arancel de Aduanas" (Decreto 5.198) — https://www.bakermckenzie.com/en/insight/publications/2026/01/venezuela-new-partial-amendment-to-the-customs-tariff-schedule (PDF en español: https://www.bakermckenzie.com/-/media/files/insight/publications/2026/01/venezuela-new-partial-amendment-to-the-customs-tariff-schedule/venezuela-new-partial-amendment-to-the-customs-tariff-schedule-spanish.pdf) — ene-2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
14. Tradex, "Normativa Arancelaria / Exoneración de Gravámenes y Tributos" y "SUMARIO – Reforma Arancel de Aduanas – Decreto de Exoneración G.O. 6.952" — https://www.tradex.com.ve/normativa-arancelaria/ ; https://www.tradex.com.ve/wp-content/uploads/Tradex-Reforma-Arancel-de-Aduanas-Decreto-de-Exoneracion-GO.-6.952.pdf — 2025–2026 (actualizada a ago-2026) — consultada 2026-11-18 — secundaria [BUFETE/GESTOR] (recopila Gacetas)
15. Acceso a la Justicia, "Suspensión de la aplicación de las exenciones a la importación previstas en el Decreto-Ley que establece el IVA" y "Exoneraciones de Impuestos de Importación e IVA a la importación" — https://accesoalajusticia.org/suspension-de-la-aplicacion-de-las-exenciones-a-la-importacion/ ; https://accesoalajusticia.org/exoneraciones-de-impuestos-de-importacion-e-impuesto-al-valor-agregado-a-la-importacion/ — 2025–2026 — consultada 2026-11-18 — secundaria (ONG jurídica)
16. LEĜA, "Exoneraciones en materia aduanera vigentes hasta el 31 de diciembre de 2026" — https://lega.law/en/exoneraciones-en-materia-aduanera-vigentes-hasta-el-31-de-diciembre-de-2026/ — ene-2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
17. Tinoco, Travieso, Planchart & Núñez, "Decreto Nro. 5.376…" (G.O. 43.409) — https://ttpn.com.ve/?p=5604 — jul-2026 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
18. Ámbito Aduanero, "Arancel de Aduanas de Venezuela único instrumento legal que contempla restricciones a las operaciones aduaneras" (y aviso de la Resolución N° 007-2026) — https://www.ambitoaduanero.com/home-mainmenu-1/21-jurisprudenciassecciona/87-aranceladuanasvenezuela — s/f — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
19. Holland & Knight, "Venezuela decreta exoneraciones afectando los impuestos de importación" (2023) y "Venezuela extiende exoneración del IVA a la importación" (2024) — https://www.hklaw.com/-/media/files/insights/publications/2023/07/venezueladecreeprovidesexemptionsaffectingimporttaxeses.pdf ; https://www.hklaw.com/-/media/files/insights/publications/2024/09/venezuelaextendsvatexemptiones.pdf — jul-2023 / sep-2024 — consultada 2026-11-18 — secundaria [BUFETE/GESTOR]
20. Acceso a la Justicia, "Requisitos para la importación de vehículos bajo régimen de equipaje" e "Importación de vehículo usado bajo régimen aduanero especial de equipaje"; Legiscomex, "Régimen de equipaje de pasajeros" — https://accesoalajusticia.org/requisitos-para-la-importacion-de-vehiculos-bajo-regimen-de-equipaje/ ; https://accesoalajusticia.org/importacion-de-vehiculo-usado-bajo-regimen-aduanero-especial-de-equipaje/ ; https://www.legiscomex.com/BancoMedios/Documentos%20PDF/régimen%20de%20equipaje%20de%20pasajeros.pdf — s/f — consultada 2026-11-18 — secundaria
21. Tribunal Superior Contencioso Tributario / TSJ-SPA, sentencia de 2014 sobre importación de vehículos nuevos (vLex) — https://vlexvenezuela.com/vid/tribunal-superior-contencioso-tributario-593348022 — 02-07-2014 — consultada 2026-11-18 — primaria (jurisprudencia; norma posiblemente derogada)
22. MINCIT Colombia, proyecto de decreto sobre vehículos híbridos (análisis de la 8703.40) — https://abcrepecev.com/hubfs/21-04-21-pd-vehiculos-hibridos.pdf — abr-2021 — consultada 2026-11-18 — secundaria (referencia comparada de nomenclatura). Complemento: Studocu (UCV Perú), "Clasificación de vehículos híbridos y eléctricos – 8703" — https://www.studocu.com/pe/document/universidad-cesar-vallejo/nomenclatura-arancelaria-y-valoracion-aduanera/vehiculo-hibrido-y-electricos/95358829 — s/f — [FORO/REDES]
23. Ministerio de Hacienda de Costa Rica, Resolución MH-DGA-RES-0535-2024 (clasificación de híbridos en la 8703.40) — https://www.hacienda.go.cr/docs/MH-DGA-RES-0535-2024.pdf — 2024 — consultada 2026-11-18 — secundaria (referencia comparada)
24. Easyship, "Calculadora de aranceles e impuestos – Venezuela" (método CIF) — https://www.easyship.com/es-es/duties-and-taxes-calculator/venezuela — s/f — consultada 2026-11-18 — secundaria comercial
25. Somerset Escargot, "Nuevas tasas de importación en Venezuela 2026…" — https://somersetescargot.co.uk/nuevas-tasas-de-importacion-en-venezuela-2026-cambios-en-aranceles-aduaneros-desde-marzo/ — 2026 — consultada 2026-11-18 — [FORO/REDES] (**poco fiable; no se usó para ninguna cifra**)
26. Times Brasil, "Venezuela quer elevar tarifa sobre carros brasileiros" (ACE 69) — https://timesbrasil.com.br/brasil/venezuela-quer-elevar-tarifa-sobre-carros-brasileiros/ — 2025 — consultada 2026-11-18 — [PRENSA] (contexto; no aplica a la 4Runner)
27. Pandectas Digital, "Arancel de Aduanas [Vigente]" — https://pandectasdigital.blogspot.com/2024/04/arancel-de-aduanas.html — abr-2024 — consultada 2026-11-18 — secundaria [FORO/REDES]
