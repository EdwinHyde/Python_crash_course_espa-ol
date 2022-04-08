# 9-6. Ice Cream Stand:
#       An ice cream stand is a specific kind of restaurant.
#       Write a class called IceCreamStand that inherits from the Restaurant class you wrote
#       in Exercise 9-1 (page 162) or Exercise 9-4 (page 167).
#       Either version of the class will work; just pick the one you like better.
#       Add an attribute called flavors that stores a list of ice cream flavors.
#       Write a method that displays these flavors.
#       Create an instance of IceCreamStand, and call this method.

class Restaurante:
    """Se mostrará la descripcion de un restaurante, tipo de cocina y ubicacion. """
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0

    def descripcion_restaurante(self):
        """Se describe el lugar"""
        print(f"El restaurante {self.nombre_restaurante.title()} se encuentra ubicado en Ibagué")
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

class PuestoDeHelados(Restaurante):
    """Se define la clase secundaria"""
    def __init__(self, nombre_restaurante, tipo_cocina):
        """Se inicializan los atributos de la clase principal"""
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = ["vainilla", "chocolate", "frutos rojos", "limón"]

    def mostrar_sabores(self):
        """Muestra los sabores en pantalla"""
        print("\nNuestra heladeria le ofrece los siguientes sabores: ")
        for self.sabor in self.sabores:
            print(self.sabor.title())



puesto01 = PuestoDeHelados("mr frio", "heladeria")
puesto01.descripcion_restaurante()
puesto01.mostrar_sabores()