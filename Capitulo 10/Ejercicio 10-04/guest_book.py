# 10-4. Guest Book:
# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.

nombre_archivo = 'guest_book.txt'

while True:
    print('Registraremos sus nombres, si desea terminar, escriba s')
    nombres = input('Por favor escriba su nombre: ')
    if nombres.title() == 'S':
        print('Gracias por usar mi programa.')
        break

    print(f'{nombres.title()} muchas gracias por tu visita.')

    with open(nombre_archivo, 'a') as file_object:
        file_object.write(f'El nombre {nombres.title()} ha sido guardado.\n')
