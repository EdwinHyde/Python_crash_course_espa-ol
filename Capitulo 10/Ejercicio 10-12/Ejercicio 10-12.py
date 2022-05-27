# -*- coding: utf-8 -*-
# 10-12. Favorite Number Remembered:
# Combine the two programs from Exercise 10-11 into one file.
# If the number is already stored, report the favorite number to the user.
# If not, prompt for the user’s favorite number and store it in a file.
# Run the program twice to see that it works.

import json

nombre_archivo = "numero.json"
try:
    with open(nombre_archivo) as archivo:
        numero = json.load(archivo)
except FileNotFoundError:
    numero = input("Ingrese su numero favorito: ")
    with open(nombre_archivo, "w") as archivo:
        json.dump(numero, archivo)
        print(f"Recordaré tu numero favorito, el {numero}")

else:
    print(f"Sabemos que tu numero favorito es {numero}")