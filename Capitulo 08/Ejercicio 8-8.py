# 8-8. User Albums:
#           Start with your program from Exercise 8-7. Write a while
#           loop that allows users to enter an album’s artist and title.
#           Once you have that information, call make_album() with the user’s input
#           and print the dictionary that’s created.
#           Be sure to include a quit value in the while loop.

def make_album(artista, titulo_album, numero=None):  # Se crea la funcion que recibira 2 parametros y 1 opcional
    album_completo = {"Artista": artista.title(), "Album": titulo_album.title()}
    if numero:  # Se pone el condicional en caso que se quiera ingresar el numero de canciones.
        album_completo["Número de canciones"] = numero
    return album_completo  # Se retorna la variable con los datos


while True:
    print("\nLlenemos los datos del album: ")
    print("(Escriba salir para terminar le programa.)")
    n_artista = input("\nEscribe el nombre del artista: ")
    if n_artista.lower() == "salir":
        break
    n_album = input("Escriba el titulo del album: ")
    if n_album.lower() == "salir":
        break

    mi_album = make_album(n_album, n_artista)
    print("\nLos datos del album son: ")
    print(mi_album)
