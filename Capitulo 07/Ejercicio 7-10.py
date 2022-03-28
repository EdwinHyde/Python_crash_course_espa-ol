# 7-10. Dream Vacation:
# Write a program that polls users about their dream vacation.
#       Write a prompt similar to If you could visit one place in the world, where
#       would you go? Include a block of code that prints the results of the poll.

respuestas = {}
flag = True


while flag:
    nombre = input("\n Cual es tu nombre? ")
    encuesta = input(f"Hola {nombre.title()}, si pudieras visitar un lugar en el mundo, a donde irias? ")

    respuestas[nombre] = encuesta
    repetir_encuesta = input("\nAlguien mas responderá la encuesta? (Si / No)")

    if repetir_encuesta.lower() == "no":
        flag = False

print("\n...::: RESULTADOS DE LA ENCUESTA :::...")
for nombre, encuesta in respuestas.items():
    print(f"A {nombre.title()} le gustaría conocer {encuesta.title()}")


