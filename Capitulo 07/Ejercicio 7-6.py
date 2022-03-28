# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
#           that do each of the following at least once:
#               •	 Use a conditional test in the while statement to stop the loop.
#               •	 Use an active variable to control how long the loop runs.
#               •	 Use a break statement to exit the loop when the user enters a 'quit' value.

aviso = ("\nIngrese por favor la lista de ingredientes para su pizza: ")
aviso += ("\nCuando haya terminado por favor digite 'salir' para salir del programa.\n")

ingredientes = ""
while True:
    ingredientes = input(aviso)
    if ingredientes == "salir":
        break
    else:
        print(f"\nAgregando {ingredientes} a su pizza")
