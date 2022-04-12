# Este modulo trabaja en conjunto con el modulo mi_auto_electrico_02.py y mis_autos02
# Se ha actualizado la clase y solamente tiene la clase Carro.

class Carro:
    """Un intento simple de representar un carro."""
    def __init__(self, fabricante, modelo, año):
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.odometro_tablero = 0

    def nombre_descriptivo(self):
        nombre_largo = f'{self.fabricante} {self.modelo} {self.año}'
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