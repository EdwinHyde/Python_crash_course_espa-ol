# Write a test case for Employee.
# Write two test methods, test_give_default _raise() and test_give_custom_raise().
# Use the setUp() method so you don’t have to create a new employee instance in each test method.
# Run your test case, and make sure both tests pass.

import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):
    """Prueba la clase Empleado"""
    def setUp(self):
        """Crea un empleado con sus datos para usar en todos los metodos de prueba"""
        nombres = "Edwin"
        apellidos = "Chica"
        self.salario = 50000
        self.empleado = Empleado(nombres, apellidos, self.salario)

    def test_aumento_standard(self):
        """Comprueba que se hace el aumento predeterminado"""
        self.empleado.dar_aumento()
        self.assertEqual(self.empleado.salario_anual, self.salario + 5000)

    def test_aumento_personalizado(self):
        """Comprueba que se hace un aumento de forma personalizada"""
        aumento_personalizado = 4000
        self.empleado.dar_aumento(aumento_personalizado)
        self.assertEqual(self.empleado.salario_anual, self.salario + aumento_personalizado)

if __name__ == "__main__":
    unittest.main
