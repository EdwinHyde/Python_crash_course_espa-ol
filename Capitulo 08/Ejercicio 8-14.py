# 8-14. Cars:
# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs,
# such as a color or an optional feature.
# Your function should work for a call like this one:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary that’s returned to make sure all the information was stored correctly.

# la funcion recibirá nombre de fabricante y modelo y argumentos arbitrarios keyword
def informacion_carro(fabricante, modelo, **kwargs):
    """Construyendo diccionario con la información del auto."""
    kwargs['fabricante'] = fabricante  # La funcion recibe el fabricante y el modelo y lo retorna
    kwargs['modelo'] = modelo
    return kwargs


carro = informacion_carro("subaru", "outback", color="azul", remolque=True)
print(carro)
carro = informacion_carro("ford", "fiesta", color="blanco", turbo=False)
print(carro)
carro = informacion_carro("mazda", "2015", vidrio="electrico", sonido=True)
print(carro)
