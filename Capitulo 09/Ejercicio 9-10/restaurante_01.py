# 9-10. Imported Restaurant:
#           Using your latest Restaurant class, store it in a module.
#           Make a separate file that imports Restaurant.
#           Make a Restaurant instance, and call one of Restaurant’s methods
#           to show that the import statement is working properly.

import restaurante

mi_chuzo = restaurante.Restaurante("la  bufalera", "carne de bufalo", "la dorada")
mi_chuzo.descripcion_restaurante()
mi_chuzo.abrir_restaurante()
print(f"El numero de mesas servidas en ete momento es {mi_chuzo.numero_servido} mesas")
mi_chuzo.incrementar_numero_servido(10)
print(f"El numero de mesas servidas en ete momento es {mi_chuzo.numero_servido} mesas")
mi_chuzo.incrementar_numero_servido(4)
print(f"El numero de mesas servidas en ete momento es {mi_chuzo.numero_servido} mesas")