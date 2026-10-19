"""Experimento 001 — comprobación técnica del núcleo de Génesis DIG.

Este experimento comprueba que el motor ejecuta reglas explícitas y es reproducible.
No pretende demostrar emergencia, gravedad ni ninguna ley física.

Ejecutar desde la raíz del repositorio:
    python experiments/nivel_0/experimento_001.py

Autoría: José María Pérez Rodríguez (JMPR).
"""

import json
from pathlib import Path
import sys

# Permite ejecutar el archivo directamente desde la raíz del repositorio.
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from genesis_dig.motor import MotorGenesisDIG, Regla


def crear_motor(semilla: int = 17) -> MotorGenesisDIG:
    # A, B y C son etiquetas abstractas, no partículas ni propiedades físicas.
    reglas = {
        ("A", "B"): Regla("persistir"),
        ("A", "C"): Regla("transformar", nuevo_estado="A*"),
        ("B", "C"): Regla("anular"),
        ("A*", "B"): Regla("persistir"),
        ("A*", "C"): Regla("transformar", nuevo_estado="A**"),
        ("A*", "A"): Regla("persistir"),
        ("A**", "B"): Regla("persistir"),
        ("A**", "C"): Regla("persistir"),
    }
    return MotorGenesisDIG(["A", "B", "C"], reglas, semilla=semilla)


def main() -> None:
    motor = crear_motor()
    eventos = motor.ejecutar(pasos=12)
    salida = {
        "experimento": "Génesis DIG — Nivel 0 — E001",
        "objetivo": "Comprobación técnica de reglas y reproducibilidad",
        "nota": "Las reglas son ilustrativas y se han definido de antemano.",
        "resumen": motor.resumen(),
        "historial": eventos,
    }
    print(json.dumps(salida, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
