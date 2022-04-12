# IMPORTANDO UN MODULO EN UN MODULO.
# Para trabajar este modulo es necesario el modulo auto2.py y mis_autos_02.py

'''Un conjunto de clases que se pueden usar para representar carros electricos'''

from auto2 import Carro  # La clase CarroElectrico necesita acceso a su clase principal Carro
# asi que importamos directamente Carro dentro del modulo.

class Bateria:  # Definimos una nueva clase: Bateria, que no hereda de ninguna otra clase
    """Un simple intento de modelar una bateria para un auto electrico."""
    def __init__(self, tamaño=75):  # tamaño es un parametro opcional que pone el tamaño de la bateria en 75.
        """Inicializa los atributos de la clase Bateria"""
        self.tamaño = tamaño

    def describir_bateria(self):  # Se crea el metodo para describir la bateria.
        """Se imprime una oracion que describa el tamaño de la bateria"""
        print(f"Este auto tiene una bateria de {self.tamaño} kWh")

    def obtener_rango(self):
        """Imprime una declaracion sobre el rango que proporciona la bateria"""
        if self.tamaño == 75:
            rango = 260
        elif self.tamaño == 100:
            rango = 315

        print(f"Este auto puede recorrer hasta {rango} kilometros con una carga completa.")


class CarroElectrico(Carro):
    """Representa aspectos de un carro, especificamente de uno electrico"""

    def __init__(self, fabricante, modelo, año):
        """
        Se inicializan los atributos de la clase padre,
        luego se inicializan los atributos para un carro electrico.
        """
        super().__init__(fabricante, modelo, año)
        self.bateria = Bateria()  # Esta linea le dice a python que cree una nueva instancia de Bateria.
        # la cual tiene un valor predeterminado (75) y asigna esa instancia al atributo self.bateria
        # esto ocurrira cada vez que el metodo constructor es llamado. Cualquier instancia de CarroElectrico
        # ahora tendrá una instancia de Bateria creada automaticamente.

    def tanquear_gasolina(self):
        """Los autos electricos no necesitan gasolina"""
        print("Este auto no necesita un tanque de gasolina... Es eléctrico.")

