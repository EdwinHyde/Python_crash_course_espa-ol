# -*- coding: utf-8 -*-
# 10-11. Favorite Number:
# Write a program that prompts for the user’s favorite number.
# Use json.dump() to store this number in a file.
# Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”

import json

nombre_archivo = "numero.json"
with open(nombre_archivo) as archivo:
    numero = json.load(archivo)
    print(f"Se que tu numero favorito es: {numero}")