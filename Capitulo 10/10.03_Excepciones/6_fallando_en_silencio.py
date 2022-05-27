# Algunas veces  se desea que cuando ocurra una excepcion el programa continue como si no pasara nada.
# se le llama fallar en silencio y es decirle a python que no haga algo en el bloque except.
# para ello se hace uso de la sentencia pass.

def contar_palabras(archivo):
    """Cuenta un nomero aproximado de palabras en un archivo"""

    try:
        with open(archivo, encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:
        pass  # En este caso no pasará nada, ni aparecerá algun mensaje, pero no generará tampoco algun error.

    else:
        palabras = contenido.split()
        numero_palabras = len(palabras)
        print(f'El archivo {archivo} tiene un aproximado de {numero_palabras} palabras.')

archivos = ['alice.txt', 'siddhartha.txt', 'el quijote', 'moby_dick.txt', 'little_women.txt']  # Falta el archivo siddhartha.
for archivo in archivos:
    contar_palabras(archivo)