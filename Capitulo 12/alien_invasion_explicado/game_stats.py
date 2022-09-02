class GameStats:
    """Rastrea estaditicas para el juego de invasion alien"""
    def __init__(self, juego):
        """Inicializa las estadisticas"""
        self.configuracion = juego.configuracion
        self.resetear_estadisticas()

        # Iniciar el juego en estado activo
        self.juego_activo = True # Agregamos una bandera como un atributo para finalizar el juego cuando el jugador
        # agote sus naves.

    def resetear_estadisticas(self):
        """inicializa las estadisticas que pueden cambiar durante el juego"""
        self.naves_restantes = self.configuracion.limite_naves