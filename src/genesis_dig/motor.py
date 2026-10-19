"""Núcleo mínimo de Génesis DIG.

Versión inicial de ingeniería: estados abstractos e interacciones explícitas.
No representa todavía una teoría física ni presupone espacio, partículas o gravedad.
Autoría: José María Pérez Rodríguez (JMPR).
"""

from dataclasses import dataclass
import random
from typing import Dict, Iterable, List, Tuple


@dataclass
class Posibilidad:
    """Estado abstracto que puede participar en una interacción."""
    id: int
    estado: str
    activa: bool = True


@dataclass(frozen=True)
class Regla:
    """Regla explícita para un par de estados, sin interpretación física."""
    accion: str  # "persistir", "transformar" o "anular"
    nuevo_estado: str = ""


class MotorGenesisDIG:
    """Motor mínimo reproducible para explorar interacciones entre posibilidades."""

    ACCIONES = {"persistir", "transformar", "anular"}

    def __init__(
        self,
        estados_iniciales: Iterable[str],
        reglas: Dict[Tuple[str, str], Regla],
        semilla: int = 0,
    ):
        self.rng = random.Random(semilla)
        self.semilla = semilla
        self.posibilidades = [
            Posibilidad(id=i, estado=estado)
            for i, estado in enumerate(estados_iniciales)
        ]
        self.reglas = {
            tuple(sorted(par)): regla for par, regla in reglas.items()
        }
        self.ciclo = 0
        self.historial: List[dict] = []

        for par, regla in self.reglas.items():
            if len(par) != 2:
                raise ValueError("Cada regla debe definir un par de estados.")
            if regla.accion not in self.ACCIONES:
                raise ValueError(f"Acción desconocida: {regla.accion}")

    def paso(self) -> dict:
        """Ejecuta una interacción entre dos posibilidades activas."""
        activas = [p for p in self.posibilidades if p.activa]

        if len(activas) < 2:
            evento = {
                "ciclo": self.ciclo,
                "resultado": "sin_par_activo",
                "ids": [],
            }
            self.historial.append(evento)
            self.ciclo += 1
            return evento

        a, b = self.rng.sample(activas, 2)
        clave = tuple(sorted((a.estado, b.estado)))
        regla = self.reglas.get(clave)

        if regla is None:
            resultado = "sin_regla"
        elif regla.accion == "persistir":
            resultado = "persistencia"
        elif regla.accion == "transformar":
            objetivo = a if a.id < b.id else b
            estado_anterior = objetivo.estado
            objetivo.estado = regla.nuevo_estado or (objetivo.estado + "'")
            resultado = "transformacion"
        else:  # anular
            a.activa = False
            b.activa = False
            resultado = "anulacion"

        evento = {
            "ciclo": self.ciclo,
            "ids": [a.id, b.id],
            "estados_antes": [a.estado, b.estado] if resultado != "transformacion" else None,
            "resultado": resultado,
            "regla": regla.accion if regla else None,
        }
        if resultado == "transformacion":
            evento["estado_anterior"] = estado_anterior
            evento["estado_nuevo"] = objetivo.estado
            evento["estados_antes"] = None

        self.historial.append(evento)
        self.ciclo += 1
        return evento

    def ejecutar(self, pasos: int) -> List[dict]:
        """Ejecuta un número fijo de pasos y devuelve los eventos."""
        if pasos < 0:
            raise ValueError("El número de pasos no puede ser negativo.")
        return [self.paso() for _ in range(pasos)]

    def resumen(self) -> dict:
        """Devuelve un resumen simple del estado actual."""
        activas = [p for p in self.posibilidades if p.activa]
        return {
            "semilla": self.semilla,
            "ciclo": self.ciclo,
            "total_posibilidades": len(self.posibilidades),
            "activas": len(activas),
            "anuladas": len(self.posibilidades) - len(activas),
            "estados_activos": [
                {"id": p.id, "estado": p.estado} for p in activas
            ],
            "eventos": len(self.historial),
        }
