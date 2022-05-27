# 0-1. Learning Python:
# Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far.
# Start each line with the phrase In Python you can. . . .
# Save the file as learning_python.txt in the same directory as your exercises from this chapter.
# Write a program that reads the file and prints what you wrote three times.
# Print the contents once by reading in the entire file, once by looping over the file object,
# and once by storing the lines in a list and then working with them outside the with block.

# LECTURA DEL ARCHIVO ENTERO.
print('Parte 1'.center(30, ':'))
with open('aprendizaje.txt') as file_object:
    contenido = file_object.read()

print(contenido)

# LECTURA DEL ARCHIVO RECORRIENDOLO CON UN BUCLE.
print('Parte 2'.center(30, ':'))
with open('aprendizaje.txt') as file_object:
    lineas = file_object.readlines()

for linea in lineas:
    print(linea.strip())

# LECTURA DEL ARCHIVO ALMACENANDO LAS LINEAS EN UNA LISTA Y TRABAJANDO FUERA DEL BLOQUE WITH.
print('\nParte 3'.center(30, ':'))
with open('aprendizaje.txt') as file_object:
    lineas = file_object.readlines()

cadena_texto = ''
for linea in lineas:
    cadena_texto += linea.strip()

print(cadena_texto)