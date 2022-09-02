# Despues de elegir una imagen para la nave, necesitamos mostrarla en pantalla. Para usarla, crearemos un modulo
# que contenga la clase Nave, la cual manejará el comportamiento de la nave del jugador.

import pygame

class Nave:
    """Clase que permite administrar la nave"""

    def __init__(self, ai_juego):  # El metodoinit toma dos parametros: su propia referencia y una referencia a la
        # intancia actual de la clase AlienInvasion.

        """Inicializa la nave y establece su posicion inicial"""
        self.pantalla = ai_juego.pantalla  # asignamos la pantalla a un atributo de Nave, asi podemos acceder facilmente
        # a el en todos los metodos de esta clase

        self.configuracion = ai_juego.configuracion  # Este atributo sera usado en el metodo mover()

        self.pantalla_rect = ai_juego.pantalla.get_rect()  # Accedemos al atributo del rectangulo de la pantalla usando
        # el metodo get_rect() y asignandolo a self.pantalla_rect. Haciendolo asi, permite ubicar la nave en la
        # localizacion correcta en la pantalla.

        # CARGAR LA IMAGEN Y OBTENER SU RECTANGULO.
        self.imagen = pygame.image.load("images/nave.png") # se da la ubicacion de la imagen de la nave. Esta funcion
        # retorna una superficie que representa la nave la cual asignamos a self.imagen, cuando se carga la imagen
        self.rect = self.imagen.get_rect()  # se llama a get_rect() para acceder al atributo del rectangulo de la
        # superficie de la nave y asi se pueda usarlo mas adelante para poner la nave

        # CADA NAVE NUEVA INICIA CENTRADA EN EL FONDO DE LA PANTALLA.
        self.rect.midbottom = self.pantalla_rect.midbottom  # Colocaremos la nave en la parte inferior central de la
        # pantalla. Para hacerlo, el valor de self.rect.midbottom debe coincidir con el atributo midbottom del
        # rectángulo de la pantalla.

        # ALMACENAR VALOR DECIMAL PARA LA POSICION HORIZONTAL DE LA NAVE (X)
        self.x = float(self.rect.x)


        # BANDERA PARA MOVIMIENTO.
        self.movimiento_derecha = False
        self.movimiento_izquierda = False

    def mover(self):
        """Actualiza la posicion de la nave basado en la bandera (verdadero, falso)"""
        # Actualizamos el valor de x  de la nave, no del rectangulo
        if self.movimiento_derecha and self.rect.right < self.pantalla_rect.right:
            # De esta forma la nave no sobrepasará los limites de la pantalla derecha
            self.x += self.configuracion.velocidad
        if self.movimiento_izquierda and self.rect.left > 0:
            # De esta forma la nave no sobrepasará los limites de la pantalla izquierda
            self.x -= self.configuracion.velocidad

        # Se actualiza el objeto rectangulo desde x
        self.rect.x = self.x


    def blitme(self): # Este método pinta la imagen en la pantalla en la posicion establecida mediante self.rect
        """Pinta las naves en su actual posicion"""
        self.pantalla.blit(self.imagen, self.rect)

    def centrar_nave(self):
        """Centra la nave en la pantalla"""
        self.rect.midbottom = self.pantalla_rect.midbottom
        self.x = float(self.rect.x)





