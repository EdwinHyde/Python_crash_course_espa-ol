# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
#           pizza toppings until they enter a 'quit' value. As they enter each topping,
#           print a message saying you’ll add that topping to their pizza.

aviso = ("\nIngrese por favor la lista de ingredientes para su pizza: ")
aviso += ("\nCuando haya terminado por favor digite 'salir' para salir del programa.\n")

ingredientes = ""
while ingredientes.lower() != 'salir':
    ingredientes = input(aviso)

    if ingredientes.lower() != "salir":
        print(f"\nAgregaremos {ingredientes.title()} a su pizza")
