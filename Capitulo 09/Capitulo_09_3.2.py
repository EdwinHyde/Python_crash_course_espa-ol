# INSTANCIAS COMO ATRIBUTOS

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


tesla = CarroElectrico('tesla', 'modelo s', 2019)
print(tesla.nombre_descriptivo())
tesla.bateria.describir_bateria()  # Se crea un auto electrico y se asigna a la variable tesla
# Cuando queremos describir la bateria, necesitamos trabajar con el atributo de la bateria del carro.
tesla.bateria.obtener_rango()
tesla.bateria.tamaño = 100
tesla.bateria.obtener_rango()
