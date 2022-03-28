# Modificando listas dentro de una funcion - Capitulo 8.

# Consider a company that creates 3D printed models of designs that
# users submit. Designs that need to be printed are stored in a list, and after
# being printed they’re moved to a separate list. The following code does this
# without using functions:


#  se inicia con algunos diseños que necesitan ser impresos
diseños_no_impresos = ['telefono', 'robot', 'dodecaedro']
modelos_completos = []

# simular imprimir cada diseño, hasta que no falte algunos
# mover cada diseño a modelos_completos despues de imprimir.
while diseños_no_impresos:
    diseño_actual = diseños_no_impresos.pop()
    print(f"Imprimiendo el modelo: {diseño_actual}")
    modelos_completos.append(diseño_actual)

# mostrando todos los modelos completados.
print("\nLos siguientes modelos han sido impresos: ")
for completado in modelos_completos:
    print(completado)




    

