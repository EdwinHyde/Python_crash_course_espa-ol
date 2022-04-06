# HERENCIA.
# Tomamos la clase Carro de los ejercicios anteriores.
# Cuando se crea una clase hija, la clase padre tiene que ser parte del archivo actual.
# y debe aparecer antes de la clase hija en el archivo

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


class CarroElectrico(Carro):
    """Se define la clase hija, CarroElectrico.
    El nombre de la clase padre debe ir entre parentesis en la definicion de la clase hija."""

    def __init__(self, fabricante, modelo, año):  # El metodo constructor toma la informacion requerida
        # para crear una instancia de Carro.
        """Se inicializan los atributos de la clase padre"""
        super().__init__(fabricante, modelo, año)
        # La funcion super() es una funcion especial que permite llamar un metodo desde la padre clase.
        # Esto le dice a python que llame el metodo __init__ desde Carro, lo cual le da a una instancia de
        # CarroElectrico todos los atributos definidos en este metodo.
        # El nombre super proviene de una convención de llamar a la clase principal
        # una superclase y a la clase secundaria una subclase.


tesla = CarroElectrico('tesla', 'modelo s', 2019)
# Se crea una instancia de CarroElectrico y esta llama el metodo constructor definido en CarroElectrico
# la cual a su vez llama al metodo contructor de la clase padre Carro. Se proporcionan los argumentos
# tesla, modelo s, 2019. Aun no hay metodos particulares de CarroElectrico, solo comportamientos de Carro.
print(tesla.nombre_descriptivo())
