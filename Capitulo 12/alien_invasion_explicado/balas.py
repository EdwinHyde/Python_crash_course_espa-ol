import pygame
from pygame.sprite import Sprite

class Balas(Sprite): # La clase hereda desde Sprite, la cual es importada. Esto permite agrupar elementos relacionados
    # en el juego y actuar en todos los elementos agrupados a la vez.
    """Una clase que maneja las balas disparadas por la nave"""
    def __init__(self, ai_juego):
        """Crea un objeto de tipo Bala en la posicion actual de la nave"""
        super().__init__()  # Para heredar correctamente es necesario llamar el metodo super()

        # Se crean los atributos y objetos de pantalla y configuracion, asi como el color de la bala
        self.pantalla = ai_juego.pantalla
        self.configuracion = ai_juego.configuracion
        self.color = self.configuracion.color_balas

        # Crear un rectangulo para la bala en la posicion (0, 0) y luego la pone en la posicion correcta.
        # Se crea un atributo rectangulo para la bala, este no esta basado en una imagen, asi que se crea desde cero
        # usando la clase pygame.Rect(). Esta clase requiere las coordenadas x & y desde la esquina superior izquierda
        # y el ancho y alto del rectangulo, los cuales inicializan en (0, 0) pero deben ser movidos porque su posicion
        # depende de la posicion de la nave. Estos valores los obtenemos desde los valores almacenados en configuracion.
        self.rect = pygame.Rect(0, 0, self.configuracion.ancho_balas, self.configuracion.altura_balas)

        # hacemos que coincida el atributo midtop del rectangulo con el atributo de la nave.
        # Esto hace que las balas salgan de la parte alta de la nave como si fueran disparadas por ella.
        self.rect.midtop = ai_juego.nave.rect.midtop

        # Almacenar la posicion de las balas como un valor decimal.
        self.y = float(self.rect.y)

    def update(self):  # Este debe ser el nombre del metodo, de lo contrario no funcionará.
        # Este metodo, maneja la posicion de las balas, cuando se dispara una, esta se mueve hacia arriba, lo que
        # corresponde a disminuir el valor de las coordenadas en Y. Para actualizar la posicion, restamos la cantidad
        # almacenada en configuracion.velocidad_balas menos self.y
        """Mueve las balas por la pantalla"""
        # actualizar la posicion decimal de la bala
        self.y -= self.configuracion.velocidad_balas
        # actualizar la posicion del rectangulo
        self.rect.y = self.y

    def dibujar_balas(self):
        # Cuando se dibuja una bala, se llama el metodo dibujar_balas(). La funcion draw.rect() llena la parte de la
        # pantalla definida por el rectangulo de las balas con el color almacenado en self.color
        """Dibuja las balas en la pantalla"""
        pygame.draw.rect(self.pantalla, self.color, self.rect)
