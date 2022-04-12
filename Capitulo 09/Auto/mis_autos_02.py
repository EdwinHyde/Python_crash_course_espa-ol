# Este modulo trabaja en conjunto con los modulos auto2.py y mi_auto_electrico_02.py
# IMPORTANDO MODULO EN UN MODULO.

from auto2 import Carro  # importamos Carro desde su modulo auto2
from mi_auto_Electrico_02 import CarroElectrico  # importamos CarroElectrico desde su modulo mi_auto_electrico_02

escarabajo = Carro("volkswagen", "escarabajo", 2019)  # Se crea el escarabajo
print(f"Acá hemos creado un {escarabajo.nombre_descriptivo()}")

tesla = CarroElectrico("tesla", "roadster", 2019) # Se crea el auto tesla.
print(f"Acá hemos creado un {tesla.nombre_descriptivo()}")