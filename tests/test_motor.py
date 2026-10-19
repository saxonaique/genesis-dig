import unittest

from genesis_dig.motor import MotorGenesisDIG, Regla


def crear_motor(semilla=23):
    reglas = {
        ("A", "B"): Regla("persistir"),
        ("A", "C"): Regla("transformar", "A*"),
        ("B", "C"): Regla("anular"),
        ("A*", "B"): Regla("persistir"),
    }
    return MotorGenesisDIG(["A", "B", "C"], reglas, semilla=semilla)


class TestMotorGenesisDIG(unittest.TestCase):
    def test_estado_inicial(self):
        motor = crear_motor()
        self.assertEqual(len(motor.posibilidades), 3)
        self.assertEqual(motor.resumen()["activas"], 3)

    def test_misma_semilla_reproduce_historial(self):
        a = crear_motor(semilla=42)
        b = crear_motor(semilla=42)
        self.assertEqual(a.ejecutar(20), b.ejecutar(20))
        self.assertEqual(a.resumen(), b.resumen())

    def test_regla_de_anulacion(self):
        motor = MotorGenesisDIG(
            ["A", "B"],
            {("A", "B"): Regla("anular")},
            semilla=1,
        )
        evento = motor.paso()
        self.assertEqual(evento["resultado"], "anulacion")
        self.assertEqual(motor.resumen()["activas"], 0)

    def test_rechaza_accion_desconocida(self):
        with self.assertRaises(ValueError):
            MotorGenesisDIG(["A", "B"], {("A", "B"): Regla("magia")})

    def test_rechaza_pasos_negativos(self):
        with self.assertRaises(ValueError):
            crear_motor().ejecutar(-1)


if __name__ == "__main__":
    unittest.main()
