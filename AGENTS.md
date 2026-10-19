# Instrucciones para Codex — Génesis DIG

**Autor del proyecto:** José María Pérez Rodríguez (JMPR)  
**Ámbito actual:** Génesis DIG, Nivel 0.  
**Idioma de trabajo y documentación:** español.

## Objetivo

Ayudar a desarrollar una investigación computacional reproducible. El trabajo actual consiste en auditar y ejecutar los experimentos del Nivel 0 antes de proponer nuevos modelos.

## Reglas obligatorias

1. **No inventes resultados.** Ejecuta el código y registra la salida real. No deduzcas cifras y luego las presentes como medidas.
2. **No confundas funcionamiento del programa con validación física.** Los experimentos abstractos sirven para estudiar el modelo definido por el código; por sí solos no validan la teoría DIG ni describen necesariamente el universo.
3. **Inspecciona antes de modificar.** Lee el código, los tests y la documentación pertinente. Explica cualquier discrepancia entre ellos.
4. **Haz cambios pequeños y trazables.** No reescribas el proyecto entero ni cambies reglas del experimento sin autorización. Si detectas un error, reproduce el problema y propone una corrección mínima.
5. **Reproducibilidad.** Anota los comandos ejecutados, versión de Python, resultados y cualquier limitación del entorno. Usa semillas explícitas cuando proceda.
6. **Pruebas.** Ejecuta la suite pertinente después de modificar código. Informa del número de pruebas que pasan o fallan; no afirmes que pasan si no se ejecutaron.
7. **Documentación sincronizada.** Si cambian resultados, actualiza los documentos y resúmenes derivados únicamente a partir de la ejecución real. Comprueba que coincidan con el código.
8. **Preserva el historial.** No borres experimentos ni resultados previos. No hagas commits ni push salvo que José María lo pida expresamente.
9. **Claridad científica.** Separa observaciones, interpretación, hipótesis y limitaciones. Explicita las decisiones operativas del modelo.
10. **Autoría.** En documentos de investigación nuevos, conserva la autoría «José María Pérez Rodríguez (JMPR)» cuando corresponda.

## Primera tarea: auditoría de E002

Trabaja en este orden:

1. Lee `experiments/nivel_0/experimento_002.py`, `tests/test_experimento_002.py`, `docs/EXPERIMENTO_002.md`, `docs/TRANSFERENCIA_IA_E002.md` y `results/nivel_0/experimento_002_resumen.json`.
2. Comprueba la definición de persistencia temporal y de composición absorbente. Busca errores de lógica, casos límite y desajustes entre doc, tests y código.
3. Ejecuta las pruebas existentes y el experimento completo desde la raíz del repositorio. Registra la versión de Python, los comandos y la salida real.
4. Compara los resultados reales con el documento y el JSON versionados. En particular, verifica la cifra de ejecuciones con composición final absorbente; no la des por correcta de antemano.
5. Si hay discrepancias, no cambies silenciosamente el diseño experimental. Describe primero qué no coincide y por qué. Propón la corrección mínima y actualiza los resultados/documentos solo cuando la lógica esté comprobada.
6. Añade o ajusta pruebas para cubrir los casos relevantes, manteniendo claro qué comportamiento se está verificando.
7. Termina con un informe breve: archivos inspeccionados/cambiados, comandos ejecutados, pruebas y resultados, discrepancias, limitaciones y siguiente paso recomendado.

No empieces E003 ni introduzcas nuevas hipótesis hasta cerrar esta auditoría y recibir autorización de José María.
