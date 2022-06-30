# El metodo setUp() permite crear los objetos una sola vez y luego usarlo en cada metodo de test creado.
# Cuando se incluye un metodo setUp() en una clase TestCase, python ejecuta este metodo antes de ejecutar cada
# metodo que inicie con la palabra test_. Cualquier objeto creado en el metodo setUp(), estará luego disponible
# en cada metodo test que se escriba.

import unittest
from L1_Encuesta import EncuestaAnonima

class TestEncuestaAnonima(unittest.TestCase):
    """Tests para la clase EncuestaAnonima"""

    def setUp(self):
        """
        Crea una encuesta y un conjunto de respuestas para usar en todos los metodos test
        """
        pregunta = "¿Cuál lenguaje aprendiste a hablar primero?"
        self.mi_encuesta = EncuestaAnonima(pregunta)  # atributos creados con el prefijo self, lo que indica que
        # podrán ser usadas en cualquier lugar de la clase.
        self.respuestas = ["Español", "Inglés", "mandarin"]

    def test_almacenar_simple_respuesta(self):
        """Comprueba que una respuesta simple es almacenada correctamente"""
        self.mi_encuesta.almacenar_respuesta(self.respuestas[0])
        # Este metodo verifica que la primer respuesta en self.respuestas[0] se almacena correctamente
        self.assertIn(self.respuestas[0], self.mi_encuesta.respuestas)

    def test_tres_respuestas(self):
        """Comprueba que se pueden almacenar tres respuestas individuales correctamente"""
        for respuesta in self.respuestas:
            self.mi_encuesta.almacenar_respuesta(respuesta)
        for respuesta in self.respuestas:
            self.assertIn(respuesta, self.mi_encuesta.respuestas)
    
