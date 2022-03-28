#  Usando argumentos arbitrarios de palabra clave (keywords)
#  Es posible escribir funciones que acepten tantos pares de clave-valor como 
#  el llamado proporcione.

def crear_perfil(nombres, apellidos, **informacion_usuario):
    #  El doble asterisco crea un diccionario vacio(**informacion_usuario) y empaqueta pares nombre-valor.
    #  dentro de la funcion se puede acceder a la informacion del diccionario como se hace con cualquier diccionario.
    """Construir un diccionario que contenga todo lo que sabemos sobre un usuario."""
    informacion_usuario["nombres"] = nombres    #  Se agregan nombres y apellidos al diccionario (informacion_usuario).
    informacion_usuario["apellidos"] = apellidos
    return informacion_usuario  #  Se retorna el diccionario informacion_usuario a la linea del llamado de funcion.



perfil_usuario = crear_perfil('albert', 'einstein', #  Se llama a la funcion pasando nombres y apellidos y dos valores clave-valor: residencia, campo
                              residencia = 'princeton',
                              campo = 'fisica')

print(perfil_usuario) #  Se asigna el valor retornado a perfil_usuario y se imprime perfil_usuario.
#  El diccionario retornado contiene nombres y apellidos del usuario y
#  en este caso, la residencia y campo de estudio. La funcion trabajaia sin importar
#  cuantos pares de valores de clave-valor se proporcione en el llamado a la funcion.




