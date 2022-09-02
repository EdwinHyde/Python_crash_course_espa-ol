import pygame as pg
from pygame.sprite import Sprite

class Disparos(Sprite):
    """Clase para administrar los disparos de a nave"""
    def __init__(self, juego):
        """Crea un objeto de tipo disparo en la posicion actual de la nave"""
        super().__init__()
        self.pantalla = juego.pantalla
        self.ajustes = juego.ajustes
        self.color = self.ajustes.disparo_color

        # Crea figura del disparo.
        self.rect = pg.Rect(0, 0, self.ajustes.disparo_ancho, self.ajustes.disparo_altura)
        self.rect.midright = juego.nave.rectangulo_nave.midright
        self.x = float(self.rect.x)  # Se almacena en valor decimal a coordenada x


    def update(self):
        """Mueve los disparos por la pantalla"""
        self.x += self.ajustes.velocidad_balas  # actualiza la posicion decimal del disparo
        self.rect.x = self.x


    def pintar_disparos(self):
        """Dibuja los disparos en la pantalla"""
        pg.draw.rect(self.pantalla, self.color, self.rect )