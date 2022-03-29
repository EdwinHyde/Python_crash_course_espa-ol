# 8-15. Printing Models:
# Put the functions for the example printing_models.py in a
# separate file called printing_functions.py.
# Write an import statement at the top of printing_models.py,
# and modify the file to use the imported functions.

def imprimir_modelos(diseños_sin_imprimir, modelos_completos):
    """
    Simular la impresion de cada diseño, hasta que no quede alguno,
    Mover cada diseño a modelos_completos despues de imprimir.
    """
    while diseños_sin_imprimir:
        diseño_actual = diseños_sin_imprimir.pop()
        print(f"Imprimiendo modelo {diseño_actual.title()}")
        modelos_completos.append(diseño_actual)


def mostrar_modelos_completos(modelos_completos):
    """ Mostrar todos los modelos que fueron impresos """
    print("\nLos siguientes modelos han sido impresos: ")
    for modelo in modelos_completos:
        print(modelo)