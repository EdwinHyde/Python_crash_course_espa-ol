import json

# Guardar datos con json es util cuando se trabaja con datos generados por el usuario, porque si no se almacena
# esta informacion de alguna manera, esta se perdera cuando el programa se detenga.
nombre_usuario = input("Ingrese su nombre por favor: ")

nombre_archivo = 'usuarios.json'
with open(nombre_archivo, 'w') as archivo:
    json.dump(nombre_usuario, archivo)
    print(f'Este nombre quedara guardado cuando vuelvas, {nombre_usuario}')