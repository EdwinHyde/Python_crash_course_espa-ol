import json

# En este caso se muestra como se combinan los dos archivos vistos anteriormente.
# Se carga el nombre del usuario si ha sido previamente cargado
# Sino, se solicita al usuario y se guarda

nombre_archivo = 'usuarios.json'
try:
    with open(nombre_archivo) as archivo:  # Si el archivo existe se leera la informacion que contiene.
        usuario = json.load(archivo)  # Se imprime un mensaje de bienvenida  en el bloque else.
        # Si el archivo no existe, se saltará este bloque y pasa al bloque except

except FileNotFoundError:  # Al no existir el archivo, se solicitará la informacion al usuario.
    usuario = input("Por favor ingrese su nombre: ")
    with open(nombre_archivo, 'w') as archivo:
        json.dump(usuario, archivo)  # se hace uso de json.dump() para almacenar el nombre de usuario
        print(f'Este nombre quedara guardado cuando vuelvas, {usuario}')  # se imprime un saludo.
else:
    print(f'Bienvenido nuevamente {usuario}')