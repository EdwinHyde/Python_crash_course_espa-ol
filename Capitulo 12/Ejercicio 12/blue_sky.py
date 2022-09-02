# 12-1. Blue Sky: Make a Pygame window with a blue background.

import pygame, sys
from personaje import Personaje

class BlueSky:
    """Una clase que crea una pantalla con fondo azul"""
    def __init__(self):
        """Inicia los recursos del juego"""
        pygame.init()
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Sky".center(200))
        self.fondo_pantalla = (242, 225, 111)
        self.personaje = Personaje(self)

    def iniciar_juego(self):
        """Inicia el bucle infinito del juego"""
        while True:
            self._eventos()
            self._actualizar_pantalla()

    def _eventos(self):
        """Revisa los eventos del teclado y raton"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

    def _actualizar_pantalla(self):
        """Actualiza las imagenes en la pantalla"""
        self.pantalla.fill(self.fondo_pantalla)
        self.personaje.blit()
        pygame.display.flip()

# ----------------------------------------------------------------------------------------

# SE CREAN LAS INSTANCIAS DEL JUEGO.
sky = BlueSky()
sky.iniciar_juego()

