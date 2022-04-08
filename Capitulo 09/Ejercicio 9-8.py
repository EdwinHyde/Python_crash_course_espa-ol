# 9-8. Privileges:
#       Write a separate Privileges class.
#       The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
#       Move the show_privileges() method to this class.
#       Make a Privileges instance as an attribute in the Admin class.
#       Create a new instance of Admin and use your method to show its privileges.

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
    def __init__(self, privilegios=["puede postear", "puede eliminar post", "puede banear usuarios",
                            "puede tomar cerveza", "puede bloquear usuarios"]):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        """Muestra en pantalla los privilegios del administador."""
        print("\nEl administrador creado tiene los siguientes privilegios: ")
        for privilegio in self.privilegios:
            print(f"* {privilegio.title()}")


class Admin(Usuario):
    """Se crea la clas secundaria"""
    def __init__(self, nombres, apellidos, residencia, telefono, ocupacion):
        """Se inicializan los atributos de la clase principal"""
        super().__init__(nombres, apellidos, residencia, telefono, ocupacion)
        self.privilegios = Privilegios()


el_administrador = Admin("edwin", "chica", "casabianca", "32112312312", "músico")
el_administrador.describir_usuario()
el_administrador.privilegios.mostrar_privilegios()