# Génesis DIG — Registro de continuidad de E023–E030

**Autor:** José María Pérez Rodríguez (JMPR)  
**Fecha de consolidación:** 22 de noviembre de 2026  
**Estado:** Registro de continuidad E023–E030; resultados comunicados pendientes de auditoría independiente  
**Repositorio:** `saxonaique/genesis-dig`

---

## 1. Propósito y preservación de continuidad

Este documento conserva el estado de la investigación de Génesis DIG desde E023 hasta E029 y establece cómo continuarla sin depender de Perplexity ni de ningún otro servicio conversacional.

La investigación debe poder trasladarse entre herramientas sin perder preguntas, parámetros, semillas, resultados, decisiones ni limitaciones. Las herramientas son sustituibles; el registro científico y los artefactos reproducibles deben permanecer en este repositorio.

Este documento recoge información comunicada por José María desde los informes de ejecución y análisis disponibles en la conversación. **No afirma que los experimentos, cálculos, ajustes o resultados hayan sido reproducidos o verificados independientemente** por el autor de esta consolidación. Para ello se necesitan los scripts, datos y registros originales.

## 2. Principios de continuidad

1. Mantener un registro acumulativo de cada experimento y de las decisiones metodológicas.
2. Conservar pregunta, objetivo, hipótesis cuando proceda, procedimiento, parámetros, semillas, resultados, interpretación, limitaciones y estado.
3. Distinguir siempre entre resultados comunicados por otra herramienta/persona y verificaciones propias.
4. No pedir a José María que reconstruya información ya aportada ni repetir trabajo por pérdida de contexto de una plataforma.
5. No declarar una ley, causalidad o determinismo a partir de correlaciones o ajustes sin auditar definiciones, datos, código y validación.
6. No modificar la dinámica del motor durante un experimento. Cualquier ampliación debe justificarse y versionarse entre experimentos.
7. Las nuevas preguntas surgidas durante una prueba se registran para etapas posteriores, sin desviar la pregunta en curso.
8. Los informes cerrados, código, parámetros y datos necesarios para reproducirlos se conservan en GitHub con autoría JMPR.
9. Perplexity puede ser una herramienta de apoyo, pero nunca el único lugar donde exista el registro de la investigación.

## 3. Configuración y alcance común comunicados

- Ventana temporal principal de análisis: pasos 8.000–10.000.
- Semillas comunicadas: 7, 21, 42, 99 y 2024.
- En E029 se dividió la ventana en entrenamiento 8.000–9.000 y test 9.000–10.000.
- No se han incorporado en esta consolidación los datos crudos, series completas ni scripts de E023–E029.
- No se deben inferir parámetros del motor que no figuren expresamente en los informes disponibles.

## 4. E023 — Descomposición algebraica y diferencias entre semillas

**Pregunta:** ¿Cómo se distribuyen el término de equilibrio y el término de desequilibrio entre las semillas examinadas?

**Resultados comunicados:**
- Se aplicó una descomposición algebraica en un término de equilibrio y otro de desequilibrio.
- Semillas 7, 42 y 99: descompensación y deriva.
- Semillas 21 y 2024: compensación prácticamente perfecta.
- La deriva comunicada fue negativa en 7 y 42, y positiva en 99.

**Interpretación provisional:** la misma estructura de descomposición algebraica aparece en las cinco semillas examinadas, pero los estados de compensación y los signos de deriva difieren.

**Límite:** cinco semillas no permiten generalizar a todas las condiciones ni concluir una ley universal de la dinámica.

**Estado:** resultados comunicados; pendiente de verificación con datos y código originales.

## 5. E024 — Relación temporal entre desequilibrio y deriva

**Pregunta:** ¿Cómo varían temporalmente el desequilibrio y la deriva neta en la ventana observada?

**Procedimiento comunicado:** análisis paso a paso en la ventana 8.000–10.000.

**Resultados comunicados:**
- Correlación entre desequilibrio y deriva neta de aproximadamente 0,9999–1,0 en el mismo paso.
- Se comunicaron correlaciones similares con desfases de ±1 en semillas con deriva apreciable.
- En semillas 21 y 2024 se informó que p₋ = 0,5 y q₋ = −q₊ paso a paso, con deriva aproximada de 10⁻¹¹.

**Interpretación provisional:** existe una covariación muy estrecha entre las magnitudes definidas en la ventana examinada.

**Límites metodológicos:**
- Si la deriva neta es una suma algebraica que incluye el término de desequilibrio, la correlación entre ambos no constituye una comprobación independiente.
- La autocorrelación temporal puede producir correlaciones elevadas en el mismo paso y en pasos vecinos.
- No se demuestra causalidad ni dirección de influencia.

**Estado:** resultados comunicados; pendiente de auditoría de definiciones algebraicas y series temporales.

## 6. E025 — Media del campo y deriva posterior

**Pregunta:** ¿La media global del campo en el paso 8.000 se asocia con la dirección y magnitud de la deriva posterior?

**Resultados comunicados en el paso 8.000:**

| Semilla | Clasificación comunicada | Media del campo | Deriva posterior |
|---:|---|---:|---:|
| 7 | Descompensación | −0,09105 | −1,219 × 10⁻⁵ |
| 21 | Equilibrio | −0,00049 | −9,3 × 10⁻¹³ |
| 42 | Descompensación | −0,57772 | −7,310 × 10⁻⁵ |
| 99 | Descompensación | +0,38478 | +4,875 × 10⁻⁵ |
| 2024 | Equilibrio | −0,00323 | +1,1 × 10⁻¹² |

También se comunicó que en las semillas 21 y 2024 se mantenían p₋ = 0,5 y q₋ = −q₊, mientras que en las restantes aparecían pequeñas asimetrías.

**Interpretación provisional:** en las cinco observaciones comunicadas, la media del campo se asocia con la dirección de la deriva posterior.

**Límite:** el tamaño de muestra es cinco semillas. La asociación no demuestra que la media cause la deriva ni que permita predecirla en otras condiciones.

**Estado:** resultados comunicados; pendiente de verificación.

## 7. E026 — Razón entre deriva y media

**Pregunta:** ¿La razón entre deriva y media presenta valores comparables en las semillas con deriva apreciable?

**Resultados comunicados:**
- Semilla 7: razón aproximada 1,339 × 10⁻⁴.
- Semilla 42: razón aproximada 1,265 × 10⁻⁴.
- Semilla 99: razón aproximada 1,267 × 10⁻⁴.
- Correlación media–deriva comunicada: 0,999978.
- Correlación media–asimetría poblacional comunicada: −0,999979.
- Semillas 21 y 2024: magnitudes próximas a cero.

**Interpretación provisional:** las tres semillas con deriva apreciable presentan razones de magnitud similar.

**Límites:** las correlaciones se basan en cinco semillas y no prueban la cadena causal propuesta en el informe original (media → asimetría → deriva). Debe comprobarse también cómo se definió la razón y cómo se trataron los casos próximos a cero.

**Estado:** resultados comunicados; pendiente de verificación.

## 8. E027 — Invariancia ante traslación uniforme

**Pregunta:** ¿La asimetría de las diferencias locales cambia al aplicar una traslación uniforme al campo?

**Resultados comunicados:**
- Correlación entre media del campo y asimetría de diferencias locales (d_skew): −0,999961.
- Prueba de invariancia ante traslación uniforme: error 0 en las cinco semillas.
- La traslación uniforme no altera las diferencias locales ni la asimetría poblacional definida a partir de ellas.

**Interpretación:** la invariancia ante traslación uniforme es una propiedad algebraica de las diferencias locales: sumar la misma constante a todos los valores deja las diferencias sin cambio.

**Límite:** esta invariancia no demuestra que la relación entre media y asimetría sea causal ni que exista un mecanismo dinámico que las acople.

**Estado:** resultado algebraico comunicado; pendiente de revisar implementación y cálculo.

## 9. E028 — Evolución temporal de media y asimetría local

**Pregunta:** ¿Cómo evolucionan conjuntamente la media global M y la asimetría de diferencias locales S en la ventana 8.000–10.000?

**Resultados comunicados:**

| Semilla | Corr(M,S), niveles | Corr(ΔM,ΔS) | Corr. residuos | Desfases −1/0/+1 |
|---:|---:|---:|---:|---|
| 7 | −0,9727 | 0,9957 | 0,9980 | similares |
| 21 | +0,99999 | +0,99999 | +0,99999 | similares |
| 42 | −0,9730 | 0,9953 | 0,9979 | similares |
| 99 | −0,9726 | 0,9955 | 0,9980 | similares |
| 2024 | +0,99994 | +0,99994 | +0,99997 | similares |

**Interpretación provisional:** las series presentan una asociación temporal muy elevada en las condiciones comunicadas.

**Límites metodológicos:**
- Las correlaciones de niveles e incrementos pueden verse afectadas por autocorrelación.
- Deben examinarse las amplitudes absolutas, especialmente en las semillas 21 y 2024, para descartar que variaciones diminutas o ruido numérico dominen el coeficiente.
- El detrending no elimina por sí solo todos los problemas de dependencia temporal.
- La similitud entre desfases no demuestra simultaneidad causal.
- No se puede concluir causalidad ni un mecanismo físico a partir de estas correlaciones.

**Estado:** resultados comunicados; pendiente de auditoría de series, amplitudes y definiciones.

## 10. E029 — Ajuste predictivo de ΔS a partir de ΔM

**Pregunta:** ¿Existe una relación matemática reproducible que permita relacionar el cambio de asimetría S con el cambio de media M?

**Diseño comunicado:**
- Entrenamiento: pasos 8.000–9.000.
- Test: pasos 9.000–10.000.
- Modelos evaluados:
  - A, lineal: ΔS = a·ΔM + b.
  - B, cuadrático: ΔS = a·ΔM + b·(ΔM)² + c.
  - C, dependiente del estado: ΔS = f(M,S,ΔM).

**R² comunicados:**

| Semilla | A train | A test | B train | B test | C train | C test |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 0,9979 | −0,2067 | 0,9979 | −0,2067 | 1,0000 | 1,0000 |
| 21 | 1,0000 | 0,9965 | 1,0000 | 0,9999 | 1,0000 | 1,0000 |
| 42 | 0,9976 | −0,3338 | 1,0000 | 0,9933 | 1,0000 | 1,0000 |
| 99 | 0,9977 | −0,2682 | 0,9977 | −0,2682 | 1,0000 | 0,9999 |
| 2024 | 1,0000 | 0,9813 | 1,0000 | 0,9984 | 1,0000 | 1,0000 |
| Agrupado | 0,7127 | −1,5292 | 0,9108 | −1,7873 | 0,9665 | −0,3738 |

**Lectura provisional:**
- A y B muestran resultados de test muy diferentes según la semilla.
- C presenta R² de test prácticamente perfecto por semilla, pero su rendimiento agrupado es negativo.
- El patrón es compatible con relaciones muy específicas de cada trayectoria o semilla, pero no permite afirmar todavía que exista una ley determinista del campo.
- El fallo del ajuste agrupado impide tratar el resultado como una relación universal compartida por todas las semillas.

**Auditoría obligatoria antes de aceptar el modelo C:**
1. Fórmula exacta de f y forma funcional implementada.
2. Número de parámetros libres y grados de libertad efectivos.
3. Valores de los parámetros ajustados por semilla y procedimiento de ajuste.
4. Código exacto de entrenamiento, selección y evaluación.
5. Confirmación de que el conjunto de test no intervino directa o indirectamente en el ajuste, selección del modelo o normalización.
6. Datos de entrenamiento y test, con sus índices temporales.
7. Comprobación de posibles dependencias algebraicas entre M, S y sus incrementos.
8. Comparación con modelos de referencia más sencillos y evaluación fuera de muestra sin fuga de información.

Un R² = 1 no demuestra determinismo por sí solo. Si f tiene demasiados grados de libertad, puede existir sobreajuste o fuga de información. La especificidad por semilla tampoco demuestra todavía que la semilla sea la causa de los coeficientes.

**Estado:** experimento ejecutado según el informe recibido; interpretación provisional. **No cerrar como ley matemática ni como determinismo demostrado hasta completar la auditoría del modelo C.**

## 11. Decisión metodológica inmediata

La prioridad inmediata no es iniciar otra batería de correlaciones ni dar por confirmada una ley. Es auditar E029-C con el código, la fórmula, los parámetros y los datos de entrenamiento/test.

Hasta disponer de esa auditoría:
- E029 permanece abierto en cuanto a su interpretación matemática.
- No se declara validado el determinismo.
- No se da por demostrada una ley universal ni una ley específica de semilla.
- Cualquier experimento posterior debe partir de lo que revele la auditoría, sin presuponer su resultado.

La propuesta de estudiar las condiciones iniciales que anticipan los coeficientes de E029 queda reservada. No debe ejecutarse como siguiente etapa antes de entender exactamente qué representa y cómo se obtuvo el modelo C.

## 12. Protocolo de actualización desde E030 en adelante

Cada nueva entrada deberá incluir:
- Identificador y pregunta concreta.
- Objetivo e hipótesis, cuando proceda.
- Versión del motor y código utilizado.
- Parámetros completos, semillas y condiciones iniciales.
- Procedimiento y criterios definidos antes de observar los resultados.
- Resultados comunicados, con sus fuentes y archivos.
- Verificaciones independientes realizadas y por quién.
- Interpretación, límites y preguntas reservadas.
- Estado: planificado, ejecutado, pendiente de auditoría, no concluyente o cerrado.

Cuando se cierre un experimento, se incorporará un informe definitivo con autoría JMPR y referencias a código, datos y resultados reproducibles. Este registro se actualizará para reflejar la continuidad; no se reemplazarán silenciosamente resultados anteriores ni se borrarán decisiones metodológicas.

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG — Registro de continuidad E023–E030*  
*22 de noviembre de 2026*


## 13. E030 — Identificación de las condiciones iniciales del acoplamiento

**Investigador:** José María Pérez Rodríguez (JMPR)  
**Pregunta:** ¿Qué propiedades del estado inicial permiten explicar o anticipar las diferencias entre semillas en los coeficientes del acoplamiento observados en E029?

**Diseño comunicado:**
- Se mantuvo intacta la dinámica del motor.
- Se examinaron las semillas 7, 21, 42, 99 y 2024.
- Se calcularon propiedades del estado inicial (paso 0) y se compararon con los coeficientes atribuidos al modelo C de E029.
- Las propiedades consideradas incluyeron media, varianza/dispersión, simetría, distribución espacial, correlaciones entre vecinos y distribución de diferencias locales. El informe recibido no aporta los valores completos de todas estas medidas, por lo que no pueden auditarse aquí.

**Resultados comunicados:**

| Semilla | Media inicial | Asimetría inicial | p₋ inicial | coef_M | coef_S | coef_dM | Intercepto |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | −0,00075 | +0,0146 | 0,5010 | −2,3×10⁻¹³ | −9,37×10⁻⁴ | +6,9×10⁻⁶ | +3,7×10⁻⁶ |
| 21 | +0,00040 | −0,0211 | 0,5000 | +9,8×10⁻⁴ | −2,51×10⁻³ | +4,9×10⁻⁶ | +4,8×10⁻⁷ |
| 42 | −0,00029 | −0,0459 | 0,5059 | +1,1×10⁻¹² | −9,37×10⁻⁴ | −3,7×10⁻⁴ | +2,2×10⁻⁵ |
| 99 | −0,00005 | −0,0882 | 0,4961 | −9,8×10⁻¹⁴ | −9,43×10⁻⁴ | +1,6×10⁻⁵ | −1,5×10⁻⁵ |
| 2024 | +0,00003 | +0,0346 | 0,5000 | +9,4×10⁻⁴ | −2,43×10⁻³ | +4,0×10⁻⁶ | +3,0×10⁻⁶ |

Se comunicaron las siguientes correlaciones exploratorias:
- init_p_neg frente al intercepto: 0,985.
- init_mean frente a coef_M / coef_S: aproximadamente ±0,75.
- Las demás propiedades iniciales examinadas no mostraron una relación clara y consistente con los coeficientes.

**Conclusión comunicada:** con cinco semillas no se identifica una propiedad inicial aislada que explique de forma robusta las diferencias entre los coeficientes del acoplamiento. Las correlaciones observadas son indicios exploratorios, no una ley predictiva.

**Límites y cautelas:**
1. El tamaño de muestra es cinco configuraciones; las correlaciones son muy sensibles a cada punto y a la selección de variables examinadas.
2. La correlación 0,985 no debe interpretarse como evidencia suficiente de predicción o causalidad.
3. Los coeficientes comparados proceden del modelo C de E029. Mientras no se auditen su fórmula exacta, significado, grados de libertad, ajuste y validación, tampoco está plenamente establecido qué magnitudes se están intentando explicar.
4. El R² de entrenamiento igual a 1 por trayectoria, comunicado para E029-C, no distingue por sí solo entre una relación determinista y un ajuste excesivo. Debe revisarse el número de parámetros y cualquier posible fuga de información.
5. No se aportan aquí las series crudas, el script ni el detalle numérico completo de todas las características iniciales. Los resultados permanecen como datos comunicados, no como verificación independiente.

**Interpretación provisional:** las diferencias entre semillas no quedan explicadas por ninguna de las propiedades iniciales aisladas examinadas en este conjunto. Esto no demuestra que el estado inicial carezca de influencia; deja abierta la posibilidad de combinaciones de propiedades, estructuras espaciales más complejas o dependencia de la trayectoria.

**Decisión metodológica:** no modificar el motor ni introducir mecanismos para forzar resultados. No avanzar todavía a una interpretación teórica de familias dinámicas. La prioridad sigue siendo auditar E029-C. Después podrá diseñarse una ampliación del conjunto de semillas con criterios definidos de antemano y validación fuera de muestra, evitando repetir una búsqueda de correlaciones sobre cinco puntos.

**Estado:** E030 ejecutado según el informe recibido; conclusión exploratoria no concluyente; pendiente de auditoría independiente de E029-C y de reproducción de los datos de E030.

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG — Registro de continuidad E023–E030*  
*22 de noviembre de 2026*


## 14. Auditoría de E029-C — Colinealidad y retirada de la interpretación determinista

**Investigador:** José María Pérez Rodríguez (JMPR)  
**Objeto:** determinar si el ajuste prácticamente perfecto del modelo C de E029 identifica una relación dinámica genuina entre M, S y ΔM, o si está afectado por degeneración de la matriz de diseño.

**Resultados de auditoría comunicados:**

| Semilla | Número de condición | Rango comunicado | VIF (M, S, ΔM) | Residuo máximo | Corr(ΔM, ΔS) |
|---:|---:|---:|---|---:|---:|
| 7 | 1,3×10¹⁴ | 3 de 4 | 70 / 113.537 / 299.092 | 6,8×10⁻¹⁷ | 0,9957 |
| 21 | 8,4×10¹⁶ | 3 de 4 | 170.799 / 170.799 / 1,0×10⁹ | 7,9×10⁻¹⁷ | 0,99999 |
| 42 | 3,4×10¹² | 4 de 4 | 45.534 / 93.952 / 269.083 | 1,9×10⁻¹⁶ | 0,9953 |
| 99 | 7,0×10¹³ | 3 de 4 | 44.068 / 107.111 / 287.312 | 1,7×10⁻¹⁶ | 0,9955 |
| 2024 | 5,8×10¹⁶ | 3 de 4 | 27.362 / 27.362 / 8,9×10⁸ | 9,1×10⁻¹⁷ | 0,99994 |

**Interpretación de la auditoría comunicada:**
- Los números de condición, del orden de 10¹²–10¹⁶, indican matrices extremadamente mal condicionadas.
- Los VIF comunicados, de hasta 10⁹, indican inflación extrema de la varianza asociada a la dependencia entre predictores.
- El rango comunicado es 3 de 4 en cuatro semillas y 4 de 4 en una. La interpretación exacta depende de la construcción y escalado de la matriz de diseño; debe conservarse el código de auditoría para verificar qué columnas se incluyeron y cómo se calculó el rango.
- Los residuos máximos, del orden de 10⁻¹⁶, son compatibles con un ajuste a precisión de máquina, pero por sí solos no acreditan identificabilidad ni capacidad predictiva.
- La correlación comunicada entre ΔM y ΔS es muy alta en las cinco trayectorias.

**Corrección de la interpretación de E029-C:**

Se retira la interpretación anterior según la cual el R² ≈ 1 del modelo C constituía evidencia de una ley determinista de tres variables. Los diagnósticos comunicados apuntan a colinealidad severa y falta de identificabilidad estable de los coeficientes. El ajuste casi perfecto no permite atribuir significado independiente a M, S y ΔM ni afirmar que el modelo C haya descubierto una ley adicional.

La corrección no invalida las series originales ni elimina la asociación observada entre ΔM y ΔS. Sí invalida la lectura del ajuste perfecto de C como prueba de determinismo o de un acoplamiento genuino de tres variables.

**Estado del modelo A (ΔS = a·ΔM + b):**
La correlación comunicada entre ΔM y ΔS, de 0,9957 a 0,99999 por semilla, indica una asociación muy elevada en las series examinadas. No equivale por sí sola al R² de un modelo validado ni demuestra una ley dinámica. Deben comprobarse la definición exacta de la regresión, sus coeficientes, interceptos, escalas y amplitudes, así como su estabilidad en ventanas y datos independientes.

**Conclusión provisional corregida:**

El modelo C de E029 no aporta evidencia fiable de una ley determinista de tres variables: su ajuste perfecto está acompañado de diagnósticos de colinealidad extrema. La relación ΔM–ΔS merece conservarse como resultado empírico destacado, pero su interpretación como ley reproducible queda pendiente de pruebas adicionales.

**Siguientes comprobaciones recomendadas, sin modificar la dinámica del motor:**
1. Conservar y revisar el código exacto de construcción de la matriz de diseño y del cálculo de rango, número de condición y VIF.
2. Comprobar escalado, centrado, intercepto y unidades de las columnas antes de interpretar el número de condición.
3. Ajustar y documentar el modelo A por semilla: coeficiente, intercepto, error, amplitud de ΔM y ΔS y residuos.
4. Comprobar estabilidad en ventanas temporales distintas y en semillas no utilizadas para formular la relación.
5. Comparar predicción fuera de muestra con una referencia sencilla y evitar particiones que filtren información temporal.
6. No volver a interpretar los coeficientes inestables del modelo C como propiedades físicas o parámetros intrínsecos del campo.

**Límite de verificación:** los valores de esta auditoría se incorporan como resultados comunicados por el investigador. Hasta disponer del script, matriz de diseño y datos originales, esta consolidación no constituye una reproducción independiente de los diagnósticos.

**Estado:** interpretación determinista de E029-C retirada; colinealidad severa comunicada; relación ΔM–ΔS conservada como asociación empírica fuerte pendiente de validación.

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG — Auditoría de E029-C*  
*22 de noviembre de 2026*


## 15. E031 — Ejecución metodológicamente inválida por inclusión de la fase transitoria

**Investigador:** José María Pérez Rodríguez (JMPR)  
**Pregunta prevista:** ¿La relación ΔM → ΔS conserva su forma y capacidad predictiva al cambiar la ventana temporal y la semilla?

**Incidencia comunicada:**
La ejecución de E031 registró M y S desde el paso 1, en vez de restringir el ajuste de la prueba principal a la meseta. En consecuencia, el entrenamiento incorporó una fase transitoria que no formaba parte del intervalo de meseta usado en E029.

**Comparación comunicada:**

| Aspecto | E029 | E031 ejecutada |
|---|---|---|
| Entrenamiento de la prueba principal | 8.000–8.999 | 2–8.999 |
| Test | 9.000–9.999 | 9.000–9.999 |
| R² de entrenamiento comunicado | 0,9979–1,0 | 0,0122–0,5646 |
| R² de test comunicado | −0,2067 a 0,9813 | −10¹⁴ a −10¹⁷ |

Los intervalos se reproducen según el informe recibido; debe comprobarse el indexado exacto en el script antes de una reproducción independiente.

**Interpretación metodológica:**
La inclusión de la fase transitoria cambia la población de datos usada para estimar el modelo. Por ello, los resultados de E031 no son directamente comparables con el ajuste de E029 restringido a la meseta. Los R² de test extremadamente negativos indican un fallo predictivo del ajuste realizado, pero no pueden atribuirse a una propiedad del campo ni utilizarse para caracterizar el comportamiento de la meseta.

**Qué aporta E029 y qué no:**
- En E029, el modelo A presentó R² de entrenamiento entre 0,9979 y 1,0 por semilla.
- En el test temporal 9.000–9.999, las semillas 7, 42 y 99 presentaron R² negativos; las semillas 21 y 2024 mantuvieron R² altos.
- Esto demuestra que el ajuste lineal ΔS = a·ΔM + b no tuvo capacidad predictiva temporal uniforme en las cinco trayectorias examinadas.
- No demuestra por sí solo que la relación no se generalice entre todas las ventanas temporales.
- Tampoco equivale a una prueba estricta de transferencia entre semillas. El resultado agrupado comunicado en E029 es una evaluación conjunta, pero sin el protocolo exacto no debe confundirse con entrenar en unas semillas y evaluar en semillas completamente excluidas.

**Conclusión corregida:**
E031, en su ejecución actual, queda invalidada para responder a la pregunta prevista sobre la estabilidad del acoplamiento en la meseta. No permite concluir que la relación ΔM → ΔS sea una propiedad general o que haya desaparecido. E029 sí aporta evidencia de que el modelo lineal no predice de forma uniforme el tramo temporal posterior en todas las semillas.

**Decisión metodológica:**
- Conservar E031 como registro de una incidencia metodológica; no borrar sus resultados, pero etiquetarlos como no comparables con E029.
- No modificar la dinámica del motor.
- Si se repite la prueba, fijar explícitamente los índices de cada ventana antes del ajuste y verificar que todas las variables derivadas (M, S, ΔM, ΔS) se calculen y recorten con índices coherentes.
- Separar tres validaciones: temporal dentro de una semilla, transferencia a semillas no usadas en el ajuste y estabilidad entre ventanas de régimen.
- No declarar una conclusión general sobre ventanas o semillas hasta ejecutar esos diseños de validación correctamente.

**Estado:** ejecución realizada con error metodológico identificado; resultados no válidos para la comparación prevista; no se atribuye el fallo al campo. Pendiente decidir si se repite con ventanas correctamente delimitadas.

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG — Registro de continuidad E023–E031*  
*22 de noviembre de 2026*


## 16. E031 corregida — Comprobación del error absoluto del modelo A

**Investigador:** José María Pérez Rodríguez (JMPR)  
**Pregunta:** ¿Los R² altos de las semillas 21 y 2024 se deben únicamente a amplitudes diminutas de ΔS, o el error predictivo también es pequeño respecto a la variación observada en test?

**Metodología comunicada:** se mantuvo la prueba temporal del modelo A: entrenamiento 8.000–9.000 y test 9.000–10.000, restringidos a la meseta. Se calculó MAE y su cociente respecto a la amplitud de ΔS en test.

**Resultados comunicados:**

| Semilla | R² test | MAE test | MAE / amplitud test | Amplitud ΔS test |
|---:|---:|---:|---:|---:|
| 7 | −0,2067 | 1,31×10⁻¹³ | 0,9950 | 1,32×10⁻¹³ |
| 21 | 0,9965 | 5,02×10⁻¹⁵ | 0,0546 | 9,18×10⁻¹⁴ |
| 42 | −0,3338 | 2,26×10⁻¹² | 1,0457 | 2,16×10⁻¹² |
| 99 | −0,2682 | 1,09×10⁻¹³ | 1,0203 | 1,06×10⁻¹³ |
| 2024 | 0,9813 | 1,54×10⁻¹⁴ | 0,1272 | 1,21×10⁻¹³ |

**Interpretación:** el error de test del modelo A es pequeño en relación con la amplitud de ΔS en las semillas 21 (5,46%) y 2024 (12,72%). En 7, 42 y 99, el error es aproximadamente igual o superior a dicha amplitud (99,50%, 104,57% y 102,03%). Esto refuerza la distinción entre trayectorias donde el modelo conserva capacidad predictiva temporal y aquellas donde no.

**Precisión estadística:** MAE dividido por la amplitud de test no es una medida convencional de error relativo ni, por sí solo, demuestra que el modelo supera a la predicción de la media. Los R² negativos de 7, 42 y 99 sí indican que el modelo obtuvo peor error cuadrático que la referencia de la media de test, según la definición habitual de R². Para afirmar una comparación en MAE con esa referencia, debe calcularse explícitamente el MAE del predictor constante. Los valores normalizados no descartan todos los efectos de escala, pero muestran que la amplitud pequeña no explica por sí sola los errores relativos bajos comunicados en 21 y 2024.

**Conclusión provisional:** el modelo A presenta capacidad predictiva temporal dentro de las trayectorias 21 y 2024 en la ventana examinada, y no la presenta en 7, 42 y 99. Esto es evidencia de comportamiento específico de trayectoria en esta prueba, no demostración de causalidad, mecanismo ni ley universal. Tampoco acredita transferencia entre semillas.

**Límite de verificación:** los números se incorporan como resultados comunicados; no se han reproducido independientemente con series crudas y código.

**Estado:** complemento de E031 corregida; resultados comunicados, pendientes de reproducción independiente.

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG — Complemento E031 corregida*  
*22 de noviembre de 2026*


## 17. E033 — Caracterización estructural de configuraciones con distinto comportamiento predictivo

**Investigador:** José María Pérez Rodríguez (JMPR)  
**Pregunta:** ¿Qué características estructurales distinguen las configuraciones en las que el modelo A conserva capacidad predictiva temporal de aquellas en las que no?

**Metodología comunicada:** se reutilizó exactamente la dinámica de experimentos anteriores. Se compararon cinco semillas (7, 21, 42, 99, 2024), clasificadas según los resultados predictivos comunicados en E031 corregida: equilibrio/predictividad (21, 2024) y descompensación/fallo predictivo (7, 42, 99). Se calcularon características del estado inicial y de la meseta, incluyendo media, desviación, asimetría, curtosis, autocorrelación espacial, correlación con tablero de ajedrez y estadísticos de diferencias locales.

**Tres propiedades separadoras comunicadas:**

| Propiedad | Media semillas 21, 2024 | Media semillas 7, 42, 99 | Separación comunicada |
|---|---:|---:|---:|
| Curtosis inicial de diferencias locales (init_d_kurt) | +0,0917 | −0,1268 | 1,89 |
| Correlación tablero en meseta (plat_checkerboard) | +0,0010 | +0,0247 | 1,59 |
| Media inicial (init_mean) | +0,000213 | −0,000364 | 1,51 |

**Valores por semilla comunicados:**

| Semilla | Grupo | init_d_kurt | plat_checkerboard | init_mean |
|---:|---|---:|---:|---:|
| 7 | Descompensación | −0,1381 | +0,0138 | −0,000753 |
| 21 | Equilibrio | +0,1079 | +0,0056 | +0,000401 |
| 42 | Descompensación | −0,0559 | +0,0196 | −0,000293 |
| 99 | Descompensación | −0,1865 | +0,0406 | −0,000045 |
| 2024 | Equilibrio | +0,0754 | −0,0036 | +0,000025 |

**Patrón descriptivo comunicado:** en este conjunto, las semillas 21 y 2024 presentan curtosis inicial positiva, correlación de tablero próxima a cero y media inicial positiva; las semillas 7, 42 y 99 presentan curtosis negativa, correlación de tablero positiva y media inicial negativa. Las tres variables separan los grupos sin solapamiento en los cinco casos observados.

**Interpretación provisional:** aparece una firma estructural candidata asociada al comportamiento predictivo temporal del modelo A. La curtosis de las diferencias locales iniciales, la organización tipo tablero durante la meseta y la media inicial podrían ser variables relevantes para caracterizar las configuraciones.

**Límites metodológicos:**
1. La muestra contiene únicamente cinco semillas, con grupos de dos y tres casos. Una separación perfecta en una muestra tan pequeña puede ser accidental y no estima adecuadamente la variabilidad entre configuraciones.
2. Las propiedades se identificaron explorando múltiples características. La selección posterior de las que mejor separan los grupos introduce riesgo de selección/múltiples comparaciones; las separaciones comunicadas no deben interpretarse como significación estadística ni como capacidad predictiva validada.
3. La clasificación de grupos deriva de resultados de E031 corregida y describe el comportamiento observado, no una clase intrínseca demostrada del campo.
4. La correlación con tablero se mide en la meseta, mientras que curtosis y media se miden inicialmente; no se debe asumir que todas son propiedades exclusivamente iniciales ni atribuirles causalidad.
5. Los resultados proceden del informe comunicado y no se han reproducido independientemente con código y datos crudos.

**Conclusión provisional:** E033 identifica una firma estructural candidata que separa descriptivamente las cinco configuraciones examinadas según su comportamiento predictivo. No demuestra que estas tres propiedades causen el acoplamiento ni que permitan clasificar nuevas semillas. La evidencia es exploratoria.

**Decisión metodológica:** la siguiente etapa recomendada es una prueba de confirmación con un conjunto ampliado de semillas, protocolo y métricas fijados antes de calcular resultados, sin modificar la dinámica del motor. Debe evaluarse si la firma propuesta se mantiene en configuraciones nuevas y si mejora la predicción frente a referencias simples. Evitar volver a seleccionar características sobre el conjunto de confirmación.

**Estado:** E033 ejecutado según el informe recibido; firma estructural exploratoria comunicada; pendiente confirmación fuera de muestra y verificación independiente.

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG — E033*  
*22 de noviembre de 2026*


## 18. E034 — Validación de la firma estructural en semillas nuevas

**Investigador:** José María Pérez Rodríguez (JMPR)  
**Pregunta:** ¿La firma estructural candidata de E033 clasifica de forma predictiva configuraciones nuevas según el comportamiento del modelo A?

**Metodología comunicada:** se reutilizó exactamente la dinámica de etapas anteriores. Se evaluaron diez semillas nuevas, no utilizadas en E023–E033 (11, 13, 17, 19, 23, 29, 31, 37, 41 y 43). Se midieron curtosis de diferencias locales iniciales (`init_d_kurt`), correlación con tablero en meseta (`plat_checkerboard`) y media inicial (`init_mean`), y se aplicó la regla de clasificación comunicada como fijada antes de observar los resultados. El criterio de comportamiento predictivo fue `mae_rel < 0,5`.

**Resultados comunicados:**

| Semilla | init_d_kurt | plat_checkerboard | init_mean | Predicción | Resultado real | mae_rel | Correcta |
|---:|---:|---:|---:|---|---|---:|---|
| 11 | −0,1154 | +0,0318 | +0,00012 | Descompensación | Descompensación | 0,9926 | Sí |
| 13 | +0,3010 | +0,0096 | +0,00014 | Equilibrio | Descompensación | 1,0792 | No |
| 17 | +0,0774 | −0,0223 | +0,00017 | Descompensación | Descompensación | 1,0845 | Sí |
| 19 | +0,0141 | +0,0125 | −0,00041 | Descompensación | Descompensación | 1,0854 | Sí |
| 23 | −0,0972 | −0,0214 | −0,00039 | Descompensación | Descompensación | 1,0808 | Sí |
| 29 | +0,0626 | +0,0032 | −0,00020 | Descompensación | Descompensación | 0,9495 | Sí |
| 31 | −0,0043 | +0,0214 | +0,00015 | Descompensación | Descompensación | 0,9873 | Sí |
| 37 | −0,0328 | +0,0183 | −0,00038 | Descompensación | Descompensación | 0,8949 | Sí |
| 41 | +0,0124 | 0,0000 | −0,00010 | Descompensación | Descompensación | 1,0947 | Sí |
| 43 | +0,0353 | −0,0204 | −0,00019 | Descompensación | Descompensación | 1,0363 | Sí |

Las diez semillas presentaron `mae_rel` superior a 0,5 y fueron clasificadas como descompensación por el criterio comunicado.

**Evaluación del resultado 9/10:** nueve de las diez semillas son descompensadas. Un clasificador constante que predijera descompensación para todas también obtendría 9/10 (90 %). La firma predijo equilibrio únicamente para la semilla 13, y esa predicción fue incorrecta. Por tanto, el porcentaje de aciertos no evidencia poder discriminante por encima de la tasa base en esta muestra. La rama positiva de la firma (equilibrio) no obtuvo ningún acierto.

**Interpretación provisional:** la firma estructural identificada exploratoriamente en E033 no queda validada en este conjunto de semillas nuevas. E034 no demuestra que las características carezcan de relación con el comportamiento; muestra que la regla aplicada no identificó configuraciones equilibradas en la muestra de confirmación. La ausencia de casos equilibrados entre las diez semillas limita la capacidad de evaluar sensibilidad o discriminación de ambas clases.

**Límites metodológicos:**
1. Los resultados son comunicados y no se han reproducido independientemente con código y datos crudos.
2. La tasa base de 9/10 descompensadas hace que la exactitud global sea una métrica insuficiente; deben comunicarse resultados por clase y compararse con la regla constante.
3. No se observó ningún caso positivo de equilibrio en el conjunto de confirmación, por lo que no se puede estimar la capacidad de la firma para detectar configuraciones equilibradas.
4. Diez semillas constituyen una muestra limitada; no debe inferirse que el equilibrio sea raro en la población de todas las configuraciones sin conocer el esquema de selección de semillas y ampliar la muestra.
5. Debe conservarse la regla de clasificación original y evitar redefinir umbrales o seleccionar nuevas características a partir de estas diez semillas como si fueran un conjunto independiente de confirmación.

**Conclusión provisional:** E034 no valida la firma estructural de E033. El 9/10 de aciertos es igual a la tasa base de la clase mayoritaria; la única predicción de equilibrio fue falsa. El resultado no demuestra que la firma sea inútil ni que el equilibrio sea intrínsecamente raro, pero no aporta evidencia de capacidad discriminante en esta prueba.

**Decisión metodológica:** registrar E034 como validación no confirmatoria. Si se continúa, ampliar la muestra con un procedimiento de selección de semillas previamente definido, conservar criterios de clasificación y evaluación, y asegurar suficientes casos de ambas clases para evaluar discriminación. No modificar el motor ni reajustar la firma usando el conjunto de confirmación ya observado.

**Estado:** E034 ejecutado según el informe recibido; firma no validada; resultado exploratorio de confirmación pendiente de reproducción independiente.

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG — E034*  
*22 de noviembre de 2026*
