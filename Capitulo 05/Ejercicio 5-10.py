# 5-10. Checking Usernames: Do the following to create a program that simulates
#       how websites ensure that everyone has a unique username.
#           •	 Make a list of five or more usernames called current_users.
#           •	 Make another list of five usernames called new_users. Make sure one or
#               two of the new usernames are also in the current_users list.
#           •	 Loop through the new_users list to see if each new username has already
#               been used. If it has, print a message that the person will need to enter a
#               new username. If a username has not been used, print a message saying
#               that the username is available.
#           •	 Make sure your comparison is case insensitive. If 'John' has been used,
#               'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
#               current_users containing the lowercase versions of all existing users.)

usuarios_actuales = ["gris", "pao", "france", "manu", "stefa", "edwin"]
usuarios_actuales_my = ["GRIS", "PAO", "FRANCE", "MANU", "STEFA", "EDWIN"]
usuarios_nuevos = ["pao", "rodri", "freddy", "EDWIN", "sandra", "juan"]

for nuevos in usuarios_nuevos:
    if (nuevos in usuarios_actuales) or (nuevos in usuarios_actuales_my):
        print(f'{nuevos}: Ingresa un nuevo nombre de usuario, el que escribiste ya se encuentra en uso.')
    else:
        print(f'{nuevos}: Tu nombre de usuario está disponible y se será asignado como: {nuevos.title()}')
