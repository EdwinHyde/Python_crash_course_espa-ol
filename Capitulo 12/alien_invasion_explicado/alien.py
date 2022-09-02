import pygame
from pygame.sprite import Sprite

class NaveAlien(Sprite):
    """Esta clase representa una nave alien de la flota alienigena"""
    def __init__(self, ai_juego):
        """Inicia los atributos de la nave alien y establece su posicion"""
        super().__init__()
        self.pantalla = ai_juego.pantalla
        self.configuracion = ai_juego.configuracion  # Creamos un parametro de configuracion. Cada vez que actualizamos
        # la posicion de una nave alien, movemos hacia la derecha la cantidad almacenada en velocidad_aliens

        # Cargar la imagen de la nave alien y definir su atributo rectangulo
        self.image = pygame.image.load('images/alien.png')  # self.image debe quedarse asi, no con otro nombre
        self.rect = self.image.get_rect()  # No se puede renombrar este atributo en el modulo. Debe ser siempre rect

        # Iniciar cada nueva nave cerca a la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenar la posicion horizontal exacta de la nave alien
        self.x = float(self.rect.x)

    def revisar_bordes(self):
        """Retorna True si la nave alien esta en el borde de la pantalla"""
        pantalla_rect = self.pantalla.get_rect()
        # La nave alien esta en el borde derecho si el atributo de su rectangulo es mayor o igual que el atributo
        # derecho del rectangulo de la pantalla. Está al borde izquierdo si el valor izquierdo es menor o igual a 0
        if self.rect.right >= pantalla_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Mueve las naves alien hacia la derecha"""
        # Si la direccion de la flota es 1, el valor de la velocidad de la nave alien sera agregada a la actual posicion
        # de la nave alien, moviendo la nave alien hacia la derecha; si la direccion es -1, el valor sera restado
        # de la posicion de la nave alien moviendola hacia la izquierda
        self.x += (self.configuracion.velocidad_aliens * self.configuracion.direccion_flota_alien)
        # Rastreamos la posicion exacta con el atributo self.x, la cual puede guardar valores decimales
        self.rect.x = self.x  # y usamos el valor de self.x para actualizar la posicion del rectangulo de la nave alien.

