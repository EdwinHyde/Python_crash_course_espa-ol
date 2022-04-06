# DEFINIENDO ATRIBUTOS Y METODOS PARA LA CLASE HIJA.

class Carro:
    '''Un intento simple de representar un carro.'''
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

class CarroElectrico(Carro):
    '''Representa aspectos de un carro, especificamente de uno electrico'''

    def __init__(self, fabricante, modelo, año):
        """
        Se inicializan los atributos de la clase padre,
        luego se inicializan los atributos para un carro electrico.
        """
        super().__init__(fabricante, modelo, año)
        self.tamaño_bateria = 75  # Este atributo es exclusivo de la clase CarroElectrico

    def describir_bateria(self):  # Metodo exclusivo de la clase CarroElectrico.
        """Imprime un mensaje sobre la descrpicion de la bateria"""
        print(f'Este auto tiene una batería de {self.tamaño_bateria} kWH.')

    def tanquear_gasolina(self):
        '''Los autos electricos no necesitan gasolina'''
        print("Este auto no necesita un tanque de gasolina... Es eléctrico.")

tesla = CarroElectrico('tesla', 'modelo s', 2019)
print(tesla.nombre_descriptivo())
tesla.describir_bateria()