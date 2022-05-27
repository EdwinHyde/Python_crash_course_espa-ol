filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contenido = f.read()
except FileNotFoundError:
    print(f'Lo sentimos, el archivo {filename} no existe o se encuentra en otra ubicación.')

else:
    # Contamos el numero aproximado de palabras en el archivo.
    palabras = contenido.split()
    numero_palabras = len(palabras)
    print(f'El archivo de nombre {filename}, tiene alrededor de {numero_palabras} palabras.')