# 10-7. Addition Calculator:
# Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers
# even if they make a mistake and enter text instead of a number.

# 1. Se envuelve el codigo del ejercicio anterior en un bucle while:
while True:
    # Se piden los numeros al usuario:
    print('Sumaremos tus numeros, cuando quieras salir, presiona s')
    numero1 = input('Ingrese el primer numero: ')
    if numero1 == "s":  # Si se presiona la s, el programa se termina
        break
    numero2 = input('Ingrese el segundo numero: ')
    if numero2 == 's':
        break

    try:
        resultado = int(numero1) + int(numero2)
        print(f'El resultado es: {resultado}')

    except ValueError:  # Si el usuario proporciona un valor diferente a numero, no pasará nada.
        pass


# print('Ingrese dos números para sumarlos. \nCuando desee salir presione s')
#
# while True:
#     numero1 = input('Ingrese un numero: ')
#     if numero1 == 's':
#         break
#
#     numero2 = input('Ingrese otro numero: ')
#     if numero2 == 's':
#         break
#
#     try:
#         resultado = int(numero1) + int(numero2)
#         print(f'El resultado es: {resultado}')
#
#     except ValueError:
#         print('Por favor ingrese solamente numeros, no se admiten letras o simbolos.')
#         print('El programá finalizará...')
