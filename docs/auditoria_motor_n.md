# Auditoría inicial del código histórico de Motor N

**Proyecto:** Génesis DIG  
**Autoría:** José María Pérez Rodríguez (JMPR)  
**Fecha:** 2026-10-19  
**Estado:** revisión estática inicial; no equivale a ejecución ni validación experimental.

## Objetivo

Determinar qué partes del código histórico pueden reutilizarse, cuáles deben mantenerse solo como referencia y cuáles no deben incorporarse directamente al Nivel 0 de Génesis DIG.

## Repositorios examinados

- [saxonaique/motor-n](https://github.com/saxonaique/motor-n)
- [saxonaique/motor_n_dig](https://github.com/saxonaique/motor_n_dig)

Se inspeccionaron los árboles completos publicados en la rama `main` (34 entradas en `motor-n` y 152 en `motor_n_dig`, incluyendo directorios y archivos compilados), y se leyeron varios módulos centrales. La búsqueda de este inventario no identificó scripts denominados Experimentos 001–005 ni una secuencia inequívoca equivalente. Esto no demuestra que nunca existieran: solo que no han sido localizados en los árboles actuales examinados.

## Hallazgos principales

### 1. Motor de campo numérico

Archivos revisados:
- `motor_n_dig.py`
- `motor_n_dig_extendido.py`
- `MotorN_README.md`
- `motor-n/.../laboratorio_n.py`
- `motor-n/.../convert_edf_to_pattern.py`

El código proporciona prototipos funcionales en concepto para evolucionar matrices, inyectar patrones, visualizar campos y registrar métricas. Es un antecedente útil para aprender cómo se construyeron las primeras simulaciones.

Problemas que impiden considerarlo validado:
- El campo en rejilla y sus condiciones de contorno se imponen desde el comienzo.
- En `MotorN`, el término denominado entropía local es una desviación estándar local que se resta directamente en cada paso. No se justifica que esa operación represente una ley general de evolución; puede producir una disminución sistemática del campo.
- La métrica de entropía del histograma en `laboratorio_n.py` utiliza frecuencias de histograma con `density=True` como si fueran probabilidades. La entropía de Shannon requiere una distribución normalizada de probabilidades.
- Las inicializaciones aleatorias no exponen una semilla controlable de forma uniforme, lo que dificulta repetir resultados.
- Hay métodos duplicados en `motor_n_dig.py` y dependencias declaradas de forma incompleta o inconsistente entre prototipos.
- Las etiquetas y umbrales usados en patrones de ansiedad/depresión son supuestos del simulador; no acreditan diagnóstico, efecto terapéutico ni correspondencia clínica.

**Decisión:** conservarlo como legado y referencia. No usar sus ecuaciones ni sus métricas como fundamento del primer experimento de Génesis DIG sin definirlas, justificarlas y probarlas por separado.

### 2. Simulación de nodos y colapsos

Archivos revisados:
- `IA_DIG_Prototipo/motorN_life/motor/campo.py`
- `IA_DIG_Prototipo/motorN_life/motor/nodos.py`
- `IA_DIG_Prototipo/motorN_life/motor/reglas.py`
- `IA_DIG_Prototipo/motorN_life/main.py`

Aportaciones reutilizables como ideas de ingeniería:
- separar estado, reglas y visualización en módulos;
- registrar cambios y eventos;
- mantener un historial de colapsos;
- disponer de una configuración externa.

Limitaciones conceptuales y técnicas:
- Cada nodo ya tiene coordenadas, densidad `rho`, curvatura `kappa` y estados predefinidos (`vivo`, `degradado`, `colapsado`). Por tanto, no es neutral respecto a qué entidades existen ni qué significan.
- Las vecindades se deciden mediante una distancia euclídea y un radio fijo; se presupone un espacio geométrico.
- El movimiento y los cambios de estado contienen perturbaciones aleatorias y umbrales escogidos previamente.
- Las reglas implementadas no constituyen todavía una teoría general de interacción ni un conjunto de controles experimentales.
- La interfaz de ejecución periódica y el registro son útiles como patrones de programación, pero no validan el comportamiento modelado.

**Decisión:** no importar este modelo como motor de Nivel 0. Recuperar, cuando proceda, solo patrones de organización del código y registro de eventos, sin heredar sus entidades, geometría o reglas.

## Matriz de reutilización

| Componente | Decisión | Motivo |
|---|---|---|
| Registro de eventos y exportación JSON | Reutilizar la idea | Facilita trazabilidad y análisis posterior |
| Separación entre motor, reglas y visualizador | Reutilizar como patrón arquitectónico | Mejora el mantenimiento |
| Visualización de matrices/campos | Reutilizable más adelante | Útil si el experimento genera una representación adecuada |
| Rejilla 2D de 50 × 50 | No imponer en Nivel 0 | Introduce estructura espacial previa |
| `rho`, `kappa` y estados de nodo | No heredar como ontología | Son conceptos predefinidos del prototipo |
| Difusión y resta de “entropía” actuales | No aceptar sin pruebas | La interpretación matemática y sus efectos requieren validación |
| Clasificación ansiedad/depresión | Mantener fuera de Génesis DIG | Pertenece a otro problema y no valida el Nivel 0 |
| Scripts E001–E005 originales | No localizados todavía | Requiere seguir revisando historial y otras ubicaciones |

## Recomendación operativa

1. Mantener intactos los repositorios históricos: no sobrescribirlos ni mezclarlos con el proyecto nuevo.
2. Identificar el material antiguo recuperado como **original histórico**; marcar cualquier adaptación como **reconstrucción** o **código nuevo**.
3. No portar directamente el motor de campo ni el sistema de nodos a `genesis-dig`.
4. Para el primer experimento de Génesis DIG, construir un núcleo mínimo independiente que permita definir estados abstractos, reglas explícitas, semillas aleatorias, controles y registro reproducible, sin presuponer rejilla, coordenadas, partículas ni etiquetas físicas.
5. Antes de implementar ese experimento, continuar la búsqueda histórica de los Experimentos 001–005 mediante el historial de commits y archivos antiguos.

## Alcance y cautela

Esta auditoría es una revisión estática de archivos accesibles en las ramas examinadas. No se ejecutaron los programas ni se verificó experimentalmente su salida. Las conclusiones sobre reutilización se refieren a adecuación conceptual y calidad del código, no a que el programa sea incapaz de ejecutarse.

**Principio rector:** conservar el legado, aprender de él y no permitir que sus supuestos decidan de antemano lo que Génesis DIG debe descubrir.
