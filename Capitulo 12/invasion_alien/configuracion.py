class Configuracion:
    """Una clase para almacenar todas las configuraciones del juego Invasion Alien"""
    def __init__(self):
        """Inicializa las configuraciones del juego"""
        # CONFIGURACIONES DE LA PANTALLA
        self.dimensiones_pantalla = (1200, 700)  # Ancho y alto de la pantalla
        self.fondo_de_pantalla = (42, 49, 50)  # Color de fondo en valores RGB

        # CONFIGURACION DE LA NAVE.
        self.velocidad_nave = 1.5