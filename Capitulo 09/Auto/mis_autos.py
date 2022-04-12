# IMPORTANDO UN MODULO ENTERO.

import auto  # Se importa el modulo, con el nombre del archivo

escarabajo = auto.Carro("volkswagen", "escarabajo", 2019)  # Acceder a las clases que necesitamos con notacion de punto
print(f"Acá hemos creado un {escarabajo.nombre_descriptivo()}")

tesla = auto.CarroElectrico("tesla", "roadster", 2019)
print(f"Acá hemos creado un {tesla.nombre_descriptivo()}")
