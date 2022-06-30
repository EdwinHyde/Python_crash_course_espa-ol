# Ahora vamos a escribir una prueba para personas que tienen un segundo nombre. Lo hacemos agregando otro metodo
# a la clase NombresTestCase

import unittest
from L4_names_function import obtener_nombre_formateado
from L5_names_function_corregida import obtener_nombre_formateado

class NombresTestCase(unittest.TestCase):
    """Pruebas para la funcion names_function_corregida.py"""

    def test_nombre_apellido(self):  # El nombre del metodo debe iniciar con la palabra test
        """Funcionan nombres como 'Joaquin Sabina'?"""
        nombre_formateado = obtener_nombre_formateado("Joaquin", "Sabina")
        self.assertEqual(nombre_formateado, 'Joaquin Sabina')

    def test_primer_segundo_nombre(self):
        """Funcionan nombres como 'Ludwig Van Bethoveen'?"""
        nombre_formateado = obtener_nombre_formateado("ludwig", "bethoveen", "van")
        self.assertEqual(nombre_formateado, "Ludwig Van Bethoveen")

if __name__ == "__main__":
    unittest.main