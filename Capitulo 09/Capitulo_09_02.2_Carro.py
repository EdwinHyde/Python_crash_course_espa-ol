# Modificando los valores de un atributo.

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
        Rechazar el cambio si se intenta retroceder el odometro
        """
        # Con el condicional nos aseguramos de que nadie intente hacer retroceder la lectura del odómetro
        if kilometraje >= self.odometro_tablero:
            self.odometro_tablero = kilometraje
        else:
            print("No es posible retroceder el odometro")

carro_nuevo = Carro('audi', 'a4', 2019)
print(carro_nuevo.nombre_descriptivo())

carro_nuevo.actualizar_odometro(23)  # Se llama al metodo actualizar_odometro() y se asigna 23 como argumento
# Esto pone el tablero odometro a 23
carro_nuevo.leer_odometro()  # Imprime la lectura

# Usamos notacion de punto para acceder al atributo y poner el valor directamente.
# carro_nuevo.odometro_tablero = 23
# carro_nuevo.leer_odometro()