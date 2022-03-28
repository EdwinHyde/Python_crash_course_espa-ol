# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
#       •	 Start with your program from Exercise 3-4. Add a print() call at the end
#       of your program stating the name of the guest who can’t make it.
#       •	 Modify your list, replacing the name of the guest who can’t make it with
#       the name of the new person you are inviting.
#       •	 Print a second set of invitation messages, one for each person who is still
#       in your list.

listaInvitados = ["Freddy Mercury", "George Harrison", "Eric Clapton"]
print(f'Lamentamos comunicar que el señor {listaInvitados[1]} no podrá asistir')
print(f'Además, informamos que el gran {listaInvitados[2]} ha cancelado en ultimo momento')

listaInvitados[1] = "Charlie Parker"
listaInvitados[2] = "Paul McCartney"
print(f'Bienvenido {listaInvitados[0]} a esta gran cena')
print(f'Bienvenido {listaInvitados[1]} a esta gran cena')
print(f'Bienvenido {listaInvitados[2]} a esta gran cena')

len(listaInvitados)