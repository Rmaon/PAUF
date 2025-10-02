from persona import Persona

class Jugador(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador, puntuacion_total=0, chagepeteador, entregadorTardio, ausencias, hablador):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador, puntuacion_total)
        self.chagepeteador = chagepeteador
        self.entregadorTardio = entregadorTardio
        self.ausencias = ausencias
        self.hablador = hablador
        self.puntuacion_total = puntuacion_total

