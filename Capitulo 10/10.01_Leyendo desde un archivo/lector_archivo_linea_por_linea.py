# LEYENDO UN ARCHIVO LINEA POR LINEA

nombre_archivo = 'texto.txt' # Asiganmos la ruta del archivo que estamos leyendo a la variable nombre_archivo.
# Es una convencion comun al trabajar con archivos, porque el nombre de la variable no representa el archivo actual
# solo es un string que le indica a python donde encontrar el archivo el cual se puede intercambiar por
# cualquier otro archivo.

with open(nombre_archivo) as archivo_objeto: # Despues de llamar el metodo open() un objeto representara el archivo
    # y su contenido es asigando a la variable
    for linea in archivo_objeto: # Para examinar el contenido del archivo, recorremos cada linea
        # en el archivo con el bucle for a traves del archivo_objeto.
        print(linea) # Se puede usar rstrip() para eliminar las lineas en blanco generadas, una por el archivo
        # y otra por el metodo print()
