# Análisis Estructural - EH2025_Persona.sav

## Resumen General del Dataset
- **Total de registros (filas):** 39,485
- **Total de variables (columnas):** 276
- **Fuente:** Encuesta de Hogares 2025 (INE Bolivia) - Módulo Persona

## Diccionario de Variables
| Variable | Etiqueta / Descripción | Tipo | Nulos | % Nulos |
|----------|------------------------|------|-------|---------|
| `folio` | Id hogar anonimizado | object | 0 | 0.0% |
| `area` | Urbana Rural | float64 | 0 | 0.0% |
| `depto` | Departamento | float64 | 0 | 0.0% |
| `nro` | Número de persona | float64 | 0 | 0.0% |
| `s01a_02` | ¿Es hombre o mujer? | float64 | 0 | 0.0% |
| `s01a_03` | ¿Cuántos años cumplidos tiene? | float64 | 0 | 0.0% |
| `s01a_04a` | ¿Cuál es la fecha de su nacimiento? Día | float64 | 0 | 0.0% |
| `s01a_04b` | ¿Cuál es la fecha de su nacimiento? Mes | float64 | 0 | 0.0% |
| `s01a_04c` | ¿Cuál es la fecha de su nacimiento? Año | float64 | 0 | 0.0% |
| `s01a_05` | ¿Qué parentesco tiene (...) con la Jefa o Jefe del hogar? | float64 | 0 | 0.0% |
| `s01a_05a` | Su esposa/o compañera/o CODIGO | float64 | 7,772 | 19.68% |
| `s01a_05b` | Su padre/ padrastro CODIGO | float64 | 11 | 0.03% |
| `s01a_05c` | Su madre/ madrastra CODIGO | float64 | 2 | 0.01% |
| `s01a_06` | En la presente gestión 2024 ¿Principalmente que persona dedicó mas horas al cuidado de (…)? | float64 | 30,765 | 77.92% |
| `s01a_07_1` | ¿Qué idiomas habla?, según el mayor uso: 1° | float64 | 0 | 0.0% |
| `s01a_07_2` | ¿Qué idiomas habla?, según el mayor uso: 2° | float64 | 28,903 | 73.2% |
| `s01a_07_3` | ¿Qué idiomas habla?, según el mayor uso: 3° | float64 | 38,946 | 98.63% |
| `s01a_08` | ¿Cuál es el primer idioma o lengua en el que aprendió a hablar en su niñez? | float64 | 1,282 | 3.25% |
| `s01a_09` | ¿Se autoidentifica con alguna nación pueblo indígena originario campesino o afroboliviano? | float64 | 0 | 0.0% |
| `s01a_09npioc` | ¿Se autoidentifica con alguna nación pueblo indígena originario campesino o afroboliviano? ¿Con cuál? | float64 | 31,175 | 78.95% |
| `s01a_10` | ¿Cuál es su estado civil o conyugal actual? | float64 | 7,746 | 19.62% |
| `s01b_11a` | ¿Dónde vivía hace 5 años (2020)? | float64 | 0 | 0.0% |
| `s01b_11b` | Especifique el Departamento  dónde vivía hace 5 años (2020) | object | 0 | 0.0% |
| `s01b_11c` | Especifique la Provincia dónde vivía hace 5 años (2020) | object | 0 | 0.0% |
| `s01b_11d` | Especifique el Municipio dónde vivía hace 5 años (2020) | object | 0 | 0.0% |
| `s01b_11e` | Especifique el País dónde vivía hace 5 años (2020) | object | 0 | 0.0% |
| `s01b_12` | ¿Cuál fue la razón por la que dejó ese lugar? | float64 | 38,269 | 96.92% |
| `s01b_12e` | ¿Cuál fue la razón por la que dejó ese lugar? Otra razón (Especifique) | object | 0 | 0.0% |
| `s01b_13a` | ¿Desde qué año y mes vive aquí? Año | float64 | 38,269 | 96.92% |
| `s01b_10a` | ¿Dónde nació? | float64 | 21 | 0.05% |
| `s01b_13b` | ¿Desde qué año y mes vive aquí? Mes | float64 | 38,269 | 96.92% |
| `s02a_01a` | ¿Está (...) registrada(o) o afiliada(o) a: 1° | float64 | 0 | 0.0% |
| `s02a_01b` | ¿Está (...) registrada(o) o afiliada(o) a: 2° | float64 | 39,416 | 99.83% |
| `s02a_01e` | ¿Está (...) registrada(o) o afiliada(o) a: Otro (Especifique) | object | 0 | 0.0% |
| `s02a_02a` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… A. puesto/centro/hospital de salud público? | float64 | 0 | 0.0% |
| `s02a_02b` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… B. Cajas de salud (Caja Nacional de Salud/Caja de la Banca Privada/Caja Petrolera/Banca Estatal/COSSMIL/ Seguro Universitario u otras Cajas)? | float64 | 0 | 0.0% |
| `s02a_02c` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… C. consultorio/clínica/hospital de salud privados? | float64 | 0 | 0.0% |
| `s02a_02d` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… D. atención médica en domicilio? | float64 | 0 | 0.0% |
| `s02a_02e` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… E. servicios de medicina tradicional ancestral? | float64 | 0 | 0.0% |
| `s02a_02f` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… F. soluciones caseras? | float64 | 0 | 0.0% |
| `s02a_02g` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… G. farmacia sin receta médica (automedicación)? | float64 | 0 | 0.0% |
| `s02a_02h` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… H. otro? | float64 | 0 | 0.0% |
| `s02a_02he` | En los últimos 12 meses, por problemas de salud, ¿acudió o se atendió en… H. otro? (especifique) | object | 0 | 0.0% |
| `s02a_03a` | En los últimos 12 meses, ¿cuánto tuvo que pagar el hogar por los cuidados de salud de (…) por concepto de: A. Servicios médicos por consulta externa: | float64 | 0 | 0.0% |
| `s02a_03b` | En los últimos 12 meses, ¿cuánto tuvo que pagar el hogar por los cuidados de salud de (…) por concepto de: B. Aparatos: | float64 | 0 | 0.0% |
| `s02a_03c` | En los últimos 12 meses, ¿cuánto tuvo que pagar el hogar por los cuidados de salud de (…) por concepto de: C. Internación hospitalaria: | float64 | 0 | 0.0% |
| `s02a_03d` | En los últimos 12 meses, ¿cuánto tuvo que pagar el hogar por los cuidados de salud de (…) por concepto de: D. Exámenes o servicio de ambulancia: | float64 | 0 | 0.0% |
| `s02a_03e` | En los últimos 12 meses, ¿cuánto tuvo que pagar el hogar por los cuidados de salud de (…) por concepto de: E. Medicinas: | float64 | 0 | 0.0% |
| `s02a_04a` | ¿Tiene (…) dificultad permanente para… A. ver, incluso cuando usa lentes? | float64 | 0 | 0.0% |
| `s02a_04b` | ¿Tiene (…) dificultad permanente para… B. oir, incluso cuando usa audífonos? | float64 | 0 | 0.0% |
| `s02a_04c` | ¿Tiene (…) dificultad permanente para… C. caminar,subir gradas, usar brazos o manos? | float64 | 0 | 0.0% |
| `s02a_04d` | ¿Tiene (…) dificultad permanente para… D. comunicarse, aprender, concentrarse o razonar? | float64 | 0 | 0.0% |
| `s02a_05` | ¿(…) fue registrada/o en el Sistema de Información del Programa de Registro Único Nacional de Personas con Discapacidad (SIPRUNPCD) del Ministerio de Salud y Deportes o en el Sistema de Control de Afiliados (SICOA) del Instituto Boliviano de la Ceguera? | float64 | 34,768 | 88.05% |
| `s02b_06` | ¿Está o estuvo alguna vez embarazada? | float64 | 28,108 | 71.19% |
| `s02b_06b` | ¿Está o estuvo alguna vez embarazada? ¿Cuántas veces? (incluyendo el actual embarazo) | float64 | 33,151 | 83.96% |
| `s02b_07` | ¿Cuántas hijas e hijos nacidos vivos ha tenido? (aunque después hayan muerto) | float64 | 33,151 | 83.96% |
| `s02b_08` | De ellos ¿Cuántos están vivos actualmente? | float64 | 33,259 | 84.23% |
| `s02b_09a` | ¿En qué mes y año nació su última hija o hijo nacido vivo? (aunque después haya muerto) Mes. | float64 | 33,259 | 84.23% |
| `s02b_09b` | ¿En qué mes y año nació su última hija o hijo nacido vivo? (aunque después haya muerto) Año. | float64 | 33,259 | 84.23% |
| `s02b_10` | ¿Quién atendió su último parto? | float64 | 36,898 | 93.45% |
| `s02b_10e` | ¿Quién atendió su último parto? Especifique. | object | 0 | 0.0% |
| `s02b_11` | En su último embarazo, ¿se ha inscrito al Bono Juana Azurduy (BJA)? | float64 | 33,151 | 83.96% |
| `s02b_12a1` | En los últimos 12 meses, ¿cobró usted el Bono Juana Azurduy por: A. Controles prenatales realizados? | float64 | 36,635 | 92.78% |
| `s02b_12a2` | En los últimos 12 meses, ¿cobró usted el Bono Juana Azurduy por: A. Controles prenatales realizados? Nº de Controles | float64 | 39,163 | 99.18% |
| `s02b_12b` | En los últimos 12 meses, ¿cobró usted el Bono Juana Azurduy por: B. El parto y primer control postparto? | float64 | 36,632 | 92.77% |
| `s02b_13` | En su último embarazo, ¿recibió el Subsidio Universal Prenatal por la Vida (Productos con valor de Bs 300)? | float64 | 36,631 | 92.77% |
| `s02b_14` | En los últimos 12 meses, ¿recibió el Subsidio Universal Prenatal por la Vida (Productos con valor de Bs 300)? | float64 | 36,856 | 93.34% |
| `s02b_14a` | En los últimos 12 meses, ¿recibió el Subsidio Universal Prenatal por la Vida (Productos con valor de Bs 300)¿Cuántos meses? | float64 | 39,143 | 99.13% |
| `s02c_15` | Durante este año, ¿(…) asiste o asistió a algún centro infantil que no sea pre kinder ni kinder?? | float64 | 36,216 | 91.72% |
| `s02d_16` | ¿Alguna vez inscribieron a (…) al Bono Juana Azurduy? | float64 | 36,883 | 93.41% |
| `s02d_17` | En los últimos 12 meses, ¿cobró usted el Bono Juana Azurduy por los controles integrales de salud de (…)? | float64 | 37,899 | 95.98% |
| `s02d_17a` | En los últimos 12 meses, ¿cobró usted el Bono Juana Azurduy por los controles integrales de salud de (…)? ¿Cuántos controles cobró? | float64 | 38,875 | 98.46% |
| `s03a_01` | ¿Sabe leer y escribir? | float64 | 2,000 | 5.07% |
| `s03a_01a` | ¿Es (…) capaz de sumar o multiplicar números, ya sea en papel o mentalmente? | float64 | 2,000 | 5.07% |
| `s03a_02a` | ¿Cuál fue el NIVEL Y CURSO más alto de instrucción que aprobó? Nivel | float64 | 2,000 | 5.07% |
| `s03a_02c` | ¿Cuál fue el NIVEL Y CURSO más alto de instrucción que aprobó? Curso | float64 | 2,000 | 5.07% |
| `s03a_03a` | Para ingresar a ese nivel ¿Cuál fue el NIVEL Y CURSO anterior de educación que aprobó? Nivel | float64 | 37,231 | 94.29% |
| `s03a_03c` | Para ingresar a ese nivel ¿Cuál fue el NIVEL Y CURSO anterior de educación que aprobó? Curso | float64 | 37,231 | 94.29% |
| `s03a_04` | Durante este año, ¿se inscribió o matriculó en algún curso o grado de educación escolar, alternativa, superior o postgrado? | float64 | 2,000 | 5.07% |
| `s03a_05` | ¿Por qué razón no se inscribió/matriculó? (Indague la razón más importante) | float64 | 15,621 | 39.56% |
| `s03a_05e` | ¿Por qué razón no se inscribió/matriculó? (Indague la razón más importante) Especifique. | object | 0 | 0.0% |
| `s03a_06a` | ¿A qué NIVEL Y CURSO de educación escolar, alternativa, superior o postgrado se inscribió/matriculó este año? Nivel | float64 | 25,864 | 65.5% |
| `s03a_06c` | ¿A qué NIVEL Y CURSO de educación escolar, alternativa, superior o postgrado se inscribió/matriculó este año? Curso | float64 | 25,864 | 65.5% |
| `s03a_07a` | En esta gestión, ¿recibió Desayuno/ Almuerzo o merienda escolar? | float64 | 29,112 | 73.73% |
| `s03a_07b` | ¿Cuantos meses aproximadamente? | float64 | 30,939 | 78.36% |
| `s03a_08` | ¿Recibió el Bono Juancito Pinto el año pasado (2024)? | float64 | 29,112 | 73.73% |
| `s03a_09` | El establecimiento en el que se matriculó esta gestión 2025 es: | float64 | 25,864 | 65.5% |
| `s03b_10` | Actualmente, ¿(…) pasa clases en el nivel y curso al que se matriculó esta gestión 2025? | float64 | 25,864 | 65.5% |
| `s03b_11` | ¿Cuál es la principal razón por la que no pasa clases actualmente (ya sea presencial, semipresencial, a distancia o virtual)? | float64 | 33,203 | 84.09% |
| `s03b_11e` | ¿Cuál es la principal razón por la que no pasa clases actualmente (ya sea presencial, semipresencial, a distancia o virtual)? Otro (Especifique) | object | 0 | 0.0% |
| `s03b_12` | Actualmente, ¿se encuentra en periodo de vacación, descanso pedagógico o receso? | float64 | 39,427 | 99.85% |
| `s03c_13` | ¿(....) dispone de teléfono celular para uso personal? | float64 | 2,602 | 6.59% |
| `s03c_13a` | ¿El teléfono celular puede conectarse a Internet? | float64 | 10,788 | 27.32% |
| `s03c_14` | ¿En los últimos 3 meses, (....) ha utilizado teléfono celular? | float64 | 2,602 | 6.59% |
| `s03c_15a` | ¿En los últimos 3 meses, (…) ha utilizado computadora de escritorio, laptop, tablet, en cualquier lugar? | float64 | 2,602 | 6.59% |
| `s03c_15b` | ¿En los últimos 3 meses, (…) ha utilizado computadora de escritorio, laptop, tablet, en cualquier lugar? ¿Con qué frecuencia? | float64 | 28,898 | 73.19% |
| `s03c_16a` | ¿En los últimos 3 meses, (…) ha utilizado Internet en cualquier lugar? | float64 | 2,602 | 6.59% |
| `s03c_16b` | ¿En los últimos 3 meses, (…) ha utilizado Internet en cualquier lugar? ¿Con qué frecuencia? | float64 | 13,426 | 34.0% |
| `s03c_17aa` | ¿Dónde ha utilizado usted internet en los últimos 3 meses? 1° | float64 | 13,426 | 34.0% |
| `s03c_17ab` | ¿Dónde ha utilizado usted internet en los últimos 3 meses? 2° | float64 | 25,958 | 65.74% |
| `s03c_17e` | ¿Dónde ha utilizado usted internet en los últimos 3 meses? Especifique | object | 0 | 0.0% |
| `s04a_01` | Durante la semana pasada, ¿trabajó al menos una hora? | float64 | 3,896 | 9.87% |
| `s04a_02` | Durante la semana pasada, dedicó al menos una hora a: | float64 | 22,908 | 58.02% |
| `s04a_02a` | Los cultivos agrícolas, cría de animales, caza, pesca o recolección son destinados: | float64 | 39,142 | 99.13% |
| `s04a_03` | La semana pasada, ¿tuvo algún empleo, negocio o empresa propia en la cual no trabajó por: | float64 | 23,520 | 59.57% |
| `s04a_04` | La semana pasada, ¿quería usted trabajar y estaba disponible para hacerlo? | float64 | 23,665 | 59.93% |
| `s04a_05` | Durante las últimas cuatro semanas ¿buscó trabajo o hizo gestiones para establecer algún negocio propio? | float64 | 23,665 | 59.93% |
| `s04a_06` | Es usted: | float64 | 24,606 | 62.32% |
| `s04a_06e` | Es usted: (Especifique) | object | 0 | 0.0% |
| `s04a_07` | ¿Por qué no buscó trabajo? | float64 | 24,606 | 62.32% |
| `s04a_07e` | ¿Por qué no buscó trabajo? Por otras causas (Especifique) | object | 0 | 0.0% |
| `s04a_08` | ¿Ha trabajado alguna vez anteriormente? | float64 | 23,665 | 59.93% |
| `s04b_09a_cod` | Cod. COB 2023 | object | 0 | 0.0% |
| `s04b_10a_cod` | Cod. CAEB 2022 | object | 0 | 0.0% |
| `s04b_11aa` | ¿Hace cuánto tiempo trabaja en esta empresa, institución, negocio o lugar? Tiempo | float64 | 19,716 | 49.93% |
| `s04b_11ab` | ¿Hace cuánto tiempo trabaja en esta empresa, institución, negocio o lugar? Periodo | float64 | 19,716 | 49.93% |
| `s04b_11ba` | ¿Hace cuánto tiempo desempeña esta ocupación en esa empresa, institución, negocio o lugar? Tiempo | float64 | 19,716 | 49.93% |
| `s04b_11bb` | ¿Hace cuánto tiempo desempeña esta ocupación en esa empresa, institución, negocio o lugar? Periodo | float64 | 19,716 | 49.93% |
| `s04b_12` | En esta ocupación usted trabaja como | float64 | 19,716 | 49.93% |
| `s04b_13` | La administración de la empresa, institución, negocio o lugar donde trabaja es… | float64 | 32,377 | 82.0% |
| `s04b_14` | ¿Cuántas personas trabajan en la empresa, institución o lugar donde trabaja, incluido usted? | float64 | 20,028 | 50.72% |
| `s04b_15` | ¿Cuántos días a la semana trabaja regularmente en su ocupación? | float64 | 19,716 | 49.93% |
| `s04b_16aa` | ¿Cuántas horas en promedio trabaja al día en su ocupación? HORAS | float64 | 19,716 | 49.93% |
| `s04b_16ab` | ¿Cuántas horas en promedio trabaja al día en su ocupación? MINUTOS | float64 | 19,716 | 49.93% |
| `s04c_17a` | ¿Cuánto es su salario líquido, excluyendo los descuentos de ley (Gestora/AFP, IVA)? Monto (Bs) | float64 | 32,098 | 81.29% |
| `s04c_17b` | ¿Cuánto es su salario líquido, excluyendo los descuentos de ley (Gestora/AFP, IVA)? Frecuencia. | float64 | 32,098 | 81.29% |
| `s04c_18a` | Durante los últimos doce meses, ¿recibió usted pagos por: A. Bonos laborales o prima de producción? | float64 | 32,097 | 81.29% |
| `s04c_18b` | Durante los últimos doce meses, ¿recibió usted pagos por: B. Aguinaldo (Incluir si recibió este beneficio de un empleo anterior)? | float64 | 32,097 | 81.29% |
| `s04c_19aa` | Durante los últimos doce meses, ¿recibió usted pagos en efectivo por: A. Comisiones, destajo, propinas, bonos de transporte o refrigerio? Monto (Bs) | float64 | 32,097 | 81.29% |
| `s04c_19ab` | Durante los últimos doce meses, ¿recibió usted pagos en efectivo por: A. Comisiones, destajo, propinas, bonos de transporte o refrigerio? Frecuencia de pago: | float64 | 38,668 | 97.93% |
| `s04c_19ba` | Durante los últimos doce meses, ¿recibió usted pagos en efectivo por: B. Horas Extras? Monto (Bs) | float64 | 32,097 | 81.29% |
| `s04c_19bb` | Durante los últimos doce meses, ¿recibió usted pagos en efectivo por: B. Horas Extras? Frecuencia de pago: | float64 | 39,033 | 98.86% |
| `s04c_20a1` | Durante los últimos doce meses, ¿recibió usted: A. Subsidio prenatal o de lactancia (Cajas de Salud)? | float64 | 32,097 | 81.29% |
| `s04c_20a2` | Durante los últimos doce meses, ¿recibió usted: A. Subsidio prenatal o de lactancia (Cajas de Salud)? NÚMERO DE MESES | float64 | 39,359 | 99.68% |
| `s04c_20b` | Durante los últimos doce meses, ¿recibió usted: B. Bono de natalidad? | float64 | 32,097 | 81.29% |
| `s04c_20a_1` | ¿En su actual ocupación Ud. recibe o recibirá los siguientes beneficios: A. Vacaciones? | float64 | 32,097 | 81.29% |
| `s04c_20a_2` | ¿En su actual ocupación Ud. recibe o recibirá los siguientes beneficios: B. Seguro de salud? | float64 | 32,097 | 81.29% |
| `s04c_21a` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… A. Alimentos y bebidas para ser consumidos dentro o fuera del lugar de trabajo? | float64 | 32,097 | 81.29% |
| `s04c_21a1` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… A. Alimentos y bebidas para ser consumidos dentro o fuera del lugar de trabajo? ¿Con qué frecuencia? | float64 | 38,060 | 96.39% |
| `s04c_21a2` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… A. Alimentos y bebidas para ser consumidos dentro o fuera del lugar de trabajo? (Valorar en Bs) | float64 | 38,060 | 96.39% |
| `s04c_21b` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… B. Transporte hacia y desde el lugar de su trabajo? | float64 | 32,097 | 81.29% |
| `s04c_21b1` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… B. Transporte hacia y desde el lugar de su trabajo? ¿Con qué frecuencia? | float64 | 39,143 | 99.13% |
| `s04c_21b2` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… B. Transporte hacia y desde el lugar de su trabajo? (Valorar en Bs) | float64 | 39,143 | 99.13% |
| `s04c_21c` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… C. Vestidos y calzados utilizados frecuentemente tanto dentro como fuera de su lugar de trabajo? | float64 | 32,097 | 81.29% |
| `s04c_21c1` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… C. Vestidos y calzados utilizados frecuentemente tanto dentro como fuera de su lugar de trabajo? ¿Con qué frecuencia? | float64 | 38,559 | 97.65% |
| `s04c_21c2` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… C. Vestidos y calzados utilizados frecuentemente tanto dentro como fuera de su lugar de trabajo? (Valorar en Bs) | float64 | 38,556 | 97.65% |
| `s04c_21d` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… D. Vivienda o alojamiento cedido por servicios que pueden ser utilizados por los miembros del hogar? | float64 | 32,097 | 81.29% |
| `s04c_21d1` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted...D. Vivienda o alojamiento cedido por servicios que pueden ser utilizados por los miembros del hogar? ¿Con qué frecuencia? | float64 | 39,293 | 99.51% |
| `s04c_21d2` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted...D. Vivienda o alojamiento cedido por servicios que pueden ser utilizados por los miembros del hogar? (Valorar en Bs) | float64 | 39,293 | 99.51% |
| `s04c_21e` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted… E. Otros, como servicio de guardería, instalaciones deportivas y/o recreativas? | float64 | 32,097 | 81.29% |
| `s04c_21e1` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted...E. Otros, como servicio de guardería, instalaciones deportivas y/o recreativas? ¿Con qué frecuencia? | float64 | 39,466 | 99.95% |
| `s04c_21e2` | Además de los ingresos recibidos en dinero por su trabajo, en los últimos doce meses ¿recibió, usted...E. Otros, como servicio de guardería, instalaciones deportivas y/o recreativas? (Valorar en Bs) | float64 | 39,466 | 99.95% |
| `s04d_22a` | ¿Cuánto es su ingreso total en su ocupación principal? Monto (Bs) | float64 | 29,832 | 75.55% |
| `s04d_22b` | ¿Cuánto es su ingreso total en su ocupación principal? Frecuencia de ingreso: | float64 | 29,867 | 75.64% |
| `s04d_23aa` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… A. Comprar materia prima, materiales o mercadería para su actividad o negocio? Monto (Bs) | float64 | 29,866 | 75.64% |
| `s04d_23ab` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… A. Comprar materia prima, materiales o mercadería para su actividad o negocio? Frecuencia de gasto: | float64 | 31,688 | 80.25% |
| `s04d_23ba` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… B. Pagar por prestación de servicios a terceros para su actividad o negocio? Monto (Bs) | float64 | 29,866 | 75.64% |
| `s04d_23bb` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… B. Pagar por prestación de servicios a terceros para su actividad o negocio? Frecuencia de gasto: | float64 | 37,642 | 95.33% |
| `s04d_23ca` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… C. Pagar sueldos, salarios, bonos, gratificaciones, horas extras, Gestora a sus empleados? Monto (Bs) | float64 | 29,866 | 75.64% |
| `s04d_23cb` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… C. Pagar sueldos, salarios, bonos, gratificaciones, horas extras, Gestora a sus empleados? Frecuencia de gasto: | float64 | 38,764 | 98.17% |
| `s04d_23da` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… D. Pagar alquiler del local/vehiculo que dispone para su actividad o negocio? Monto (Bs) | float64 | 29,866 | 75.64% |
| `s04d_23db` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… D. Pagar alquiler del local/vehiculo que dispone para su actividad o negocio? Frecuencia de gasto: | float64 | 37,710 | 95.5% |
| `s04d_23ea` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… E. Pagar servicios de agua, luz, gas, teléfono o internet que usa para la actividad o negocio? Monto (Bs) | float64 | 29,866 | 75.64% |
| `s04d_23eb` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… E. Pagar servicios de agua, luz, gas, teléfono o internet que usa para la actividad o negocio? Frecuencia de gasto: | float64 | 36,154 | 91.56% |
| `s04d_23fa` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… F. Pagar cuotas regulares por concepto de microcrédito/crédito para su actividad o negocio? Monto (Bs) | float64 | 29,866 | 75.64% |
| `s04d_23fb` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… F. Pagar cuotas regulares por concepto de microcrédito/crédito para su actividad o negocio? Frecuencia de gasto: | float64 | 39,053 | 98.91% |
| `s04d_23ga` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… G. Pagar impuestos, sentajes? Monto (Bs) | float64 | 29,866 | 75.64% |
| `s04d_23gb` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… G. Pagar impuestos, sentajes? Frecuencia de gasto: | float64 | 37,760 | 95.63% |
| `s04d_23ha` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… H. Pagar cuotas a sindicatos, gremios, asociaciones? Monto (Bs) | float64 | 29,866 | 75.64% |
| `s04d_23hb` | Del ingreso total declarado en la pregunta anterior, ¿cuánto utiliza o guarda para… H. Pagar cuotas a sindicatos, gremios, asociaciones? Frecuencia de gasto: | float64 | 38,068 | 96.41% |
| `s04d_24a` | Una vez descontadas todas sus obligaciones (sueldos, salarios, compra de material, mercadería, etc.), ¿cuánto le queda para uso del hogar? Monto (Bs) | float64 | 29,832 | 75.55% |
| `s04d_24b` | Una vez descontadas todas sus obligaciones (sueldos, salarios, compra de material, mercadería, etc.), ¿cuánto le queda para uso del hogar? Frecuencia de ingreso: | float64 | 29,876 | 75.66% |
| `s04d_24ba` | En esta ocupación, de su producción agricola, crianza de animales o sus productos derivados, ¿destinó una parte para alimentación/consumo de su hogar?: | float64 | 37,242 | 94.32% |
| `s04d_24bb` | En esta ocupación, de su producción agricola, crianza de animales o sus productos derivados, ¿destinó una parte para alimentación/consumo de su hogar? Frecuencia | float64 | 37,740 | 95.58% |
| `s04d_24bc` | En esta ocupación, de su producción agricola, crianza de animales o sus productos derivados, ¿destinó una parte para alimentación/consumo de su hogar? Monto(Bs) | float64 | 37,740 | 95.58% |
| `s04e_25` | Además de la actividad mencionada anteriormente, ¿realizó otro trabajo durante la semana pasada? | float64 | 19,716 | 49.93% |
| `s04e_26_cod` | Cod. CAEB 2022 | object | 0 | 0.0% |
| `s04e_27` | En esta otra ocupación usted trabaja como: | float64 | 38,009 | 96.26% |
| `s04e_28` | La administración de la empresa, institución, negocio o lugar donde trabaja en esta otra ocupación es… | float64 | 39,297 | 99.52% |
| `s04e_29` | ¿Cuántos días a la semana trabaja regularmente en esta otra ocupación? | float64 | 38,009 | 96.26% |
| `s04e_30a` | ¿Cuántas horas en promedio trabaja al día en esta otra ocupación? HORAS | float64 | 38,009 | 96.26% |
| `s04e_30b` | ¿Cuántas horas en promedio trabaja al día en esta otra ocupación? MINUTOS | float64 | 38,009 | 96.26% |
| `s04f_31a` | ¿Cuánto es su salario líquido en ésta otra ocupación,  excluyendo los descuentos de ley (Gestora/AFP, IVA)? | float64 | 39,293 | 99.51% |
| `s04f_31b` | ¿Cuánto es su salario líquido en ésta otra ocupación,  excluyendo los descuentos de ley (Gestora/AFP, IVA)? Frecuencia de ingreso: | float64 | 39,293 | 99.51% |
| `s04f_32a` | Durante los últimos doce meses, ha recibido: A. ¿Pago por horas extras, bono o prima de producción, aguinaldo? | float64 | 39,293 | 99.51% |
| `s04f_32a1` | Durante los últimos doce meses, ha recibido: A. ¿Pago por horas extras, bono o prima de producción, aguinaldo? Monto (Bs) | float64 | 39,470 | 99.96% |
| `s04f_32b` | Durante los últimos doce meses, ha recibido: B. ¿Alimentos, transporte, vestimenta? | float64 | 39,293 | 99.51% |
| `s04f_32b1` | Durante los últimos doce meses, ha recibido: B. ¿Alimentos, transporte, vestimenta? Monto (Bs) | float64 | 39,449 | 99.91% |
| `s04f_32c` | Durante los últimos doce meses, ha recibido: C. ¿Vivienda, alojamiento, otros? | float64 | 39,293 | 99.51% |
| `s04f_32c1` | Durante los últimos doce meses, ha recibido: C. ¿Vivienda, alojamiento, otros? Monto (Bs) | float64 | 39,477 | 99.98% |
| `s04f_33a` | ¿Cuánto es su ingreso total en ésta otra ocupación? Monto (Bs) | float64 | 38,515 | 97.54% |
| `s04f_33b` | ¿Cuánto es su ingreso total en ésta otra ocupación? Frecuencia de ingreso: | float64 | 38,528 | 97.58% |
| `s04f_34a` | Una vez pagadas todas sus obligaciones (sueldos, salarios, compra de materiales, etc.), ¿cuánto le queda para uso del hogar? Monto (Bs) | float64 | 38,516 | 97.55% |
| `s04f_34b` | Una vez pagadas todas sus obligaciones (sueldos, salarios, compra de materiales, etc.), ¿cuánto le queda para uso del hogar? Frecuencia de ingreso: | float64 | 38,531 | 97.58% |
| `s04f_34ba` | En esta otra ocupación, de su producción agrícola, crianza de animales o sus productos derivados, ¿destinó una parte para alimentación/consumo de su hogar? | float64 | 39,111 | 99.05% |
| `s04f_34bb` | En esta otra ocupación, de su producción agrícola, crianza de animales o sus productos derivados, ¿destinó una parte para alimentación/consumo de su hogar? Frecuencia | float64 | 39,169 | 99.2% |
| `s04f_34bc` | En esta otra ocupación, de su producción agrícola, crianza de animales o sus productos derivados, ¿destinó una parte para alimentación/consumo de su hogar? Monto(Bs) | float64 | 39,169 | 99.2% |
| `s04f_35` | ¿Está usted afiliada(o) a la Gestora (AFP)? | float64 | 3,896 | 9.87% |
| `s04f_36` | Actualmente, ¿está usted aportando a la Gestora? | float64 | 34,303 | 86.88% |
| `s05a_01a` | Recibe usted ingresos (rentas) por: A. ¿Jubilación (vejez)? Excluya el monto de la Renta Dignidad (MENSUAL) | float64 | 25,206 | 63.84% |
| `s05a_01b` | Recibe usted ingresos (rentas) por: B. ¿Benemérito? Excluya el monto de la Renta Dignidad (MENSUAL) | float64 | 34,034 | 86.19% |
| `s05a_01c` | Recibe usted ingresos (rentas) por: C. ¿Invalidez? (MENSUAL) | float64 | 9,336 | 23.64% |
| `s05a_01d` | Recibe usted ingresos (rentas) por: D. ¿Viudez, orfandad? (MENSUAL) | float64 | 3,895 | 9.86% |
| `s05a_01e` | Recibe usted ingresos (rentas) por: E. ¿Renta Dignidad? (MENSUAL) | float64 | 34,034 | 86.19% |
| `s05a_01e0` | Recibe usted ingresos (rentas) mensuales por: E. ¿Renta Dignidad? (MENSUAL) Monto (Bs) | float64 | 34,492 | 87.35% |
| `s05a_01f` | Recibe usted ingresos (rentas) mensuales por: F. ¿Aguinaldo de la Renta Dignidad? | float64 | 34,480 | 87.32% |
| `s05a_02a` | Además de los ingresos mencionados, recibe usted ingresos (rentas) mensuales por: A. ¿Intereses? (por depósitos bancarios, préstamos, etc.) | float64 | 12,467 | 31.57% |
| `s05a_02b` | Además de los ingresos mencionados, recibe usted ingresos (rentas) mensuales por: B. ¿Alquiler de propiedades inmuebles casas, etc.? | float64 | 12,467 | 31.57% |
| `s05a_02c` | Además de los ingresos mencionados, recibe usted ingresos (rentas) mensuales por: C. ¿Otras rentas? | float64 | 12,466 | 31.57% |
| `s05a_02ce` | Además de los ingresos mencionados, recibe usted ingresos (rentas) mensuales por: C. ¿Otras rentas? (Especifique) | object | 0 | 0.0% |
| `s05a_03a` | Durante los últimos doce meses, ¿recibió usted: (en montos anuales) A. Alquileres de propiedades agrícolas? | float64 | 12,466 | 31.57% |
| `s05a_03b` | Durante los últimos doce meses, ¿recibió usted: (en montos anuales) B. Dividendos, utilidades empresariales o retiros de sociedades? | float64 | 12,466 | 31.57% |
| `s05a_03c` | Durante los últimos doce meses, ¿recibió usted: (en montos anuales) C. Alquiler de maquinaria y/o equipo? | float64 | 12,466 | 31.57% |
| `s05a_04a` | Además de los ingresos mencionados anteriormente, durante los últimos doce meses, ¿recibió, usted… A. Indemnización por dejar algún trabajo? | float64 | 9,336 | 23.64% |
| `s05a_04b` | Además de los ingresos mencionados anteriormente, durante los últimos doce meses, ¿recibió, usted… B. Indemnización de Seguros? | float64 | 3,895 | 9.86% |
| `s05a_04c` | Además de los ingresos mencionados anteriormente, durante los últimos doce meses, ¿recibió, usted… C. Ingresos por anticrético de propiedades inmuebles, casas, etc.? | float64 | 12,466 | 31.57% |
| `s05a_04d` | Además de los ingresos mencionados anteriormente, durante los últimos doce meses, ¿recibió, usted… D. Otros ingresos extraordinarios (ej. Becas de estudio, derechos de autor, marcas y patentes)? | float64 | 3,895 | 9.86% |
| `s05b_05aa` | En los últimos doce meses, ¿recibió usted… A. Asistencia familiar por divorcio o separación? Monto (Bs) | float64 | 1 | 0.0% |
| `s05b_05ab` | En los últimos doce meses, ¿recibió usted… A. Asistencia familiar por divorcio o separación? Frecuencia | float64 | 38,446 | 97.37% |
| `s05b_05ba` | En los últimos doce meses, ¿recibió usted… B. Dinero de otras personas que residen en este u otro lugar del país? Monto (Bs) | float64 | 0 | 0.0% |
| `s05b_05bb` | En los últimos doce meses, ¿recibió usted… B. Dinero de otras personas que residen en este u otro lugar del país? Frecuencia | float64 | 37,794 | 95.72% |
| `s05b_05ca` | En los últimos doce meses, ¿recibió usted… C. Alimentos o regalos de otras personas que residen en este u otro lugar del país? Monto (Bs) | float64 | 0 | 0.0% |
| `s05b_05cb` | En los últimos doce meses, ¿recibió usted… C. Alimentos o regalos de otras personas que residen en este u otro lugar del país? Frecuencia | float64 | 38,099 | 96.49% |
| `s05b_06aa` | En los últimos doce meses, ¿recibió usted… A. Bono de Indigencia por ceguera o Bono mensual para personas por discapacidad? Monto (Bs) | float64 | 0 | 0.0% |
| `s05b_06ab` | En los últimos doce meses, ¿recibió usted… A. Bono de Indigencia por ceguera o Bono mensual para personas por discapacidad? Frecuencia | float64 | 39,300 | 99.53% |
| `s05b_06ae` | En los últimos doce meses, ¿recibió usted… A. Bono de Indigencia por ceguera o Bono mensual para personas por discapacidad? (Especifique) | object | 0 | 0.0% |
| `s05b_06ba` | En los últimos doce meses, ¿recibió usted… B. Otros bonos sociales  en efectivo? Monto (Bs) | float64 | 0 | 0.0% |
| `s05b_06bb` | En los últimos doce meses, ¿recibió usted… B. Otros bonos sociales  en efectivo? Frecuencia | float64 | 39,388 | 99.75% |
| `s05b_06be` | En los últimos doce meses, ¿recibió usted… B. Otros bonos sociales  en efectivo? (Especifique) | object | 0 | 0.0% |
| `s05b_06ca` | En los últimos doce meses, ¿recibió usted… C. Otros bonos sociales en especie? (VALORAR EN BS.) Monto (Bs) | float64 | 2 | 0.01% |
| `s05b_06cb` | En los últimos doce meses, ¿recibió usted… C. Otros bonos sociales en especie? (VALORAR EN BS.) Frecuencia | float64 | 30,398 | 76.99% |
| `s05b_06ce` | En los últimos doce meses, ¿recibió usted… C. Otros bonos sociales en especie? (VALORAR EN BS.) (Especifique) | object | 0 | 0.0% |
| `s05c_07` | En los últimos 12 meses, ¿recibió (...) dinero o encomiendas de otras personas que residen en el exterior del país? | float64 | 3,896 | 9.87% |
| `s05c_08` | ¿Con que frecuencia recibió el dinero o encomiendas mencionadas? | float64 | 38,506 | 97.52% |
| `s05c_09a` | Si recibió dinero, ¿cuál es el monto y en qué moneda lo recibió? Monto Bs. | float64 | 38,505 | 97.52% |
| `s05c_09b` | Si recibió dinero, ¿cuál es el monto y en qué moneda lo recibió? Moneda | float64 | 38,570 | 97.68% |
| `s05c_09be` | Si recibió dinero, ¿cuál es el monto y en qué moneda lo recibió? Moneda (Especifique) | object | 0 | 0.0% |
| `s05c_09aa` | En los últimos 12 meses, principalmente, ¿a través de qué medio recibió remesas ? | float64 | 38,570 | 97.68% |
| `s05c_10` | Si recibió en especie, valorar en Bolivianos. | float64 | 38,506 | 97.52% |
| `upm` | Unidad Primaria de Muestreo | object | 0 | 0.0% |
| `estrato` | Estrato | object | 0 | 0.0% |
| `factor` | Factor de expansion Rev2025 | float64 | 0 | 0.0% |
| `tipohogar` | Tipo de hogar recodificado | float64 | 0 | 0.0% |
| `niv_ed` | Nivel educativo detallado | float64 | 2,000 | 5.07% |
| `niv_ed_g` | Nivel educativo general | float64 | 2,000 | 5.07% |
| `cmasi` | Condición de Matriculación y Asistencia | float64 | 2,000 | 5.07% |
| `educ_prev` | Años de estudio previos | float64 | 37,231 | 94.29% |
| `aestudio` | Años de estudio | float64 | 2,000 | 5.07% |
| `cobersalud` | Cobertura de Seguro de Salud | float64 | 0 | 0.0% |
| `hnv_ult_a` | Hijos nacidos vivos en el último año | float64 | 28,109 | 71.19% |
| `quienatenparto` | Personal de atención del parto | float64 | 36,898 | 93.45% |
| `cob_op` | Grupo Ocupacional ocupación principal | float64 | 19,716 | 49.93% |
| `caeb_op` | Clasificación de Actividad Económica de Bolivia Ocupacion principal | float64 | 19,716 | 49.93% |
| `caeb_os` | Clasificación de Actividad Económica de Bolivia Ocupacion secundaria | float64 | 38,009 | 96.26% |
| `pet` | Poblacion en edad de trabajar 14 o más años | float64 | 0 | 0.0% |
| `pea` | Poblacion Activa | float64 | 3,896 | 9.87% |
| `pei` | Poblacion Inactiva | float64 | 3,896 | 9.87% |
| `condact` | Condicion de Actividad Ocupacion Principal | float64 | 3,896 | 9.87% |
| `phrs` | Horas trabajadas a la semana Ocupación Principal | float64 | 19,716 | 49.93% |
| `shrs` | Horas trabajadas a la semana Ocupación Secundaria | float64 | 38,009 | 96.26% |
| `tothrs` | Horas trabajadas a la semana | float64 | 19,716 | 49.93% |
| `yprilab` | Ingreso laboral Ocupación Principal (Bs/Mes) | float64 | 22,489 | 56.96% |
| `yseclab` | Ingreso laboral Ocupación Secundaria (Bs/Mes) | float64 | 38,339 | 97.1% |
| `ylab` | Ingreso laboral (Bs/Mes) | float64 | 22,447 | 56.85% |
| `ynolab` | Ingreso no laboral (Bs/Mes) | float64 | 0 | 0.0% |
| `yper` | Ingreso personal (Bs/Mes) | float64 | 0 | 0.0% |
| `yhog` | Ingreso del hogar (Bs/Mes) | float64 | 21 | 0.05% |
| `yhogpc` | Ingreso percápita del hogar (Bs/Mes) | float64 | 21 | 0.05% |
| `z` | Línea de pobreza (Bs/persona/mes) | float64 | 0 | 0.0% |
| `zext` | Línea de pobreza extrema o de indigencia (bs/persona/mes) | float64 | 0 | 0.0% |
| `p0` | Pobreza por ingreso | float64 | 21 | 0.05% |
| `p1` | Brecha de pobreza por ingreso | float64 | 21 | 0.05% |
| `p2` | Magnitud de pobreza por ingreso | float64 | 21 | 0.05% |
| `pext0` | Pobreza extrema o indigencia por ingreso | float64 | 21 | 0.05% |
| `pext1` | Brecha de pobreza extrema por ingreso | float64 | 21 | 0.05% |
| `pext2` | Magnitud de pobreza extrema por ingreso | float64 | 21 | 0.05% |
