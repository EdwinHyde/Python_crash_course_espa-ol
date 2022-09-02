import pygame
import pygame as pg, sys
from ajustes import Ajustes
from nave import Nave
from disparos import Disparos

class Juego:
    """Módulo principal del juego"""
    def __init__(self):
        """Metodo que inicia los atributos del juego"""
        pg.init()
        self.ajustes = Ajustes()
        self.pantalla = pg.display.set_mode((0,0), pygame.FULLSCREEN)  # Pantalla completa
        self.ajustes.tamaño_pantalla = self.pantalla.get_rect().width  # Pantalla completa
        self.fondo_pantalla = self.ajustes.fondo_pantalla
        pg.display.set_caption("Jueguito de naves en forma horizontal.")

        self.nave = Nave(self)
        self.disparos = pg.sprite.Group()


    def iniciar_juego(self):
        """Inicia el bucle del juego"""
        while True:
            self._capturar_eventos()
            self.nave.mover_nave()
            self._actualizar_disparos()
            self.actualizar_pantalla()


    def _capturar_eventos(self):
        """Captura los eventos del teclado y mouse"""
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                sys.exit()

            # Mover la nave
            elif evento.type == pg.KEYDOWN:
                self._capturar_eventos_tecla_presionada(evento)
            elif evento.type == pg.KEYUP:
                self._capturar_eventos_tecla_levantada(evento)

    def _capturar_eventos_tecla_presionada(self, evento):
        """Captura cuando se presiona una tecla"""
        if evento.key == pg.K_UP:
            self.nave.mover_arriba = True
        elif evento.key == pg.K_DOWN:
            self.nave.mover_abajo = True

        elif evento.key == pg.K_q:  # Salir de la pantalla al presionar la tecla q
            sys.exit()
        elif evento.key == pg.K_SPACE:
            self._disparar()

    def _capturar_eventos_tecla_levantada(self, evento):
        """Captura eventos al soltar la tecla"""
        if evento.key == pg.K_UP:
            self.nave.mover_arriba = False
        elif evento.key == pg.K_DOWN:
            self.nave.mover_abajo = False

    def _disparar(self):
        """Crea un nuevo disparo y lo agrega al grupo de disparos"""
        if len(self.disparos) < self.ajustes.disparos_permitidos:
            disparo_nuevo = Disparos(self)
            self.disparos.add(disparo_nuevo)

    def _actualizar_disparos(self):
        """Actualiza posicion de las balas y se deshace de los disparos usados"""
        self.disparos.update()
        # Deshacerse de las balas que desaparecen
        for disparo in self.disparos.copy():
            if disparo.rect_disparo.left >= self.pantalla.get_rect().right:
                self.disparos.remove(disparo)

    def actualizar_pantalla(self):
        """Actualiza la pantalla y los elementos en ella"""
        self.pantalla.fill(self.fondo_pantalla)
        self.nave.dibujar_nave()
        for disparo in self.disparos.sprites():
            disparo.pintar_disparos()
        pg.display.flip()


if __name__ == "__main__":
    juego = Juego()
    juego.iniciar_juego()