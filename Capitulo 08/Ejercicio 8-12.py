# 8-12. Sandwiches:
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that’s being ordered.
# Call the function three times, using a different number of arguments each time

def preparar_sandwich(*args):  # Se crea la funcion que recibira los argumentos (*args o *ingredientes)
    """Resumiendo los sandwiches solicitados"""
    print("\nAgregando los siguientes ingredientes al sandwich: ")
    for arg in args:    # Se recorre la lista de ingredientes
        print(f"- {arg.title()}")


preparar_sandwich('bocadillo', 'queso')  # Se llama a la funcion 3 veces con diferente numero de argumentos.
preparar_sandwich('queso', 'jamon', 'mortadela', 'lechuga')
preparar_sandwich('lechuga')
