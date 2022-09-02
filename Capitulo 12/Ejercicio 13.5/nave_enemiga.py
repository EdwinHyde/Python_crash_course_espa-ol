from random import randint

import pygame
from pygame.sprite import Sprite

class NaveEnemiga(Sprite):
    """Una clase que representa  a una anve enemiga en toda la flota"""
    def __init__(self, juego):
        """Inicializa los atributos de la nave enemiga y establece su posicion inicial"""
        super().__init__()
        self.pantalla = juego.pantalla
        self.ajustes = juego.ajustes

        # Cargar la imagen
        self.image = pygame.image.load("img/nave_enemiga.png")
        self.rect = self.image.get_rect()

        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height

        # Hacer que se ubique la nave enemiga en la esquina superior derecha.
        self.rect.left = self.pantalla.get_rect().right
        alto_maximo_nave_enemiga = self.ajustes.tamaño_pantalla - self.rect.height
        self.rect.top = randint(0, alto_maximo_nave_enemiga)

        self.x = float(self.rect.x)

    def update(self):
        """Mover las naves enemigas constantemente hacia la izquierda"""
        self.x -= self.ajustes.velocidad_nave_enemiga
        self.rect.x = self.x