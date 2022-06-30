# 11-3. Employee:
# Write a class called Employee.
# The __init__() method should take in a first name, a last name, and an annual salary,
# and store each of these as attributes.
# Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts
# a different raise amount.

class Empleado:

    def __init__(self, nombres, apellidos, salario_anual):
        """Almacena nombres, apellidos y sueldo anual"""
        self.nombres = nombres
        self.apellidos = apellidos
        self.salario_anual = salario_anual

    def dar_aumento(self, aumento=5000):
        """Hace un aumento de 5000 u otra cantidad"""
        self.salario_anual += aumento
