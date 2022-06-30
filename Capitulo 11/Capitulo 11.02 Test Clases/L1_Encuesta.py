# Escribiremos una clase para hacer el test.
# Consideremos una clase que ayude a administrar encuestas anonimas.

class EncuestaAnonima():  # Creamos la clase, la cual incluye una pregunta que uno mismo proporciona
    """Recolecta respuestas anonimas de una pregunta de encuesta"""

    def __init__(self, pregunta):
        """Almacena una pregunta y prepara para almacenar respuestas"""
        self.pregunta = pregunta
        self.respuestas = []  # Se crea una lista vacia que almacenará respuestas

    def mostrar_pregunta(self):  # Se crea metodo para mostrar pregunta
        """Muestra la pregunta de la encuesta"""
        print(self.pregunta)

    def almacenar_respuesta(self, nueva_respuesta):  # Se crea metodo para guardar las respuestas
        """Almacena una simple respuesta a la encuesta"""
        self.respuestas.append(nueva_respuesta)

    def mostrar_resultados(self):  # Se crea metodo para mostrar los resultados
        """Muestra todas las respuestas que han sido dadas"""
        print("***** Resultados de la encuesta *****")
        for respuesta in self.respuestas:
            print(f"- {respuesta.title()}")

# Para crear una instancia de esta clase, lo que se tiene que proporcionar es una pregunta.
# Una vez que se tiene la instancia que representa una encuesta en particular, se muestra la pregunta
# con el metodo mostrar_pregunta(), se almacena una respuesta usando almacenar_respuesta() y muestra los resultados
# con mostrar_resultados().
# Para mostrar que la clase EncuestaAnonima funciona, debemos escribir un programa que use la clase (siguiente modulo).

