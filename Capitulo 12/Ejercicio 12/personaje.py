# 12-2. Game Character: Find a bitmap image of a game character you like or convert an image to a bitmap.
# Make a class that draws the character at the center of the screen and match the background color of the image
# to the background color of the screen, or vice versa
import pygame.image


class Personaje:
    """Esta clase administra los recursos y configuracion del personaje."""
    def __init__(self, sky):
        """Inicializa el personaje y determina su ubicacion"""
        self.pantalla = sky.pantalla
        self.rectangulo_pantalla = sky.pantalla.get_rect()
        self.imagen = pygame.image.load("imagenes/vamp.png")  # Cargar la imagen
        self.rectangulo_imagen = self.imagen.get_rect()
        self.rectangulo_imagen.midleft = self.rectangulo_pantalla.midleft

    def blit(self):
        """Dibuja el personaje en la posicion establecida"""
        self.pantalla.blit(self.imagen, self.rectangulo_imagen)

