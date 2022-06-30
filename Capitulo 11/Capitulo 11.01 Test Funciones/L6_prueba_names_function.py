import unittest
from L4_names_function import obtener_nombre_formateado
from L5_names_function_corregida import obtener_nombre_formateado

class NombresTestCase(unittest.TestCase):
    """Pruebas para la funcion testing.py"""

    # ESta version deberia trabajar para personas con segundo nombre, pero cuando hacemos el test, vemos que la funcion
    # falla para personas con solo un primer nombre y apellido.

    # PRUEBA CON MODULO  names_function.py
    # def test_nombre_apellido(self):
    #     """Funcionan nombres como 'Joaquin Sabina'?"""
    #     nombre_formateado = obtener_nombre_formateado("Joaquin", "Sabina")
    #     self.assertEqual(nombre_formateado, 'Joaquin Sabina')

    # PRUEBA CON MODULO names_function_corregida.py
    def test_nombre_apellido(self):
        """Funcionan nombres como 'Joaquin Sabina'?"""
        nombre_formateado = obtener_nombre_formateado("Joaquin", "Sabina")
        self.assertEqual(nombre_formateado, 'Joaquin Sabina')


if __name__ == "__main__":
    unittest.main

# Esta prueba generará un error, pues falta un argumento.
# Cuando una prueba falla, no se cambia el test, se debe corregir el codigo que causa la falla. Examinar los cambios
# hechos a la funcion y descubrir como esos cambios afectaron el comportamiento deseado.