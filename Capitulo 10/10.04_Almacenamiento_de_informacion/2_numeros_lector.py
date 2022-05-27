import json  # Importamos el modulo json

archivo = 'numeros.json'   # nos aseguramos leer desde el mismo archivo que se escribio antes.

with open(archivo) as a:  # se abre el archivo en modo lectura, pues solo se necesita leer desde el archivo.
    numeros = json.load(a)  # se usa la funcion json.load() para cargar la informacion almacenada en numeros.json

print(numeros)  # Se imprime la lista recuperada de numeros y se observa que es la misma lista creada antes.
