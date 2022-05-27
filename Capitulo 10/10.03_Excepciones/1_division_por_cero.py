# Es imposible dividir un numero por cero.

# print(5/0)  # Esto arrojará un traceback (rastreo) ya que python no puede hacer esta operacion.

# Para solucionar lo anterior se escribe un bloque try-except
# De esta forma el codigo seguira ejecutandose pero con un mensaje de error que el usuario pueda entender.


try:
    print(5/0)
except ZeroDivisionError:
    # Enviamos a imprimir 5/0, linea que causó el error, dentro de un bloque try.
    # Si el codigo dentro del bloque funciona, python se salta el bloque except.
    # Si el codigo dentro del bloque try causa un error, Python busca un bloque de excepción cuyo error
    # coincida con el que se generó y ejecuta el código en ese bloque.
    print('No es posible dividir un número por cero')



