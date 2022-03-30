# 9-3. Users:
# Make a class called User. Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class Usuario:
    def __init__(self, nombres, apellidos, residencia, telefono, ocupacion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.residencia = residencia
        self.telefono = telefono
        self.ocupacion = ocupacion

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


docente = Usuario("edwin", "chica", "palocabildo", "3164426962", "estudiante")
docente.describir_usuario()
docente.saludar_usuario()

directivo = Usuario("rodrigo", "marin", "casabianca", "3123234567", "rector")
directivo.describir_usuario()
directivo.saludar_usuario()

estudiante = Usuario("juliana", "villegas", "llanadas", "3142345764", "estudiante")
estudiante.describir_usuario()
estudiante.saludar_usuario()
