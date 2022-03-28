#  Consideremos una funcion que haga una pizza, la cual necesita recibir una cantidad de ingredientes
#  pero no se conoce cuantos ingredientes quiere la persona. La siguiente funcion tiene un parametro
#  pero este parametro recibe tantos argumentos que se proporcionen cuando se hace el llamado a la funcion.

def hacer_pizza(*ingredientes): 
    #  El asterisco en el parametro ingredientes le dice a python que cree una tupla vacia
    #  y empaqueta cualqueir valor que reciba esta tupla.
    """Resumir la pizza que estamos a punto de hacer"""
    print("\nHaciendo una pizza con los siguientes ingredientes: ")
    for ingrediente in ingredientes:    #  Se recorre la tupla enviada desde los argumentos
        print(f" ° {ingrediente}")
        
#  La funcion responde correctamente si recibe un valor o tres valores.
#  Esta sintaxis trabaja sin importar cuantos argumentos recibe la funcion.
hacer_pizza("pepperoni")
hacer_pizza("hongos", "piña", "queso extra")

