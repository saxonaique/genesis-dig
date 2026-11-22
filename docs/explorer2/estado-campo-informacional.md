# Génesis DIG — Estado de la investigación del campo informacional

**Autor:** José María Pérez Rodríguez (JMPR)  
**Proyecto:** Génesis DIG — Nivel 0  
**Fecha de actualización:** 22 de noviembre de 2026  
**Ámbito:** evolución autónoma del campo informacional  
**Estado del documento:** registro de continuidad basado en resultados comunicados; pendiente de incorporar y auditar los artefactos originales de ejecución.

---

## 1. Propósito y principio de trabajo

Este documento conserva el estado de la línea experimental que estudia la dinámica autónoma del campo informacional. Su función es evitar que las decisiones, resultados y limitaciones dependan exclusivamente del historial de conversación.

La investigación estudia cómo la interacción entre los principios informacional y entrópico actúa sobre un mismo campo y genera su estado. Las definiciones computacionales actuales de ambos operadores son traducciones operativas provisionales, no definiciones físicas definitivas.

**Principio de fase vigente:** primero se investiga el campo en evolución autónoma. No se introducen todavía puntos cuánticos, partículas, elementos externos ni perturbaciones añadidas deliberadamente. Esa fase posterior solo se abrirá cuando se haya caracterizado suficientemente el comportamiento propio del campo. La decisión no implica que el campo deba quedar inmóvil; interesa determinar si sus propiedades estadísticas globales alcanzan un régimen de referencia estable mientras la dinámica local continúa.

La teoría y el motor deben evolucionar conjuntamente: la teoría orienta preguntas y diseños, y los resultados pueden exigir revisar tanto la formulación teórica como la arquitectura computacional. No se impondrán interpretaciones físicas a los resultados del Nivel 0.

## 2. Dinámica de referencia comunicada para la línea del campo

Configuración base descrita para los experimentos 002 y siguientes:

- Campo escalar sobre una malla computacional de 32 × 32.
- Condiciones de contorno periódicas.
- Estado inicial neutro con pequeñas fluctuaciones aleatorias de amplitud 0,01.
- Semillas habituales: 7, 21, 42, 99 y 2024.
- Operador informacional: suavizado/integración local.
- Operador entrópico: amplificación saturada de diferencias locales.
- Ambos operadores actúan sobre el mismo estado previo.

Regla operativa comunicada:

`local = neighbor_mean(previous)`

`information = 0.08 * (local - previous)`

`entropy = 0.012 * tanh((previous - local) / 0.10)`

`field = previous + information + entropy`

Esta descripción debe cotejarse con el código fuente original antes de considerarla una especificación reproducida. La malla es una representación computacional y no presupone espacio físico.

## 3. Registro de experimentos y estado

### E001 — Comparación de interpretaciones

Se compararon dos lecturas: información y entropía como campos coexistentes, y ambos principios como operadores sobre un mismo estado. Con la misma regla simétrica, malla 32 × 32, 120 pasos, parámetros comunicados y cinco semillas, se informó de diferencias máximas nulas entre las dos formulaciones.

**Interpretación comunicada:** cambiar el lenguaje conceptual sin cambiar reglas ni observables no produce dinámicas distinguibles.

**Estado:** resultado histórico comunicado; no confundir equivalencia de esa implementación concreta con equivalencia general de las dos formulaciones.

### E002 — Generación del campo

- Malla 32 × 32; 240 pasos; cinco semillas.
- Se comunicaron desviaciones típicas finales entre 0,108069 y 0,127246.

**Interpretación comunicada:** la dinámica genera variabilidad espacial a partir de un estado casi homogéneo.

**Estado:** resultado comunicado, pendiente de reproducción independiente en esta línea de trabajo.

### E002-B — Persistencia temporal

- Extensión a 2.000 pasos.
- Se comunicaron desviaciones típicas finales entre 0,162804 y 0,323621.
- Se informó de un aumento de la diferencia local media y de correlaciones finales moderadas con el estado inicial.

**Interpretación comunicada:** la variabilidad continúa desarrollándose; estos datos por sí solos no demuestran un atractor ni crecimiento ilimitado.

**Estado:** comunicado, pendiente de reproducción independiente.

### E002-C — Diferenciación espacial

Se comunicó una reducción del número de componentes/regiones detectados mediante umbrales respecto a la media y desviación típica, compatible con la formación de agrupaciones espaciales mayores. También se comunicaron 100 eventos de correspondencia, cuya definición requiere revisar el procedimiento.

**Estado:** interpretación histórica provisional; depende de la segmentación empleada.

### E003 — Seguimiento inicial de regiones

Se comunicaron 7.244 regiones y análisis de persistencia con umbrales de 0,25, 0,5 y 1,0 desviaciones típicas. Los resultados iniciales sugerían duraciones largas.

Posteriormente se detectaron errores en el seguimiento y asignación de identidades. Por ello, las cifras de persistencia de esta versión no deben utilizarse como evidencia de estructuras duraderas.

**Estado:** resultados históricos suspendidos para interpretación; no borrar.

### E004–E005 — Organización y trayectorias con seguimiento inicial

Se comunicaron métricas de solapamiento, desplazamiento, duración y trayectorias. Parte de la interpretación inicial fue invalidada al descubrirse errores en el seguimiento de identidades y en la asignación de índices. Las cifras iniciales de persistencia de cientos de pasos y desplazamientos de varias celdas no son fiables.

En E004 también se corrigieron posteriormente los valores comunicados de IoU: medias 0,764, 0,860 y 0,933 para los tres umbrales; los valores iniciales 0,958–0,989 deben considerarse erróneos.

**Estado:** histórico, con interpretaciones afectadas por errores metodológicos.

### E006 — Corrección del seguimiento

Se corrigió la mezcla de índices base cero/base uno y se ensayó emparejamiento húngaro por IoU. La prueba sintética de fusión siguió mostrando contaminación de identidades y no representó adecuadamente una relación muchos-a-uno.

**Conclusión comunicada:** el emparejamiento uno-a-uno no basta para modelar genealogías con fusiones y divisiones.

**Estado:** diagnóstico metodológico comunicado.

### E007 — Validación sintética genealógica

Se comunicó que el rastreador genealógico superó seis baterías sintéticas: región estática, traslación, dos regiones independientes, fusión, división y desaparición/aparición.

**Límite:** las pruebas sintéticas validan los casos construidos, no garantizan por sí solas un seguimiento correcto en campos complejos.

**Estado:** PASS comunicado; código y salidas originales pendientes de inspección independiente.

### E008 — Revalidación sobre la dinámica del campo

Con el rastreador genealógico se comunicaron 11.179 regiones con trayectorias de al menos dos registros y 16.609 eventos. Las duraciones medianas comunicadas fueron 25, 16 y 7 pasos para los umbrales 0,25, 0,5 y 1,0; los desplazamientos netos medios fueron reducidos.

**Interpretación provisional:** las regiones detectadas son predominantemente transitorias y el campo se reorganiza continuamente. Esto no descarta organización estadística global.

**Incidencia pendiente:** se indicó que los estados se registraban cada 10 pasos, pero se comunicaron duraciones medianas inferiores a 10 pasos. Debe aclararse si el rastreador utilizó estados intermedios, interpolación, otra unidad temporal o una convención de cálculo como `death = step - 1`. Las cifras temporales no se consideran fiables hasta revisar código y CSV.

**Estado:** revalidación provisional; no cerrar las cifras de duración.

### E009 — Organización espacial del campo

Análisis directo de los valores del campo, sin identificar regiones ni genealogías. Se comunicaron estos valores finales:

| Semilla | Longitud de correlación final (celdas) | Autocorrelación a distancia 1 |
|---:|---:|---:|
| 7 | 3 | 0,5607 |
| 21 | 5 | 0,7267 |
| 42 | 6 | 0,8536 |
| 99 | 4 | 0,6776 |
| 2024 | 5 | 0,8090 |

También se comunicó un pico espectral de frecuencia 1 en cuatro semillas y de frecuencia 2 en una.

**Interpretación comunicada:** el campo presenta correlación espacial y una organización estadística medible, aunque las regiones individuales sean transitorias.

**Auditorías necesarias:** definición exacta de autocorrelación y longitud de correlación; tratamiento de la media y componente DC en Fourier; normalización, promediado radial y efectos de la malla periódica.

**Estado:** resultados comunicados; reproducción independiente pendiente.

### E010 — Evolución prolongada y posible saturación

Se comunicaron longitudes de correlación:

| Semilla | Paso 2.000 | Paso 4.000 | Paso 5.000 |
|---:|---:|---:|---:|
| 7 | 3 | 4 | 5 |
| 21 | 5 | 5 | 6 |
| 42 | 6 | 6 | 7 |
| 99 | 4 | 4 | 4 |
| 2024 | 5 | 6 | 6 |

La longitud aumentó entre los pasos 4.000 y 5.000 en tres semillas y permaneció constante en dos. Por ello, E010 se interpreta como evidencia de desaceleración y posible aproximación a una meseta, no como demostración definitiva de saturación.

Se comunicaron 105 registros correspondientes a cinco semillas y 21 puntos de control, con muestreo cada 250 pasos.

**Estado:** evidencia provisional de desaceleración; artefactos originales pendientes de auditoría.

### E011 — Comprobación prolongada de estacionariedad

Se comunicó una extensión hasta 10.000 pasos, manteniendo la dinámica y parámetros anteriores, con registros cada 250 pasos.

Entre los pasos 8.000 y 10.000 se comunicó que la longitud de correlación permaneció constante para las cinco semillas, con valores finales 5, 6, 7, 4 y 7 celdas, respectivamente. También se informó de una variación inferior a 0,002 en la autocorrelación vecina durante ese intervalo. Se comunicó que esta última métrica se estabilizó en valores aproximados entre 0,68 y 0,91.

**Interpretación provisional:** resultados compatibles con un régimen estadístico estacionario durante el intervalo observado, mientras la dinámica local puede continuar.

**Límite de verificación:** todavía no se han inspeccionado aquí el código, el CSV de evolución ni las gráficas originales. Por tanto, “confirmada” describe el resultado comunicado por la ejecución, no una reproducción independiente realizada en esta auditoría.

**Estado:** estacionariedad comunicada para 8.000–10.000 pasos; pendiente de verificación con artefactos originales.

## 4. Síntesis de lo aprendido hasta E011

La línea experimental sugiere distinguir tres propiedades:

1. **Diferenciación:** el campo desarrolla variabilidad espacial.
2. **Organización estadística:** los valores del campo presentan correlaciones espaciales y escalas características.
3. **Persistencia local:** las regiones individuales detectadas pueden ser transitorias y no conservar identidades durante largos periodos.

La posible estabilidad de las propiedades estadísticas globales no exige que las regiones individuales sean permanentes. Esta distinción debe mantenerse en los análisis posteriores.

## 5. Principios para las siguientes pruebas

- Continuar investigando el campo autónomo; no introducir todavía puntos cuánticos ni perturbaciones externas.
- No modificar la dinámica de referencia sin una pregunta experimental que lo justifique.
- No asumir que la meseta comunicada es universal o definitiva.
- Separar el efecto de las condiciones iniciales, las semillas, los parámetros y el tamaño de malla mediante experimentos específicos, sin mezclar variables.
- No utilizar la identificación de regiones como único indicador de organización.
- Mantener análisis directos del campo y controles que permitan distinguir propiedades dinámicas de artefactos de medición.
- Toda nueva etapa debe formular una pregunta concreta, objetivo, procedimiento, resultados, interpretación, limitaciones y conclusión.
- No afirmar que un resultado está reproducido hasta disponer del código y los datos originales y ejecutar las comprobaciones pertinentes.

## 6. Próximo trabajo pendiente

Antes de diseñar la siguiente etapa, recuperar e inspeccionar los artefactos originales de E009, E010 y E011, especialmente:

- Código exacto de cálculo de autocorrelación, espectro de Fourier y longitud de correlación.
- CSV de evolución temporal completo.
- Gráficas generadas por las ejecuciones.
- Parámetros, semillas y versión del código.
- Comandos y entorno utilizados.

Comprobar en particular que la meseta de E011 no se debe a redondeo, cuantización de la longitud de correlación, límites del estimador o tamaño finito de la malla.

Después de esa auditoría se formulará E012 a partir de la pregunta que mejor se desprenda de los resultados. No se fija aquí una hipótesis ni se modifica el motor por anticipado.

---

**Autor:** José María Pérez Rodríguez (JMPR)  
**Génesis DIG — Nivel 0**
