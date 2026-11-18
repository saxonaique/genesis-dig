# Génesis DIG — Etapa 1: almacenamiento temporal observacional

**Autoría:** José María Pérez Rodríguez (JMPR)  
**Proyecto:** Génesis DIG  
**Motor de referencia:** Explorer Extended 0.6 — Clau  
**Archivo de referencia comunicado:** `explorer2_v0_4_6-1.py`  
**Estado:** etapa cerrada según los resultados comunicados; sin acoplamiento de la memoria al campo.

---

## 1. Pregunta experimental

¿Puede un sistema conservar una representación temporal de perturbaciones anteriores y mostrar cómo se acumula, evoluciona y desvanece, sin que esa información intervenga en la evolución del campo?

## 2. Objetivo y alcance

Caracterizar una memoria externa estrictamente observacional. La memoria registra información derivada de estados anteriores, pero no modifica el campo ni realimenta su dinámica.

Esta etapa no pretende demostrar memoria física ni validar la teoría DIG. Su objetivo es comprobar la capacidad computacional de almacenamiento temporal bajo las reglas definidas.

## 3. Diseño comunicado

Se mantuvo el motor de referencia sin modificar. La memoria se implementó externamente mediante:

\[
m^{n+1}=(1-\alpha)m^n+\alpha(\rho^n-\rho_0)
\]

La evolución del campo permaneció desacoplada de la memoria:

\[
\rho^{n+1}=L(\rho^n+dt\,S(n))
\]

La memoria se actualizaba a partir del campo \(\rho(n)\), antes de incorporar la fuente del paso correspondiente. No existía término de realimentación desde \(m\) hacia \(\rho\).

Configuración comunicada:
- Malla: 32 × 32.
- Fondo: \(\rho_0=0.1\).
- Difusión: \(D=0.01\).
- Paso temporal: \(dt=0.001\).
- Fronteras periódicas.
- Ruido desactivado.
- Memoria inicial nula, salvo la prueba específica de decaimiento.
- Parámetros de memoria: \(\alpha=0.01, 0.05, 0.1, 0.2\).
- Fuente gaussiana positiva/negativa según la prueba, con tasa máxima 0.4, centro normalizado (0.515625, 0.515625) y sigma 0.05.

Se comunicaron tres pruebas de respuesta:
- **A:** fuente positiva durante 2.100 pasos.
- **B:** fuente positiva durante 100 pasos y después 2.000 pasos libres.
- **C:** fuente positiva durante 50 pasos, negativa durante 50 y después 2.000 pasos libres.

Además, se realizó una prueba separada de entrada nula, inicializando la memoria en 1 y dejando la entrada a cero durante 2.000 actualizaciones.

## 4. Resultados comunicados

### 4.1. Decaimiento con entrada nula

La memoria siguió la ley esperada:

\[
m(n+k)=(1-\alpha)^k m(n)
\]

Los errores máximos comunicados entre la memoria calculada y la predicción algebraica fueron:

| α | Error máximo absoluto |
|---:|---:|
| 0.01 | 1.665 × 10⁻¹⁶ |
| 0.05 | 1.665 × 10⁻¹⁶ |
| 0.1 | 1.110 × 10⁻¹⁶ |
| 0.2 | 5.551 × 10⁻¹⁷ |

Los valores finales comunicados coincidieron con la predicción de decaimiento exponencial, dentro de la precisión numérica.

### 4.2. Reconstrucción

El informe externo comunicó que la memoria pudo reconstruirse a partir de los campos registrados, con errores del orden de 10⁻¹⁶.

### 4.3. Respuesta a las secuencias A, B y C

La ejecución se comunicó como completa y se indicaron archivos de resultados, métricas y gráficas. Sin embargo, no se conservaron en esta conversación las tablas completas de métricas temporales de A, B y C. Por ello, este documento no atribuye valores cuantitativos adicionales a esas pruebas.

## 5. Interpretación

Los resultados disponibles respaldan que:
1. La variable de memoria externa almacena una representación temporal del campo.
2. Su evolución depende del parámetro \(\alpha\).
3. Con entrada nula, la memoria decae conforme a la ley exponencial definida.
4. La reconstrucción comunicada desde los campos registrados es consistente con la ecuación de actualización.
5. La memoria no intervino en la evolución del campo durante esta etapa, por diseño.

La prueba valida el mecanismo matemático y computacional de almacenamiento observacional implementado. No demuestra que el sistema tenga memoria dinámica intrínseca ni que la memoria represente un fenómeno físico.

## 6. Limitaciones

- La ejecución y sus resultados proceden de informes externos de Perplexity; ChatGPT no ejecutó el motor ni inspeccionó directamente los archivos generados.
- No se dispone aquí de las series completas ni de las métricas detalladas de las pruebas A, B y C.
- La validación algebraica del decaimiento es sólida según los errores comunicados, pero no sustituye el análisis completo de todas las respuestas temporales.
- La memoria es una extensión externa observacional, no una capacidad nativa de la dinámica de difusión examinada.

## 7. Conclusión y cierre de etapa

**Conclusión:** la Etapa 1 cumple su objetivo operativo: se implementó externamente una memoria observacional que conserva una representación temporal del campo, cuya actualización y decaimiento siguen la ecuación especificada, sin influir en la dinámica del campo.

**Estado: CERRADA.**

La etapa siguiente puede investigar por separado qué ocurre cuando esa memoria se acopla al campo. Esa cuestión corresponde a la Etapa 2 y no forma parte de la conclusión de esta etapa.

No se interpreta este resultado como evidencia de memoria física ni como confirmación de DIG.

## 8. Procedencia y trazabilidad

Los parámetros, resultados y errores numéricos de este documento proceden de los informes de ejecución de Perplexity compartidos por JMPR en las conversaciones de trabajo. La atribución del motor corresponde a Explorer Extended 0.6 — Clau, según la identificación documental adoptada para el proyecto.

No se afirma que ChatGPT haya ejecutado el motor ni inspeccionado directamente los archivos originales.

**Autoría:** José María Pérez Rodríguez (JMPR)  
**Proyecto:** Génesis DIG
