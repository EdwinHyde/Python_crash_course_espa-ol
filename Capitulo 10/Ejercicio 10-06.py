# 0-6. Addition:
# One common problem when prompting for numerical input occurs when people provide text instead of numbers.
# When you try to convert the input to an int, you’ll get a ValueError.
# Write a program that prompts for two numbers.
# Add them together and print the result.
# Catch the ValueError if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.

# 1. Se solicitan los numeros al usuario
numero1 = input('Ingrese un numero: ')
numero2 = input('Ingrese otro numero: ')

# 2. Se crea el bloque que podria producir el error al ingresar un valor diferente a un numero.
try:
    resultado = int(numero1) + int(numero2)
    print(f'El resultado es: {resultado}')

# 3. Se muestra un mensaje amable al usuario sobre el error.
except ValueError:
    print('Por favor ingrese solamente numeros, no se admiten letras o simbolos.')
    print('El programá finalizará...')
