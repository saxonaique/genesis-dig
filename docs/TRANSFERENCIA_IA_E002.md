# Nota de transferencia para revisión externa — Génesis DIG E002

**Autor del proyecto:** José María Pérez Rodríguez (JMPR)  
**Fecha:** 2026-10-19  
**Repositorio maestro:** https://github.com/saxonaique/genesis-dig

## Encargo

Revisa el Experimento E002 de manera independiente. No lo presentes como una validación de DIG ni conviertas las hipótesis del proyecto en premisas que el código deba confirmar. Prioriza errores de implementación, definiciones operacionales ambiguas, controles ausentes y experimentos capaces de refutar la interpretación inicial.

## Archivos relevantes

- `experiments/nivel_0/experimento_002.py`: implementación reproducible.
- `tests/test_experimento_002.py`: pruebas básicas de invariantes y reproducibilidad.
- `docs/EXPERIMENTO_002.md`: pregunta, diseño, resultados y limitaciones.
- `results/nivel_0/experimento_002_resumen.json`: salida registrada.
- `README.md`: estado general actualizado del proyecto.

## Resultado de referencia

La exploración enumera 729 tablas de interacción, cinco semillas por tabla y 200 pasos por ejecución (3.645 ejecuciones). Con el criterio de al menos 30 transiciones consecutivas sin cambio de composición, 1.080 ejecuciones (29,63 %) presentan persistencia temporal. La composición final se clasifica como absorbente en 1.059 ejecuciones. Se observan 21 composiciones finales distintas y una media de 97,27 cambios individuales de estado por ejecución.

Estos números son resultados de un modelo abstracto específico, no propiedades físicas.

## Preguntas que debe responder la revisión

1. ¿La definición de composición absorbente es correcta para todas las parejas de individuos posibles y para la regla de actualización del individuo de menor índice?
2. ¿Las pruebas cubren casos límite suficientes? ¿Qué pruebas adicionales detectarían errores?
3. ¿La métrica de persistencia temporal está bien definida y calculada? ¿Conviene informar por separado rachas máximas, estados finales absorbentes y ciclos?
4. ¿Qué sesgos introducen la elección aleatoria de parejas y la actualización del individuo de menor índice?
5. Diseña controles negativos y positivos que permitan detectar persistencia por construcción.
6. Propón un análisis de sensibilidad mínimo que pueda ejecutarse con recursos modestos.
7. Señala resultados que contradigan o debiliten la interpretación inicial, no solo los que parezcan apoyarla.

## Criterio de aceptación

No propongas nuevas interpretaciones físicas hasta que el código, las métricas y los controles hayan sido revisados. Devuelve recomendaciones concretas y priorizadas, con pruebas reproducibles cuando sea posible. Distingue claramente errores demostrados, riesgos metodológicos y sugerencias opcionales.
