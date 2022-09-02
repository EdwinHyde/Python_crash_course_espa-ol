import sys, pygame
from configuracion import Configuracion
from nave import Nave


class InvasionAlien:
    # °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    """Clase general para manejar los activos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa y crea los recursos del juego"""
        pygame.init()
        self.configuracion = Configuracion()  # Instancia de la configuracion del juego para accedera sus valores.
        # Crea la pantalla del juego en modo full screen(superficie)
        self.pantalla = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.configuracion.dimensiones_pantalla = self.pantalla.get_rect().width
        self.configuracion.dimensiones_pantalla = self.pantalla.get_rect().height

        pygame.display.set_caption("Invasion Alien".center(365))  # Titulo que aparece en la ventana, centrado.
        self.nave = Nave(self)  # Instancia de la nave
        self.fondo_pantalla = self.configuracion.fondo_de_pantalla  # Valores traidos desde el modulo configuracion.

    # °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

    # ******************************************************************************************************************
    def iniciar_juego(self):
        """Inicia el ciclo del juego"""
        while True:
            self._check_eventos()
            self.nave.mover_nave()
            self._actualizar_pantalla()

    def _check_eventos(self):  # Metodo auxiliar
        """ Observar los eventos del teclado y raton"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si se hace clic en el boton X de la ventana, cierra la pantalla.
                sys.exit()
                # EVENTOS PARA MOVER LA NAVE
            elif event.type == pygame.KEYDOWN:  # Si el tipo de evento es de presionar la tecla.
                self._chequear_eventos_keydown(event)
            # Evento al soltar las flechas de direccion
            elif event.type == pygame.KEYUP:  # Evento que se activa al soltar la tecla.
                self._chequear_eventos_keyup(event)

    def _chequear_eventos_keydown(self, event):
        """Responde cuando se presiona una tecla"""
        if event.key == pygame.K_RIGHT:  # Si la tecla (key) presionada es la flehca hacia la derecha.
            self.nave.mov_derecha = True  # La nave se moverá hacia la derecha.
        elif event.key == pygame.K_LEFT:  # Misma logica para mover hacia la izquierda.
            self.nave.mov_izquierda = True
        elif event.key == pygame.K_q:  # Habilitamos la tecla q para cerrar el juego.
            sys.exit()

    def _chequear_eventos_keyup(self, event):
        """Responde cuando se suelta una tecla."""
        if event.key == pygame.K_RIGHT:  # Si se suelta la flcha de direccion hacia la derecha
            self.nave.mov_derecha = False  # Se detiene la nave.
        elif event.key == pygame.K_LEFT:
            self.nave.mov_izquierda = False

    def _actualizar_pantalla(self):
        """Actualiza las imagenes en pantalla y pasa a la nueva pantalla"""
        self.pantalla.fill(self.fondo_pantalla)  # Pinta la pantalla en cada paso por el bucle
        self.nave.blitme()
        # Actualizar constantemente la pantalla
        pygame.display.flip()
    # ******************************************************************************************************************


if __name__ == "__main__":
    ia = InvasionAlien()  # Se crea una instancia llamada ia
    ia.iniciar_juego()  # La instancia inicia el juego
