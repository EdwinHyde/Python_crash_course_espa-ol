# 9-12. Multiple Modules:
#           Store the User class in one module, and store the Privileges and Admin classes in a separate module.
#           In a separate file, create an Admin instance and call show_privileges() to show that everything is still
#           working correctly.

"""Almacenando las clases Privilegios y Admin en modulo separado"""

from modulos1 import Usuario


class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        """Muestra en pantalla los privilegios del administador."""
        print("\nEl administrador creado tiene los siguientes privilegios: ")
        for privilegio in self.privilegios:
            print(f"* {privilegio.title()}")


class Admin(Usuario):
    """Se crea la clas secundaria"""
    def __init__(self, nombres, apellidos, residencia, telefono, ocupacion, privilegios):
        """Se inicializan los atributos de la clase principal"""
        super().__init__(nombres, apellidos, residencia, telefono, ocupacion)
        self.privilegios = Privilegios(privilegios)

