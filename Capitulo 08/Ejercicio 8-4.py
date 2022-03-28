# 8-4. Large Shirts:
#       Modify the make_shirt() function so that shirts are large by default
#       with a message that reads I love Python. Make a large shirt and a
#       medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(tamaño = "Grande", texto="Amo Python"): #  Se modifica la funcion que recibirá un argumento predeterminado (default).
    print(f"Hola, has elegido una camiseta talla {tamaño}, la cual llevará "
          f"el siguiente texto: '{texto}'")

make_shirt() #  Se hace el llamado a la funcion con los argumentos predeterminados
make_shirt(tamaño="Mediana") #  Se modifica solamente el primer argumento, el segundo sigue predeterminado
make_shirt(tamaño="S", texto="Me encanta aprender a programar") #  Se modifican los dos argumentos