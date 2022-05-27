# Refactorizar es cuando el codigo funciona pero reconocemos que es posible optimizarlo dividiendolo en una
# serie de funciones que tienen trabajos especificos.
# Refactorizar hace codigo mas limpio, mas facil de leer.

import json

def saludar_usuario():
    """Saludar al usuario por su nombre"""
    nombre_archivo = 'usuarios.json'
    try:
        with open(nombre_archivo) as archivo:
            usuario = json.load(archivo)

    except FileNotFoundError:
        usuario = input("Por favor ingrese su nombre: ")
        with open(nombre_archivo, 'w') as archivo:
            json.dump(usuario, nombre_archivo)
            print(f"Cuando regreses, recordaremos tu nombre {usuario}")

    else:
        print(f'Bienvenido nuevamente {usuario}!!!')


saludar_usuario()