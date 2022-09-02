class Ajustes:
    """Clase que configura diferentes caracteristicas del juego."""
    def __init__(self):
        """Inicializa los atributos de los ajustes"""
        self.tamaño_pantalla = (800, 600)
        self.fondo_pantalla = (143, 175, 197)

        # CONFIGURACION DE LA NAVE
        self.velocidad_nave = 1.5

        # CONFIGURACION DE DISPAROS.
        self.velocidad_balas = 3.0
        self.disparo_ancho = 12
        self.disparo_altura = 3
        self.disparo_color = (118, 55, 37)
        self.disparos_permitidos = 3

        # CONFIGURACION NAVE ENEMIGA
        # La frecuencia de la nave enemiga  controla que tan seguido aparece una nueva nave enemiga
        self.frecuencia_nave_enemiga = 0.008
        self.velocidad_nave_enemiga = 1.5



        
