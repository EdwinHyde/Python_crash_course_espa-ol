# 9-9. Battery Upgrade:
#       Use the final version of electric_car.py from this section.
#       Add a method to the Battery class called upgrade_battery().
#       This method should check the battery size and set the capacity to 100 if it isn’t already.
#       Make an electric car with a default battery size, call get_range() once, and
#       then call get_range() a second time after upgrading the battery.
#       You should see an increase in the car’s range.

class Carro:
    """Un intento simple de representar un carro."""
    def __init__(self, fabricante, modelo, año):
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.odometro_tablero = 0

    def nombre_descriptivo(self):
        nombre_largo = f'{self.año} {self.fabricante} {self.modelo}'
        return nombre_largo

    def leer_odometro(self):
        print(f"Este carro tiene {self.odometro_tablero} kilómetros recorridos.")

    def actualizar_odometro(self, kilometraje):
        if kilometraje >= self.odometro_tablero:
            self.odometro_tablero = kilometraje
        else:
            print("No es posible retroceder el odometro")

    def incrementar_odometro(self, kilometros):
        if kilometros < 0:
            print("Lo sentimos, no se puede retroceder el odometro")
        else:
            self.odometro_tablero += kilometros


class Bateria:  # Definimos una nueva clase: Bateria, que no hereda de ninguna otra clase
    """Un simple intento de modelar una bateria para un auto electrico."""
    def __init__(self, tamaño=75):  # tamaño es un parametro opcional que pone el tamaño de la bateria en 75.
        """Inicializa los atributos de la clase Bateria"""
        self.tamaño = tamaño

    def describir_bateria(self):  # Se crea el metodo para describir la bateria.
        """Se imprime una oracion que describa el tamaño de la bateria"""
        print(f"Este auto tiene una bateria de {self.tamaño} kWh")

    def actualizar_bateria(self):
        if self.tamaño != 100:
            self.tamaño = 100
            print(f"La capacidad de la bateria ha sido actualizada. Ahora esta en {self.tamaño} kWH")
        else:
            print("La capacidad de la bateria está en el estado correcto.")

    def obtener_rango(self):
        """Imprime una declaracion sobre el rango que proporciona la bateria"""
        if self.tamaño >= 50 and self.tamaño <=75:
            rango = 260
        elif self.tamaño < 50:
            rango = 100
        elif self.tamaño == 100:
            rango = 315

        print(f"Este auto puede recorrer hasta {rango} kilometros con esta carga.")


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


mi_auto_electrico = CarroElectrico("Tesla", "V-5000", 2022)
print(mi_auto_electrico.nombre_descriptivo())
mi_auto_electrico.bateria.tamaño = 35
mi_auto_electrico.bateria.obtener_rango()
mi_auto_electrico.bateria.actualizar_bateria()
mi_auto_electrico.bateria.obtener_rango()

