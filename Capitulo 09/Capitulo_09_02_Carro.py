# Vamos a escribir una clase que represente un carro.
# Almacenará informacion sobre el tipo de carro con que estamos trabajando.
# Tendrá un metodo que resuma la informacion.

class Carro:
    '''Un intento simple de representar un carro.'''

    def __init__(self, fabricante, modelo, año):  # Definimos el metodo de inicio junto a tres parametros.
        # El metodo __init__() toma los 3 parametros y los asigna a los atributos que se asociaran
        # con las instancias creadas desde esta clase.
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año

    def nombre_descriptivo(self):
        #  Definimos un metodo llamado nombre_descriptivo() que pone el fabricante, modelo y año
        #  del carro. Esto evitará tener que imprimir el valor de cada atributo individualmente.
        '''Retorna un nombre descriptivo en un formato ordenado'''
        nombre_largo = f'{self.año} {self.fabricante} {self.modelo}'
        return nombre_largo

carro_nuevo = Carro('audi', 'a4', 2019)  # Creamos una instancia desde la clase Carro y se asigna a la variable
# carro_nuevo
print(carro_nuevo.nombre_descriptivo())  # Se llama el metodo nombre_descriptivo() para mostrar el carro.
# En este caso se debe enviar "print", pues el metodo solo retorna el valor, mas no lo imprime.