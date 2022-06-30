# Para hacer opcional los segundos nombres, movemos el parametro segundo_nombre al final de la lista de parametros
# en la definicion de la funcion y se le otorga un valor por defecto vacio. También agregamos una prueba if
# que construya el nombre completo de forma correcta, dependiendo si el segundo nombres es o no proporcionado.

def obtener_nombre_formateado(primer_nombre, apellidos, segundo_nombre=""):
    """Genera un nombre completo bien formateado"""
    if segundo_nombre:
        nombre_completo = f'{primer_nombre} {segundo_nombre} {apellidos}'
    else:
        nombre_completo = f'{primer_nombre} {apellidos}'
    return nombre_completo.title()

# En esta version de la funcion, el segundo nombre es opcional.
# Si se pasa un segundo nombre a la funcion, el nombre completo contendra los tres datos, sino, el nombre completo
# consistira solo de primer nombre y apellidos. La funcion deberia trabajar para ambos tipos de nombres.

# Ahora podemos probar el test.