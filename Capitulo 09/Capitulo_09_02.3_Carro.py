# INCREMENTANDO EL VALOR DE UN ATRIBUTO A TRAVES DE UN METODO.

class Carro:
    '''Un intento simple de representar un carro.'''
    def __init__(self, fabricante, modelo, año):
        """Inicializa los traibutos para describir un carro"""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.odometro_tablero = 0

    def nombre_descriptivo(self):
        '''Retorna un nombre descriptivo en un formato ordenado'''
        nombre_largo = f'{self.año} {self.fabricante} {self.modelo}'
        return nombre_largo

    def leer_odometro(self):
        """Imprime un enunciado mostrando el kilometraje del carro"""
        print(f"Este carro tiene {self.odometro_tablero} kilómetros recorridos.")

    # Modificando el valor del atributo a traves de un metodo.
    def actualizar_odometro(self, kilometraje):
        """
        Poner el tablero del odometro al valor proporcionado.
        Rechazar el cambio si se intenta retroceder el odometro        """

        if kilometraje >= self.odometro_tablero:
            self.odometro_tablero = kilometraje
        else:
            print("No es posible retroceder el odometro")

    def incrementar_odometro(self, kilometros):
        # Este nuevo metodo toma un numero de kms, y agrega ese valor a la variable odometro_tablero.
        # and adds this value to self.odometer_reading
        """Agrega la cantidad dada a odometro tablero"""
        if kilometros < 0:
            print("Lo sentimos, no se puede retroceder el odometro")
        else:
            self.odometro_tablero += kilometros

carro_usado = Carro('audi', 'a4', 2019)
print(carro_usado.nombre_descriptivo())

carro_usado.actualizar_odometro(23_500)  # Se pone en 23.500 el odometro llamando al metodo y pasando el valor
carro_usado.leer_odometro()

carro_usado.incrementar_odometro(-300)  # Se llama el metodo incrementar_odometro y se pide que agregue 100 km
carro_usado.leer_odometro()