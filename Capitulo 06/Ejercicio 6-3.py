# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
#       However, to avoid confusion, let’s call it a glossary.
#           •	 Think of five programming words you’ve learned about in the previous
#               chapters. Use these words as the keys in your glossary, and store their
#               meanings as values.
#           •	 Print each word and its meaning as neatly formatted output. You might
#               print the word followed by a colon and then its meaning, or print the word
#               on one line and then print its meaning indented on a second line. Use the
#               newline character (\n) to insert a blank line between each word-meaning
#               pair in your output.

glosario = {}
glosario["variable"] = "Espacio reservado en memoria para guardar un dato especifico"
glosario["Lista"] = "Arreglo de elementos ordenados y que contienen mucha informacion"
glosario["Bucle"] = "Es una secuencia de instrucciones de código que se ejecuta repetidas veces, " \
                    "hasta que la condición asignada a dicho bucle deja de cumplirse"
glosario["Tupla"] = "Es una lista ordenada finita de elementos.\n Una n-tupla es una secuencia de n elementos, " \
                    "donde n es un número entero no negativo"
glosario["Diccionario"] = "Es una estructura de datos y un tipo de dato en Python con características especiales\n " \
                          "que nos permite almacenar cualquier tipo de valor como enteros, cadenas, " \
                          "listas e incluso otras funciones."
print(f'Variable: \n {glosario["variable"]}\n')
print(f'Lista: \n {glosario["Lista"]}\n')
print(f'Bucle: \n {glosario["Bucle"]}\n')
print(f'Tupla: \n {glosario["Tupla"]}\n')
print(f'Diccionario: \n {glosario["Diccionario"]}\n')