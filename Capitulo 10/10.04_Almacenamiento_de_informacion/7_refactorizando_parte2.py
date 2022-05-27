import json

# Los codigos anteriores ahora se han fragmentado en varias tareas especificas.

def recuperar_usuario_almacenado():
    """Recupera un usuario almacenado, si esta disponible"""
    nombre_archivo = "usuarios.json"
    try:  # Esta funcion recibe un usuario almacenado y retorna el usuario, si lo encuentra (bloque else:)
        with open(nombre_archivo) as archivo:
            usuario = json.load(archivo)

    except FileNotFoundError:
        return None  # si la funcion no encuentra el archivo la funcion retorna None
    else:
        return usuario  # Como buena practica, una fucnion deberia retornar el valor esperado, sino retornar None.


def obtener_nuevo_usuario():
    """Solicita un nuevo usuario"""
    usuario = input("Ingrese por favor su nombre: ")
    nombre_archivo = "usuarios.json"
    with open(nombre_archivo, 'w') as archivo:
        json.dump(usuario, nombre_archivo)
    return usuario


def saludar_usuario():
    """Saluda al usuario por su nombre"""
    usuario = recuperar_usuario_almacenado()
    if usuario:  # Se muestra un mensaje de bienvenida si se recupera con exito el usuario, sino pide un nuevo usuario.
        print(f"Bienvenido nuevamente {usuario}")
    else:
        usuario = obtener_nuevo_usuario()
        print(f"{usuario}, te recordaremos la proxima vez que ingreses.")


saludar_usuario()
