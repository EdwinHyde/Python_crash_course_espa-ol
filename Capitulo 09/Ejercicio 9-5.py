# 9-5. Login Attempts:
#       Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
#       Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
#       Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
#       Make an instance of the User class and call increment_login_attempts() several times.
#       Print the value of login_attempts to make sure it was incremented properly,
#       and then call reset_login_attempts().
#       Print login_attempts again to make sure it was reset to 0.

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


docente = Usuario("edwin", "chica", "palocabildo", "3164426962", "docente")
docente.describir_usuario()
docente.saludar_usuario()
docente.incremento_intentos_login()
docente.incremento_intentos_login()
docente.incremento_intentos_login()
docente.incremento_intentos_login()
docente.incremento_intentos_login()
docente.incremento_intentos_login()

docente.reset_intentos_login()
docente.incremento_intentos_login()
