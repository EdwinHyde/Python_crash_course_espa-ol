# 9-13. Dice:
#           Make a class Die with one attribute called sides, which has a default value of 6.
#           Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
#           Make a 6-sided die and roll it 10 times.
#                   Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Dado:
    """Crea una clase simple de un dado"""
    def __init__(self, lados=6):
        self.lados = lados

    def tirar_dados(self):
        print(f"El número del dado es: {randint(1,self.lados)}")


print("\nPrimer Dado")
mi_dado = Dado()
for i in range(0,10):
    mi_dado.tirar_dados()

print("\nSegundo Dado")
otro_dado = Dado(10)
for i in range(0,10):
    otro_dado.tirar_dados()

print("\nTercer Dado")
mas_dado = Dado(20)
for i in range(0,10):
    mas_dado.tirar_dados()