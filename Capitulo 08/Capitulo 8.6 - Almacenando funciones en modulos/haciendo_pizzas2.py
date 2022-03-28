# Importando funciones especificas

# Se pueden importar solamente las funciones necesarias sin importar el modulo completo
# si se importan varias, deberan ir separadas por una coma.
# Ej: from pizza import funcion1, funcion2, funcion3

from pizza import hacer_pizza   # Solamente se ha importado la funcion hacer_pizza

# Con esta sintaxis solo se hace el llamado a la funcion sin llamar al archivo.
hacer_pizza("grandota", "mani", "nueces", "lechuga")
hacer_pizza("chiquita", "piña", "jamon", "queso")


