# Poniendo un alias a la función
# Se puede usar un "alias" como nombre alterno o nickname a la funcion al importar.

# Desde el archivo pizza se importa la funcion hacer_pizza y se renombra con el alias hp
# para hacer mas entendible el codigo
from pizza import hacer_pizza as hp  # La palabra clave en este caso es "as"

hp("chiquitica", "piña", "pepperoni", "hongos")  # Se llama la funcion con el alias asignado (hp)
hp("familiar", "huevo", "tocino", "lechuga", "maicitos", "pimenton")  # Ayuda a evitar confusiones al llamar funciones

