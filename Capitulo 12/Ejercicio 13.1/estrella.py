import pygame
from pygame.sprite import Sprite

class Estrella(Sprite):
    """Clase para crear y administrar estrellas en una cuadricula"""
    def __init__(self, juego):
        """Inicia las estrellas y las ubica en su posicion correcta"""
        super().__init__()
        self.ventana = juego.ventana
        # Cargar imagen de estrella
        self.image = pygame.image.load("imagenes/estrella_peque.png")
        self.rect = self.image.get_rect()

        # Ubicar estrella parte superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


