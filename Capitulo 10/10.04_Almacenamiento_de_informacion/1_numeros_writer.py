import json  # Importamos el modulo json

numeros = [1, 2, 4, 8, 16, 32, 64]  # Creamos la lista de numeros.

# La funcion json.dump() toma dos argumentos: un dato para almacenar y un objeto de archivo que puede usar
# para almacenar los datos.

archivo = 'numeros.json'  # Primero elegimos un nombre de archivo en el cual se almacena la lista de numeros.
# Es habitual utilizar la extension de archivo .json para indicar que los datos del archivo se almacenan en formato JSON
with open(archivo, 'w') as a:  # Se abre el archivo en modo escritura y se da un alias (a)
    json.dump(numeros, a)  # se usa la funcion json.dump() para almacenar la lista de numeros en el archivo numeros.json



