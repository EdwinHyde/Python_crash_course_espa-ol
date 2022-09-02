# 12-4. Rocket:
# Make a game that begins with a rocket in the center of the screen.
# Allow the player to move the rocket up, down, left, or right using the four arrow keys.
# Make sure the rocket never moves beyond any edge of the screen.

import pygame, sys
from configuracion import Configuracion
from nave import Ship

class Rocket:
    """Clase para crear e inicializar el juego"""
    def __init__(self):
        pygame.init()
        """Inicializa los atributos del juego"""
        self.configuracion = Configuracion()

        # PANTALLA EN MODO FULLSCREEN
        self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.configuracion.tamaño_pantalla = self.pantalla.get_rect().width
        self.configuracion.tamaño_pantalla = self.pantalla.get_rect().height

        pygame.display.set_caption("Rocket")
        self.nave = Ship(self)
        self.fondo = self.configuracion.background

    def iniciar(self):
        """Inicia el bucle infinito del juego"""
        while True:
            self._chequear_eventos()
            self.nave.mover_nave()
            self.actualizar_pantalla()


    def _chequear_eventos(self):
        """Captura los eventos del teclado y el raton"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
        # MOVIMIENTOS DE LA NAVE
            elif evento.type == pygame.KEYDOWN:
                self._chequear_eventos_keydown(evento)
            elif evento.type == pygame.KEYUP:
                self._chequear_eventos_keyup(evento)

    def _chequear_eventos_keydown(self, evento):
        """Captura los eventos cuando se presiona una tecla."""
        if evento.key == pygame.K_RIGHT:
            self.nave.mov_derecha = True
        elif evento.key == pygame.K_LEFT:
            self.nave.mov_izquierda = True
        elif evento.key == pygame.K_DOWN:
            self.nave.mov_abajo = True
        elif evento.key == pygame.K_UP:
            self.nave.mov_arriba = True
        # SALIR DEL JUEGO CON LA TECLA Q
        elif evento.key == pygame.K_q:
            sys.exit()

    def _chequear_eventos_keyup(self, evento):
        """Captura los eventos cuando se suelta una tecla"""
        if evento.key == pygame.K_RIGHT:
            self.nave.mov_derecha = False
        elif evento.key == pygame.K_LEFT:
            self.nave.mov_izquierda = False
        elif evento.key == pygame.K_DOWN:
            self.nave.mov_abajo = False
        elif evento.key == pygame.K_UP:
            self.nave.mov_arriba = False


    def actualizar_pantalla(self):
        """Actualiza la pantalla constantemente"""
        self.pantalla.fill(self.fondo)
        self.nave.dibujar_nave()
        pygame.display.flip()


if __name__ == "__main__":
    rocket = Rocket()
    rocket.iniciar()


