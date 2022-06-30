# Write a second test called test_city_country_population() that verifies you can call your
# function with the values 'santiago', 'chile', and 'population=5000000'.
# Run test_cities.py again, and make sure this new test passes.

import unittest
from poblacion import ciudad_pais

class TestEjercicio(unittest.TestCase):
    def test_ciudad_pais(self):
        pais_completo = ciudad_pais("bogotá", "colombia")
        self.assertEqual(pais_completo, "Bogotá Colombia")

    def test_ciudad_pais_poblacion(self):
        pais_completo = ciudad_pais("bogotá", "colombia", "5000000")
        self.assertEqual(pais_completo, "Bogotá Colombia Población: 5000000")

if __name__ == "__main__":
    unittest.main