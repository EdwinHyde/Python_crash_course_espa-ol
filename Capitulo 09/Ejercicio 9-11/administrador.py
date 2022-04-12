# 9-11. Imported Admin:
#           Start with your work from Exercise 9-8 (page 173).
#           Store the classes User, Privileges, and Admin in one module.
#           Create a separate file, make an Admin instance, and call show_privileges() to show that
#           everything is working correctly.

"""Almacenando las clases usuario y administrador en un modulo."""
class Usuario:
    def __init__(self, nombres, apellidos, residencia, telefono, ocupacion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.residencia = residencia
        self.telefono = telefono
        self.ocupacion = ocupacion
        self.intentos_login = 0

    def describir_usuario(self):
        """Se crea un resumen con la informacion del usuario."""
        print('\nSe presenta a continuacion la informacion del usuario: ')
        print(f'Nombres: {self.nombres.title()}')
        print(f'Apellidos: {self.apellidos.title()}')
        print(f'Residencia: {self.residencia.title()}')
        print(f'Teléfono: {self.telefono}')
        print(f'Ocupación: {self.ocupacion.title()}')

    def saludar_usuario(self):
        print(f'Hola {self.nombres.title()} {self.apellidos.title()} es una alegría inmensa tenerte en nuestro sitio')
        print('Bienvenido(a) a nuestra empresa.')

    def incremento_intentos_login(self):
        self.intentos_login += 1
        print(f"Llevas {self.intentos_login} intentos de hacer login")

    def reset_intentos_login(self):
        """Resetea los intentos de login a cero"""
        self.intentos_login = 0
        print(f"El valor de los intentos de login se ha reseteado correctamente. Tienes {self.intentos_login}"
              f" intentos de login.")


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