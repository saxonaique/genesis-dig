# Génesis DIG — Etapa 2, Experimento 1: influencia de la memoria sobre el campo

**Autoría:** José María Pérez Rodríguez (JMPR)  
**Proyecto:** Génesis DIG  
**Motor de referencia:** Explorer Extended 0.6 — Clau  
**Archivo de referencia comunicado:** `explorer2_v0_4_6-1.py`  
**Fecha de documentación:** 2026-11-18  
**Estado:** resultados numéricos parciales documentados; auditoría complementaria pendiente por falta de series completas.

---

## 1. Pregunta experimental

¿Puede una memoria externa que conserva información de estados anteriores modificar la evolución futura del campo y transmitir diferencias históricas entre dos ramas (A y B) que parten de campos espacialmente equivalentes?

## 2. Objetivo

Evaluar la influencia de una memoria externa acoplada al campo, distinguiendo entre:

- el efecto general del acoplamiento;
- la posible transmisión de la diferencia histórica entre A y B;
- el comportamiento del control desacoplado.

Este experimento es computacional y exploratorio. No presupone una interpretación física ni constituye una demostración de la teoría DIG.

## 3. Configuración comunicada

- Malla: 32 × 32.
- Campo de fondo: \(\rho_0=0.1\).
- Difusión: \(D=0.01\).
- Paso temporal: \(dt=0.001\).
- Fronteras: periódicas.
- Ruido: desactivado.
- Memoria inicial: cero.
- Fuente original: gaussiana, tasa máxima 0.4, centro normalizado (0.515625, 0.515625), sigma 0.05.
- Rama A: fuente original durante 100 pasos.
- Rama B: misma fuente más una perturbación compensada en los dos primeros pasos, con magnitud de referencia \(10^{-2}\).
- Fase libre: 2.000 pasos.
- Parámetros de memoria: \(\alpha=0.01, 0.05, 0.1, 0.2\).
- Acoplamiento: \(\kappa=0, +0.001, -0.001\).

La memoria externa se describió mediante:

\[
m(n+1)=(1-\alpha)m(n)+\alpha(\rho(n)-\rho_0)
\]

y el campo acoplado mediante:

\[
\rho(n+1)=L[\rho(n)+\kappa m(n)]
\]

donde \(L\) representa un paso de difusión. La memoria utilizada para actualizar el campo es \(m(n)\).

## 4. Equivalencia inicial de los campos

La comparación inicial comunicada entre A y B fue:

- Diferencia máxima absoluta: \(1.3878\times10^{-17}\).
- Diferencia L2: \(1.5391\times10^{-16}\).

Por tanto, los campos iniciales de ambas ramas son equivalentes dentro de la precisión numérica comunicada.

Las memorias sí conservaban diferencias iniciales dependientes de \(\alpha\):

| α | Diferencia máxima de memoria A-B | Diferencia L2 |
|---:|---:|---:|
| 0.01 | 3.3647 × 10⁻⁸ | 1.0551 × 10⁻⁷ |
| 0.05 | 2.9552 × 10⁻⁹ | 9.2667 × 10⁻⁹ |
| 0.1 | 2.9544 × 10⁻¹¹ | 9.2641 × 10⁻¹¹ |
| 0.2 | 5.7352 × 10⁻¹⁶ | 1.8032 × 10⁻¹⁵ |

Con α = 0.2, la diferencia inicial de memoria es prácticamente indistinguible de cero a la precisión indicada.

## 5. Efecto del acoplamiento sobre el campo

La siguiente tabla recoge la diferencia máxima absoluta del campo de cada rama respecto a su control desacoplado (κ = 0), al paso 2.000:

| α | κ = +0.001 | κ = -0.001 |
|---:|---:|---:|
| 0.01 | 0.01243745 | 0.00206413 |
| 0.05 | 0.01425312 | 0.00200366 |
| 0.1 | 0.01446602 | 0.00199536 |
| 0.2 | 0.01456527 | 0.00199101 |

El acoplamiento modifica el campo respecto al control. En las configuraciones comunicadas, el efecto con κ positivo es claramente mayor que con κ negativo.

Esta asimetría describe la respuesta de las ecuaciones implementadas. Por sí sola no demuestra atracción, repulsión ni ningún fenómeno físico.

## 6. Transmisión de diferencias históricas A-B

Diferencia máxima absoluta entre los campos A y B al paso 2.000:

| α | κ = +0.001 | κ = -0.001 |
|---:|---:|---:|
| 0.01 | 1.3057 × 10⁻⁹ | 2.7718 × 10⁻¹¹ |
| 0.05 | 2.7058 × 10⁻¹¹ | 5.1564 × 10⁻¹³ |
| 0.1 | 1.3860 × 10⁻¹³ | 2.6368 × 10⁻¹⁵ |
| 0.2 | 8.3267 × 10⁻¹⁷ | 0 |

La diferencia histórica A-B aparece en el campo acoplado, pero es extremadamente pequeña frente a la modificación común del campo respecto al control.

Ejemplo: para α = 0.1 y κ = +0.001, cada rama se desvía del control en aproximadamente 0.014466, mientras que la diferencia máxima entre A y B es aproximadamente \(1.386\times10^{-13}\).

Por tanto, el efecto general del acoplamiento es mucho mayor que la señal que distingue las dos historias.

## 7. Control desacoplado

Para κ = 0, la diferencia máxima entre el campo acoplado y la ejecución desacoplada fue exactamente 0 para los cuatro valores de α comunicados.

La diferencia A-B del campo en el control κ = 0 permaneció en el orden de la precisión de máquina (máximo comunicado de aproximadamente \(1.39\times10^{-17}\)).

Este control respalda que las desviaciones observadas con κ distinto de cero proceden del término de acoplamiento implementado y no de una discrepancia apreciable entre las ejecuciones de control.

## 8. Interpretación

Los resultados disponibles respaldan las siguientes observaciones:

1. Una memoria externa puede intervenir en la evolución del campo cuando se introduce el acoplamiento.
2. El signo de κ produce respuestas de magnitud diferente en esta configuración.
3. La diferencia histórica entre A y B llega al campo acoplado, pero su magnitud final es muy pequeña.
4. La modificación del campo respecto al control es prácticamente igual en A y B.
5. Para α = 0.2, la memoria inicial A-B ya es prácticamente nula, aunque el acoplamiento sigue modificando el campo. Esto muestra que la modificación común del campo no puede interpretarse como transmisión de la diferencia histórica entre las ramas.

La conclusión más ajustada es que el experimento muestra influencia de la memoria externa sobre el campo, pero no demuestra una transmisión históricamente diferenciada de magnitud significativa.

## 9. Limitaciones y comprobaciones pendientes

El análisis se basa en los resultados y el JSON facilitados en la conversación. No se han inspeccionado directamente los archivos binarios o las series completas de la ejecución.

El JSON contiene métricas en los pasos 1, 100 y 2.000, pero no las series de todos los pasos. Por ello quedan pendientes:

- suma total del campo y masa de exceso durante toda la ejecución;
- variación de masa respecto al estado inicial;
- diferencia de masa entre A y B;
- descomposición temporal de la memoria común \((m_A+m_B)/2\) y la memoria diferencial \(m_A-m_B\);
- evolución completa, paso a paso, de las diferencias de campo y memoria;
- relación cuantitativa entre memoria diferencial y diferencia de campo a lo largo de toda la fase libre.

La conservación de masa no se confirma ni se descarta con los datos actuales. Tampoco se afirma estabilidad numérica completa: el informe de ejecución no comunicó fallos, pero faltan las series necesarias para una revisión exhaustiva.

No se repitió la simulación ni se modificaron el motor, las ecuaciones o los parámetros para elaborar este informe.

## 10. Conclusión provisional

**Resultado:** el acoplamiento de la memoria externa modifica la evolución del campo. Sin embargo, la diferencia entre las historias A y B apenas se refleja en la diferencia final entre sus campos.

La evidencia disponible se aproxima a la categoría:

**A. Modifica el campo sin transmitir diferencias históricas apreciables**, con la precisión de que se observa una diferencia A-B muy pequeña, no exactamente nula en todas las configuraciones.

La conservación de masa y la evolución temporal completa permanecen sin determinar.

Este resultado caracteriza únicamente el sistema computacional y los parámetros examinados. No demuestra memoria física ni valida la teoría DIG.

## 11. Procedencia y trazabilidad

Los valores de este documento proceden del JSON y de los informes de ejecución compartidos por JMPR en la conversación. La ejecución se atribuye al informe externo de Perplexity sobre Explorer Extended 0.6 — Clau. Este documento no afirma que ChatGPT haya ejecutado el motor ni inspeccionado directamente los archivos originales.

**Autoría:** José María Pérez Rodríguez (JMPR)  
**Proyecto:** Génesis DIG
