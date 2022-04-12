# IMPORTANDO MULTIPLES CLASES DESDE UN MÓDULO.

"""Un conjunto de clases usadas para representar autos de gasolina y electricos"""

# Se importan multiples clases desde un modulo, separando cada clase con una coma (,)
# Cuando se hayan importado las clases necesarias, se pueden crear tantas instancias de cada clase
# como se necesiten.
from auto import Carro, CarroElectrico

# En este ejemplo creamos un escarabajo volskwagen y un carro electrico.
escarabajo = Carro("volskwagen", "escarabajo", 2000)
print(f"\nLos datos de este auto son: \n{escarabajo.nombre_descriptivo()}")

tesla = CarroElectrico("Musk", "mazzinger x", "2050")
print(f"\nLos datos de este auto eléctrico son: \n{tesla.nombre_descriptivo()}")
tesla.bateria.describir_bateria()
tesla.bateria.obtener_rango()
