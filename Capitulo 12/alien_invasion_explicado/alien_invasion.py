# Primero, importamos los modulos sys & pygame.
# El modulo pygame contiene la funcionalidad necesaria para crear el juego.
# Se hará uso de las herramientas del modulo sys para salir del juego cuando el jugador lo decida

import sys
from time import sleep
import pygame
from configuracion import Configuracion
from nave import Nave
from balas import Balas
from alien import NaveAlien
from game_stats import GameStats



class AlienInvasion:
    """Clase general para administrar el comportamientos y los activos del juego"""

    def __init__(self):
        """Inicializa y crea los recursos del juego """
        pygame.init()  # Esta función propia de pygame, inicializa la configuracion de fondo necesaria para funcionar.
        self.configuracion = Configuracion()  # Creamos una instancia del modulo Configuracion y lo asignamos

        # FULL SCREEN MODO.
        self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Cuando se crea la superficie de la pantalla, se le pasa la tupla (0, 0) y el parametro pygame.FULLSCREEN.
        # Esto le indica a python que averigue un tamaña de ventana que llene la pantalla, porque no conocemos el ancho
        # y alto de la pantalla.
        self.configuracion.ancho_ventana = self.pantalla.get_rect().width
        self.configuracion.alto_ventana = self.pantalla.get_rect().height

        # Se hace uso de los atributos ancho y alto desde el modulo de configuracion: dimensiones de la ventana
        # 1200 px (ancho) * 700px (alto), valores que se ajustan de acuerdo a las condiciones.
        # self.pantalla = pygame.display.set_mode((self.configuracion.ancho, self.configuracion.alto))
        pygame.display.set_caption("Invasión  ALien")

        # Creamos una instancia para almacenar la estadistica del juego
        self.estadisticas = GameStats(self)  # Creamos una instancia despues de crear la ventana del juego pero antes de
        # definir otros elementos del juego.

        # ----- LA NAVE -----
        self.nave = Nave(self)  # Despues que ha sido creada la pantalla, creamos una instancia de Nave.
        # recibe un argumento. El argumento self acá se refiere a la actual instancia de AlienInvasion. Este parametro
        # le da a la Nave acceso a los recursos del juego, como el objeto de la pantalla. Asignamos esta instancia
        # a self.ship

        # LAS BALAS
        # Se crea un grupo para almacenar las balas, de esta forma se pueden administrar las que han sido disparadas
        # se usa este grupo para pintar balas en la pantalla en cada pase a traves del bucle principal y actualiza
        # su posicion.
        self.grupo_balas = pygame.sprite.Group()
        self.grupo_aliens = pygame.sprite.Group()
        self._crear_flota_alien()

    # ----- QUE COMIENCE EL JUEGO -----
    def ejecutar_juego(self):  # El juego será controlado por este metodo.
        """Inicia el ciclo principal del juego"""
        while True:  # Este bucle contiene un evento y el codigo que administra las actualizaciones en pantalla
            # Observa los eventos de teclado y mouse.

            # METODO AUXILIAR
            self._check_events()  # Para llamar un metodo desde dentro de una clase se usa notacion de punto con la
            # variable self y el nombre del metodo

            if self.estadisticas.juego_activo:
                self.nave.mover()
                self._update_balas()
                self._actualizar_naves_alien()
                # Ubicamos las posiciones de las nave alien para actualizar despues que las balas han sido actualizadas
                # ya que pronto revisaremos para ver si las alas han golpeado a una nave alien
            self._actualizar_pantalla()


    def _check_events(self):  # Llamamos al metodo auxiliar desde dentro del bucle while en ejecutar_juego().
        """Responde a las pulsaciones de tecla y eventos del mouse"""
        for event in pygame.event.get():  # Esta funcion retorna una lista de eventos que han tomado lugar
            # desde la ultima vez que fue llamada la funcion
            if event.type == pygame.QUIT:  # Cuando el jugador hace clic en el boton cerrar de la ventana, el
                # evento pygame.QUIT se detecta y llama a sys.exit() para salir del juego.
                sys.exit()

            # MOVER LA NAVE HACIA LA DERECHA
            elif event.type == pygame.KEYDOWN:  # Si se detecta que el usuario ha presionado una tecla
                self._revisar_eventos_keydown(event)
            elif event.type == pygame.KEYUP:  # Si se detecta que el usuario ha dejado de presionar la tecla
                self._revisar_eventos_keyup(event)

    def _revisar_eventos_keydown(self, event):  # Metodo auxiliar creado para facilitar la lectura del codigo.
        """Responde a la presion de la tecla"""
        if event.key == pygame.K_RIGHT:  # Si la tecla presionada es la flecha hacia la derecha
            self.nave.movimiento_derecha = True  # se mueve el rectangulo de la nave a la derecha en X en +1
        elif event.key == pygame.K_LEFT:
            self.nave.movimiento_izquierda = True

        # Si se presiona la tecla "q", el juego terminará.
        elif event.key == pygame.K_q:
            sys.exit()

        # Presionar la barra espaciadora para disparar
        elif event.key == pygame.K_SPACE:
            self._disparar_balas()

    def _revisar_eventos_keyup(self, event):  # Metodo auxiliar creado para facilitar la lectura del codigo.
        """Responde cuando se suelta la tecla"""
        if event.key == pygame.K_RIGHT:
            self.nave.movimiento_derecha = False  # El movimiento de la nave se detiene.
        if event.key == pygame.K_LEFT:
            self.nave.movimiento_izquierda = False

    def _impacto_nave(self):
        """Responde cuando la nave recibe impacto de una nave alien"""
        # Este metodo coordina la respuesta cuando una nave alien impacta la nave. El numero de naves que van quedando
        # se van restando en razon de 1, despues vaciamos el grupo de naves alien y balas, luego se crea una nueva flota
        # y se centra la nave. Mas adelante se agrega una pequeña pausa despues que se han hecho las actualizaciones
        # a todos los elementos del juego, pero antes que los cambios hayan sido pintados en la pantalla.

        if self.estadisticas.naves_restantes > 0:
            # Restar las vidas de las naves
            self.estadisticas.naves_restantes -= 1

            # Deshacerse de naves aliens y balas restantes
            self.grupo_aliens.empty()
            self.grupo_balas.empty()

            # Crear nueva flota y centrar la nave
            self._crear_flota_alien()
            self.nave.centrar_nave()

            # Pausar
            sleep(0.5)
        else:
            self.estadisticas.juego_activo = False

    def _aliens_tocan_fondo_pantalla(self):
        # Este metodo revisa si  alguna nave alien ha alcanzado el fondo de la pantalla
        """Revisa si las naves alien llegan al fondo de la pantalla"""
        pantalla_rect = self.pantalla.get_rect()
        for alien in self.grupo_aliens.sprites():
            # Una nave alien alcanza el fondo cuando el valor de su rect.bottom es mayor o igual que el atributo del
            # rectangulo de del fondo de la pantalla (pantalla_rect.bottom)
            if alien.rect.bottom >= pantalla_rect.bottom:
                # Tratarlo como si la nave hubiera hecho impacto con la nave alien
                self._impacto_nave()
                # Si la nave alien alcanza el fondo llamamos _impacto_nave. Si alguna nave alien impacta con el fondo
                # no hay necesidad de revisar el resto, asi que se sale del bucle despues de llamar _impacto_nave
                break

    def _disparar_balas(self):
        # Creamos una instancia de Balas y la nombramos nueva_bala.
        """Crea una nueva bala y la agrega al grupo de balas"""
        if len(self.grupo_balas) < self.configuracion.balas_permitidas:
            # Si la cantidad de balas es menor que las balas permitidas:
            nueva_bala = Balas(self)
            # Se usa el metodo add para agrupar las balas, es un metodo similar a append pero es exclusivo para grupos de
            # Pygame
            self.grupo_balas.add(nueva_bala)

    def _update_balas(self):
        """Actualiza la posicion de las balas y se deshace de balas viejas."""
        # Actualiza la posicion de las balas.
        self.grupo_balas.update()
        # Deshacerse de las balas que van desapareciendo.
        for bala in self.grupo_balas.copy():  #
            if bala.rect.bottom <= 0:
                self.grupo_balas.remove(bala)
        # print(len(self.balas))

        self.revisar_colision_balas_alien()

    def revisar_colision_balas_alien(self):
        """Responde a las colisiones de las balas con las naves alien"""
        # Revisar si las balas golpean las naves alien
        # Si es asi, deshacerse de la bala y de la nave alien
        collisions = pygame.sprite.groupcollide(self.grupo_balas, self.grupo_aliens, True, True)

        # REPOBLANDO LA FLOTA DE ALIENS
        if not self.grupo_aliens:  # Revisamos si el grupo_aliens esta vacio
            # Destruir balas existentes y crear una flota de naves alien nueva
            self.grupo_balas.empty()  # Si el grupo esta vacio, nos deshacemos de cualquier bala existente usando el
            # metodo empty() el cual quita los sprites sobrantes de un grupo
            self._crear_flota_alien()  # Llamamos este metodo el cual llena la pantalla con naves alien de nuevo


    def _actualizar_naves_alien(self):
        """Revisa si la flota esta en el borde luego actualiza las posiciones de las naves alien en la flota"""
        self._revisar_bordes_flota()
        self.grupo_aliens.update()  # Llamamos al metodo update()

        # Revisar colisiones nave-nave alien
        if pygame.sprite.spritecollideany(self.nave, self.grupo_aliens): # La funcion spritecollideany() toma dos
            # argumentos: un sprite y un grupo. Esta funcion busca cualquier miembro de un grupo que ha chocado
            # con el sprite y deja de recorrer el grupo tan pronto como encuentra un miembro  que ha chocado con el
            # sprite.
            self._impacto_nave()

        # Revisar si las naves alien impctan con el fondo de la pantalla
        self._aliens_tocan_fondo_pantalla()

    def _crear_flota_alien(self):
        """Crea una flota de naves alien"""
        # Creacion una nave alien y halla el numero de naves alien en una fila
        # El espacio entre cada nave alien es igual al ancho de una nave alien
        nave_alien = NaveAlien(self)
        ancho_nave_alien, alto_nave_alien = nave_alien.rect.size  # calcula el ancho y alto de la nave alien
        # El espacio disponible en pantalla es igual al ancho de la pantalla menos el ancho de la nave * 2
        # print(ancho_nave_alien)  # Para conocer el tamaño del ancho de la nave
        espacio_disponible_coordenadas_x = self.configuracion.ancho_ventana - (ancho_nave_alien * 2)
        # El numero de naves disponibles en pantalla es igual al espacio disponible dividido entre el ancho de la nave
        # alien multiplicado por 2
        # print(self.configuracion.ancho_ventana)  # Nos muestra el ancho total de la ventana
        # print(espacio_disponible_coordenadas_x)  # Muestra el espacio que queda despues de la operacion
        numero_naves_alien_x = espacio_disponible_coordenadas_x // (ancho_nave_alien * 2)
        # print(numero_naves_alien_x)  # Nos dice cuantas naves caben en pantalla de forma horizontal

        # DETERMINA EL NUMERO DE FILAS DE NAVES ALIEN QUE CABEN EN PANTALLA
        alto_nave = self.nave.rect.height
        espacio_disponible_coordenadas_y = (self.configuracion.alto_ventana - (alto_nave_alien * 3) - alto_nave)
        numero_filas = espacio_disponible_coordenadas_y // (alto_nave_alien * 2)

        # CREANDO LA FLOTA ALIEN
        for numero_fila in range(numero_filas):
            for numero_nave_alien in range(numero_naves_alien_x):
                # Crea una nave alien y la pone en la fila
                self._crear_naves_alien(numero_nave_alien, numero_fila)


    def _crear_naves_alien(self, numero_nave_alien, numero_fila):
        """Crea una nave alien y la pone en la fila"""
        nave_alien = NaveAlien(self)  # Creea un objeto de tipo nave alien
        ancho_nave_alien, alto_nave_alien = nave_alien.rect.size
        nave_alien.x = ancho_nave_alien + 2 * ancho_nave_alien * numero_nave_alien
        # print(nave_alien.x)
        nave_alien.rect.x = nave_alien.x
        nave_alien.rect.y = alto_nave_alien + 2 * alto_nave_alien * numero_fila
        self.grupo_aliens.add(nave_alien)


    def _revisar_bordes_flota(self):
        """Responde de forma apropiada si alguna nave alien alcanza un borde"""
        for alien in self.grupo_aliens.sprites():
            if alien.revisar_bordes():
                self._cambiar_direccion_flota()
                break

    def _cambiar_direccion_flota(self):
        """Baja la flota entera y cambia la direccion de la flota"""
        for alien in self.grupo_aliens.sprites():
            alien.rect.y += self.configuracion.velocidad_caida_aliens
        self.configuracion.direccion_flota_alien *= -1

    def _actualizar_pantalla(self):
        # REPINTAR LA PANTALLA DURANTE CADA PASO A TRAVES DEL BUCLE.
        # CAMBIANDO EL FONDO (BACKGROUND)
        # red = 250, green = 250, Blue = 250 RGB
        self.pantalla.fill(self.configuracion.color_de_fondo)
        # llenamos la pantalla mediante el metodo fill() que actua sobre la superficie (surface) y toma
        # solo un argumento: un color

        self.nave.blitme()  # pintamos la nave en la pantalla llamando a nave.blitme(), de esta forma, la nave
        # aparece centrada en la parte baja de la pantalla.

        for bala in self.grupo_balas.sprites():
            bala.dibujar_balas()

        self.grupo_aliens.draw(self.pantalla)

        # Crea la mas reciente vista reciente
        pygame.display.flip()
        # Cuando movemos los elementos del juego, pygame.display.flip() actualiza continuamente la pantalla
        #  para mostrar las pnuevas posiciones de los elementos del juego y oculta las viejas, creando la ilusion
        # de movimiento suave


if __name__ == "__main__":
    # Creamos una instancia y corremos el juego
    ai = AlienInvasion()
    ai.ejecutar_juego()
