import unittest  # Importamos el modulo unittest y la clase EncuestaAnonima a la cual queremos hacer test
from L1_Encuesta import EncuestaAnonima

class TestEncuestaAnonima(unittest.TestCase):  # Creamos la clase, la cual hereda de unittest.TestCase
    """Prueba la clase EncuestaAnonima"""
    def test_almacenar_simple_respuesta(self):  # este metodo verificara que cuando almacenemos una respuesta a la
        # pregunta de la encuesta, la respuesta termine en la lista respuestas de la encuesta.
        pregunta = "¿Cuál lenguaje aprendiste a hablar primero?"
        mi_encuesta = EncuestaAnonima(pregunta)  # creamos una instancia con la pregunta creada
        mi_encuesta.almacenar_respuesta("Español")  # almacenamos una simple respuesta haciendo uso del metodo
        # almacenar_respuestas()
        self.assertIn("Español", mi_encuesta.respuestas)  # verificamos que la respuesta se almacenó correctamente
        # en la lista  respuestas mediante el metodo assert.

# Esto es bueno, pero una encuesta es util solo cuando se genera mas de una respuesta. Verifiquemos si se pueden
# almacenar 3 respuestas correctamente. Para esto, agreguemos otro metodo a la clase de pruebas.

    def test_tres_respuestas(self):
        """Hace unt est para comprobar que se almacenan correctamente tres respuestas individuales"""
        pregunta = "¿Cuál lenguaje aprendiste a hablar primero?"
        mi_encuesta = EncuestaAnonima(pregunta)
        respuestas = ["Español", "Inglés", "mandarin"]  # creamos una lista que contenga 3 respuestas diferentes.
        for respuesta in respuestas:  # recorremos la lista y se almacenan las respuestas.
            mi_encuesta.almacenar_respuesta(respuesta)

        for respuesta in respuestas:  # Una vez que se han almacenado las respuestas, escribimos otro bucle y afirmamos
            # que cada respuesta esta ahora dentro de mi_encuesta.respuestas
            self.assertIn(respuesta, mi_encuesta.respuestas)


if __name__ == "__main__":
    unittest.main

# Esto trabaja perfectamente, sin embargo, estos test son un poco repetitivos, asi que usaremos otra caracteristica
# de unittest para hacerlos mas eficientes.
