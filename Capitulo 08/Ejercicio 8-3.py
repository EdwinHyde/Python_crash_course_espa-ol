# 8-3. T-Shirt:
#       Write a function called make_shirt() that accepts a size and the
#       text of a message that should be printed on the shirt. The function should print
#       a sentence summarizing the size of the shirt and the message printed on it.
#       Call the function once using positional arguments to make a shirt. Call the
#       function a second time using keyword arguments.

def make_shirt(tamaño, texto): #  Se crea la funcion que recibirá dos argumentos.
    print(f"Hola, has elegido una camiseta talla {tamaño}, la cual llevará "
          f"el siguiente texto: '{texto}'")

make_shirt(16, "El mejor padre del mundo") #  Se hace el llamado a la funcion usando argumentos posicionales
make_shirt(texto="'Hola, soy groot'", tamaño="M") #  argumentos palabra:clave, ene ste caso invertidos.
