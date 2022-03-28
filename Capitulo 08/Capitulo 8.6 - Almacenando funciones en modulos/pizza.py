# Se crea un archivo que contendra una o varias funciones que luego seran
# importadas desde otro archivo, para tener mas ordenado el programa.

def hacer_pizza(tamaño, *ingredientes):  # Se crea la funcion
    """Resumiendo la pizza que estamos haciendo."""
    print(f"Haciendo una pizza de tamaño {tamaño.title()}, con los siguientes ingredientes: ")
    for ingrediente in ingredientes:  # Se recorre la tupla con los ingredientes
        print(f"° {ingrediente.title()}")  # Se imprime la tupla.
