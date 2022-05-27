# 10-3. Guest:
# Write a program that prompts the user for their name.
# When they respond, write their name to a file called guest.txt.

nombre_archivo = 'guest.txt'

nombre_usuario = input('Escriba por favor su nombre: ')

with open(nombre_archivo, 'a') as file_object:
    file_object.write(nombre_usuario.title())

