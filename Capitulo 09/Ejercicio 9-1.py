# 9-1. Restaurant:
#       Make a class called Restaurant. The __init__() method for # Restaurant should store two attributes:
#           a restaurant_name and a cuisine_type.
#       Make a method called describe_restaurant() that prints these two pieces of information,
#       and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#       Make an instance called restaurant from your class.
#       Print the two attributes individually, and then call both methods.

class Restaurante:
    """Se mostrará la descripcion de un restaurante, tipo de cocina y ubicacion. """
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def descripcion_restaurante(self):
        """Se describe el lugar"""
        print(f"El restaurante {self.nombre_restaurante.title()} se encuentra ubicado en Ibagué")
        print(f"Ademas, nuestro restaurante ofrece el tipo de cocina {self.tipo_cocina}")

    def abrir_restaurante(self):
        """Se hace la simulacion que el lugar esta abierto"""
        print(f"El restaurante {self.nombre_restaurante.title()} está abierto en este momento.")


restaurante01 = Restaurante("don pedro", "tipica colombiana")
print(f'El restaurante se llama {restaurante01.nombre_restaurante.title()}')
print(f'El restaurante ofrece el tipo de cocina {restaurante01.tipo_cocina}')
restaurante01.descripcion_restaurante()
restaurante01.abrir_restaurante()
