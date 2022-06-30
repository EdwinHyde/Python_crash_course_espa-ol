from L1_Encuesta import EncuestaAnonima

# Definir una pregunta  y se crea una encuesta.
pregunta = "¿Cuál lenguaje aprendiste a hablar primero?"
mi_encuesta = EncuestaAnonima(pregunta)

# Mostrar la pregunta y almacenar las respuestas a la pregunta
mi_encuesta.mostrar_pregunta()
print("Escriba 's' en cualquier momento para salir.\n")
while True:
    respuesta = input("Idioma: ")
    if respuesta.lower() == "s":
        break
    mi_encuesta.almacenar_respuesta(respuesta)

# Mostrar los resultados de la encuesta
print("\nGracias a todos los que participaron en esta maravillosa encuesta.")
mi_encuesta.mostrar_resultados()