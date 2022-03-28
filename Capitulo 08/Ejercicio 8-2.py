# 8-2. Favorite Book:
#       Write a function called favorite_book() that accepts one parameter, title.
#       The function should print a message, such as One of my # favorite books is Alice in Wonderland.
#       Call the function, making sure to include a book title as an argument
#       in the function call.

def libro_favorito(titulo):  # se crea la funcion y se agrega entre parentesis un "parametro" (titulo)
    print(f"Uno de mis libros favoritos es {titulo.title()}")  # Se agrega la variable creada en el parametro


libro_favorito("romeo y julieta")  # Se invoca la funcion ingresando el "argumento" en los parentesis
#  El cual se almacena en la variable creada en el parametro
