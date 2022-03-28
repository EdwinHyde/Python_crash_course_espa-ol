# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#           up the code from Exercise 6-3 (page 99) by replacing your series of print()
#           calls with a loop that runs through the dictionary’s keys and values. When
#           you’re sure that your loop works, add five more Python terms to your glossary.
#           When you run your program again, these new words and meanings should
#           automatically be included in the output.

glosario = {
    "variable": "Espacio reservado en memoria para guardar un dato especifico",
    "Lista": "Arreglo de elementos ordenados y que contienen mucha informacion",
    "Bucle": "Es una secuencia de instrucciones de código que se ejecuta repetidas veces, "
             "hasta que la condición asignada a dicho bucle deja de cumplirse",
    "Tupla": "Es una lista ordenada finita de elementos.\n Una n-tupla es una secuencia de n elementos, " 
             "donde n es un número entero no negativo",
    "Diccionario": "Es una estructura de datos y un tipo de dato en Python con características especiales\n "
                   "que nos permite almacenar cualquier tipo de valor como enteros, cadenas, "
                   "listas e incluso otras funciones.",
    }

glosario["constante"] = "Espacio reservado en memoria para guardar un dato, pero no se puede modificar"
glosario["set"] = "Arreglo de elementos que no se repiten y que siempre cambia el orden"
glosario["IDLE"] = "Programa que sirve para crear programas en python"

for palabra, significado in glosario.items():
    print(f'{palabra.title()}:\n\t {significado}\n')
