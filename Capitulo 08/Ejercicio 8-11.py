# 8-11. Archived Messages:
#           Start with your work from Exercise 8-10.
#           Call the function send_messages() with a copy of the list of messages.
#           After calling the # function, print both of your lists to show that the original
#           list has retained its messages.

def enviar_mensajes(mensajes, enviados):
    """La funcion imprime los mensajes que recibe de la lista 'mensajes' """
    while mensajes:  # Mientras la lista mensajes no este vacia
        mensaje_actual = mensajes.pop()  # Se elimina el ultimo mensaje y se almacena en mensaje_actual
        print(f"Imprimiendo mensaje: {mensaje_actual}")  # Se simula la impresion del mensaje guardado
        enviados.append(mensaje_actual)  # El mensaje eliminado se agrega a la lista enviados


def mensajes_enviados(enviados):
    """Esta función muestra los mensajes que se guardaron el lista enviados."""
    print("\nLos siguientes mensajes han sido impresos: ")
    for enviado in enviados:  # El ciclo recorre los mensajes que se guardaron en la lista enviados.
        print(enviado)  # Muestra el mensaje enviado.


mensajes = ["Hola, espero que estes bien", "Que tengas un lindo dia", "Feliz cumpleaños"]
enviados = []

enviar_mensajes(mensajes[:], enviados)  # Se envia el argumento con copia para conservar la lista original
mensajes_enviados(enviados)  # Se envian los argumentos a la funcion mensajes_enviados

print(f"\nLista mensajes: {mensajes}")  # Se comprueba que la lista original se conserve
print(f"Lista enviados: {enviados}")  # Se comprueba que la lista haya sido movida correctamente
