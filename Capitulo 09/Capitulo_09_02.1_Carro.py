# Poniendo valores predeterminados para un atributo.

class Carro:
    '''Un intento simple de representar un carro.'''
    def __init__(self, fabricante, modelo, año):
        """Inicializa los traibutos para describir un carro"""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.odometro_tablero = 0  # Python crea un nuevo atributo (odometro_tablero) e inicia su valor en 0

    def nombre_descriptivo(self):
        '''Retorna un nombre descriptivo en un formato ordenado'''
        nombre_largo = f'{self.año} {self.fabricante} {self.modelo}'
        return nombre_largo

    def leer_odometro(self):  # Creamos un metodo nuevo llamado leer_odometro() que leerá el kilometraje del carro.
        """Imprime un enunciado mostrando el kilometraje del carro"""
        print(f"Este carro tiene {self.odometro_tablero} kilómetros recorridos.")

carro_nuevo = Carro('audi', 'a4', 2019)
print(carro_nuevo.nombre_descriptivo())
carro_nuevo.leer_odometro()