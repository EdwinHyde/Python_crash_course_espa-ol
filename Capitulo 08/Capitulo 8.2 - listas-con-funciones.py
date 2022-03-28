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

diseños_sin_imprimir = ["robot", 'telefono', 'figura geometrica'] # Creacion de la lista
modelos_completos = [] # Esta lista se llena con los datos de diseños_sin_imprimir

imprimir_modelos(diseños_sin_imprimir[:], modelos_completos) #  Al hacer slice [:] se envia una copia de la lista, dejando la lista original llena, sin eliminar elementos
#  Si se quiere vaciar la lista original, se quita el slice[:] y la lista quedará vacía.
mostrar_modelos_completos(modelos_completos)

# print(diseños_sin_imprimir) # Se puede comprobar que la lista aun sigue sin modificaciones, pues se envió una copia
# print(modelos_completos)

    
    