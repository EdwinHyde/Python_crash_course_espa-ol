# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
#   not empty.
#       •	 If the list is empty, print the message We need to find some users!
#       •	 Remove all of the usernames from your list, and make sure the correct
#           message is printed.

usuarios = ["administrador", "profesor", "estudiante", "padre de familia", "invitado"]

if usuarios:
    for usuario in usuarios:
        if usuario == "administrador":
            print(f'Hola {usuario.title()}: \nBienvenido al sistema, le gustaria ver su reporte del dia?')
        else:
            print(f'Hola {usuario.title()}: Gracias por ingresar de nuevo')

else:
    print("Necesitamos conseguir algunos usuarios")

usuarios.pop(0)
usuarios.pop(0)
usuarios.remove("estudiante")
usuarios.remove("invitado")
usuarios.pop()

if usuarios:
    for usuario in usuarios:
        if usuario == "administrador":
            print(f'Hola {usuario.title()}: \nBienvenido al sistema, le gustaria ver su reporte del dia?')
        else:
            print(f'Hola {usuario.title()}: Gracias por ingresar de nuevo')

else:
    print("Necesitamos conseguir algunos usuarios")

