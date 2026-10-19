import unittest
from itertools import product

from experiments.nivel_0.experimento_002 import (
    ESTADOS, PARES, ejecutar, explorar, es_composicion_absorbente
)


class Experimento002Tests(unittest.TestCase):
    def test_seis_pares_y_729_tablas(self):
        self.assertEqual(len(PARES), 6)
        self.assertEqual(3 ** len(PARES), 729)

    def test_reproducible_para_misma_semilla(self):
        tabla = tuple("ABCABC")
        self.assertEqual(ejecutar(tabla, 17), ejecutar(tabla, 17))

    def test_composicion_toda_A_absorbente_si_AA_devuelve_A(self):
        tabla = tuple("A" for _ in PARES)
        self.assertTrue(es_composicion_absorbente(tabla, ("A", "A", "A")))

    def test_composicion_toda_A_no_absorbente_si_AA_devuelve_B(self):
        tabla = ["A"] * len(PARES)
        tabla[0] = "B"
        self.assertFalse(es_composicion_absorbente(tuple(tabla), ("A", "A", "A")))

    def test_ejecucion_registra_medidas(self):
        tabla = tuple("A" for _ in PARES)
        resultado = ejecutar(tabla, 0, pasos=10, ventana=3)
        self.assertIn("persistencia_temporal", resultado)
        self.assertIn("composicion_absorbente_final", resultado)
        self.assertIn("cambios_de_estado", resultado)


if __name__ == "__main__":
    unittest.main()
