# 8-9. Messages: Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.

def mostrar_mensajes(mensajes):
    """La funcion imprime los mensajes que recibe de la lista 'mensajes' """
    for mensaje in mensajes:
        print(mensaje)


mensajes = ["Hola, espero que estes bien", "Que tengas un lindo dia", "Feliz cumpleaños"]
mostrar_mensajes(mensajes)
