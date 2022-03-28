# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
#       a person’s age. If a person is under the age of 3, the ticket is free; if they are
#       between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
#       $15. Write a loop in which you ask users their age, and then tell them the cost
#       of their movie ticket.

aviso = ("\nBienvenido a su cine, indiquenos por favor su edad, "
         "para decirle el precio de su tiquete: ")
aviso += ("\nCuando haya terminado, escriba salir para finalizar el programa. \n")

while True:
    edad = input(aviso)
    if edad == "salir":
        break
    else:
        edad = int(edad)
        if edad < 3:
            precio = 0
        elif edad <= 12:
            precio = 10000
        else:
            precio = 15000
        print(f"El precio de tu entrada es {precio}")