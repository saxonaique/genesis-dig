"""Experimento 002 — exploración de persistencia sin acción explícita.

Se enumeran todas las tablas deterministas de interacción entre tres estados.
En cada paso se seleccionan dos individuos; el de menor índice adopta el estado
asignado por la tabla al par de estados observado. No existe una acción llamada
'persistir'. La persistencia temporal se mide como 30 pasos consecutivos sin
cambio en la composición global (multiconjunto de estados).

Este modelo es abstracto y exploratorio: no representa una ley física ni valida
la teoría DIG. La estabilidad temporal no equivale a un estado absorbente.

Autoría: José María Pérez Rodríguez (JMPR).
"""

from collections import Counter
from itertools import combinations_with_replacement, product
import json
import random

ESTADOS = ("A", "B", "C")
PARES = tuple(combinations_with_replacement(ESTADOS, 2))
INDICE_PAR = {par: i for i, par in enumerate(PARES)}
ESTADO_INICIAL = ("A", "B", "C", "A", "B", "C")
PASOS = 200
VENTANA_ESTABILIDAD = 30
SEMILLAS = range(5)


def composicion(estados):
    """Representación canónica de la composición, ignorando el orden."""
    return tuple(sorted(Counter(estados).items()))


def es_composicion_absorbente(tabla, estados):
    """Comprueba si ninguna pareja de individuos puede cambiar la composición.

    En este modelo, el individuo de menor índice adopta la salida de la tabla.
    La composición final es absorbente si esa salida coincide con su estado
    actual para todas las parejas posibles de individuos.
    """
    for i in range(len(estados)):
        for j in range(i + 1, len(estados)):
            par = tuple(sorted((estados[i], estados[j])))
            if tabla[INDICE_PAR[par]] != estados[i]:
                return False
    return True


def ejecutar(tabla, semilla, pasos=PASOS, ventana=VENTANA_ESTABILIDAD):
    """Ejecuta una tabla y devuelve medidas observables y estado final."""
    rng = random.Random(semilla)
    estados = list(ESTADO_INICIAL)
    composiciones = [composicion(estados)]
    cambios = 0

    for _ in range(pasos):
        i, j = rng.sample(range(len(estados)), 2)
        par = tuple(sorted((estados[i], estados[j])))
        salida = tabla[INDICE_PAR[par]]
        objetivo = min(i, j)
        anterior = estados[objetivo]
        estados[objetivo] = salida
        if estados[objetivo] != anterior:
            cambios += 1
        composiciones.append(composicion(estados))

    racha = 1
    racha_maxima = 1
    for anterior, actual in zip(composiciones, composiciones[1:]):
        if actual == anterior:
            racha += 1
            racha_maxima = max(racha_maxima, racha)
        else:
            racha = 1

    # 30 transiciones sin cambio equivalen a 31 composiciones observadas iguales.
    racha_maxima_transiciones = racha_maxima - 1
    return {
        "semilla": semilla,
        "cambios_de_estado": cambios,
        "racha_maxima_composicion_sin_cambio": racha_maxima_transiciones,
        "persistencia_temporal": racha_maxima_transiciones >= ventana,
        "composicion_final": composicion(estados),
        "composicion_absorbente_final": es_composicion_absorbente(tabla, estados),
    }


def explorar():
    """Enumera las 3^6 tablas y cinco semillas por tabla."""
    ejecuciones = []
    frecuencias_finales = Counter()
    total_tablas = 0

    for tabla in product(ESTADOS, repeat=len(PARES)):
        total_tablas += 1
        for semilla in SEMILLAS:
            resultado = ejecutar(tabla, semilla)
            ejecuciones.append(resultado)
            frecuencias_finales[resultado["composicion_final"]] += 1

    persistentes = sum(e["persistencia_temporal"] for e in ejecuciones)
    absorbentes = sum(e["composicion_absorbente_final"] for e in ejecuciones)
    cambios_totales = sum(e["cambios_de_estado"] for e in ejecuciones)
    return {
        "experimento": "E002",
        "autor": "José María Pérez Rodríguez (JMPR)",
        "estados": list(ESTADOS),
        "pares_posibles": [list(p) for p in PARES],
        "estado_inicial": list(ESTADO_INICIAL),
        "pasos_por_ejecucion": PASOS,
        "umbral_persistencia_transiciones": VENTANA_ESTABILIDAD,
        "tablas_examinadas": total_tablas,
        "ejecuciones": len(ejecuciones),
        "ejecuciones_con_persistencia_temporal": persistentes,
        "fraccion_persistencia_temporal": persistentes / len(ejecuciones),
        "ejecuciones_con_composicion_final_absorbente": absorbentes,
        "promedio_cambios_estado": cambios_totales / len(ejecuciones),
        "composiciones_finales_distintas": len(frecuencias_finales),
        "composiciones_finales_mas_frecuentes": [
            {"composicion": [list(x) for x in comp], "frecuencia": n}
            for comp, n in frecuencias_finales.most_common(10)
        ],
        "limitaciones": [
            "La persistencia temporal depende del umbral operacional elegido.",
            "Una composición sin cambios durante una ventana finita no demuestra estabilidad indefinida.",
            "La selección de pares, la actualización del individuo de menor índice y las tablas son decisiones de modelado.",
            "La absorbencia se comprueba para todas las parejas de individuos posibles en la composición final, bajo las reglas de este modelo.",
            "Los resultados no representan una ley física ni validan DIG."
        ],
    }


if __name__ == "__main__":
    print(json.dumps(explorar(), ensure_ascii=False, indent=2))
