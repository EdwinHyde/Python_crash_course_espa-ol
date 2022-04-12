# 9-10. Imported Restaurant:
#           Using your latest Restaurant class, store it in a module.
#           Make a separate file that imports Restaurant.
#           Make a Restaurant instance, and call one of Restaurant’s methods
#           to show that the import statement is working properly.

class Restaurante:
    """Se mostrará la descripcion de un restaurante, tipo de cocina y ubicacion. """
    def __init__(self, nombre_restaurante, tipo_cocina, ubicacion):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.ubicacion = ubicacion
        self.numero_servido = 0

    def descripcion_restaurante(self):
        """Se describe el lugar"""
        print(f"El restaurante {self.nombre_restaurante.title()} se encuentra ubicado en {self.ubicacion.title()}")
        print(f"Ademas, nuestro restaurante ofrece el tipo de cocina {self.tipo_cocina}")

    def abrir_restaurante(self):
        """Se hace la simulacion que el lugar esta abierto"""
        print(f"El restaurante {self.nombre_restaurante.title()} está abierto en este momento.")

    def poner_numero_servido(self, consumidores):
        """Se modifica la cantidad de mesas servidas"""
        self.numero_servido = consumidores

    def incrementar_numero_servido(self, incremento):
        """Incrementar a traves de un metodo el numero de clientes servidos"""
        self.numero_servido += incremento
