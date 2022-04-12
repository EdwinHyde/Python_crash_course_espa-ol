# 9-12. Multiple Modules:
#           Store the User class in one module, and store the Privileges and Admin classes in a separate module.
#           In a separate file, create an Admin instance and call show_privileges() to show that everything is still
#           working correctly.

"""Almacenando la clase Usuario en modulo actual."""

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