# 9-14. Lottery:
#           Make a list or tuple containing a series of 10 numbers and five letters.
#           Randomly select four numbers or letters from the list and print a message saying that any ticket
#           matching these four numbers or letters wins a prize.

from random import choice

lista = [1, 5, 3, 2, 7, 8, 9, 4, 6, 0, "a", "e", "i", "o", "u"]

print("Las siguientes boletas ha sido ganadores de un premio: ")
for i in range(0, 4):
    print(choice(lista))
