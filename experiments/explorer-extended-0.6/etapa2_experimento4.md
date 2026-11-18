# Génesis DIG — Etapa 2, Experimento 4
## Duración de la transmisión histórica durante el decaimiento de la memoria

**Responsable:** JMPR  
**Motor declarado:** Explorer Extended 0.6  
**Desarrollador declarado:** Clau  
**Identificador:** `EXPLORER_EXTENDED`  
**Archivo ejecutado según el informe:** `explorer2_v0_4_6-1.py`  
**SHA-256 comunicado como verificado por la ejecución:** `4bf4f0daeea51d3fac892b281fe68831fc9d6597867442fc250c2a4b99f98b2e`  
**Estado:** Resultado comunicado por Perplexity; no ejecutado ni verificado independientemente por ChatGPT.

### 1. Pregunta de investigación

¿Cuánto tiempo permanece observable en el campo una diferencia histórica almacenada en la memoria externa cuando deja de recibir nuevas diferencias de entrada y evoluciona mediante su mecanismo de actualización y decaimiento?

### 2. Objetivo

Medir la evolución de la diferencia entre dos ramas con campos inicialmente equivalentes y memorias históricas diferentes, manteniendo activo el acoplamiento y retirando la fuente externa.

### 3. Procedimiento y configuración comunicados

- Malla 32 × 32; fondo 0.1.
- D = 0.01; dt = 0.001; fronteras periódicas; ruido desactivado.
- α = 0.01; κ = +0.001.
- Fuente gaussiana de tasa máxima 0.4, centro (0.515625, 0.515625), sigma 0.05.
- 100 pasos de estimulación y 2.000 pasos libres acoplados.
- Rama A: fuente de referencia.
- Rama B: misma fuente más perturbación compensada de amplitud 0.01 durante los dos primeros pasos.
- Durante la fase libre se retiró la fuente externa, pero se mantuvieron las ecuaciones de memoria y acoplamiento:
  - m(n+1) = (1 − α)m(n) + α[rho(n) − rho0]
  - rho(n+1) = L[rho(n) + κm(n)]
- Según el informe, no se modificó el motor.

### 4. Equivalencia al inicio de la fase libre

| Métrica | Valor comunicado |
|---|---:|
| Diferencia máxima entre campos A/B | 1.3878e-17 |
| Diferencia L2 entre campos | 1.5391e-16 |
| Diferencia máxima entre memorias A/B | 3.3647e-8 |
| Diferencia L2 entre memorias | 1.0551e-7 |

Los campos son equivalentes con margen respecto a la tolerancia 1e-10, mientras que las memorias conservan una diferencia histórica medible.

### 5. Resultados comunicados

| Paso libre | Tiempo | Campo: diferencia máxima | Campo: diferencia L2 | Memoria: diferencia máxima | Memoria: diferencia L2 |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.000 | 1.39e-17 | 1.54e-16 | 3.36e-8 | 1.06e-7 |
| 1 | 0.001 | 3.34e-11 | 1.05e-10 | 3.33e-8 | 1.04e-7 |
| 10 | 0.010 | 3.10e-10 | 9.88e-10 | 3.04e-8 | 9.55e-8 |
| 50 | 0.050 | 1.13e-9 | 3.81e-9 | 2.06e-8 | 6.47e-8 |
| 100 | 0.100 | 1.58e-9 | 5.67e-9 | 1.30e-8 | 4.11e-8 |
| 250 | 0.250 | 1.63e-9 | 7.05e-9 | 4.20e-9 | 1.42e-8 |
| 500 | 0.500 | 1.25e-9 | 7.03e-9 | 1.58e-9 | 7.51e-9 |
| 750 | 0.750 | 1.08e-9 | 7.34e-9 | 1.15e-9 | 7.21e-9 |
| 1000 | 1.000 | 1.03e-9 | 8.05e-9 | 1.04e-9 | 7.74e-9 |
| 1500 | 1.500 | 1.09e-9 | 1.05e-8 | 1.07e-9 | 9.90e-9 |
| 2000 | 2.000 | 1.31e-9 | 1.44e-8 | 1.26e-9 | 1.35e-8 |

### 6. Controles comunicados

| Control | Resultado |
|---|---|
| Dos ramas con historia idéntica | Diferencias de campo y memoria: 0 |
| Reproducción de la rama A | Diferencias de campo y memoria: 0 |
| Sin acoplamiento, κ = 0 | Diferencia de campo A/B al paso 2000: 1.39e-17 |
| Sin acoplamiento, κ = 0 | Diferencia de memoria A/B al paso 2000: 6.30e-17 |
| Valores no finitos | 0, según el informe |
| Modificación del motor | Ninguna, según el informe |

### 7. Interpretación y límites

El resultado comunicado muestra que la diferencia histórica se transmite al campo cuando existe acoplamiento. La diferencia máxima del campo crece hasta aproximadamente 1.63e-9 en torno al paso 250 y continúa siendo medible al paso 2000, alrededor de 1.31e-9. El control con κ = 0 elimina prácticamente la diferencia entre campos.

Hay dos matices importantes:

1. No se observa una desaparición completa de la diferencia de memoria. Al paso 2000 sigue siendo aproximadamente 1.26e-9 en norma máxima y 1.35e-8 en L2. Por tanto, no puede afirmarse que el campo conserve una huella después de que la diferencia de memoria haya desaparecido.
2. Las normas máximas de las diferencias de memoria disminuyen, pero sus normas L2 vuelven a crecer en la parte final: de 7.51e-9 en el paso 500 a 1.35e-8 en el paso 2000. La L2 de la diferencia de campo también crece de 7.03e-9 a 1.44e-8 en ese intervalo, aunque su diferencia máxima permanece del orden de 1e-9. Esto es compatible con una redistribución espacial de la diferencia, pero las métricas resumidas no bastan para demostrar su forma o mecanismo.

En consecuencia, la conclusión precisa no es que la memoria desaparezca y el campo conserve después una huella autónoma. Lo que se observa en los datos comunicados es que, durante la fase libre acoplada, la diferencia histórica sigue transmitiéndose y redistribuyéndose entre memoria y campo.

El resultado es coherente con el mecanismo matemático implementado. No demuestra memoria física, gravedad emergente ni la teoría DIG.

### 8. Conclusión

En la configuración probada, la diferencia histórica permanece observable en el campo durante los 2.000 pasos libres con acoplamiento. El efecto depende del acoplamiento, como indica el control κ = 0. Sin embargo, la diferencia de memoria no ha desaparecido al final del intervalo y las normas L2 crecen en la parte final; por ello, este experimento no demuestra todavía que el campo conserve una huella una vez extinguida la diferencia de memoria.

### 9. Procedencia y limitaciones documentales

Los datos, controles, hash y confirmación de ausencia de valores no finitos proceden del resultado comunicado por Perplexity en la conversación. ChatGPT no ejecutó el motor ni inspeccionó de forma independiente el archivo de código o las series completas. El informe conserva esta distinción y no presenta los resultados como verificación independiente.

**Autoría: JMPR**
