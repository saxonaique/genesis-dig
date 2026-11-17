# Informe de caracterización experimental de Explorer 2 — Primera batería

**Proyecto:** Génesis DIG  
**Motor evaluado:** Explorer 2 v0.4.6  
**Autor:** José María Pérez Rodríguez (JMPR)  
**Fecha de cierre:** 17 de noviembre de 2026  
**Estado:** Primera batería experimental cerrada

---

## 1. Objeto y alcance

Este informe consolida cinco experimentos realizados para caracterizar el comportamiento básico de Explorer 2 v0.4.6 antes de investigar mecanismos informacionales más complejos en el marco de Génesis DIG.

El documento separa expresamente:

- **Resultados observados:** datos comunicados de las ejecuciones.
- **Interpretación:** lectura de esos resultados dentro de las dinámicas ensayadas.
- **Límites:** conclusiones que todavía no pueden sostenerse y aspectos no investigados.

Los resultados proceden de los registros e informes de ejecución aportados para esta batería. Este documento no afirma que el autor del informe haya vuelto a ejecutar los scripts.

## 2. Principios metodológicos

1. No se modificó Explorer 2 para obtener los resultados de esta batería.
2. Cada prueba partió de una pregunta experimental concreta.
3. Se mantuvieron registrados los parámetros y las condiciones iniciales.
4. Se distinguieron observaciones, interpretaciones y conclusiones.
5. Los resultados no se consideran una confirmación de DIG.
6. La caracterización obtenida servirá como referencia para futuras investigaciones, sin predeterminar qué debe producir el motor.

## 3. Experimento 1 — Estabilidad temporal

**Pregunta:** ¿Puede Explorer ejecutar una simulación prolongada y mantener una evolución temporal y un estado interno coherentes?

### Configuración

- Malla: 16 × 16.
- Frontera: periódica.
- Condición inicial: fondo 0,1 con una concentración gaussiana centrada.
- Dinámica: `DiffusionDynamics`.
- Coeficiente de difusión: D = 0,01.
- Paso temporal: dt = 0,001.
- Pasos: 1.000.
- Ruido: desactivado.
- Memoria: `full`.

### Resultados comunicados

- Estado: `completed`; 1.000 de 1.000 pasos.
- Tiempo de ejecución: 0,097 s.
- Tiempo final: aproximadamente 1,0.
- Sin NaN ni infinitos.
- Suma inicial: 27,61059306181753.
- Suma final: 27,610593061817532.
- Media: 0,107854, estable.
- Máximo: 0,438317 → 0,155209.
- Norma: 1,860416 → 1,737551.

### Interpretación

La ejecución mantuvo estabilidad numérica y conservación de la suma dentro de la precisión de cálculo comunicada. El máximo y la norma descendieron durante la evolución, de acuerdo con la dispersión difusiva esperada.

### Límites

La prueba caracteriza una configuración concreta. No estudia pasos temporales mayores, perturbaciones extremas, otras condiciones de frontera ni todos los regímenes posibles del motor.

## 4. Experimento 2 — Interacción entre concentraciones

**Pregunta:** ¿Cómo evolucionan dos concentraciones en un mismo campo bajo difusión?

### Configuración

- Malla: 32 × 32; frontera periódica.
- Fondo: 0,1.
- Dos gaussianas de amplitud 0,4 y sigma 0,05.
- Centros: (0,3; 0,3) y (0,7; 0,7).
- D = 0,01; dt = 0,001; 1.000 pasos.
- Ruido desactivado; memoria `full`.

### Resultados comunicados

- Estado: `completed`; 1.000 de 1.000 pasos.
- Tiempo: 0,1335 s.
- Suma inicial y final comunicadas: 115,26796349460102.
- Valores finitos y simetría conservada.
- Picos: 0,4984 → 0,1449.
- Distancia entre centroides (índices de malla): 18,098 → 18,026.
- Valor en el punto medio: 0,1000005 → 0,115235.
- Correlación con las gaussianas iniciales: 0,696 → 0,435.

### Interpretación

Las dos concentraciones se dispersaron y el espacio intermedio se rellenó. La pequeña variación de la distancia entre centroides no demuestra atracción; es una medida geométrica de la evolución de los perfiles bajo difusión.

### Límites

No se ensayaron interacciones no lineales ni mecanismos de atracción o repulsión efectiva. La distancia entre centroides debe interpretarse con cautela a medida que los perfiles se ensanchan.

## 5. Experimento 3 — Influencia de la intensidad inicial

**Pregunta:** ¿Cómo influye la intensidad inicial en la evolución temporal bajo difusión?

### Configuración

Tres ejecuciones independientes con:

- Malla: 32 × 32; frontera periódica.
- Fondo: 0,1.
- Una gaussiana centrada en (0,5; 0,5), sigma 0,05.
- Amplitudes del exceso: 0,2; 0,4; 0,8.
- D = 0,01; dt = 0,001; 1.000 pasos.
- Ruido desactivado; memoria `full`.

### Resultados comunicados

- Las tres ejecuciones completaron los 1.000 pasos.
- Las sumas se conservaron dentro de la precisión numérica.
- No se registraron NaN ni infinitos.
- Las proporciones del exceso sobre el fondo se mantuvieron en relación 1:2:4 en los pasos registrados: 0, 100, 250, 500, 750 y 1.000.
- Los máximos descendieron y la norma comunicada decreció.

### Interpretación

En las amplitudes y condiciones ensayadas, la respuesta mantuvo la proporcionalidad esperada de una dinámica de difusión lineal.

### Límites

No se exploraron amplitudes extremas ni posibles regímenes no lineales o de saturación. La conclusión se limita al intervalo probado.

## 6. Experimento 4 — Influencia de la distancia inicial

**Pregunta:** ¿Cómo influye la separación inicial entre dos concentraciones en su evolución bajo difusión?

### Configuración

- Malla: 32 × 32; frontera periódica.
- Fondo: 0,1.
- Dos gaussianas idénticas, amplitud 0,4 y sigma 0,05.
- D = 0,01; dt = 0,001; 1.000 pasos.
- Tres separaciones horizontales:
  - A: (0,35; 0,50) y (0,65; 0,50), separación 0,30.
  - B: (0,40; 0,50) y (0,60; 0,50), separación 0,20.
  - C: (0,45; 0,50) y (0,55; 0,50), separación 0,10.
- Ruido desactivado; memoria `full`.

### Resultados comunicados

Las tres ejecuciones completaron los 1.000 pasos y conservaron la suma dentro de la precisión numérica.

**Valor puente:**

| Paso | A | B | C |
|---:|---:|---:|---:|
| 0 | 0,1206 | 0,2361 | 0,5051 |
| 100 | 0,1459 | 0,2464 | 0,3954 |
| 250 | 0,1620 | 0,2314 | 0,3072 |
| 500 | 0,1643 | 0,2032 | 0,2373 |
| 750 | 0,1590 | 0,1832 | 0,2024 |
| 1.000 | 0,1529 | 0,1694 | 0,1816 |

**Distancia entre centroides, en índices de malla:**

| Caso | Inicial | Paso 500 | Paso 1.000 |
|---|---:|---:|---:|
| A | 9,603 | 10,204 | 11,140 |
| B | 6,459 | 7,862 | 9,282 |
| C | 3,758 | 6,277 | 8,075 |

Durante el análisis se corrigió la interpretación de los ejes para coordenadas generadas con `indexing='ij'`: el primer índice corresponde al primer eje de la matriz. La corrección afectó al análisis externo, no al motor.

### Interpretación

La separación inicial condicionó el solapamiento y la evolución del valor puente. Las distancias entre centroides medidas aumentaron en los tres casos; este resultado es compatible con la expansión de los perfiles difusivos, pero no debe interpretarse por sí solo como repulsión.

### Límites

El cálculo de centroides requiere cautela cuando los perfiles se solapan y se ensanchan. No se investigaron separaciones próximas al tamaño de la malla ni otros efectos de la frontera periódica.

## 7. Experimento 5 — Relajación y evolución de una perturbación localizada

**Pregunta:** ¿Cómo evoluciona un campo después de recibir una perturbación localizada y cuánto tarda en aproximarse a una distribución espacial homogénea?

### Configuración

- Malla: 32 × 32; frontera periódica.
- Fondo: 0,1.
- Una gaussiana de amplitud 0,4, sigma 0,05, centrada en (0,5; 0,5).
- D = 0,01; dt = 0,001; 2.000 pasos.
- Ruido desactivado; memoria `full`.
- No se introdujeron nuevas perturbaciones durante la ejecución.

### Resultados comunicados

- Estado: `completed`; 2.000 de 2.000 pasos.
- Tiempo: 0,233 s.
- Suma inicial: 108,83398175455193.
- Suma final: 108,8339817545519.
- Masa del exceso comunicada: 6,4339817545519, conservada.
- Valores finitos: `true`.

| Paso | Máximo | Norma del exceso | Radio efectivo |
|---:|---:|---:|---:|
| 0 | 0,4628 | 1,1344 | 2,2627 |
| 100 | 0,3148 | 0,8503 | 3,0358 |
| 250 | 0,2316 | 0,6583 | 3,9192 |
| 500 | 0,1796 | 0,5092 | 5,0595 |
| 1.000 | 0,1444 | 0,3790 | 6,7757 |
| 1.500 | 0,1307 | 0,3154 | 8,0762 |
| 2.000 | 0,1235 | 0,2770 | 9,0887 |

### Aclaración de las métricas espaciales

Las métricas `var_x` y `var_y` del informe de ejecución son segundos momentos espaciales ponderados por el exceso respecto al fondo, calculados alrededor del centroide de ese exceso:

`exceso_i = max(rho_i - 0,1, 0)`

`var_x = sum((x_i - c_x)^2 * exceso_i) / sum(exceso_i)`

La expresión equivalente se utiliza para el eje y. Por tanto, estas métricas describen la extensión espacial de la perturbación; no son la varianza de los valores del campo.

Los valores comunicados crecieron simétricamente:

| Paso | Segundo momento X | Segundo momento Y |
|---:|---:|---:|
| 0 | 2,560 | 2,560 |
| 500 | 12,799 | 12,799 |
| 1.000 | 22,955 | 22,955 |
| 2.000 | 41,302 | 41,302 |

El aumento indica expansión espacial del exceso, no un aumento de las diferencias entre los valores de campo.

### Conservación y estado homogéneo

La media global conservada es aproximadamente 0,106283. En una malla periódica con difusión conservativa, el estado perfectamente homogéneo compatible con la masa total sería esa media global, no el fondo inicial de 0,1.

La ejecución no demuestra que ese estado homogéneo se haya alcanzado en 2.000 pasos. La disminución de la norma del exceso es un dato comunicado, pero no debe identificarse automáticamente con una medida directa de homogeneización. Para medir esta última de forma directa convendría registrar la varianza de los valores del campo respecto a su media global o la norma de la desviación respecto a esa media.

### Interpretación

La perturbación pierde intensidad máxima y aumenta su extensión espacial, mientras se conserva la masa del exceso. Los resultados son coherentes con redistribución difusiva sin un mecanismo adicional de relajación hacia el fondo original.

### Límites

No se midió directamente la homogeneización mediante la varianza de los valores del campo o la desviación respecto a la media global. Tampoco se determinó el tiempo completo de relajación a largo plazo.

## 8. Balance comparativo

| Experimento | Propiedad examinada | Resultado principal |
|---|---|---|
| 1. Estabilidad temporal | Evolución prolongada | Ejecución estable en la configuración ensayada. |
| 2. Interacción | Dos concentraciones | Dispersión y relleno del espacio intermedio. |
| 3. Intensidad | Amplitud inicial | Proporcionalidad 1:2:4 del exceso en los pasos registrados. |
| 4. Distancia | Separación inicial | La separación condiciona el solapamiento y su evolución. |
| 5. Relajación | Perturbación localizada | Expansión espacial y conservación de la masa del exceso. |

## 9. Conclusión general

En las cinco configuraciones examinadas, Explorer 2 mostró resultados coherentes con una dinámica de difusión lineal, conservativa y numéricamente estable.

La batería caracteriza de forma inicial su respuesta ante evolución temporal, dos concentraciones, variación de amplitud, variación de separación y una perturbación localizada.

Esta conclusión se limita a las condiciones y métricas ensayadas. No constituye una validación general de todas las capacidades del motor, ni demuestra mecanismos informacionales adicionales, memoria informacional en sentido DIG o fenómenos físicos emergentes.

## 10. Significado para Génesis DIG

La primera batería proporciona una referencia experimental del comportamiento de Explorer 2 bajo difusión convencional en las configuraciones estudiadas.

Esta referencia permitirá comparar futuras investigaciones y separar, en la medida en que los diseños experimentales lo permitan, los efectos de la difusión de los que pudieran proceder de otros mecanismos.

La teoría y el motor deberán evolucionar conjuntamente: la teoría orientará preguntas y diseños, mientras que los resultados podrán exigir revisar tanto las hipótesis como la arquitectura computacional. El motor no debe predeterminar las conclusiones teóricas.

## 11. Estado y siguiente etapa

**Primera batería experimental: CERRADA.**

La segunda batería no se diseñará para confirmar DIG. Su punto de partida será identificar qué capacidades y mecanismos reales de Explorer 2 merecen ser estudiados, formular preguntas concretas y diseñar controles adecuados.

Las preguntas nuevas surgidas durante esta batería quedan reservadas para la planificación posterior; no alteran retroactivamente las preguntas ni las conclusiones de los cinco experimentos.

## 12. Procedencia y materiales

Los resultados numéricos y las conclusiones se consolidaron a partir de los informes de ejecución de los cinco experimentos. Los scripts, resultados JSON, registros y gráficas se mencionan en dichos informes; no se incluyen en este documento porque no se han incorporado aquí como archivos verificados del repositorio.

Este informe es una consolidación documental de la batería, no una nueva ejecución independiente ni una auditoría adicional del motor.

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG*  
*Informe de caracterización experimental de Explorer 2 — Primera batería*  
*17 de noviembre de 2026*
