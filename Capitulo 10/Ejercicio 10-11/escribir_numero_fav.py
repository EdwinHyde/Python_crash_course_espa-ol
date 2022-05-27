# -*- coding: utf-8 -*-
# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number.
# Use json.dump() to store this number in a file.
# Write a separate program that reads in this value and prints the message,
# “I know your favorite number! It’s _____.”

import json

nombre_archivo = "numero.json"
numero = input("Cual es tu numero favorito? ")

with open(nombre_archivo, 'w') as archivo:
    json.dump(numero, archivo)