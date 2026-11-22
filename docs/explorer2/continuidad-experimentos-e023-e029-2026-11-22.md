# Génesis DIG — Registro de continuidad de E023–E029

**Autor:** José María Pérez Rodríguez (JMPR)  
**Fecha de consolidación:** 22 de noviembre de 2026  
**Estado:** Registro de continuidad; resultados comunicados pendientes de auditoría independiente  
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
*Génesis DIG — Registro de continuidad E023–E029*  
*22 de noviembre de 2026*
