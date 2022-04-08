# 9-7. Admin:
#       An administrator is a special kind of user.
#       Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
#       or Exercise 9-5 (page 167).
#       Add an attribute, privileges, that stores a list of strings like "can add post",
#       "can delete post", "can ban user", and so on.
#       Write a method called show_privileges() that lists the administrator’s set of privileges.
#       Create an instance of Admin, and call your method.

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


class Admin(Usuario):
    """Se crea la clas secundaria"""
    def __init__(self, nombres, apellidos, residencia, telefono, ocupacion):
        """Se inicializan los atributos de la clase principal"""
        super().__init__(nombres, apellidos, residencia, telefono, ocupacion)
        self.privilegios = ["puede postear", "puede eliminar post", "puede banear usuarios",
                            "puede tomar cerveza", "puede bloquear usuarios"]

    def mostrar_privilegios(self):
        """Muestra en pantalla los privilegios del administador."""
        print("\nEl administrador creado tiene los siguientes privilegios: ")
        for privilegio in self.privilegios:  # Creamos un bucle que recorra la lista creada en el atributo
            # privilegios.
            print(f"* {privilegio.title()}")


yo_administrador = Admin("edwin", "chica", "palocabildo", "321321321", "magister")
yo_administrador.describir_usuario()
yo_administrador.mostrar_privilegios()
