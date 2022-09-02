# 13-1. Stars:
# Find an image of a star. Make a grid of stars appear on the screen

import pygame, sys
from configuracion import Configuracion
from estrella import Estrella
from random import randint

class GrillaEstrellas:
    """Clase que creará una cuadricula llena de estrellas"""
    def __init__(self):
        """Inicializa los atributos del programa"""
        pygame.init()
        self.configuracion = Configuracion()
        self.ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.configuracion.ancho_ventana = self.ventana.get_width()
        self.configuracion.alto_ventana = self.ventana.get_height()
        pygame.display.set_caption("Ejercicio capitulo 13")

        self.estrella = Estrella(self)

        self.grupo_estrellas = pygame.sprite.Group()
        self._crear_grilla_estrellas()


    def jugar(self):
        """Inicia el bucle principal del juego"""
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        sys.exit()

            self.actualizar_pantalla()

    def _crear_grilla_estrellas(self):
        """Crea una grilla de estrellas"""
        estrella = Estrella(self)
        ancho_estrella, alto_estrella = estrella.rect.size
        espacio_disponible_x = self.configuracion.ancho_ventana - (ancho_estrella * 2)
        numero_estrellas_x = espacio_disponible_x // (ancho_estrella * 2)
        alto_estrella = self.estrella.rect.height
        espacio_disponible_y = (self.configuracion.alto_ventana - (alto_estrella * 3) - alto_estrella)
        numero_filas = espacio_disponible_y // (alto_estrella * 2)

        for numero_fila in range(numero_filas):
            for numero_estrella in range(numero_estrellas_x):
                self._dibujar_estrella(numero_estrella, numero_fila)


    def _dibujar_estrella(self, numero_estrella, numero_fila):
        """Crea una estrella y la pone en la fila"""
        estrella = Estrella(self)
        ancho_estrella, alto_estrella = estrella.rect.size
        estrella.x = ancho_estrella + (2 * ancho_estrella) * numero_estrella
        estrella.rect.x = estrella.x
        estrella.y = alto_estrella + (2 * alto_estrella) * numero_fila
        estrella.rect.y = estrella.y

        estrella.x += randint(-5, 5)
        estrella.y += randint(-5, 5)
        self.grupo_estrellas.add(estrella)


    def actualizar_pantalla(self):
        """Mantiene la pantalla actualizada"""
        self.ventana.fill(self.configuracion.fondo_ventana)
        self.grupo_estrellas.draw(self.ventana)
        pygame.display.flip()

if __name__ == "__main__":
    juego = GrillaEstrellas()
    juego.jugar()