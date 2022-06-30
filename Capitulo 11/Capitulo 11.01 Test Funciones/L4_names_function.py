# Modificaremos obtener_nombre_formateado(), asi podremos manejar segundos nombres, pero se hará de forma que la
# funcion falle para nombres con solo un nombre y apellido, como Joaquin Sabina.
# Aqui se presenta una nueva version de obtener_nombre_formateado() que solicita un segundo nombre como argumento.


def obtener_nombre_formateado(primer_nombre, segundo_nombre, apellidos):
    """Genera un nombre completo bien formateado"""
    nombre_completo = f'{primer_nombre} {segundo_nombre} {apellidos}'
    return nombre_completo.title()

# obtener_nombre_formateado("richie", "ray")

