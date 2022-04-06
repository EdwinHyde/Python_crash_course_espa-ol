# 9-4. Number Served:
#       Start with your program from Exercise 9-1 (page 162).
#       Add an attribute called number_served with a default value of 0.
#       Create an instance called restaurant from this class.
#       Print the number of customers the restaurant has served, and then change this value and print it again.
#       Add a method called set_number_served() that lets you set the number of customers that have been served.
#       Call this method with a new number and print the value again.
#       Add a method called increment_number_served() that lets you increment the number of customers
#       who’ve been served.
#       Call this method with any number you like that could represent how many customers were served in, say, a
#       day of business.

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

restaurante = Restaurante("mamma mia", "italiana")
restaurante.descripcion_restaurante()
restaurante.abrir_restaurante()
print(f"Actualmente el restaurante tiene {restaurante.numero_servido} mesas servidas.")

restaurante.numero_servido = 5
print(f"Actualmente el restaurante tiene {restaurante.numero_servido} mesas servidas.")

restaurante.poner_numero_servido(10)
print(f"Actualmente el restaurante tiene {restaurante.numero_servido} mesas servidas.")

restaurante.incrementar_numero_servido(5)
print(f"En el dia de hoy sabado fueron servidos {restaurante.numero_servido} clientes")
