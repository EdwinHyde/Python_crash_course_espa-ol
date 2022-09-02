import pygame as pg

class Nave:
    """Clase que sirve para controlar la nave y su configuracion"""
    def __init__(self, juego):
        """Inicializa los atributos de la clase nave"""
        self.pantalla = juego.pantalla
        self.ajustes = juego.ajustes
        self.rectangulo = juego.pantalla.get_rect()

        self.imagen = pg.image.load("img/nave.png")  # Ruta de la imagen
        self.rectangulo_nave = self.imagen.get_rect()  # Crea rectangulo de la imagen
        self.rectangulo_nave.midleft = self.rectangulo.midleft

        # MOVER LA NAVE.
        # Flags
        self.y = float(self.rectangulo_nave.y)
        self.mover_arriba = False
        self.mover_abajo = False

    def mover_nave(self):
        """Controla los movimientos de la nave: arriba y abajo"""
        if self.mover_arriba and self.rectangulo_nave.top > 0:
            self.y -= self.ajustes.velocidad_nave
        if self.mover_abajo and self.rectangulo_nave.bottom < self.rectangulo.bottom:
            self.y += self.ajustes.velocidad_nave

        self.rectangulo_nave.y = self.y

    def dibujar_nave(self):
        """Muestra la imagen de la nave en la pantalla"""
        self.pantalla.blit(self.imagen, self.rectangulo_nave)
