# 9-2. Three Restaurants:
# Start with your class from Exercise 9-1.
# Create three different instances from the class,
# and call describe_restaurant() for each instance.

class Restaurante:
    """Se mostrará la descripcion de un restaurante, tipo de cocina y ubicacion. """
    def __init__(self, nombre_restaurante, tipo_cocina, ubicacion):
        """Se inicializan los atributos"""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.ubicacion = ubicacion

    def descripcion_restaurante(self):
        """Se describe el lugar"""
        print(f"\nEl restaurante {self.nombre_restaurante.title()} se encuentra ubicado en {self.ubicacion.title()}")
        print(f"Ademas, el restaurante ofrece el tipo de cocina: {self.tipo_cocina}")

    def abrir_restaurante(self):
        """Se hace la simulacion que el lugar esta abierto"""
        print(f"El restaurante {self.nombre_restaurante.title()} está abierto en este momento.")


don_pedro = Restaurante("don pedro", "tipica colombiana", "ibague")
don_pedro.descripcion_restaurante()

combo = Restaurante("el combo", "carne de búfalo.", "la dorada")
combo.descripcion_restaurante()

barbas = Restaurante("barbas shots", "comidas rapidas", "villahermosa")
barbas.descripcion_restaurante()
