# 9-15. Lottery Analysis:
#           You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
#           Make a list or tuple called my_ticket.
#           Write a loop that keeps pulling numbers until your ticket wins.
#           Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice, randint


boletas = [10, 20, 30, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
ganador = choice(boletas)


for i in range(0, len(boletas)):
    print(choice(boletas))
    if boletas[i] == ganador:
      print(f'El boleto ganador es el numero {boletas[i]} y tomó {i+1} intentos.')
      break

