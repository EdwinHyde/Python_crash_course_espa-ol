import pygame

class Configuracion:
    """Esta clase administra la configuracion del juego"""
    def __init__(self):
        """Inicializa los atributos de la configuracion"""
        # PANTALLA
        self.tamaño_pantalla = (800, 600)
        self.background = (167, 230, 230)

        # VELOCIDAD DE LA NAVE
        self.velocidad = 2.0
