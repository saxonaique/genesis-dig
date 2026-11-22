# GÉNESIS DIG — Informe del Experimento E030
## Identificación de las condiciones iniciales del acoplamiento

**Investigador:** José María Pérez Rodríguez (JMPR)  
**Fecha del informe:** 22 de noviembre de 2026  
**Estado:** Resultado exploratorio; no concluyente  
**Línea:** Explorer 2 / Nivel 0

## 1. Pregunta experimental

¿Qué propiedades del estado inicial permiten explicar que distintas semillas desarrollen relaciones dinámicas diferentes entre la media global y la asimetría local?

## 2. Objetivo

Examinar si características medibles en el paso inicial permiten anticipar diferencias entre los coeficientes del modelo dependiente del estado comunicado en E029, manteniendo intacta la dinámica del motor.

## 3. Metodología comunicada

Se reutilizó la dinámica de las etapas anteriores. Para cada una de las cinco semillas (7, 21, 42, 99 y 2024) se calcularon propiedades del estado inicial (paso 0) y se compararon con los coeficientes del modelo C de E029, ajustado sobre la ventana 8.000–9.000.

Propiedades iniciales consideradas:
- Media inicial del campo.
- Varianza y dispersión.
- Asimetría de la distribución.
- Parámetro p₋ inicial.
- Autocorrelación espacial y correlación con el tablero.
- Distribución de diferencias locales.

No se comunicaron aquí los valores completos de todas las propiedades (en particular varianza, autocorrelación espacial y correlación con tablero), por lo que no se reconstruyen ni se inventan.

## 4. Resultados comunicados

| Semilla | Media inicial | Asimetría inicial | p₋ inicial | coef_M | coef_S | coef_dM | Intercepto |
|---|---:|---:|---:|---:|---:|---:|---:|
| 7 | −0,00075 | +0,0146 | 0,5010 | −2,3×10⁻¹³ | −9,37×10⁻⁴ | +6,9×10⁻⁶ | +3,7×10⁻⁶ |
| 21 | +0,00040 | −0,0211 | 0,5000 | +9,8×10⁻⁴ | −2,51×10⁻³ | +4,9×10⁻⁶ | +4,8×10⁻⁷ |
| 42 | −0,00029 | −0,0459 | 0,5059 | +1,1×10⁻¹² | −9,37×10⁻⁴ | −3,7×10⁻⁴ | +2,2×10⁻⁵ |
| 99 | −0,00005 | −0,0882 | 0,4961 | −9,8×10⁻¹⁴ | −9,43×10⁻⁴ | +1,6×10⁻⁵ | −1,5×10⁻⁵ |
| 2024 | +0,00003 | +0,0346 | 0,5000 | +9,4×10⁻⁴ | −2,43×10⁻³ | +4,0×10⁻⁶ | +3,0×10⁻⁶ |

Se comunicaron las siguientes asociaciones exploratorias:
- init_p_neg frente al intercepto: correlación aproximada de 0,985.
- init_mean frente a coef_M y coef_S: correlaciones aproximadas de magnitud ±0,75.
- Las demás propiedades iniciales examinadas no mostraron una relación clara y consistente con los coeficientes.

Estas correlaciones se basan en cinco observaciones y no constituyen evidencia suficiente de una relación general.

## 5. Interpretación

Con las cinco semillas examinadas no se identifica una propiedad inicial aislada que explique de forma robusta las diferencias entre los coeficientes del acoplamiento.

El resultado no demuestra que las condiciones iniciales sean irrelevantes. Deja abiertas, entre otras, estas posibilidades:
- Dependencias combinadas entre varias propiedades iniciales.
- Características espaciales no capturadas por los descriptores utilizados.
- Variables iniciales todavía no medidas.
- Que los coeficientes del ajuste E029-C no sean parámetros comparables o estables entre semillas.

## 6. Limitaciones y cautelas

1. **Tamaño muestral:** cinco semillas son insuficientes para establecer correlaciones robustas, estimar capacidad predictiva general o seleccionar variables con fiabilidad.
2. **Auditoría pendiente de E029-C:** no se ha verificado de forma independiente la fórmula exacta, los cuatro parámetros mencionados, los grados de libertad, el procedimiento de ajuste ni la separación entre entrenamiento y validación.
3. **Interpretación de coeficientes:** hasta completar esa auditoría, los coeficientes se consideran descriptores del ajuste comunicado, no constantes físicas ni parámetros demostrados de una ley dinámica.
4. **R² de entrenamiento:** el ajuste perfecto comunicado por semilla no permite distinguir por sí solo entre una dinámica determinista, una parametrización suficientemente flexible y un sobreajuste.
5. **Trazabilidad:** los resultados de este informe proceden de datos comunicados por el investigador; no se ha realizado aquí una reproducción independiente a partir del código y los datos crudos.

## 7. Conclusión experimental

**No se identifica una propiedad inicial que explique de forma robusta las diferencias entre semillas en los coeficientes del acoplamiento, con las cinco configuraciones y los descriptores disponibles.**

La conclusión se limita al conjunto estudiado. No permite afirmar que las condiciones iniciales no condicionen la evolución ni descartar la existencia de distintas familias o regímenes dinámicos.

## 8. Decisión metodológica y continuidad

No se modifica el motor ni su dinámica.

Antes de utilizar los coeficientes de E029-C como variables objetivo para nuevos análisis, debe auditarse el modelo C: fórmula exacta, parámetros y grados de libertad, código de ajuste, variables utilizadas, datos de entrenamiento y test, y posibles fugas de información.

Una vez auditado E029-C, el siguiente paso razonable será ampliar el número de semillas mediante un protocolo fijado de antemano y comprobar si las asociaciones exploratorias se mantienen en configuraciones no utilizadas para formularlas. No se debe presentar esa ampliación como una confirmación anticipada.

## 9. Clasificación epistemológica

- **Propiedad del campo:** comportamiento observado en las ejecuciones comunicadas.
- **Propiedad de la configuración:** diferencias entre las cinco semillas estudiadas.
- **Ley dinámica:** no identificada ni validada por E030.
- **Hipótesis teórica:** podrían existir diferentes regímenes o familias dinámicas condicionados por la configuración inicial; permanece abierta y requiere pruebas adicionales.

---
**Autoría: JMPR — José María Pérez Rodríguez**  
**Génesis DIG — Cuaderno de laboratorio**
