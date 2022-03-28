#  Mezclando argumentos posicionales y arbitrarios.
#  Python reconoce primero los argumentos posiciones y de keyword, por lo que 
#  los parametros arbitrarios se ponen al final.

def crear_pizza(tamaño, *ingredientes): #  La funcion necesita conocer el tamaño de la pizza, este debe ir antes que *ingredientes
    """Resumir la pizza que se está haciendo."""
    print(f"\nHaciendo una pizza de tamaño {tamaño.title()} con los siguientes ingredientes: ")
    for ingrediente in ingredientes:
        print(f"° {ingrediente.title()}")
        
# En la definicion de la funcion, Python asigna el primer valor que recibe a
# el parametro 'tamaño'. Los demas valores que siguen son almacenados en la tupla 'ingredientes'.
# El llamado a al funcion incluye un argumento para 'tamaño' primero, por los ingredientes que se necesiten

crear_pizza("mediana", "piña")
crear_pizza("grande", 'chicharron', 'piña', 'queso', 'salchicha')
crear_pizza("pequeña", 'pepperoni', 'maicitos', 'lechuga', 'queso extra', 'tomate', 'cebolla')


