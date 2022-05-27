import json

nombre_archivo = 'usuarios.json'

with open(nombre_archivo) as archivo:
    usuario = json.load(archivo)
    print(f"Bienvenido de nuevo, {usuario}")