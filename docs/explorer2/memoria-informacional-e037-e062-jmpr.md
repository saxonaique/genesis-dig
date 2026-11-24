# Génesis DIG — Archivo consolidado de experimentos de memoria informacional (E037–E062)

**Investigador y autoría:** José María Pérez Rodríguez (JMPR)  
**Proyecto:** Génesis DIG — Nivel 0 / Explorer  
**Objeto de este documento:** conservar la línea experimental realizada sobre el espacio informacional reconstruido por Perplexity, centrada en persistencia, diferenciación, recuperación y conservación de información histórica.

> **Alcance y procedencia.** Los resultados numéricos de E037–E062 recogidos aquí fueron comunicados durante la investigación a partir de ejecuciones realizadas en el entorno de Perplexity. No deben presentarse como reproducidos independientemente por ChatGPT. La función de dinámica compartida por Perplexity no garantiza por sí sola que se conserve todo el código, los protocolos y los scripts que generaron cada resultado. Antes de atribuir una reproducción al Explorer original, hay que identificar y verificar el archivo exacto del motor y el código completo de cada experimento.

## 1. Modelo de campo de referencia comunicado

- Rejilla de 32 × 32 puntos.
- Inicialización: distribución normal con media 0 y desviación típica 0,01.
- Fronteras periódicas.
- Generador: `np.random.default_rng(seed)`.
- Parámetros comunicados: `info_rate=0.08`, `entropy_rate=0.012`, `a=0.10`.
- Cada punto interactúa con el promedio de sus cuatro vecinos ortogonales, calculado mediante `np.roll`.
- Dinámica compartida:

```python
f = p + 0.08*(l-p) + 0.012*tanh((p-l)/0.10)
```

Aquí `p` es el estado local y `l` el promedio de los cuatro vecinos. Esta expresión se conserva como referencia del código compartido, no como prueba de que todos los experimentos posteriores usaran exactamente el mismo script completo.

## 2. Resultados experimentales

### E037 — Persistencia de consecuencias

**Diseño comunicado:** campo evolucionado hasta el paso 5000; perturbación gaussiana localizada durante 100 pasos; retirada de la perturbación y evolución posterior durante 900 pasos.

**MAE perturbado frente a control:**

| Tiempo tras retirar la perturbación | MAE |
|---:|---:|
| 0 | 1.0379 |
| 10 | 1.0308 |
| 50 | 0.9970 |
| 100 | 0.9478 |
| 200 | 0.8628 |
| 500 | 0.7275 |
| 900 | 0.6504 |

**Lectura:** la diferencia entre el campo perturbado y el control persiste durante la evolución posterior, aunque se reduce aproximadamente un 37,3 %. No permite separar por sí sola memoria de sensibilidad a condiciones iniciales o divergencia de trayectorias.

### E038 — Memoria funcional candidata

**Diseño comunicado:** dos campos inicialmente idénticos; A recibe una historia perturbada y B permanece como control. Tras evolucionar hasta el paso 6000, ambos reciben la misma señal de prueba.

**Resultados iniciales:** MAE pre-señal A/B = 0.639; MAE post-señal = 0.606; respuesta media A = 0.0642 y B = 0.00836; MAE entre respuestas = 0.0599; correlación entre respuestas = 0.2847; cociente de respuesta A/B ≈ 7,7.

**Ampliación comunicada:** cinco semillas × tres magnitudes (0,1; 0,5; 1,0). Cocientes A/B:

| Semilla | 0,1 | 0,5 | 1,0 |
|---:|---:|---:|---:|
| 7 | 2.44 | 7.68 | 13.73 |
| 21 | 2.93 | 7.99 | 14.53 |
| 42 | 1.88 | 3.44 | 6.72 |
| 99 | 1.70 | 4.23 | 7.09 |
| 2024 | 2.67 | 7.61 | 13.88 |

Los 15 cocientes fueron superiores a 1; rango 1,70–14,53; media ≈ 6,57.

**Lectura:** indicio de respuesta dependiente de la historia y posible dependencia de la magnitud de la experiencia. El denominador pequeño y la ausencia inicial de un contrafactual completo impiden atribuir todo el efecto a memoria funcional. El control recomendado fue comparar, para cada estado previo, copias idénticas con señal y sin señal.

### E039 — Origen estructural de la sensibilización

**Resultados comunicados antes de la señal:**

| Medida | A: historia | B: control |
|---|---:|---:|
| Media | 0.573 | −0.067 |
| Desviación típica | 1.381 | 0.187 |
| Asimetría | 3.074 | −0.037 |
| Curtosis | 8.875 | −0.285 |
| Autocorrelación espacial | 0.996 | 0.738 |

Sensibilidad local en nueve posiciones: A ≈ 1,56–1,57 × 10⁻²; B ≈ 6,16–6,40 × 10⁻⁴; cocientes 24,46–25,32. Correlación comunicada entre diferencias estructurales y respuesta A: 0,9647.

La dinámica derivada compartida fue:

```
f' = f - 0.08d + 0.012 tanh(10d)
```

Su derivada respecto a d es `-0.08 + 0.12 sech²(10d)`: positiva en d=0 (0,04), se anula aproximadamente en |d|=0,0659 y es negativa para diferencias mayores.

**Lectura:** las estructuras de A y B eran muy distintas y la sensibilidad también. La correlación no demuestra causalidad; la autocorrelación espacial no equivale por sí sola a memoria.

### E040 — Control de varianza y autocorrelación

El primer intento de generar campos sintéticos con varianza y autocorrelación controladas no fue válido; se conserva como intento no concluyente.

**Versión corregida, cuatro grupos comunicados:**

| Grupo | Varianza | Autocorrelación | Sensibilidad |
|---|---:|---:|---:|
| A | 0.10 | 0.539 | 3.62e−4 |
| B | 10 | 0.539 | 6.71e−5 |
| C | 0.10 | 0.890 | 1.49e−4 |
| D | 10 | 0.890 | 5.13e−5 |

Correlaciones comunicadas: −0,79 para varianza y −0,46 para autocorrelación, calculadas sobre cuatro medias de grupo. No son estimaciones robustas. Además, una perturbación fija de 0,05 representa magnitudes relativas distintas según la varianza.

**Lectura:** resultado exploratorio; no permite establecer una ley general sobre varianza o autocorrelación.

### E041 — Sensibilidad dependiente de la historia

Dos campos inicialmente idénticos: A con historia y B control. Cocientes de sensibilidad absoluta y relativa:

| Paso | Absoluta A/B | Relativa A/B | Desv. típica A/B |
|---:|---:|---:|---:|
| 6000 | 10.32 | 2.37 | 1.381 / 0.187 |
| 6200 | 9.02 | 2.09 | 1.272 / 0.188 |
| 6400 | 8.10 | 1.88 | 1.186 / 0.188 |
| 6600 | 7.39 | 1.73 | 1.118 / 0.188 |
| 6800 | 6.81 | 1.60 | 1.063 / 0.189 |
| 7000 | 6.33 | 1.50 | 1.017 / 0.189 |

**Lectura:** compatible con un estado dependiente de la historia y con una sensibilización que disminuye gradualmente. No demuestra por sí solo memoria funcional.

### E042 — Diferenciación espacial dependiente de la historia

A recibió historia en posición 1; B, en posición 2; C no recibió historia.

| Campo | Respuesta posición 1 | Respuesta posición 2 |
|---|---:|---:|
| A | 9.72e−3 | 2.22e−2 |
| B | 2.23e−2 | 9.83e−3 |
| C | ≈ 7.64e−3 | ≈ 7.64e−3 |

Cociente pos1/pos2 de A ≈ 0,44; de B ≈ 2,27.

**Lectura:** diferenciación espacial asociada a la historia, con respuesta cruzada preferente. La respuesta en la posición histórica seguía siendo superior al control; no debe describirse como inhibición respecto al control.

### E043 — Diferenciación del orden inicial

A recibió pos1→pos2; B, pos2→pos1; C no recibió historia. Respuesta en pos1: A = 2.2507e−2; B = 2.1548e−2; C = 7.6354e−3. Diferencia A−B = 9.59e−4 (≈ 4,45 %).

**Lectura:** indicio pequeño de efecto del orden, todavía no robusto.

### E044 — Consolidación del orden temporal

Cinco semillas (7, 21, 42, 99, 2024). Cocientes pos1/pos2:

| Semilla | A: pos1 primero | B: pos2 primero |
|---:|---:|---:|
| 7 | 1.0535 | 0.9515 |
| 21 | 1.0470 | 0.9476 |
| 42 | 1.0725 | 0.9455 |
| 99 | 1.0574 | 0.9458 |
| 2024 | 1.0461 | 0.9463 |

En las cinco semillas, la respuesta fue mayor en la posición de la primera perturbación. Patrón consistente en las diez comparaciones.

**Lectura:** compatible con sensibilidad al orden y contrario a una explicación simple de recencia, siempre que la igualación temporal comunicada sea correcta. No excluye otros mecanismos.

### E045 — Recuperación asociativa inicial

Diez casos: cinco semillas y dos órdenes; consulta en posición neutra; validación leave-one-out. Resultado comunicado: 8/10 (80 %). Errores en semillas 7 y 2024.

**Lectura:** primer indicio de que una consulta puede distinguir historias. Muestra pequeña; faltan detalles completos del clasificador y las dos órdenes de cada semilla no son réplicas independientes.

### E046 — Ampliación de recuperación

Diez semillas nuevas (201–210), veinte casos.

| Clasificador | Aciertos | Precisión | IC Wilson comunicado |
|---|---:|---:|---:|
| Pearson | 13/20 | 65 % | [0.4329, 0.8188] |
| Euclídeo | 14/20 | 70 % | [0.4810, 0.8545] |

Ambos resultados puntuales superan el 50 %, pero los intervalos incluyen el azar. Los clasificadores comparten casos y los dos órdenes de una semilla pueden estar relacionados.

**Lectura:** indicio preliminar, no concluyente.

### E047 — Generalización a semillas nuevas

Entrenamiento con semillas 201–210 y prueba con semillas 211–220, comunicadas como completamente nuevas. Precisión: 65 % en entrenamiento y 65 % en prueba; IC Wilson comunicado para ambos: [0.4329, 0.8188].

**Lectura:** indicio de transferencia a semillas nuevas. No descarta por completo selección previa de características o dependencias en la unidad de análisis.

### E048 — Componente que transporta la información

Tres representaciones: vector completo, magnitud sola y patrón espacial normalizado. Las tres obtuvieron 13/20 = 65 %, IC Wilson [0.4329, 0.8188].

**Lectura:** no identifica qué componente contiene la señal. Igual precisión no significa predicciones idénticas ni equivalencia estadística; habría que comparar aciertos y errores caso a caso.

### E049 — Acumulación progresiva

Tres experiencias en posiciones P1/P2/P3, diez semillas, intensidad y duración iguales. Consultas después de cada etapa, usando copias de estado para evitar contaminar la evolución y controles sin señal.

| Etapa | Aciertos | Precisión | IC Wilson |
|---|---:|---:|---:|
| P1 | 16/40 | 40 % | [0.2635, 0.5540] |
| P1 + P2 | 20/40 | 50 % | [0.3520, 0.6480] |
| P1 + P2 + P3 | 36/40 | 90 % | [0.7695, 0.9604] |

**Lectura:** la precisión comunicada aumenta con el número de experiencias. Es compatible con acumulación, pero podría reflejar magnitud global o cantidad de perturbaciones, no necesariamente identidad de las experiencias.

### E050 — Contenido con igual número de experiencias

Historias H12=P1+P2, H13=P1+P3, H23=P2+P3 y H0 control; diez semillas.

| Representación | Resultado |
|---|---:|
| Vector completo | 40/40 = 100 % |
| Magnitud | 29/40 = 72,5 %; IC [0.5716, 0.8389] |
| Patrón espacial normalizado | 40/40 = 100 % |

**Lectura:** indicio de que la identidad espacial aporta información más allá del número de experiencias. No demuestra que la señal resida exclusivamente en la estructura espacial; magnitud también contiene señal parcial. Tener en cuenta posibles dependencias de LOOCV.

### E051 — Tres experiencias entre cuatro posiciones

Historias H123, H124, H134, H234 y H0. Diez semillas de entrenamiento y prueba comunicada con semillas nuevas.

| Representación | LOOCV | Prueba con semillas nuevas |
|---|---:|---:|
| Vector completo | 50/50 = 100 % | 25/25 = 100 % |
| Magnitud | 37/50 = 74 % | 16/25 = 64 %; IC [0.4452, 0.7975] |
| Patrón espacial | 50/50 = 100 % | 25/25 = 100 %; IC [0.9286, 1] |

**Lectura:** transferencia preliminar en estas condiciones. El diseño identifica qué posición quedó sin activar; no equivale a una demostración general de memoria.

### E052 — Cuatro experiencias entre cinco posiciones

Historias H1234, H1235, H1245, H1345, H2345 y H0. Diez semillas; 60 casos por conjunto, según el informe.

- Vector completo: 60/60 = 100 % en entrenamiento y prueba.
- Magnitud: 60/60 en entrenamiento; 44/60 = 73,33 % en prueba; IC [0.6099, 0.8287].
- Patrón espacial: 60/60 = 100 % en entrenamiento y prueba; IC [0.9398, 1].

**Lectura:** todas las historias activas son combinaciones de cuatro entre cinco posiciones. Clasificarlas puede equivaler a identificar la única posición ausente. No demuestra memoria general.

### E053 — Cinco experiencias entre seis posiciones

Historias H12345, H12346, H12356, H12456, H13456, H23456 y H0. Diez semillas; 70 casos por conjunto.

- Vector completo: 70/70 = 100 %.
- Magnitud: 70/70 en entrenamiento; 43/70 = 61,43 % en prueba; IC [0.4972, 0.7195].
- Patrón espacial: 70/70 = 100 % en entrenamiento y prueba; IC [0.9480, 1].

**Lectura:** persiste el límite del diseño de una única posición ausente.

### E054 — Seis experiencias entre siete posiciones

Historias H123456, H123457, H123467, H123567, H124567, H134567, H234567 y H0. Diez semillas; 80 casos.

- Vector completo: 80/80 = 100 %.
- Patrón espacial: 80/80 = 100 %.
- Magnitud: 57/80 = 71,25 %; IC [0.6054, 0.8001].

**Lectura:** mismo límite estructural: cada historia activa deja una única posición sin activar. No equivale a una prueba general de memoria.

### E055 — Historias variables y combinaciones no triviales

Siete posiciones. Historias: H123, H145, H267, H356 (tres experiencias); H1245, H1367, H2457, H3456 (cuatro); H12345 y H13567 (cinco); más H0: once clases. Una historia inicialmente descrita como H2467 fue corregida antes de ejecutar a H13567.

Veinte semillas de entrenamiento y veinte nuevas de prueba; 220 casos por conjunto.

| Representación | Entrenamiento | Prueba |
|---|---:|---:|
| Vector completo | 220/220 = 100 % | 219/220 = 99,55 %; IC [0.9747, 0.9992] |
| Magnitud | 220/220 = 100 % | 118/220 = 53,64 %; IC [0.4704, 0.6011] |
| Patrón espacial | 220/220 = 100 % | 219/220 = 99,55 %; IC [0.9747, 0.9992] |

Evaluación dentro de grupos de igual cantidad de experiencias:

- Tres experiencias, cuatro clases, azar 25 %: vector 100 %, magnitud 67,5 %, espacial 100 %.
- Cuatro experiencias, cuatro clases, azar 25 %: vector 100 %, magnitud 86,25 %, espacial 100 %.
- Cinco experiencias, dos clases, azar 50 %: todas las representaciones 100 %.

**Lectura:** evidencia fuerte, dentro del diseño comunicado, de que la estructura espacial permite discriminar combinaciones de experiencias en semillas nuevas. No debe elevarse a demostración general de memoria robusta y escalable. El único error de clasificación completa no quedó identificado en el informe.

### E056 — Reconocimiento del orden temporal

Siete historias: H0, H12=P1→P2, H21=P2→P1, H13=P1→P3, H31=P3→P1, H23=P2→P3, H32=P3→P2. Veinte semillas de entrenamiento y veinte nuevas de prueba. Igual intensidad, duración e intervalo; consulta en posición neutra.

Resultados comunicados: entrenamiento 140/140 = 100 %; prueba 119/140 = 85 % para vector y patrón espacial; magnitud 60/140 = 42,86 %. Comparaciones binarias dentro del contexto de siete clases: H12/H21 75 %, H13/H31 100 %, H23/H32 72,5 %.

**Lectura:** posible sensibilidad al orden. El mismo tiempo total no elimina por sí solo la recencia. Distinguir las cifras de clasificación multiclase de las evaluaciones binarias posteriores.

### E057 — Separación de orden y recencia: primera evaluación

Cinco condiciones: H0, H12, H21, P2_only y P1_only.

Clasificación binaria directa H12/H21: vector 47 % entrenamiento y 41 % prueba; magnitud 52 % y 50 %; espacial 47 % y 41 %. Clasificación cruzada (entrenar H12/H21 y probar P2_only/P1_only): 0 % en las tres representaciones.

**Lectura inicial:** no concluyente; el procedimiento no replicaba el de E056. Un 0 % no demuestra reconocimiento invertido sin matriz de confusión y predicciones.

**Auditoría posterior E056–E057:** al reproducir el protocolo de siete clases con LOOCV se obtuvo 243/280 = 86,79 % global; H12 26/40 = 65 %; H21 33/40 = 82,5 %. La evaluación binaria directa H12/H21, con el mismo procedimiento, dio 59/80 = 73,75 %: H12→H12 26, H12→H21 14; H21→H12 7, H21→H21 33. Las predicciones coincidían entre E056 y E057 cuando se utilizaba el mismo procedimiento.

**Lectura auditada:** la discrepancia inicial estaba en el método de clasificación, no en los datos del campo. Hay discriminación del orden en ese protocolo, con asimetría entre clases; no elimina la hipótesis de recencia.

### E058 — Incorporación incremental inicial

Fase 1: H_A = P1→P2; H0 control. Fase 2: H_C = P3→P4; H_B = primera historia más segunda fase. Resultados comunicados:

- H_A frente a H0: 40/40 = 100 %.
- H_A frente a H_B: 40/40 = 100 %.
- H_B frente a H_C: 40/40 = 100 %.
- Clasificación completa H0/H_A/H_B/H_C: 80/80 = 100 % en entrenamiento y prueba.

**Lectura:** demuestra distinguibilidad de estados en el protocolo comunicado. No demuestra por sí sola recuperación de identidad histórica desde el estado extendido.

### E059 — Cantidad de experiencias

Cuatro clases correspondientes a etapas de 1, 2, 4 y 8 experiencias. Resultado comunicado: 40/40 = 100 % en cada etapa; azar 25 %; IC Wilson [0.9124, 1].

**Lectura:** reconocimiento de cuántas experiencias recibió el campo, no de cuáles fueron. No prueba memoria de contenido.

### E060 — Historias con igual número de experiencias

Nueve clases: H0 y ocho historias, cada una con cuatro experiencias y ocho posiciones posibles. Balance: cada posición aparece cuatro veces.

- Momento 1: 179/180 = 99,44 %, azar 11,11 %; un error H4→H5.
- Momento 2: ocho comparaciones original frente a extendida, cada una 20/20 = 100 %.

**Lectura revisada:** evidencia de diferenciación entre historias con igual cantidad de experiencias y entre estados originales y extendidos. No quedó demostrado que se recuperase la identidad de la historia original desde el estado extendido.

### E061 — Recuperación de historia original desde estado extendido

Clasificador entrenado con ocho historias originales de cuatro experiencias más H0, evaluado sobre estados extendidos de ocho experiencias (historia original más cuatro complementarias).

Patrón espacial normalizado: 20/180 = 11,11 %, igual al azar; IC Wilson [0.0731, 0.1654]. H0: 20/20; historias H1–H8: 0/160.

Matriz de confusión comunicada:

- H1→H5: 19; H1→H8: 1.
- H2→H7: 20.
- H3→H6: 20.
- H4→H0: 20.
- H5→H7: 12; H5→H6: 8.
- H6→H3: 20.
- H7→H4: 20.
- H8→H7: 18; H8→H1: 2.

**Lectura:** el clasificador entrenado en estados originales no se transfiere a estados extendidos. Resultado negativo para la transferencia directa; no demuestra que la información histórica haya sido destruida. Puede existir un cambio de representación o de distribución.

### E062 — Adaptación al estado extendido

Clasificador entrenado sobre estados extendidos, etiquetados por historia original, y probado con semillas nuevas. Resultado comunicado: 80/80 = 100 %, IC Wilson [0.9542, 1], azar 12,5 %.

Similitud espacial global original-extendido:

| Historia | Similitud original-extendido |
|---|---:|
| H1 | 0.9990 / 0.9993 |
| H2 | 0.9978 / 0.9980 |
| H3 | 0.9980 / 0.9993 |
| H4 | 0.9989 / 0.9986 |
| H5 | 0.9988 / 0.9990 |
| H6 | 0.9986 / 0.9993 |
| H7 | 0.9985 / 0.9993 |
| H8 | 0.9986 / 0.9990 |

Los pares muestran similitudes antes y después, respectivamente.

**Lectura:** el clasificador adaptado al régimen extendido recuperó la etiqueta de la historia original según el protocolo comunicado. En conjunto con E061, esto sugiere cambio de representación o domain shift, no necesariamente destrucción de la información. La similitud global cercana a 1 no demuestra por sí sola que la información discriminativa esté concentrada en un componente pequeño. Deben verificarse separación por semillas, ausencia de fuga de datos y validez de las etiquetas.

## 3. Síntesis de la línea de memoria

La secuencia E037–E062 exploró progresivamente:

1. Persistencia de diferencias después de retirar una perturbación (E037).
2. Respuestas distintas ante una misma señal según la historia previa (E038–E041).
3. Diferenciación espacial y posible sensibilidad al orden (E042–E044).
4. Recuperación de historias mediante clasificadores externos y evaluación con semillas nuevas (E045–E058).
5. Distinción entre cantidad, contenido y orden de experiencias (E049–E060).
6. Dificultad de transferir directamente un clasificador de estados originales a extendidos y recuperación al adaptar el clasificador al nuevo régimen (E061–E062).

### Conclusión prudente

Los resultados comunicados ofrecen indicios relevantes de que la dinámica del espacio informacional conserva consecuencias de experiencias previas, genera estados distinguibles y permite recuperar información histórica mediante clasificadores externos, incluso en algunas pruebas con semillas nuevas. También muestran límites importantes: confusión entre memoria y sensibilidad, posibles señales triviales de diseño, dependencia entre observaciones, cambios de representación y necesidad de auditoría del código y de los protocolos.

**No se ha demostrado en esta línea que el campo aprenda operaciones lógicas ni que utilice autónomamente la información almacenada para responder preguntas nuevas.** Esa cuestión pertenece a otra línea experimental y queda fuera del alcance de este archivo.

## 4. Estado y conservación

- E037–E062 quedan archivados como línea de investigación de memoria informacional.
- Los valores y resultados se conservan como resultados comunicados, no como reproducciones independientes.
- No modificar retrospectivamente los resultados originales; las correcciones y auditorías se registran como tales.
- No atribuir automáticamente todos los resultados a Explorer 0.4.6 ni al archivo original de Explorer sin verificar qué código se ejecutó en cada experimento.
- La línea de aprendizaje lógico E063–E071 se mantiene separada y no forma parte de este archivo.
- Cualquier continuación debe comenzar identificando el código exacto, parámetros, semillas, entradas, cronograma, decodificador y scripts de análisis.

---

**Autoría:** José María Pérez Rodríguez (JMPR)  
**Génesis DIG — Archivo histórico de experimentación sobre memoria informacional.**
