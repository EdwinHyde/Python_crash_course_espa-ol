def contar_palabras(archivo):
    """Cuenta un nomero aproximado de palabras en un archivo"""

    try:
        with open(archivo, encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:  # Hemos capturado el error y enviado el listado de libros que faltan a un nuevo txt.
        faltantes = 'Archivos_faltantes.txt'
        with open(faltantes, 'a', encoding='utf-8') as f:
            f.write(f'El archivo {archivo} ha sido agregado a la lista de faltantes\n')
        print(f'El archivo {archivo} no existe o no se encuentra en la ubicación correcta.')

    else:
        palabras = contenido.split()
        numero_palabras = len(palabras)
        print(f'El archivo {archivo} tiene un aproximado de {numero_palabras} palabras.')

# archivo = 'alice.txt'
# contar_palabras(archivo)  # Creamos la funcion que cuente las palabras desde un archivo siguiendo lo aprendido.

# Para trabajar con varios archivos, los almacenamos en una lista y con un bucle for recorremos cada archivo.

archivos = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'cien años de soledad', 'little_women.txt']  # Falta el archivo siddhartha.
for archivo in archivos:
    contar_palabras(archivo)

# El uso del bloque try-except en este ejemplo proporciona dos ventajas significativas.
# Evitamos que nuestros usuarios vean un rastreo y dejamos que el programa continúe analizando los textos
# que puede encontrar.
# Si no detectamos el FileNotFoundError que generó siddhartha.txt, el usuario vería un rastreo completo
# y el programa dejaría de ejecutarse después de intentar analizar Siddhartha.
# Nunca analizaría Moby Dick o Mujercitas.
