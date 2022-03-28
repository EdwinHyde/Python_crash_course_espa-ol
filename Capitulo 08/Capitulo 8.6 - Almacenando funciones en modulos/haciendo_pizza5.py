# IMPORTANDO TODAS LAS FUNCIONES DE UN MODULO
# Para indicar a python que se desea importar todas las funciones de un modulo se usa un *

from pizza import *  # desde el archivo pizza.py se importan todas las funciones que tenga

hacer_pizza("grande", "pepperoni", "maní")  # Como se importan todas las funciones del modulo, no es necesario usar el punto para llamar la funcion
hacer_pizza("mediana", "queso", "hongos", "pepino verde")
