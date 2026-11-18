# Agente 2 — Exportación desde EE. UU. y sanciones
**Fecha de investigación:** 2026-11-18

> **Estado de alcance:** NO se encontró ninguna 🛑 ALERTA DE ALCANCE. Ninguna fuente consultada prohíbe exportar un vehículo de pasajeros de uso civil (presumiblemente EAR99) a una persona natural o empresa privada venezolana no sancionada.
>
> **(ronda 2)** Esta conclusión se refuerza:
> - En el texto de 15 CFR 744.21 que muestra el eCFR, Venezuela está en el inciso (a)(1). Ese inciso solo alcanza a los artículos del Supl. 2 a la Parte 744; la regla de "cualquier artículo sujeto al EAR" del inciso (a)(2) solo aplica a Rusia y Bielorrusia [27][28].
> - La regla del 23-jul-2026 (91 FR 46252–, que incluye la página 46260) modifica §742.6 (estabilidad regional). Esos controles dependen de la CCL y no pueden alcanzar artículos EAR99 [30].
> - La frase de New Hampshire de que exportar vehículos nuevos está "prohibido" viene de un comunicado federal de 2013 sobre un **fraude**. No existe tal prohibición de CBP (ver K) [41].
>
> **Limitación metodológica (léala el verificador):** en esta sesión no se pudo abrir directamente ninguna página primaria. WebFetch y curl dieron error de red con ofac.treasury.gov, ecfr.gov y law.cornell.edu, y el proxy rechazó también cbp.gov, census.gov, bis.gov, federalregister.gov, irs.gov y govinfo.gov. Además se agotó el cupo de búsquedas compartido por los 8 agentes (200). Lo marcado como "verificado" se apoya en **extractos de las páginas primarias que devolvió el buscador** (URL citada), no en una lectura íntegra del texto. Todo lo demás lleva [NO VERIFICADO]. Para cerrar esos puntos hay que habilitar esos dominios en la red de la sesión o pedir una nueva ronda de búsquedas.

## Resumen ejecutivo (5 líneas)
1. Exportar la 4Runner es **legal sin licencia** si el destinatario es una persona o empresa privada venezolana que no está bloqueada ni pertenece al Gobierno de Venezuela [7][8][9][24]. **(ronda 2)** Para Venezuela, §744.21 solo cubre los artículos del Supl. 2 a la Parte 744, donde no se encontró ninguna entrada de turismos (8703). La lista MEU de Venezuela figura como "[Reserved]". No se encontró ninguna regla de BIS de 2026 que cambie esto [27][28][30].
2. Las sanciones OFAC siguen vigentes en nov-2026, suavizadas por licencias generales; la EO 13884 **no se ha revocado** y no hay embargo al sector privado [20][21][38]. **(ronda 2)** Para pagos incidentales al Gobierno de Venezuela existen dos licencias. La **GL 35** (5-nov-2019) cubre impuestos, tasas, aranceles y permisos ligados a operaciones del día a día; sigue publicada y no se le encontró revocación [31][32]. La **GL 30B** (10-feb-2026) cubre tasas portuarias y aranceles aduaneros e incluye a entidades del gobierno bloqueadas solo por la EO 13884 [33][34][38].
3. Ojo: un vehículo **nuevo** comprado en un concesionario por un comprador final (la LLC o el cliente) **cuenta como "usado"** para CBP y Census [1][2][5][6]. Esto exige entregar el MSO original (o el título) más 2 copias y presentar la EEI en AES al menos **72 h antes** de la exportación, sin importar valor ni destino. CBP no cobra tasa [2][3][4].
4. Schedule B: 8703.40 (híbrido no enchufable de gasolina). Si la exporta la LLC o el cliente, la línea es la **8703.40.0045 ("Used", 1.500–3.000 cc)**. La 8703.40.0020 ("New", ≤4 cilindros) solo aplicaría si el concesionario o un exportador-dealer la exporta sin haberla vendido antes a un comprador final [10][11].
5. El riesgo legal principal está en **los pagos y en las declaraciones al concesionario**. Lo recomendable es que paguen SENIAT y Bolipuertos el importador local en Venezuela. Si pagara la LLC, la cubren las GL 30B y 35, pero debe reportar a OFAC los pagos en USD [31]. **(ronda 2)** Nunca hay que firmar una declaración falsa de "no exportación": eso fue lo que llevó a la condena por fraude en el caso de New Hampshire [41]. Formulario 5472: pendiente con el contador [NO VERIFICADO].

## Hallazgos detallados

### A. CBP — 19 CFR 192: un vehículo nuevo vendido al comprador final cuenta como "usado"
- **Definiciones (verificado por extracto):** según 19 CFR 192.1, *"Used" refers to any self-propelled vehicle the equitable or legal title to which has been transferred by a manufacturer, distributor, or dealer to an ultimate purchaser*. El mismo artículo define *"Ultimate purchaser" means the first person, other than a dealer purchasing in his capacity as a dealer, who in good faith purchases a self-propelled vehicle for purposes other than resale* [1].
  - **Consecuencia:** si la LLC o el cliente compran la 4Runner para uso propio, se convierten en "ultimate purchaser" y la camioneta es "used" a efectos de exportación, aunque tenga 0 millas. Census lo confirma: un vehículo comprado "nuevo" en un concesionario debe declararse como "used" [6]. El estado físico o el kilometraje no importan (resolución CBP H235018) [1].
  - **Excepción relevante para la opción (c):** CBP resolvió que vehículos que solo pasaron de un dealer a otro, sin comprador final, **no** son "used" (H204515) [1]. Si un exportador "llave en mano" con licencia de dealer compra para revender al cliente en Venezuela, el vehículo podría salir como "nuevo". En ese caso no aplican el régimen de 72 h del 19 CFR 192 ni los datos de vehículo usado en la EEI, pero la EEI sigue siendo obligatoria por valor (ver B). Aplicarlo al caso concreto exige consultar a CBP o a un abogado [NO VERIFICADO para este caso].
- **Documentos (verificado por extracto de 19 CFR 192.2 y de la guía CBP) [2][3]:**
  - Si el vehículo **nunca se tituló** en EE. UU. (solo tiene MSO/MCO): **MSO original + 2 copias completas**.
  - Si el concesionario ya lo tituló a nombre del comprador: **título original (o copia certificada) + 2 copias**.
  - Por buque: documentos **y vehículo** se presentan a CBP en el puerto **al menos 72 h antes** de la exportación.
  - CBP **no puede eximir** del MSO original salvo en tránsito *in-bond*, carné ATA o TIB (resolución CBP 116070, 2003) [4].
  - Junto con los documentos de propiedad se entrega el ITN (número de transacción interna de AES) [2].
- **Tasa de CBP:** la propia CBP indica que no cobra tasa por procesar vehículos para exportación [3].
- **DIS (presentación electrónica de imágenes):** existe un piloto de CBP para enviar el título o MSO por el *Document Image System* en lugar de originales en papel. Se publicó en 2022 [26] y se **renovó por aviso en el Federal Register del 6-nov-2026 (doc. 2026-22728)** [25]. El aviso aclara que el piloto **no cambia los plazos** [25]. Qué puertos participan (p. ej., los del sur de Florida) [NO VERIFICADO; se resuelve en el aviso 2026-22728 o con el puerto de salida].
- **Qué debe acreditar el exportador ante CBP y el forwarder:**
  - Propietario que figura en el MSO o título: la LLC (EIN y documentos de constitución) o el cliente (pasaporte).
  - Autorización escrita o poder al forwarder para presentar la EEI (15 CFR 30.3) [NO VERIFICADO: texto exacto de 30.3(e)–(f)].
  - Si hay financiamiento: carta del acreedor prendario [NO VERIFICADO; con compra al contado no aplica].
  - Factura del concesionario.
- **Riesgo práctico de plazo:** si el concesionario titula el vehículo en el estado (algunos estados lo exigen al vender), hay que **esperar el título físico** para poder exportar. Esto puede añadir semanas [NO VERIFICADO: depende del estado; Agente de logística o forwarder].

### B. EEI vía AES — 15 CFR 30 (Foreign Trade Regulations)
- **Obligación (verificado por extracto):**
  - Regla general: la EEI es obligatoria cuando el valor por Schedule B supera **USD 2.500** [5].
  - Para **vehículos autopropulsados usados** (definidos en 19 CFR 192.1) es obligatoria **sin importar el valor**: 15 CFR 30.2(a)(1)(iv)(H) [5]. El CFR de 2025 añade "sin importar el destino". Census dijo en la regla de 2013 que "no habrá exenciones" [5][6].
  - Una 4Runner Trailhunter (> USD 2.500) exige EEI en cualquier caso, sea "nueva" o "usada".
- **Plazo (verificado por extracto):**
  - Para vehículos usados, el USPPI o su agente presenta la EEI y entrega la *filing citation* (ITN) a CBP **al menos 72 h antes** de la exportación.
  - La versión del FTR con la regla de agosto de 2025 añade que también hay que entregarla al transportista [5][7b].
  - **No se permite presentarla después de la salida** [5].
  - Ojo: la numeración de los subpárrafos de 30.4 cambia entre versiones; hay que citarlos contra el eCFR vigente [NO VERIFICADO: subpárrafo exacto].
- **Datos del vehículo (verificado por extracto de 15 CFR 30.6 y blog de Census 2021):**
  - VIN (o Product ID) con su calificador V/P, número de título y estado del título (código postal de 2 letras).
  - Si los códigos Schedule B aparecen en **negrita** en el Apéndice U, esos campos son obligatorios y AESDirect no deja enviar sin ellos.
  - Census recomienda poner año, marca y modelo en la descripción [6].
  - Si el vehículo no tiene título (solo MSO), cómo se rellenan los campos de título [NO VERIFICADO; lo resuelve el Apéndice U del AESTIR o el Census Data Collection Branch].
- **Otros datos de la EEI (estructura general; citas exactas [NO VERIFICADO]):**
  - USPPI con su identificación (EIN de la LLC; si el USPPI es extranjero, tipo de ID extranjero o pasaporte [NO VERIFICADO]).
  - Consignatario último (nombre y dirección en Venezuela) y país de destino VE.
  - Indicador de parte relacionada: "sí" si la LLC exporta a su propio dueño o a la C.A. del mismo dueño [NO VERIFICADO].
  - Schedule B a 10 dígitos, valor, peso, puerto de salida y modo de transporte.
  - Código de licencia "NLR" con ECCN "EAR99" [NO VERIFICADO: código AES exacto, p. ej. C33].
- **Quién presenta:** el USPPI o su agente autorizado (forwarder) [5]. AESDirect (ACE) es gratuito para quien presenta por su cuenta [NO VERIFICADO]. En la práctica la presenta el forwarder.
- **Costo típico por forwarder:** **ESTIMACIÓN sin fuente verificada**: USD 25–150 por EEI (probable ~USD 50–75). A menudo va incluida en una tarifa de "documentación/validación de título" de USD 100–300. Hay que pedir cotizaciones escritas (Agente de logística).

### C. Número Schedule B
- **Heading:** 8703.40 cubre vehículos con motor de émbolo de encendido por chispa **y** motor eléctrico para la propulsión, **excepto los que se pueden cargar enchufándolos** a una fuente externa (verificado por extracto de Census, Schedule B cap. 87) [10]. La 4Runner i-FORCE MAX es un híbrido **no enchufable**, así que va en **8703.40**, no en 8703.60 (enchufables). El motor es de 2,4 L (≈2.393 cc), en el tramo **>1.500 cc ≤3.000 cc**; que tenga 4 cilindros hay que confirmarlo en la ficha técnica de Toyota (otro frente) [NO VERIFICADO aquí].
- **Líneas a 10 dígitos (verificado por extracto del PDF de Census Schedule B 2026, cap. 87) [10]:**
  - **8703.40.0020** — "New", motores de **no más de 4 cilindros** (tramo 1.500–3.000 cc).
  - **8703.40.0045** — **"Used"**, mismo tramo.
  - La nota del capítulo indica que se declara como "used" el vehículo cuyo título ya se transfirió de un fabricante, distribuidor o dealer a un comprador final [10].
  - El índice de Schedule B 2026 indica que esos códigos se aplican a partir del 1-jul-2026 [11]. El PDF de 2024 usaba los mismos códigos; el de 2021 tenía otra numeración (usado = 8703.40.0090) [10].
- **Aplicación al caso:**
  - Opciones (a) LLC y (b) cliente → **8703.40.0045 (Used)**.
  - Opción (c), si la exporta un dealer o exportador sin venta previa a un comprador final en EE. UU. → posiblemente **8703.40.0020 (New)** [ver A; NO VERIFICADO para el caso concreto].
  - Pendiente: confirmar que 8703.40.0045 figura en **negrita** en el Apéndice U (campos de vehículo obligatorios) [NO VERIFICADO].

### D. Controles de exportación (EAR/BIS)
- **Clasificación:** un automóvil de pasajeros civil, no blindado ni diseñado especialmente para uso militar, es **probablemente EAR99**: está sujeto al EAR pero no figura en la Commerce Control List. **[NO VERIFICADO en esta sesión]**: no se pudo consultar la CCL (Supl. 1 a la Parte 774) para descartar entradas como 0A606 (vehículos terrestres militares) o 9A991. Lo resuelve la lectura de 15 CFR 774 Supl. 1 o una autoclasificación del forwarder o abogado.
- **Estatus de Venezuela en el EAR (verificado por extracto de páginas de bis.gov y del Federal Register):**
  - **79 FR 66288 (2014):** aplica a Venezuela los requisitos de licencia por uso o usuario final militar [7].
  - **84 FR 24018 (2019):** saca a Venezuela del Grupo de Países B y la pasa al **D:1**, además de añadirla a **D:2–D:4** [8].
  - **85 FR 23459 (28-abr-2020, doc. 2020-07241):** amplía los controles de uso o usuario final militar para China, Rusia y **Venezuela** [9].
  - [BUFETE/BLOG] Bass, Berry & Sims: desde 2019 Venezuela está sujeta a controles reforzados de seguridad nacional y "muchos artículos comerciales" requieren licencia [23]. Esto se refiere a artículos de la CCL, no a EAR99 [interpretación; NO VERIFICADO].
- **¿Hace falta licencia para un artículo EAR99 a un particular venezolano?**
  - Según la estructura del EAR, un EAR99 a un destino que no está embargado (Venezuela no figura en la Parte 746 [NO VERIFICADO]) **no requiere licencia (NLR)**, salvo prohibiciones de la Parte 744: usuario o uso final militar (§744.21), usuario final militar-inteligencia (§744.22), Entity List (§744.11) u otras listas, y actividades de personas estadounidenses (§744.6).
  - [BUFETE/BLOG] Un resumen profesional coincide: vender a una empresa privada venezolana no bloqueada ni estatal no está prohibido; vender a entidades estatales, PdVSA o SDN requiere licencia [24].
  - **[NO VERIFICADO — crítico]:** si el §744.21 vigente aplica a Venezuela solo para los artículos del Supl. 2 a la Parte 744 o para **"cualquier artículo sujeto al EAR"** (como ocurre con Rusia y Bielorrusia). En ambos casos solo se exige licencia si se **sabe** o hay razón para saber que el usuario o uso final es militar. Para una persona natural o una C.A. privada de uso familiar, eso no aplica, salvo banderas rojas: vínculos de la C.A. o sus socios con la FANB o cuerpos de seguridad. La política de revisión para usuarios militares en Venezuela es presumiblemente de denegación [NO VERIFICADO].
- **Cambios 2025–2026 en el EAR:**
  - La página de la Parte 742 en bis.gov enlaza una enmienda en **91 FR 46260 (23-jul-2026)** en la sección de estabilidad regional. **No se pudo ver su contenido** ni saber si afecta a Venezuela [NO VERIFICADO; lo resuelve el Federal Register 91 FR 46260].
  - La regla del 15-ene-2026 sobre computación avanzada menciona a Venezuela, pero no afecta a vehículos [22].
  - **No se encontró ninguna regla de BIS de 2025–2026 que imponga licencia a vehículos de pasajeros hacia Venezuela ni que la levante** [búsqueda limitada; ver la limitación metodológica].
- **(ronda 2) §744.21 aplicado a Venezuela (verificado por extracto del eCFR y de bis.gov; el extracto del eCFR tiene unos 405 días, ≈oct-2025) [27][28][29]:**
  - El §744.21 vigente tiene dos incisos.
    - **(a)(1):** cubre Birmania, Camboya, China, **Nicaragua y Venezuela**, y se limita a los **artículos listados en el Supl. 2 a la Parte 744**. Fuera de esos países, los usuarios finales militares se limitan a las entidades de la MEU List (Supl. 7).
    - **(a)(2):** exige licencia para **"cualquier artículo sujeto al EAR"**, pero solo con uso o usuario final militar en **Bielorrusia o Rusia** [27].
  - La regla de 2022 sobre Rusia y Bielorrusia (doc. 2022-19910) cambió el (a)(1) a la fórmula "wherever located" ("dondequiera que se encuentren"), pero no amplió el alcance de artículos para Venezuela [29].
  - **Supl. 2 a la Parte 744** ("List of Items Subject to the Military End Use or End User License Requirement of §744.21"): incluye, entre otros, el ECCN **9A991** (aeronaves n.e.s., turbinas de gas y sus partes). La regla de 2020 amplió las entradas de 3A992, 8A992 y 9A991 [9][28]. **No se encontró ninguna entrada para turismos (Schedule B 8703) ni para artículos EAR99** [28]. La versión de bis.gov dice "last updated December 18, 2024" [28].
  - **MEU List (Supl. 7):** la entrada de Venezuela figura como **"[Reserved]"**, es decir, sin entidades venezolanas listadas [27].
  - **Conclusión (ronda 2):** un turismo civil EAR99 **no está alcanzado por el §744.21** para Venezuela. Aunque hubiera un usuario militar, el artículo no está en el Supl. 2 (por lo encontrado) [27][28].
  - Siguen aplicando, para cualquier artículo:
    - §744.22 (usuario final militar-inteligencia) [NO VERIFICADO: texto vigente y entidades venezolanas];
    - la Entity List (§744.11);
    - la prohibición general 10 (no exportar sabiendo que se ha cometido o se cometerá una violación) [NO VERIFICADO].
- **(ronda 2) Contenido de 91 FR 46260 [30]:**
  - 91 FR 46260 es una página dentro de una **regla final provisional publicada el 23-jul-2026, que empieza en 91 FR 46252 (doc. FR 2026-14942)**. La regla modifica §742.6 (estabilidad regional): añade los párrafos (a)(14) y (b)(15) y entra en vigor el **20-nov-2026**. También figura en el historial de la Parte 758.
  - Los extractos mencionan los ECCN 0A509 y 9A980 y una política de revisión de licencias para ciertos productos [NO VERIFICADO: texto exacto].
  - Los controles de §742.6 se aplican a artículos de la CCL con razón de control "RS". **Por definición no alcanzan a artículos EAR99**, así que esta regla **no crea requisitos de licencia para un turismo EAR99**.
  - Qué cambia en la Parte 758 (despacho de exportación) [NO VERIFICADO].
  - Otra regla del 14-jul-2026 (EAU, doc. 2026-14132) y la de computación avanzada no afectan al caso [30].
- **(ronda 2) Sin cambios de BIS para Venezuela en 2026:** una búsqueda específica no encontró ninguna regla de BIS de 2026 que cambie el grupo de países de Venezuela (D:1–D:4 desde 84 FR 24018) ni su política de licencias [8][44].
  - [BUFETE/BLOG] Leech Tishman (mar-2026): las GL de OFAC **no** sustituyen los requisitos del EAR; según la firma, OFAC ha dicho que BIS mantiene la jurisdicción sobre las exportaciones a Venezuela [44].
- **Persona natural vs. C.A. venezolana como consignatario:** para el EAR **no hay diferencia de licencia** mientras ninguna sea usuario final militar o de inteligencia ni esté listada. La diferencia es de diligencia debida: en la C.A. hay que verificar socios, administradores y beneficiarios finales (que no sean funcionarios, militares ni SDN, y que la empresa no sea ≥50% de entidades bloqueadas).

### E. Sanciones OFAC (estado a nov-2026)
- **Marco que sigue vigente:**
  - **EO 13884 (5-ago-2019)** bloquea al Gobierno de Venezuela (GoV) y **no ha sido revocada** [BUFETE/BLOG][20][21].
  - Según asesores, la definición de GoV (sección 6(d)) incluye a quienes actúan o pretenden actuar en su nombre [20].
  - La definición completa incluye subdivisiones políticas, agencias e instrumentos, BCV, PdVSA y entidades controladas por el GoV, según 31 CFR 591.310 [NO VERIFICADO en esta sesión: texto de 31 CFR 591 y EO 13884 §6(d)].
  - Con esa definición, **SENIAT (servicio autónomo del Estado) y Bolipuertos (empresa estatal) entran en "Gobierno de Venezuela"** [inferencia razonable; NO VERIFICADO contra fuente primaria].
- **Novedades 2026 (fechas según las URL y extractos de "recent actions" de OFAC) [12–18]:**
  - **EO 14373 (9-ene-2026):** protege los "Foreign Government Deposit Funds" (ingresos petroleros venezolanos bajo custodia del Tesoro). Solo deroga a las EO anteriores en lo que afecte a esos fondos [BUFETE/BLOG][19][20].
  - **GL 30B (10-feb-2026):** operaciones de **puertos y aeropuertos** [12].
  - **GL 52 (18-mar-2026):** ciertas transacciones con PdVSA [12][16].
  - **GL 57 (14-abr-2026):** ciertos servicios financieros con **bancos venezolanos especificados** y personas del GoV [12].
  - **GL 58 (5-may-2026):** servicios al GoV para una posible reestructuración de deuda [13].
  - **GL 46E, 48D, 49B, 50C, 5W** (petróleo, suministros, inversión) [12].
  - **GL 60A (16-oct-2026)** y FAQ 1263 enmendada: ayuda por terremoto [14].
  - [BUFETE/BLOG] Delcy Rodríguez fue excluida de la SDN el **1-abr-2026**. Desde el **30-sep-2026** OFAC no ha emitido GL con número nuevo para Venezuela. Las GL pueden modificarse o retirarse en cualquier momento [21].
  - El alcance exacto de cada GL **no se pudo leer** [NO VERIFICADO: texto en ofac.treasury.gov].
- **¿Puede una persona estadounidense (la LLC) vender o exportar un vehículo a un particular o empresa privada venezolana?**
  - **Sí.** El programa de Venezuela bloquea al GoV y a las personas designadas; **no es un embargo comercial general** como el de Cuba o Irán [24][BUFETE/BLOG].
  - No se encontró ninguna disposición de 2026 que prohíba exportar bienes de consumo al sector privado.
  - Condición: ni el consignatario, ni el banco receptor, ni ningún intermediario (agente aduanal, naviera, almacén) puede ser una persona bloqueada o del GoV, salvo que lo cubra una GL.
- **Pagos a SENIAT (aranceles e IVA) y a Bolipuertos (tasas portuarias):**
  - Si los paga **el importador en Venezuela** (persona natural o C.A., que no son personas estadounidenses) desde fondos y bancos venezolanos, **sin pasar por personas o bancos de EE. UU.**, la operación queda en principio fuera de la jurisdicción de OFAC [inferencia sobre la jurisdicción de OFAC; NO VERIFICADO contra FAQ].
  - Si la **LLC** pagara directamente a SENIAT o Bolipuertos, o enviara USD a un banco estatal venezolano, eso sería una transacción de una persona estadounidense con el GoV. Necesitaría una autorización:
    - la **GL 30B** cubre operaciones portuarias, aunque su alcance exacto falta verificarlo [12];
    - para impuestos, aranceles, permisos y licencias existía históricamente una GL de "transacciones administrativas" con el GoV (el investigador cree que es la **GL 35**) [NO VERIFICADO: número, vigencia y texto en ofac.treasury.gov];
    - la **GL 57** podría cubrir pagos a través de bancos estatales [NO VERIFICADO].
  - **Recomendación:** la LLC no hace ningún pago en Venezuela. El cliente o la C.A. pagan localmente por medio de su agente aduanal.
- **¿Necesita la LLC una licencia específica de OFAC?** **No**, según lo encontrado, si cumple las condiciones de arriba. Una licencia específica solo haría falta si alguna parte fuera GoV o SDN y no la cubriera una GL.
- **¿Exporta la LLC o el cliente como persona natural?**
  - La **LLC** es persona estadounidense (constituida en EE. UU.): todas sus operaciones quedan sujetas a OFAC.
  - El **cliente** (venezolano no residente) no es persona estadounidense mientras actúe fuera de EE. UU. Sí queda sujeto si actúa dentro de EE. UU. o si **hace que** personas estadounidenses (concesionario, forwarder, banco, naviera) violen las sanciones [principio general; NO VERIFICADO contra 31 CFR 591].
  - En la práctica, el concesionario, el forwarder y los bancos estadounidenses aplican el mismo cribado en ambos casos. El riesgo regulatorio de la operación es **casi igual**; con la LLC, la responsabilidad directa recae en una entidad del cliente.

### F. Listas y diligencia debida
- **PdVSA:** sancionada. Que la GL 52 de 2026 autorice "ciertas transacciones" con PdVSA confirma que sigue bloqueada [12][16]. Es irrelevante para esta operación salvo que algún proveedor sea filial de PdVSA.
- **Bolipuertos:** como empresa estatal entra en la definición de GoV (bloqueado por la EO 13884). **No se pudo verificar** si figura con nombre propio en la SDN List [NO VERIFICADO; lo resuelve una búsqueda en sanctionssearch.ofac.treas.gov]. Las tasas portuarias las paga normalmente la naviera o el agente en destino, y la GL 30B cubre operaciones portuarias [12].
- **CONVIASA:** su designación (que el investigador recuerda de 2020) **no se verificó** en esta sesión [NO VERIFICADO]. No es relevante para transporte marítimo.
- **Navieras, agentes aduanales y almacenes venezolanos:** no se verificó ninguno concreto [NO VERIFICADO].
- **Diligencia recomendada:** antes de contratar y antes de cada pago, cribar a todas las partes en la **SDN List** de OFAC y en la **Consolidated Screening List** de trade.gov (que incluye Entity List, MEU List y otras): concesionario, forwarder, naviera, consignatario (persona natural o C.A.), agente aduanal venezolano, almacén y banco receptor. Guardar evidencia (captura con fecha). En la C.A., además, documentar los beneficiarios finales.

### G. Bancos y pagos
- **[NO VERIFICADO — toda esta sección]:** con el cupo de búsquedas agotado no se encontraron fuentes sobre políticas de bancos concretos ni sobre prácticas de *de-risking* en 2025–2026. Lo que sigue es lógica de cumplimiento, no hechos verificados:
  - Los pagos de la LLC al **concesionario** y a un **forwarder en EE. UU.** son transferencias domésticas de bajo riesgo.
  - Las transferencias que mencionan "Venezuela" o van a bancos venezolanos suelen pasar por filtros OFAC automáticos y pueden quedar retenidas para revisión. Un pago a un banco del GoV sin autorización se bloquearía.
  - Para limitar el riesgo de cierre de cuenta, conviene que **todos los pagos en Venezuela los haga el importador local**, que la LLC solo pague a contrapartes estadounidenses y que el concepto de pago sea claro (compra de vehículo, flete).
  - Pendiente de verificar: avisos de FinCEN sobre Venezuela (el investigador recuerda un aviso de corrupción de 2019) y los efectos de la GL 57 de 2026 sobre bancos venezolanos [NO VERIFICADO].
- **Zelle y cuentas de forwarders en Miami:** sin fuentes [NO VERIFICADO]. Queda como pregunta abierta para el agente de pagos o logística.

### H. Comparación de las tres opciones de comprador o exportador

| Aspecto | (a) La LLC compra y exporta | (b) El cliente (extranjero no residente) | (c) Importador o courier "llave en mano" |
|---|---|---|---|
| ¿"Used" según 19 CFR 192? | Sí (la LLC es *ultimate purchaser*) [1] | Sí [1] | Depende: si un dealer exporta sin vender antes a un comprador final, puede ser "new" [1] [NO VERIFICADO para el caso] |
| Schedule B | 8703.40.0045 [10] | 8703.40.0045 [10] | 8703.40.0045 o 0020 [10] |
| EEI obligatoria | Sí, 72 h antes, con VIN y título [5] | Sí, 72 h antes [5] | Sí (por ser usado o por valor > USD 2.500) [5] |
| USPPI | La LLC (EIN) | El cliente, si compra estando en EE. UU., o el concesionario si es una exportación "routed" [definiciones de 15 CFR 30.1/30.3; NO VERIFICADO] | El exportador o dealer |
| Quién firma | La LLC firma el poder o autorización escrita al forwarder | El cliente firma el poder (pasaporte; posible apostilla o notario) [NO VERIFICADO] | El exportador; el cliente firma su contrato con él |
| Documento de propiedad ante CBP | MSO o título a nombre de la LLC [2] | MSO o título a nombre del cliente [2] | MSO o título a nombre del exportador [2] |
| Exposición OFAC | Directa (la LLC es persona estadounidense) | Indirecta (riesgo de "causar" violaciones) [NO VERIFICADO] | Principalmente del exportador. El cliente depende de que el exportador cumpla |
| Riesgo práctico | Formulario 5472 o distribución al socio (ver I) | Concesionarios reacios a vender a extranjeros o a firmar documentos de exportación; pago desde el exterior [NO VERIFICADO] | Exportadores informales que usan compradores interpuestos ("straw buyers") en contra de las políticas anti-exportación del fabricante [NO VERIFICADO]; riesgo de contraparte |

- **Importador o consignatario en Venezuela:** para el EAR y OFAC **es indiferente** que sea la persona natural o la C.A., siempre que ninguna esté listada, sea del GoV o tenga vínculo militar. El consignatario de la EEI debe coincidir con el del conocimiento de embarque (B/L).

### I. Implicaciones fiscales y de cumplimiento de la LLC (preguntas para el contador)
**No se consultó ninguna fuente del IRS** en esta sesión (irs.gov bloqueado y cupo de búsquedas agotado). Todo lo siguiente es **[NO VERIFICADO]** y se plantea como pregunta para el contador:
1. Si la LLC es unipersonal con dueño extranjero y está tratada como *disregarded entity*, ¿debe presentar el **Formulario 5472** con un 1120 pro forma y declarar como "transacción reportable" la compra del vehículo y su entrega al socio? El investigador recuerda que la regla viene de Treas. Reg. §1.6038A-1, aplicable desde 2017, con una multa base de USD 25.000. Hay que verificarlo en las *Instructions for Form 5472* del IRS.
2. Si la LLC compra un bien de uso personal del socio y lo exporta a su nombre o al de su C.A., ¿se trata como **distribución al socio** o aportación en especie? ¿Cómo se registra?
3. Si la LLC tiene actividad comercial en EE. UU., ¿afecta esto a su sustancia o al tratamiento del vehículo como activo de la empresa? ¿Conviene que el vehículo **no** figure como activo de la LLC?
4. ¿Hay exención del impuesto estatal sobre ventas por exportación según el estado del concesionario? (Frente de costos o logística.)

### J. Sanciones aplicables por incumplimiento
- No verificado: multas del FTR por no presentar la EEI (15 CFR 30.71), sanciones de 19 USC 1627a y 19 CFR 192 (con posible incautación del vehículo; CBP publica incautaciones con multas, p. ej. "17 vehículos y USD 93.500 en multas" [3b]), y sanciones civiles de IEEPA y OFAC [NO VERIFICADO: montos ajustados por inflación en 15 CFR 30.71, 19 CFR 192 y 31 CFR 501, Apéndice A].

## Cifras clave

| Concepto | Valor | Rango mín/prob/máx (si es estimación) | Fuente [n] | Fecha de la fuente |
|---|---|---|---|---|
| Antelación para presentar a CBP los documentos y el vehículo (por buque) | 72 horas antes de la exportación | — (hecho) | [2][3] | CFR vigente (extracto); página CBP s/f |
| Antelación de la EEI para un vehículo usado | ≥72 horas; no se permite después de la salida | — (hecho) | [5][25] | FTR con la regla de ago-2025; FR 6-nov-2026 |
| Umbral general de EEI | > USD 2.500 por Schedule B | — (hecho) | [5] | FTR ago-2025 |
| Umbral de EEI para un vehículo usado | Sin umbral (cualquier valor y destino) | — (hecho) | [5][6] | FTR ago-2025; Census 2013/2021 |
| Copias del MSO o título | Original + 2 copias | — (hecho) | [2] | 19 CFR 192.2 (extracto) |
| Tasa de CBP por procesar la exportación | USD 0 | — (hecho) | [3] | página CBP s/f |
| Schedule B (exporta la LLC o el cliente) | 8703.40.0045 ("Used", 1.500–3.000 cc) | — (hecho; falta confirmar la negrita en el Apéndice U) | [10][11] | Schedule B 2026 (aplicable desde 1-jul-2026) |
| Schedule B (exporta un dealer sin venta previa a comprador final) | 8703.40.0020 ("New", ≤4 cil.) | — | [10] | Schedule B 2026 |
| Licencia BIS para un EAR99 a un particular venezolano | No requerida (NLR) si no hay uso o usuario militar o de inteligencia ni partes listadas | — (análisis; texto de §744.21 [NO VERIFICADO]) | [7][8][9][24] | 2014; 2019; 28-abr-2020 |
| Licencia OFAC para vender o exportar a un privado venezolano no bloqueado | No requerida | — (análisis) | [20][21][24] | ene–oct 2026 |
| Presentación de la EEI por forwarder | ESTIMACIÓN | 25 / 60 / 150 USD [NO VERIFICADO] | — | — |
| Documentación o validación de título del forwarder (incl. la EEI) | ESTIMACIÓN | 100 / 200 / 350 USD [NO VERIFICADO] | — | — |
| Poder notarial o apostilla al forwarder | ESTIMACIÓN | 10 / 50 / 150 USD [NO VERIFICADO] | — | — |
| Opinión legal breve OFAC/EAR (opcional) | ESTIMACIÓN | 0 / 750 / 3.000 USD [NO VERIFICADO] | — | — |
| Preparación anual del 5472 + 1120 pro forma (si aplica) | ESTIMACIÓN | 300 / 600 / 1.500 USD [NO VERIFICADO] | — | — |
| Multa por no presentar el Formulario 5472 | USD 25.000 (según recuerdo del investigador) | — [NO VERIFICADO] | — (verificar en IRS Instr. 5472) | — |
| **Costo total de cumplimiento en EE. UU. (sin flete)** | ESTIMACIÓN = documentación con EEI incluida (100/200/350) + poder (10/50/150) + opinión legal (0/750/3.000) + 5472 si aplica (0/600/1.500) | **~110 / ~1.600 / ~5.000 USD** (la diferencia la marcan la opinión legal y el 5472) [NO VERIFICADO] | — | — |

## Riesgos detectados
1. **Clasificar mal como "nuevo"**: si la LLC o el cliente declaran el vehículo como "new" (8703.40.0020) o no presentan el MSO o título 72 h antes, CBP puede retenerlo o incautarlo y multar [1][2][5]. Gravedad: alta. Probabilidad: media si el forwarder no tiene experiencia.
2. **El concesionario no entrega el MSO original o titula el vehículo en el estado** y retrasa la exportación; además, las políticas anti-exportación del fabricante y del concesionario pueden llevar a negarse a vender o a cobrar cargos [NO VERIFICADO]. Gravedad: alta para el plazo de 3–6 meses.
3. **Pagos de la LLC a entidades del GoV** (SENIAT, Bolipuertos, bancos estatales) sin cobertura de una GL serían una posible violación de la EO 13884 [20]. Mitigación: que los pague localmente el importador venezolano.
4. **Cambio regulatorio rápido**: las GL de 2026 pueden modificarse o revocarse en cualquier momento [21]. La regla 91 FR 46260 (jul-2026) está sin revisar [NO VERIFICADO]. Hay que repetir el cribado y la revisión justo antes del embarque.
5. **Contraparte sancionada o vinculada**: un agente aduanal, almacén o socio de la C.A. que sea SDN o tenga vínculos militares convertiría la operación en prohibida o sujeta a licencia (§744.21/22) [7][9]. Mitigación: cribado en SDN y CSL y documentar beneficiarios finales.
6. **De-risking bancario**: transferencias retenidas o cuentas de la LLC cerradas si hay pagos con nexo venezolano [NO VERIFICADO].
7. **Cumplimiento fiscal de la LLC**: no presentar el 5472 o tratar mal la "distribución" del vehículo al socio [NO VERIFICADO; pregunta para el contador].
8. **Opción (c)**: un exportador informal que use compradores interpuestos o declare valores falsos traslada riesgo penal o civil y de pérdida del vehículo al cliente [NO VERIFICADO].

## Preguntas abiertas
1. Texto vigente de **15 CFR 744.21(a)** para Venezuela: ¿solo Supl. 2 a la Parte 744 o "cualquier artículo sujeto al EAR"? ¿Y la política de revisión? (ecfr.gov)
2. Contenido de **91 FR 46260 (23-jul-2026)** y de cualquier otra regla de BIS de 2026 sobre Venezuela. (federalregister.gov)
3. Confirmar la **clasificación EAR99** frente a la CCL (Supl. 1 a la Parte 774). (ecfr.gov)
4. Texto y vigencia de **GL 30B, GL 57** y de la GL de transacciones administrativas con el GoV (¿GL 35?). Revisar también las FAQ de OFAC sobre pago de impuestos y tasas y sobre el sector privado venezolano. (ofac.treasury.gov)
5. ¿Figura **Bolipuertos** (o el agente o almacén que se use en el puerto de destino) en la SDN List? (sanctionssearch.ofac.treas.gov)
6. ¿Está **8703.40.0045** en negrita en el Apéndice U del AESTIR? ¿Cómo se rellenan los campos de título si solo hay MSO? (Census, Data Collection Branch)
7. ¿Qué puertos del sureste de EE. UU. participan en el piloto **DIS** renovado el 6-nov-2026? (Federal Register 2026-22728 o CBP)
8. ¿El concesionario entregará el **MSO original** sin titular el vehículo? ¿Qué exige la política de exportación de Toyota? (Agente de compra)
9. ¿Qué bancos estadounidenses procesan sin problema pagos con nexo venezolano en 2026? ¿Hay avisos de FinCEN vigentes? (Agente de pagos)
10. Para el contador de la LLC: Formulario 5472, tratamiento como distribución y exención del impuesto sobre ventas por exportación.
11. Para la opción (b): ¿qué identificación de USPPI extranjero acepta AES (pasaporte)? ¿El cliente tiene que estar físicamente en EE. UU. al comprar? (15 CFR 30.1, 30.3 y 30.6)

## Fuentes
1. 19 CFR 192.1 — Definiciones (Cornell LII y eCFR); resoluciones CBP H204515, H238308 y H235018 — https://www.law.cornell.edu/cfr/text/19/192.1 ; https://www.ecfr.gov/current/title-19/chapter-I/part-192 ; https://open-gov.usebase.io/rulings/H204515 ; https://open-gov.usebase.io/rulings/H238308 ; https://open-gov.usebase.io/rulings/H235018 — CFR vigente (fecha de actualización no visible) — consultada 2026-11-18 (extracto del buscador) — tipo: primaria (resoluciones mediante espejo de terceros)
2. 19 CFR 192.2 — Requirements for exportation — https://www.law.cornell.edu/cfr/text/19/192.2 — CFR vigente — consultada 2026-11-18 (extracto) — tipo: primaria
3. CBP, "Exporting a Motor Vehicle" — https://www.cbp.gov/trade/basic-import-export/export-docs/motor-vehicle — sin fecha visible — consultada 2026-11-18 (extracto) — tipo: primaria
3b. CBP, "CBP Officers Seize 17 Vehicles and Assess $93,500 in Fines" — https://www.cbp.gov/newsroom/local-media-release/cbp-officers-seize-17-vehicles-and-assess-93500-fines — fecha no visible — consultada 2026-11-18 (solo título) — tipo: primaria (comunicado)
4. CBP, resolución 116070, "Exportation of Used Self-Propelled Vehicle; 19 USC § 1627a" — https://rulings.cbp.gov/ruling/116070 — 2003 — consultada 2026-11-18 (extracto) — tipo: primaria
5. Census Bureau, Foreign Trade Regulations (15 CFR 30) con la regla de agosto de 2025 incorporada; eCFR 15 CFR 30.2, 30.4 y 30.6; FAQ del FTR — https://www.census.gov/foreign-trade/regulations/regs/FTR_with_August_2025_FR_Incorporated_PUBLIC.pdf ; https://www.ecfr.gov/current/title-15/subtitle-B/chapter-I/part-30/subpart-A/section-30.2 ; https://www.census.gov/foreign-trade/regulations/ftrfaqs.pdf — ago-2025 — consultada 2026-11-18 (extracto) — tipo: primaria
6. Census Bureau, blogs "How to Report Used Vehicles in AES" (feb-2021) y "What Is A Used Vehicle?" (sep-2012) — https://www.census.gov/newsroom/blogs/global-reach/2021/02/how_to_report_usedv.html ; https://www.census.gov/newsroom/blogs/global-reach/2012/09/what-is-a-used-vehicle.html — 2021 / 2012 — consultada 2026-11-18 (extracto) — tipo: primaria (blog oficial)
7. BIS, 79 FR 66288, "Venezuela: Implementation of Certain Military End Uses and End Users License Requirements under the EAR" — https://www.bis.gov/79-fr-66288-venezuela-implementation-certain-military-end-uses-end-users-license-requirements-under-export — 2014 — consultada 2026-11-18 (extracto) — tipo: primaria
7b. CBP, "Electronic Information for Cargo Exported From the United States; Technical Amendments" — https://www.federalregister.gov/documents/2017/07/13/2017-14549/electronic-information-for-cargo-exported-from-the-united-states-technical-amendments — 13-jul-2017 — consultada 2026-11-18 (extracto) — tipo: primaria
8. BIS, 84 FR 24018, "Revisions to Country Group Designations for Venezuela; Conforming Changes to License Requirements" — https://www.bis.gov/84-fr-24018-revisions-country-group-designations-venezuela-conforming-changes-license-requirements — 2019 — consultada 2026-11-18 (extracto) — tipo: primaria
9. Federal Register, "Expansion of Export, Reexport, and Transfer (in-Country) Controls for Military End Use or Military End Users in the People's Republic of China, Russia, or Venezuela" (doc. 2020-07241) — https://www.federalregister.gov/documents/2020/04/28/2020-07241/expansion-of-export-reexport-and-transfer-in-country-controls-for-military-end-use-or-military-end — 28-abr-2020 — consultada 2026-11-18 (extracto) — tipo: primaria
10. Census Bureau, Schedule B 2026, capítulo 87 (PDF); también ediciones 2024 y 2021 — https://www.census.gov/foreign-trade/schedules/b/2026/c87.pdf ; https://www.census.gov/foreign-trade/schedules/b/2024/c87.pdf ; https://www.census.gov/foreign-trade/schedules/b/2021/c87.pdf — 2026 — consultada 2026-11-18 (extracto) — tipo: primaria
11. Census Bureau, Schedule B 2026 — índice de capítulos — https://www.census.gov/foreign-trade/schedules/b/2026/index.html — 2026 (aplicable desde 1-jul-2026, según extracto) — consultada 2026-11-18 — tipo: primaria
12. OFAC, "Selected General Licenses Issued by OFAC" (incluye GL 30B 10-feb-2026, GL 52 18-mar-2026, GL 57 14-abr-2026, GL 46E, 48D, 49B, 50C y 5W) — https://ofac.treasury.gov/selected-general-licenses-issued-ofac — 2026 — consultada 2026-11-18 (extracto del buscador; no leída íntegra) — tipo: primaria
13. OFAC, Recent Actions 05-may-2026, "Issuance of Venezuela-related General License" (GL 58) — https://ofac.treasury.gov/recent-actions/20260505 — 05-may-2026 — consultada 2026-11-18 (extracto) — tipo: primaria
14. OFAC, Recent Actions 16-oct-2026, "Issuance of Amended Venezuela-related General License and Frequently Asked Question" (GL 60A, FAQ 1263) — https://ofac.treasury.gov/recent-actions/20261016 — 16-oct-2026 — consultada 2026-11-18 (extracto) — tipo: primaria
15. OFAC, Recent Actions 02-feb-2026 y 04-may-2026, "Issuance of Venezuela-related General License and Amended FAQ" — https://ofac.treasury.gov/recent-actions/20260202 ; https://ofac.treasury.gov/recent-actions/20260504 — feb/may-2026 — consultada 2026-11-18 (solo título) — tipo: primaria
16. OFAC, Recent Actions 13-feb, 13-mar, 18-mar, 19-mar y 25-jun-2026 — https://ofac.treasury.gov/recent-actions/20260213 ; https://ofac.treasury.gov/recent-actions/20260313_33 ; https://ofac.treasury.gov/recent-actions/20260318 ; https://ofac.treasury.gov/recent-actions/20260319 ; https://ofac.treasury.gov/recent-actions/20260625_33 — 2026 — consultada 2026-11-18 (solo URL y título) — tipo: primaria
17. OFAC, FAQ — tema "Venezuela Sanctions" — https://ofac.treasury.gov/faqs/topic/1581 — vigente (fecha no visible) — consultada 2026-11-18 (no leída) — tipo: primaria
18. U.S. Department of State, "Venezuela-Related Sanctions" — https://www.state.gov/venezuela-related-sanctions — fecha no visible — consultada 2026-11-18 (no leída) — tipo: primaria
19. Mayer Brown, "New Executive Order Shields Venezuelan Oil Revenue in US Government Custody"; Baker McKenzie, Sanctions blog, sobre la EO de "Foreign Government Deposit Funds" — https://www.mayerbrown.com/en/insights/publications/2026/01/new-executive-order-shields-venezuelan-oil-revenue-in-us-government-custody ; https://sanctionsnews.bakermckenzie.com/president-trump-signs-executive-order-prohibiting-judicial-proceedings-against-venezuelan-oil-revenues-held-in-us-treasury-foreign-government-deposit-funds/ — ene-2026 — consultada 2026-11-18 (extracto) — tipo: bufete [BUFETE/BLOG]
20. Cleary Gottlieb, "Navigating Venezuela Sanctions: Legal Considerations and Anticipated Developments"; Orrick, "U.S. Treasury Authorizes Venezuelan Oil Deals Under Strict Conditions" — https://www.clearytradewatch.com/2026/01/navigating-venezuela-sanctions-legal-considerations-and-anticipated-developments/ ; https://www.orrick.com/en/Insights/2026/02/US-Treasury-Authorizes-Venezuelan-Oil-Deals-Under-Strict-Conditions — ene/feb-2026 — consultada 2026-11-18 (extracto) — tipo: bufete [BUFETE/BLOG]
21. Agora Latam, "OFAC Venezuela Sanctions: October 2026 Changes and the GL 5Z Deadline"; ofacblockedfundslawyers.com, "Venezuela Sanctions 2026" — https://www.agoralatam.com/insights/ofac-venezuela-sanctions-october-2026-update ; https://ofacblockedfundslawyers.com/services/ofac-sanctions-programs/venezuela-sanctions/ — oct-2026 / 2026 — consultada 2026-11-18 (extracto) — tipo: blog/bufete [BUFETE/BLOG]
22. Federal Register, "Revision to License Review Policy for Advanced Computing Commodities" (doc. 2026-00789) — https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities — 15-ene-2026 — consultada 2026-11-18 (extracto) — tipo: primaria
23. Bass, Berry & Sims, "Update on Venezuela: Significant Trade Restrictions and Risks Continue" — https://www.bassberrygovcontrade.com/venezuela-trade-restrictions-risks-continue/ — fecha no visible — consultada 2026-11-18 (extracto) — tipo: bufete [BUFETE/BLOG]
24. Resumen profesional sobre la interacción OFAC/BIS para Venezuela (devuelto por el buscador junto con [21]); BIS, páginas de las Partes 742 y 744 del EAR (mención de 91 FR 46260, 23-jul-2026) — https://ofacblockedfundslawyers.com/services/ofac-sanctions-programs/venezuela-sanctions/ ; https://www.bis.gov/regulations/ear/742 ; https://www.bis.gov/regulations/ear/744 — 2026 — consultada 2026-11-18 (extracto) — tipo: blog [BUFETE/BLOG] / primaria (bis.gov)
25. Federal Register, "Document Image System (DIS) Pilot for Used Self-Propelled Vehicles Export Document Submission: Renewal of Test" (doc. 2026-22728) — https://www.federalregister.gov/documents/2026/11/06/2026-22728/document-image-system-dis-pilot-for-used-self-propelled-vehicles-export-document-submission-renewal — 06-nov-2026 — consultada 2026-11-18 (extracto) — tipo: primaria
26. Federal Register, "Document Imaging System (DIS) Pilot for Used Self-Propelled Vehicles Export Document Submission" (doc. 2022-09966) — https://www.federalregister.gov/documents/2022/05/10/2022-09966/document-imaging-system-dis-pilot-for-used-self-propelled-vehicles-export-document-submission — 10-may-2022 — consultada 2026-11-18 (extracto) — tipo: primaria
