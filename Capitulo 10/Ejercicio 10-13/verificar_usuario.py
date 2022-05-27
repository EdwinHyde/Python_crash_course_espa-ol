# -*- coding: utf-8 -*-
# 10-13. Verify User:
# The final listing for remember_me.py (en nuestro caso el archivo es 7_refactorizando_parte2.py)
# assumes either that the user has already entered their username or that the program is running for the first time.
# We should modify it in case the current user is not the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if this is the correct username.
# If it’s not, call get_new_username() to get the correct username.

import json

def recuperar_usuario_almacenado():
    """Recupera un usuario almacenado, si esta disponible"""
    nombre_archivo = "usuarios.json"
    try:
        with open(nombre_archivo) as archivo:
            usuario = json.load(archivo)
    except FileNotFoundError:
        return None
    else:
        return usuario


def obtener_nuevo_usuario():
    """Solicita un nuevo usuario"""
    usuario = input("Ingrese por favor su nombre: ")
    nombre_archivo = "usuarios.json"
    with open(nombre_archivo, 'w') as archivo:
        json.dump(usuario, archivo)
    return usuario


def verificar_usuario():
    usuario = recuperar_usuario_almacenado()
    verificacion = input(f"Es usted el usuario {usuario}? Responda Si/No: \n")
    if verificacion.lower() == "si":
        return usuario
    # else:
    #     obtener_nuevo_usuario()


def saludar_usuario():
    """Saluda al usuario por su nombre"""
    usuario = verificar_usuario()
    # usuario = recuperar_usuario_almacenado()
    if usuario:
        print(f"Bienvenido nuevamente {usuario}")
    else:
        usuario = obtener_nuevo_usuario()
        print(f"{usuario}, has quedado registrado y aparecerás la proxima vez..")


saludar_usuario()