# Un error comun al trabajar con archivos es el maejo de archivos perdidos porque el archivo podria estar
# en una ubicaion diferente.

filename = 'alicia.txt'

# Codigo con traceback error.

# with open(filename, encoding='utf-8') as f:  # es comun usar la variable f para representar el archivo objeto.
#     # El argumento encoding es necesario cuando la codificación predeterminada de su sistema no coincide
#     # con la codificación  del archivo que se está leyendo.
#     contenido = f.read()  # python no podrá leer el archivo, asi que arrojará el error FileNotFoundError

# Codigo con bloque try-except

try:
    with open(filename, encoding='utf-8') as f:
        contenido = f.read()

except FileNotFoundError:
    print(f"Lo sentimos, el archivo {filename} no existe o no se encuentra en la ruta establecida.")