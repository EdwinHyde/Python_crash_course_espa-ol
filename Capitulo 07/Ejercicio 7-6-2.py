# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
#           that do each of the following at least once:
#               •	 Use a conditional test in the while statement to stop the loop.
#               •	 Use an active variable to control how long the loop runs.
#               •	 Use a break statement to exit the loop when the user enters a 'quit' value.

aviso = ("\nBienvenido a su cine, indiquenos por favor su edad, "
         "para decirle el precio de su tiquete: ")
aviso += ("\nCuando haya terminado, escriba salir para finalizar el programa. \n")

active = True

while active:
    edad = input(aviso)
    if edad == "salir":
        active = False
    else:
        edad = int(edad)
        if edad < 3:
            precio = 0
        elif edad <= 12:
            precio = 10000
        else:
            precio = 15000
        print(f"El precio de tu entrada es {precio}")