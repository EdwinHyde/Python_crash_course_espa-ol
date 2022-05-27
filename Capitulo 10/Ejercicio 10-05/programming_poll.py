# 10-5. Programming Poll:
# Write a while loop that asks people why they like programming.
# Each time someone enters a reason, add their reason to a file that stores all the responses.

nombre_archivo = 'respuestas.txt'

while True:
    print('Bienvenido a nuestra encuesta. Cuando quieras terminar presiona la tecla s')
    respuestas = input('¿Por qué te gusta programar? ')

    if respuestas.title() == 'S':
        break

    with open(nombre_archivo, 'a') as file_object:
        file_object.write(f'{respuestas}\n')
