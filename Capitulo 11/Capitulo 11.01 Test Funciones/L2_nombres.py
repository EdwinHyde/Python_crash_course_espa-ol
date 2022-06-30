from L1_testing import obtener_nombre_formateado

print("Ingrese 'S' para salir del programa")
while True:
    nombres = input("\nIngrese sus nombres por favor: ")
    if nombres.lower() == 's':
        break
    apellidos = input("\nIngrese sus apellidos: ")
    if apellidos.lower() == 's':
        break

    nombre_formateado = obtener_nombre_formateado(nombres, apellidos)
    print(f"\tNombre bien formateado: {nombre_formateado}")

#  Podemos ver que los nombres generados aquí son correctos.
#  Pero digamos que queremos modificar obtener_nombre_formateado() para que también pueda manejar segundos nombres.
#  Mientras lo hacemos, queremos asegurarnos de no dañar la forma en que la función maneja los nombres
#  que solo tienen un nombre y un apellido.
# Si automatizamos la prueba de obtener_nombre_formateado(), siempre podemos estar seguros de que la función
# funcionará cuando se le den los tipos de nombres para los que hemos escrito pruebas.
