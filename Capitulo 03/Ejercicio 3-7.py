# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
#       •	 Start with your program from Exercise 3-6. Add a new line that prints a
#       message saying that you can invite only two people for dinner.
#       •	 Use pop() to remove guests from your list one at a time until only two
#       names remain in your list. Each time you pop a name from your list, print
#       a message to that person letting them know you’re sorry you can’t invite
#       them to dinner.
#       •	 Print a message to each of the two people still on your list, letting them
#       know they’re still invited.
#       •	 Use del to remove the last two names from your list, so you have an empty
#       list. Print your list to make sure you actually have an empty list at the end
#       of your program.

listaInvitados = ["Freddy Mercury", "George Harrison", "Eric Clapton"]
listaInvitados[1] = "Charlie Parker"
listaInvitados[2] = "Paul McCartney"
listaInvitados.insert(0, "Frank Sinatra")
listaInvitados.insert(2, "Brian May")
listaInvitados.append("Bob Dylan")

print("Lamentamos informar que solamente es posible invitar a dos personas :(")

artistaEliminado1 = listaInvitados.pop()
print(f'Apreciado {artistaEliminado1}, lamentamos informarle que no es posible que asista a nuestra cena, Lamentamos las molestias.')
print(listaInvitados)

artistaEliminado2 = listaInvitados.pop()
print(f'Apreciado {artistaEliminado2}, lamentamos informarle que no es posible que asista a nuestra cena, Lamentamos las molestias.')
print(listaInvitados)

artistaEliminado3 = listaInvitados.pop()
print(f'Apreciado {artistaEliminado3}, lamentamos informarle que no es posible que asista a nuestra cena, Lamentamos las molestias.')
print(listaInvitados)

artistaEliminado4 = listaInvitados.pop()
print(f'Apreciado {artistaEliminado4}, lamentamos informarle que no es posible que asista a nuestra cena, Lamentamos las molestias.')
print(listaInvitados)

print(f'Apreciado {listaInvitados[0]}, le informamos que aun está invitado a nuestra cena :)')
print(f'Apreciado {listaInvitados[1]}, le informamos que aun está invitado a nuestra cena :)')

del listaInvitados[1]
print(listaInvitados)
del listaInvitados[0]
print(listaInvitados)

len(listaInvitados)