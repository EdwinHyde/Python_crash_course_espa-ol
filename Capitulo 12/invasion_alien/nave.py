import pygame

class Nave:
    """Una clase para administrar a nave"""
    def __init__(self, juego_ia):
        """Inicializa la nave y establece su posicion inicial."""
        self.pantalla = juego_ia.pantalla
        self.configuracion = juego_ia.configuracion
        self.rectangulo_pantalla = juego_ia.pantalla.get_rect()  # rect = rectangulo.

        # Cargar la imagen y obtener su rectangulo.
        self.imagen = pygame.image.load("images/nave.png")
        self.rectangulo = self.imagen.get_rect()

        # Centrar la nave en la parte baja de la pantalla.
        self.rectangulo.midbottom = self.rectangulo_pantalla.midbottom

        self.x = float(self.rectangulo.x)  # Modificamos el eje x para que reciba valores flotantes.

        # BANDERAS PARA EL MOVIMIENTO DE LA NAVE.
        self.mov_derecha = False
        self.mov_izquierda = False

    def mover_nave(self):
        """Metodo para mover la nave hacia derecha e izquierda."""
        if self.mov_derecha and self.rectangulo.right < self.rectangulo_pantalla.right:
            # Si mov_derecha y rectangulo de la derecha son menores que que el rectangulo de la pantalla a la derecha ->
            self.x += self.configuracion.velocidad_nave  # El rectangulo de la nave se mueve hacia la derecha y llegará
            # hasta el limite de la pantalla sin salir de los bordes
        if self.mov_izquierda and self.rectangulo.left > 0:
            self.x -= self.configuracion.velocidad_nave

        # Actualiza el objeto rectangulo desde self.x
        self.rectangulo.x = self.x

    def blitme(self):
        """Dibuja la nave en la posicion establecida"""
        self.pantalla.blit(self.imagen, self.rectangulo)