class Configuracion:
    """Una clase para almacenar las configuraciones del juego Invasion Alien"""
    def __init__(self):
        """Inicia la configuracion del juego"""
        # ----- CONFIGURACION DE PANTALLA -----.
        self.ancho_ventana = 1200
        self.alto_ventana = 700
        self.color_de_fondo = (250, 250, 250)

        # CONFIGURACION DE LA NAVE.
        self.velocidad = 1.5  # Establecemos la velocidad a la que se movera el rectangulo de la imagen.
        #  Se usa un valor decimal para tener un control mas preciso de la velocidad de la nave, sin embargo algunos
        # atributos como "rect" y "x" almacenan enteros, por cual se modifica el modulo nave.
        self.limite_naves = 3

        # CONFIGURACION DE LOS DISPAROS
        self.velocidad_balas = 1.8  # Las balas se moveran un poco mas lento que la nave
        self.ancho_balas = 5  # 3 pixeles de ancho
        self.altura_balas = 15  # 15 pixeles de alto
        self.color_balas = (60, 60, 60)  # El color de las balas será gris oscuro.
        self.balas_permitidas = 3  # balas permitidas al tiempo

        # CONFIGURACION DE LAS NAVES ALIEN
        self.velocidad_aliens = 1.0
        self.velocidad_caida_aliens = 100 # Controla que tan rapido cae la flota cada vez que que una nave alien alcanza
        # cualquiera de los bordes de la pantalla, es util ajustar ambas velocidades de forma independiente (vertical y
        # horizontal)

        # Direccion de la flota: 1 representa hacia la derecha, -1 hacia la izquierda
        self.direccion_flota_alien = 1




