# E002 — Persistencia sin una acción explícita de persistir

**Autor:** José María Pérez Rodríguez (JMPR)  
**Proyecto:** Génesis DIG — Nivel 0  
**Fecha de registro:** 2026-10-19  
**Estado:** exploración computacional inicial; requiere controles adicionales.

## Pregunta

¿Puede aparecer una composición que permanezca sin cambios durante un intervalo, aunque las reglas no contengan una acción denominada «persistir»?

## Diseño operativo

- Estados abstractos: A, B y C.
- Seis individuos; estado inicial: A, B, C, A, B, C.
- Seis pares de estados posibles, incluyendo pares del mismo estado: AA, AB, AC, BB, BC y CC.
- Cada tabla asigna a cada par una salida entre A, B y C. Se enumeran todas las 3⁶ = 729 tablas.
- En cada ejecución se seleccionan al azar dos individuos. El de menor índice adopta el estado de salida asignado por la tabla al par observado.
- Cada tabla se ejecuta con cinco semillas (0–4), 200 pasos por ejecución: 3.645 ejecuciones.
- «Persistencia temporal» se define como al menos 30 transiciones consecutivas sin cambio en la composición global, ignorando el orden de los individuos.
- Por separado, se comprueba si la composición final es absorbente: bajo las reglas del modelo, ninguna pareja posible de individuos podría cambiar esa composición en un siguiente paso.

## Resultado de la ejecución registrada

- Tablas examinadas: 729.
- Ejecuciones: 3.645.
- Ejecuciones con persistencia temporal: 1.080 (29,63 %).
- Ejecuciones cuya composición final se clasifica como absorbente: 1.059.
- Composiciones finales distintas: 21.
- Promedio de cambios individuales de estado por ejecución: 97,27.

Las composiciones finales más frecuentes en esta ejecución fueron seis individuos en C (446 casos), cinco en B y uno en C (416), y dos en A, tres en B y uno en C (231).

## Qué permite concluir

En este modelo concreto, una fracción de ejecuciones satisface la definición temporal de persistencia sin que exista una instrucción explícita «persistir». El análisis también distingue la ausencia de cambios durante una ventana finita de la absorbencia de la composición final.

## Qué no permite concluir

No demuestra que la persistencia sea una propiedad fundamental del universo ni valida DIG. El comportamiento depende de las reglas enumeradas, la elección aleatoria de parejas, la actualización del individuo de menor índice, el estado inicial, el número de pasos y el umbral de persistencia. «Absorbente» significa aquí únicamente absorbente respecto a las transiciones permitidas por este programa.

## Siguientes comprobaciones

1. Revisar de forma independiente la definición y la implementación de absorbencia.
2. Añadir controles donde la persistencia esté impedida o impuesta por construcción.
3. Variar el tamaño del sistema, el estado inicial, el número de pasos y la ventana temporal, cambiando una dimensión cada vez.
4. Registrar distribuciones completas, no solo los casos más frecuentes.
5. Comprobar que las conclusiones sobreviven a cambios razonables del mecanismo de selección y actualización.
6. Ejecutar en el equipo Manjaro del autor y registrar la versión de Python y los comandos utilizados.

## Reproducción

Desde la raíz del repositorio, con Python 3:

    python experiments/nivel_0/experimento_002.py

El programa imprime un resumen JSON en la salida estándar. Los resultados deben regenerarse si se modifica el código; este documento describe la ejecución registrada, no garantiza que cualquier versión futura produzca idénticos valores.

**Autor:** José María Pérez Rodríguez (JMPR).
