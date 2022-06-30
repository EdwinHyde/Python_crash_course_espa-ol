# Esta es una funcion simple que toma el primer nombre y apellido y retorna un nombre
# formateado de forma ordenada.

def obtener_nombre_formateado(nombres, apellidos):
    """Genera un nombre completo bien formateado"""
    nombre_completo = f'{nombres} {apellidos}'
    return nombre_completo.title()

# La funcion obtener_nombre_formateado() combina los nombres y apellidos con un espacio entre ellos
# para generar el nombre completo y pone su inicial en mayuscula y retorna el nombre completo.
# Para revisar que la funcion trabaja, crearemos un programa que usa la funcion, el programa nombres.py
# donde el usuario ingresa un nombre y apellidos y asi ver un nombre completo bien formateado.