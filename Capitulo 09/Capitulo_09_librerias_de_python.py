# LA BIBLIOTECA STANDARD DE PYTHON
# MODULO Random
# El modulo Random no deberia usarse en la creacion de aplicaciones relacionadas con seguridad.
# pero es bastante buena para muchos proyectos divertidos e interesantes.

# La funcion randint toma dos argumentos de numeros enteros y regresa uno al azar entre estos dos numeros.
from random import randint
# La funcion choice toma una lista o tupla y retorna un elemento elegido al azar.
from random import choice

print(randint(1,5))  # Genera un numero al azar entre 1 y 5

jugadores = ['charles', 'martina', 'michael', 'florence', 'eli']
eleccion = choice(jugadores)
print(eleccion.title())




