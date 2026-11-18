# Génesis DIG — Etapa 2, Experimento 3
## Robustez y sensibilidad de la transmisión histórica

**Proyecto:** Génesis DIG  
**Autoría:** JMPR  
**Motor declarado:** Explorer Extended 0.6 (Clau)  
**Archivo declarado:** `explorer2_v0_4_6-1.py`  
**SHA-256 declarado por el ejecutor:** `4bf4f0daeea51d3fac892b281fe68831fc9d6597867442fc250c2a4b99f98b2e`

**Procedencia de resultados:** ejecución y métricas comunicadas por Perplexity y aportadas por el investigador. ChatGPT no ejecutó el motor ni inspeccionó los archivos binarios/CSV generados. La identificación/hash se consignan como datos reportados, no como verificación independiente.

---

## 1. Pregunta

¿La diferencia histórica transmitida al campo mediante acoplamiento cambia de forma ordenada cuando se modifica la intensidad de la perturbación que distingue las historias A y B?

## 2. Configuración

- Malla: 32 × 32.
- Fondo: 0.1.
- Difusión: D = 0.01.
- Paso temporal: dt = 0.001.
- Fronteras periódicas; ruido desactivado.
- Fuente gaussiana: tasa 0.4; centro (0.515625, 0.515625); sigma 0.05.
- Estimulación: 100 pasos; fase libre acoplada: 2000 pasos.
- Memoria: alpha = 0.01.
- Acoplamiento: kappa = +0.001.
- Amplitudes de perturbación de las ramas B: 0.0025, 0.005, 0.01 y 0.02.
- Ecuaciones externas declaradas:
  - m(n+1) = (1-alpha)m(n) + alpha(rho(n)-rho0)
  - rho(n+1) = L[rho(n) + kappa*m(n)]

El motor se declara sin modificaciones. La memoria y el acoplamiento son extensiones externas.

## 3. Equivalencia inicial de los campos

| Variante | Amplitud | Diferencia máxima A-B | Diferencia L2 |
|---|---:|---:|---:|
| B1 | 0.0025 | 1.39e-17 | 1.20e-16 |
| B2 | 0.005 | 1.39e-17 | 1.11e-16 |
| B3 | 0.01 | 1.39e-17 | 1.54e-16 |
| B4 | 0.02 | 1.39e-17 | 1.35e-16 |

Según el informe de ejecución, las cuatro variantes cumplen holgadamente la tolerancia de equivalencia de 1e-10.

## 4. Diferencias iniciales de memoria

| Variante | Amplitud | Diferencia máxima de memoria | Diferencia L2 |
|---|---:|---:|---:|
| B1 | 0.0025 | 8.41e-9 | 2.64e-8 |
| B2 | 0.005 | 1.68e-8 | 5.28e-8 |
| B3 | 0.01 | 3.36e-8 | 1.06e-7 |
| B4 | 0.02 | 6.73e-8 | 2.11e-7 |

Las diferencias de memoria aumentan proporcionalmente con la amplitud introducida.

## 5. Diferencias de campo al paso 2000

| Variante | Amplitud | Diferencia máxima A-B | Diferencia L2 |
|---|---:|---:|---:|
| B1 | 0.0025 | 3.26e-10 | 3.61e-9 |
| B2 | 0.005 | 6.53e-10 | 7.21e-9 |
| B3 | 0.01 | 1.31e-9 | 1.44e-8 |
| B4 | 0.02 | 2.61e-9 | 2.88e-8 |

El informe comunica que la diferencia de campo aparece desde el primer paso acoplado, alcanza un máximo alrededor del paso 250 y después se mantiene en un orden semejante hasta el paso 2000. La tabla completa de valores intermedios no fue incluida en el material recibido.

B3 reproduce, según el ejecutor, el resultado del Experimento 2.

## 6. Controles comunicados

- Historia idéntica: diferencias de campo y memoria exactamente cero.
- Acoplamiento nulo (kappa = 0): las diferencias A-B no se transmiten al campo y siguen el comportamiento desacoplado.
- Reproducción B3: resultado coincidente con el Experimento 2.
- Equivalencia inicial: cumplida para las cuatro variantes.

Estos controles se consignan según el informe de Perplexity; no se dispone aquí de las series completas para una auditoría independiente.

## 7. Interpretación

El resultado comunicado es compatible con transmisión de diferencias históricas desde la memoria al campo en el modelo computacional ensayado. En el rango de amplitudes 0.0025–0.02, la diferencia final A-B del campo escala aproximadamente de forma lineal con la amplitud de la perturbación.

**Matiz matemático importante:** esta proporcionalidad no constituye por sí sola evidencia de un mecanismo nuevo o de una ley física emergente. Las ecuaciones utilizadas son lineales en el campo y en la memoria, y el operador de difusión empleado también es lineal. Con las mismas condiciones y sin saturaciones, es esperable que escalar la perturbación inicial escale proporcionalmente la diferencia posterior. Por tanto, el experimento comprueba coherencia y sensibilidad del mecanismo implementado dentro del intervalo ensayado; no demuestra una relación universal ni permite extrapolar fuera de ese intervalo.

El efecto histórico A-B es pequeño en magnitud absoluta (del orden de 10^-10 a 10^-9 en diferencia máxima de campo). Su distinción respecto del error numérico queda respaldada por los controles comunicados, aunque una auditoría independiente requeriría las series completas y los datos de ejecución.

## 8. Conclusión

**Conclusión limitada:** bajo las ecuaciones externas y parámetros ensayados, las diferencias históricas almacenadas en la memoria se transmiten al campo cuando existe acoplamiento. La magnitud de la diferencia transmitida crece aproximadamente en proporción a la amplitud de la perturbación inicial en las cuatro variantes probadas.

Esto no demuestra memoria física fundamental, gravedad emergente ni valida la teoría DIG. Tampoco establece que la respuesta vaya a ser lineal para otras amplitudes, otros valores de alpha/kappa o dinámicas distintas.

## 9. Archivos declarados por el ejecutor

- `output/genesis_dig_002C_stage2_experiment3/campos_y_memorias.npz`
- `output/genesis_dig_002C_stage2_experiment3/resultados.csv`
- `output/genesis_dig_002C_stage2_experiment3/resultados.json`
- `output/genesis_dig_002C_stage2_experiment3/evolucion_diferencias.png`

No se han incorporado al repositorio ni inspeccionado en esta revisión.

---

**Estado:** Experimento 3 analizado a partir del informe y las cifras proporcionadas. La conclusión es favorable dentro del modelo y del intervalo estudiado, con la salvedad de que la proporcionalidad es esperable por la linealidad de las ecuaciones.
