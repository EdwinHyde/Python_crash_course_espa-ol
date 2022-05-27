# USANDO EXCEPCIONES PARA PREVENIR BLOQUEOS.

print("Dame un par de numeros y los dividiré: ")
print("cuando quiera salir, presione 'q' ")

while True:
    primer_numero = input("\ningrese el primer número: ")
    if primer_numero == 'q':
        break

    # al dividir por 0 en este bloque ocurrirá un error, por lo tanto, acá debe ir el bloque try-except.
    segundo_numero = input("\nIngrese el segundo número: ")
    if segundo_numero == 'q':
        break
    try:
        solucion = int(primer_numero) / int(segundo_numero)  # Bloque try-except
    except ZeroDivisionError:
        print("No es posible dividir por cero.")
    else:  # En caso que la division sea exitosa, el bloque else sera usado para mostrar el resultado
        print(solucion)
