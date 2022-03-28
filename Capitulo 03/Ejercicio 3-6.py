# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
#       •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
#       call to the end of your program informing people that you found a bigger
#       dinner table.
#       •	 Use insert() to add one new guest to the beginning of your list.
#       •	 Use insert() to add one new guest to the middle of your list.
#       •	 Use append() to add one new guest to the end of your list.
#       •	 Print a new set of invitation messages, one for each person in your list.

listaInvitados = ["Freddy Mercury", "George Harrison", "Eric Clapton"]
listaInvitados[1] = "Charlie Parker"
listaInvitados[2] = "Paul McCartney"

print(f'Apreciado {listaInvitados[0]}: nuestra mesa es demasiado grande, razon por la cual, tendremos algunos invitados extra')
print(f'Apreciado {listaInvitados[1]}: nuestra mesa es demasiado grande, razon por la cual, tendremos algunos invitados extra')
print(f'Apreciado {listaInvitados[2]}: nuestra mesa es demasiado grande, razon por la cual, tendremos algunos invitados extra')

listaInvitados.insert(0, "Frank Sinatra")
listaInvitados.insert(2, "Brian May")
listaInvitados.append("Coldplay")

print(f'Bienvenido {listaInvitados[0]} a esta celebración.')
print(f'Bienvenido {listaInvitados[1]} a esta celebración.')
print(f'Bienvenido {listaInvitados[2]} a esta celebración.')
print(f'Bienvenido {listaInvitados[3]} a esta celebración.')
print(f'Bienvenido {listaInvitados[4]} a esta celebración.')
print(f'Bienvenido {listaInvitados[5]} a esta celebración.')

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.
print(len(listaInvitados))

