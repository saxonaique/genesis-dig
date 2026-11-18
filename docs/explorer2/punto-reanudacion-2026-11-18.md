# Génesis DIG — Punto de reanudación de Explorer 2

**Autor:** José María Pérez Rodríguez (JMPR)  
**Fecha:** 18 de noviembre de 2026  
**Estado:** Documento de continuidad; trabajo experimental en curso  
**Repositorio:** `saxonaique/genesis-dig`

---

## 1. Propósito de este documento

Este documento preserva el estado intelectual, metodológico y experimental de la investigación con Explorer 2 para poder continuar aunque se pierdan los archivos de un entorno temporal de ejecución.

No sustituye al código fuente, a los JSON originales ni a los registros de ejecución. Tampoco afirma que los resultados aquí resumidos hayan sido reejecutados o verificados independientemente por quien redacta esta consolidación. Los resultados de los experimentos 002-A, 002-B y 002-C proceden de informes que José María compartió desde el entorno de Perplexity/Claude.

La primera batería de caracterización de Explorer 2 está documentada por separado en:
`docs/explorer2/primera-bateria-caracterizacion.md`.

## 2. Principios metodológicos no negociables

1. Cada experimento parte de una pregunta concreta y se mantiene centrado en responderla.
2. Cada experimento documenta pregunta, objetivo, hipótesis cuando proceda, procedimiento, resultados e interpretación/conclusión.
3. Las preguntas nuevas que aparezcan durante una ejecución se anotan para experimentos posteriores; no se mezclan con la pregunta en curso.
4. No se modifica el motor durante una ejecución experimental.
5. Sí se puede ampliar el motor entre experimentos cuando una pregunta legítima requiere una capacidad que todavía no existe.
6. Toda ampliación debe tener justificación experimental, ser neutral respecto al resultado, estar versionada y probarse por separado.
7. Se deben conservar las versiones anteriores y comparar, cuando proceda, el comportamiento con la capacidad nueva desactivada y activada.
8. No se deben añadir mecanismos para producir un resultado deseado ni ajustar retrospectivamente los criterios.
9. Los resultados del motor no equivalen por sí mismos a una demostración física ni a una validación de la teoría DIG.
10. La teoría y el motor evolucionan conjuntamente: la teoría plantea preguntas; la ciencia y las matemáticas existentes ayudan a construir métodos; los experimentos pueden exigir revisar la teoría y/o la arquitectura.

Principio rector: **no estamos construyendo un motor para que DIG tenga razón; estamos construyendo un motor que permita averiguar si DIG tiene razón, en qué aspectos y hasta dónde.**

## 3. Estado general antes de la interrupción del entorno

- La auditoría técnica inicial de Explorer 2 se dio por cerrada. No debe reabrirse por defecto.
- La primera batería de caracterización (experimentos 1–5) está cerrada y archivada en el documento indicado arriba.
- La investigación 001 sobre perturbación gaussiana está cerrada.
- La investigación 002, «Persistencia informacional», está en curso.
- Explorer 2 v0.4.7 fue la versión comunicada para los experimentos 002-B/002-C, con capacidades incorporadas para estímulos externos y memoria histórica.
- El entorno temporal de Perplexity/Claude informó que había sido reiniciado y que ya no conservaba los archivos de v0.4.7, el script E002-C ni sus resultados originales. Por tanto, esos archivos no deben darse por disponibles.
- La decisión acordada es que Claude prepare/incorpore las capacidades necesarias en la nueva versión del motor prevista para el siguiente turno de trabajo. Después se repetirá una batería abreviada de comprobación.
- No reconstruir a ciegas v0.4.5/v0.4.6/v0.4.7 ni presentar una reconstrucción como si fuera el código original validado.

## 4. Investigación 002 — Persistencia informacional

### Pregunta central

**¿Puede una perturbación introducida en el campo dejar una configuración que siga siendo distinguible después de retirar la perturbación externa?**

Conceptos que deben mantenerse separados:

- **Persistencia:** una configuración sigue siendo reconocible durante cierto tiempo.
- **Estabilidad:** conserva propiedades frente a pequeñas perturbaciones.
- **Memoria:** el estado presente o su evolución depende de la historia previa, incluso al comparar condiciones actuales equivalentes.
- **Histéresis:** dependencia de trayectoria en un protocolo de variación/ciclo de parámetros; no es sinónimo de persistencia ni de memoria en sentido amplio.

Una diferencia residual que desaparece lentamente puede explicarse por relajación difusiva y no basta para demostrar memoria.

## 5. Experimento 002-A — Persistencia después de retirar el estímulo

### Diseño

Dos ejecuciones comparables:

- A: campo de fondo 0,1; introducir una gaussiana de amplitud 0,4, centro (0,5; 0,5), sigma 0,05 durante 100 pasos; retirar el estímulo y continuar 2.000 pasos sin volver a estimular.
- B: control uniforme de fondo 0,1, sin estímulo.
- Malla 32 × 32, frontera periódica, D = 0,01, dt = 0,001, ruido desactivado.
- La memoria `full` se utiliza como registro/trazabilidad, no debe suponerse que interviene dinámicamente.

Para hacerlo posible se añadió, según el informe de ejecución, `ExternalStimulusDynamics`: durante los pasos 0–99 suma `profile * dt` al campo y se desactiva en el paso 100. Después continúa únicamente la difusión original.

### Resultados comunicados

- Ambas ejecuciones: 2.100 pasos.
- En el paso 100: máximo A = 0,1276; B = 0,1; norma L2(A−B) = 0,0968.
- Norma L2(A−B): paso 200 = 0,0771; 350 = 0,0618; 600 = 0,0490; 1.100 = 0,0371; 1.600 = 0,0311; 2.100 = 0,0274.
- Máximo A: 0,1276 → 0,1023.
- Radio efectivo: 2,6811 → 9,1776.
- Masa del exceso en toda la malla, definida como suma de max(rho−0,1, 0): 0,6434, comunicada como constante.

### Conclusión delimitada

Se comunicó una huella espacial distinguible durante 2.000 pasos después de retirar el estímulo, con dispersión progresiva y masa del exceso conservada. Es compatible con relajación difusiva lenta. No demuestra memoria histórica, histéresis ni estabilidad.

**Estado:** cerrado formalmente.

## 6. Experimento 002-B — Dependencia de la historia

### Pregunta

**¿Pueden dos campos informacionales que presentan estados observables equivalentes, pero que han llegado a ellos mediante historias de estimulación diferentes, mostrar evoluciones posteriores distintas bajo las mismas condiciones?**

### Diseño comunicado

- Historia A: estímulo gaussiano intenso, amplitud 0,4 durante 100 pasos.
- Historia B: estímulo más débil y prolongado; calibrar amplitud/duración para aproximar el estado final de A.
- Malla 32 × 32, fondo 0,1, D = 0,01, dt = 0,001, fronteras periódicas, ruido desactivado.
- Inspeccionar el estado dinámico completo, `rho`, `Memory(full)`, variables internas, snapshots y estímulos.
- Comparar estados completos, no solo máximo/media.
- Retirar estímulos y comparar la evolución posterior bajo condiciones idénticas.
- No forzar equivalencia ni introducir memoria artificial.

### Inspección y resultados comunicados

Según el informe de Perplexity:
- `rho` era la única variable del estado dinámico.
- La difusión era determinista y función de `rho`.
- `Memory(full)` solo registraba; no influía en la dinámica.
- No había variables internas ni acumuladores históricos adicionales.
- Se podían guardar snapshots completos y variar/retirar estímulos.

Calibración de la historia B, duración 400 pasos:
- amplitud 0,050 → L2 = 0,02472;
- amplitud 0,075 → L2 = 0,01461 (mejor ajuste);
- amplitud 0,100 → L2 = 0,02207;
- amplitud 0,125 → L2 = 0,03783;
- amplitud 0,150 → L2 = 0,05520.

Comparación A/B:
- En el paso 400, L2 residual = 0,01461.
- Máximo A = 0,11046; máximo B = 0,11297.
- Diferencia L2 posterior: paso 400 = 0,01461; 500 = 0,01100; 650 = 0,00917; 900 = 0,00811; 1.400 = 0,00707; 1.900 = 0,00641; 2.400 = 0,00597.

### Conclusión delimitada

No se alcanzó equivalencia suficiente entre estados para responder a la pregunta central. La diferencia residual disminuyó monótonamente, compatible con homogeneización difusiva. No hay evidencia de dependencia histórica en este experimento. La arquitectura inspeccionada carecía de un estado histórico dinámico adicional a `rho`.

**Clasificación:** experimento no concluyente para la pregunta de dependencia histórica; limitación de capacidad identificada.

## 7. Ampliación de Explorer 2: memoria histórica

Se autorizó ampliar el motor porque la pregunta de investigación requería una capacidad inexistente. La ampliación no debe presuponer qué resultado debe aparecer.

### Dos capacidades funcionales principales

**A. ExternalStimulusDynamics**
- Introducir un perfil externo configurable durante un intervalo de pasos.
- Permitir retirar el estímulo sin borrar la perturbación ya incorporada al campo.
- Continuar la evolución después de la retirada.
- Mantener separada esta entrada externa de la difusión y de la memoria.

**B. Subsistema de memoria histórica**
Separar explícitamente tres funciones:

1. **Registro:** almacenar estados anteriores del campo.
2. **Recuperación:** consultar estados anteriores por retardos temporales.
3. **Influencia dinámica:** permitir, opcionalmente, que información histórica intervenga en la evolución futura.

La existencia de registro no implica que la memoria influya dinámicamente.

### Componentes y responsabilidades

- `DiffusionDynamics`: dinámica de difusión original, preservada.
- `ExternalStimulusDynamics`: entrada externa temporal.
- `Memory(full)`: registro y trazabilidad general.
- `HistoryMemory`: almacenamiento y recuperación de historia del campo.
- `HistoryMemoryDynamics`: acoplamiento opcional de la historia con la evolución.

### Primera familia experimental de acoplamiento

Se propuso como primera implementación configurable, no como formulación definitiva de DIG:

`∂rho(t)/∂t = D∇²rho(t) + κ D Σ[k=1..m] w_k ∇²rho(t−kΔt)`

Parámetros:
- `enabled`
- `memory_strength` (κ)
- `memory_depth` (m)
- `sampling_interval` (Δt)
- `memory_kernel`
- `history_recording`

Kernels iniciales propuestos: exponencial y uniforme finito. Los pesos deben estar definidos y normalizados cuando exista historial suficiente. El arranque sin historial debe estar definido sin inventar estados pasados.

Condiciones esenciales:
- Memoria desactivada o κ = 0 debe reproducir la dinámica original de forma exacta o dentro de una tolerancia explícita y comprobada.
- La influencia histórica debe poder desactivarse independientemente del registro.
- El historial debe guardar copias independientes, orden temporal, paso y profundidad.
- Los snapshots deben incluir campo, historial, contador, parámetros, kernel, activación e índices temporales.
- Restaurar un snapshot y continuar debe reproducir la continuación correspondiente de una ejecución continua.
- Mantener la misma operación espacial y condiciones de frontera que la difusión original.
- No ocultar inestabilidades mediante recortes o normalizaciones improvisadas.
- No introducir gravedad, atracción, repulsión ni otros fenómenos DIG por anticipado.
- Conservar versiones previas y documentar cualquier cambio.

### Pruebas de validación exigidas para la memoria

1. Compatibilidad con la dinámica original.
2. Registro sin influencia dinámica.
3. Influencia histórica al activar el acoplamiento.
4. Comparación de kernels.
5. Comparación de profundidades.
6. Snapshot y restauración del historial.
7. Conservación de la suma global en las condiciones donde el operador lo garantiza.
8. Estabilidad y ausencia de NaN/inf.
9. Reproducibilidad de ejecuciones idénticas.

El formalismo se inspira en ideas generales de dinámica con memoria y ecuaciones generalizadas, pero esta implementación no debe denominarse una derivación exacta de Mori–Zwanzig. Es una construcción experimental concreta.

## 8. Experimento 002-C — Efecto de la memoria activa durante y después del estímulo

### Pregunta operativa

¿Cambia la evolución del campo cuando se activa el mecanismo de influencia histórica, comparado con la misma dinámica sin esa influencia?

### Diseño comunicado

- Misma historia de estimulación: gaussiana de amplitud 0,4 durante 100 pasos.
- Malla 32 × 32; fondo 0,1; difusión original y condiciones iguales.
- Brazo A: memoria desactivada (difusión pura).
- Brazo B: memoria activada, κ = 0,5, kernel exponencial, profundidad 5.
- Total: 2.100 pasos.
- Sin ruido.

### Resultados comunicados

| Paso | Máximo sin memoria | Máximo con memoria | Norma L2(A−B) | Suma A | Suma B |
|---:|---:|---:|---:|---:|---:|
| 100 | 0,12759 | 0,12495 | 0,00741 | 103,0434 | 103,0434 |
| 200 | 0,11791 | 0,11425 | 0,01213 | 103,0434 | 103,0434 |
| 500 | 0,10866 | 0,10624 | 0,01143 | 103,0434 | 103,0434 |
| 1.000 | 0,10464 | 0,10322 | 0,00920 | 103,0434 | 103,0434 |
| 1.500 | 0,10317 | 0,10217 | 0,00799 | 103,0434 | 103,0434 |
| 2.100 | 0,10230 | 0,10156 | 0,00707 | 103,0434 | 103,0434 |

Aclaración posterior comunicada por Perplexity:
- La memoria empieza a influir en el paso 1, cuando ya existe una entrada histórica.
- En el paso 0 el historial está vacío y no hay contribución histórica.
- Por tanto, la memoria interviene tanto durante los pasos de estimulación (1–99) como después de retirar el estímulo (paso 100 en adelante).
- El paso 100 es el primer punto de muestreo comunicado, no el instante de activación de la memoria.
- La diferencia observada se acumula durante la evolución; que después disminuya es compatible con la dinámica difusiva, pero los datos resumidos no bastan para afirmar de forma concluyente que «la difusión domina».

Sobre reproducibilidad:
- Las dinámicas ensayadas se comunicaron como deterministas y sin ruido/RNG.
- Cambiar la semilla no constituye una prueba de robustez en estas condiciones.
- Una prueba T9 habría confirmado ejecuciones idénticas con los mismos parámetros, según el informe; no equivale a robustez frente a cambios en condiciones iniciales.

### Conclusión delimitada

En la configuración ensayada, activar `HistoryMemoryDynamics` produjo una evolución distinta de la difusión sin memoria, mientras la suma global comunicada permaneció idéntica. Esto demuestra un efecto del mecanismo implementado en esa configuración, no memoria física ni validación de DIG. El experimento no separó la contribución de memoria durante el estímulo de la contribución posterior a su retirada.

**Estado:** resultados recibidos e interpretados; falta comprobación de robustez y una prueba específica de activación diferida.

## 9. Próximo trabajo acordado

### Paso 1 — Nueva versión del motor

La nueva versión será preparada por Claude a partir de los archivos que sí estén disponibles en su entorno o de una base que se identifique expresamente. No se debe afirmar que es idéntica a v0.4.7 si se ha reconstruido.

Pedir a Claude que implemente y documente las dos capacidades:
1. `ExternalStimulusDynamics`.
2. `HistoryMemory` + `HistoryMemoryDynamics`, manteniendo separadas grabación, recuperación e influencia dinámica.

Debe conservar la difusión original, incluir pruebas automatizadas, documentar diferencias respecto a la versión de partida y guardar el código y los resultados en un repositorio persistente. No se debe modificar el motor durante los experimentos.

### Paso 2 — Validación técnica abreviada

Antes de repetir experimentos:
- comprobar que la difusión original funciona con memoria desactivada;
- comprobar que el registro no altera por sí solo la dinámica;
- comprobar activación/desactivación de la influencia histórica;
- comprobar snapshots/restauración;
- comprobar conservación, estabilidad y reproducibilidad;
- conservar la versión anterior y la nueva de forma separada.

### Paso 3 — Repetición abreviada de la batería

Repetir, de forma controlada y con el mismo código versionado:
- 001: difusión/estabilidad básica, como control de referencia;
- 002-A: persistencia tras retirar estímulo;
- 002-B: comparación de historias distintas, sin forzar equivalencia;
- 002-C: memoria activada frente a desactivada;
- robustez de 002-C frente a pequeñas variaciones del fondo inicial.

No es necesario repetir todos los barridos de la primera batería si la nueva versión conserva la dinámica original y las pruebas de compatibilidad lo confirman.

## 10. Diseño cerrado para la comprobación de robustez

**Pregunta:** ¿Se mantiene cualitativamente el efecto de la memoria histórica ante pequeñas variaciones del fondo inicial?

Tres fondos:
- 0,1000
- 0,1001
- 0,0999

Para cada fondo, ejecutar dos brazos:
- memoria desactivada;
- memoria activada: κ = 0,5, kernel exponencial, profundidad 5.

Mantener idénticos los demás parámetros: malla, frontera, amplitud 0,4, estímulo gaussiano, duración 100 pasos, D, dt, duración total 2.100 pasos y muestreo.

Comparar cada pareja de brazos dentro de su mismo fondo. No comparar directamente las sumas globales entre fondos distintos, porque cambiar el fondo cambia la masa total inicial.

Registrar:
1. norma L2 entre campos con/sin memoria a lo largo del tiempo;
2. evolución de máximos y mínimos;
3. suma global de cada ejecución y conservación dentro de cada pareja;
4. valores no finitos o inestabilidades;
5. signo y evolución cualitativa del efecto en los tres fondos.

Criterio cualitativo: el efecto de memoria debe seguir siendo observable y presentar una evolución comparable en las tres condiciones. No exigir coincidencia numérica exacta. Si desaparece o cambia de forma sustancial en una condición, documentarlo; no ajustar parámetros para rescatar el resultado.

Esta prueba no ha sido ejecutada todavía.

## 11. Experimento posterior reservado: activación diferida

No mezclar con la prueba de robustez.

**Pregunta:** ¿Puede la historia acumulada durante la perturbación modificar la evolución posterior una vez retirado el estímulo?

Diseño conceptual:
- Desde el paso 0, registrar el historial mientras la influencia dinámica está desactivada.
- Aplicar el estímulo durante 100 pasos.
- En el paso 100, retirar el estímulo y activar la influencia histórica sin borrar el historial.
- Control idéntico que mantiene la influencia histórica desactivada.
- Comparar la evolución posterior.

Antes de ejecutarlo, inspeccionar que la arquitectura permita separar `history_recording` de la activación del acoplamiento dinámico y controlar el instante de activación. Si no lo permite, ampliar la arquitectura entre experimentos con justificación, pruebas y versionado. No simular una memoria previa ni crear un resultado ad hoc.

## 12. Estado de los archivos y trazabilidad

En el momento de redactar este documento:
- El entorno temporal que contenía los archivos de Explorer 2 v0.4.7, el script E002-C y sus resultados comunicó que había sido reiniciado.
- No se dispone aquí del código fuente original de v0.4.7, del script E002-C ni de sus JSON/gráficas.
- Los nombres de rutas que aparecieron en informes anteriores (por ejemplo, `/home/claude/v047/E002C_experiment.py` y `/home/claude/v047/E002C_result.json`) son rutas del entorno anterior y no deben considerarse accesibles.
- No reconstruir ni atribuir código fuente original a partir de fragmentos o descripciones.
- La primera batería sí está documentada en este repositorio en un archivo independiente.
- Al crear la nueva versión, guardar código, pruebas, configuración, resultados JSON, gráficas e informe en el repositorio persistente.

## 13. Resumen de estado

| Elemento | Estado |
|---|---|
| Auditoría técnica inicial | Cerrada |
| Primera batería de caracterización (1–5) | Cerrada y archivada |
| Investigación 001 | Cerrada |
| Experimento 002-A | Cerrado |
| Experimento 002-B | No concluyente; limitación de capacidad identificada |
| Experimento 002-C | Resultado comunicado; efecto dinámico observado en la configuración ensayada |
| Robustez 002-C | Pendiente |
| Nueva versión con estímulo externo y memoria histórica | Pendiente de implementación/documentación por Claude |
| Activación diferida | Experimento posterior reservado |

---

**JMPR — José María Pérez Rodríguez**  
*Génesis DIG — Punto de reanudación de Explorer 2*  
*18 de noviembre de 2026*
