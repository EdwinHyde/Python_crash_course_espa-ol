# 8-13. User Profile:
# Start with a copy of user_profile.py from page 149.
# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you.

def crear_usuario(nombres, apellidos, **informacion_usuario):  # Se crea la funcion que recibira un diccionario
    """Se construye un diccionario que contiene la informacion del usuario."""
    informacion_usuario['nombres: '] = nombres  # Se agrega al diccionario la informacion de nombres y apellidos.
    informacion_usuario['apellidos: '] = apellidos

    return informacion_usuario  # Se retorna la informacion del usuario


perfil_usuario = crear_usuario('edwin', 'chica',
                               direccion="palocabildo",
                               estudios="musica",
                               hobby="tocar guitarra")

print(perfil_usuario)
