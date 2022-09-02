import pygame

class Ship:
    """Clase para administrar las funciones de la nave"""
    def __init__(self, juego):
        """Inicializa los atributos de la nave"""
        self.pantalla = juego.pantalla
        self.configuracion = juego.configuracion
        self.rectangulo_pantalla = juego.pantalla.get_rect()

        # Cargar la imagen y establecer posicion
        self.img = pygame.image.load("imagenes/Recurso 8.png")
        self.rectangulo_img = self.img.get_rect()

        # Centrar la nave
        self.rectangulo_img.midbottom = self.rectangulo_pantalla.midbottom

        # Velocidad de la nave
        self.x = float(self.rectangulo_img.x)
        self.y = float(self.rectangulo_img.y)

        # BANDERAS PARA MOVER LA NAVE
        self.mov_derecha = False
        self.mov_izquierda = False
        self.mov_arriba = False
        self.mov_abajo = False

    def mover_nave(self):
        """Permite mover la nave hacia la derecha, izquierda, arriba y abajo"""
        # Mover nave y que no s salga de los bordes de la pantalla.
        if self.mov_derecha and self.rectangulo_img.right < self.rectangulo_pantalla.right:
            self.x += self.configuracion.velocidad
        if self.mov_izquierda and self.rectangulo_img.left > 0:
            self.x -= self.configuracion.velocidad
        if self.mov_arriba and self.rectangulo_img.top > 0:
            self.y -= self.configuracion.velocidad
        if self.mov_abajo and self.rectangulo_img.bottom < self.rectangulo_pantalla.bottom:
            self.y += self.configuracion.velocidad


        self.rectangulo_img.x = self.x
        self.rectangulo_img.y = self.y

    def dibujar_nave(self):
        """Dibuja la nave en la posicion establecida"""
        self.pantalla.blit(self.img, self.rectangulo_img)
