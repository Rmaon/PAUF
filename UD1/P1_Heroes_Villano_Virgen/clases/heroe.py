from persona import Persona

class Heroe(Persona):
    def __init__(self, codigoLimpio, bienDocumentado, gitGod, arquitecto, detallista, nombre, apellidos, fecha_nacimiento, identificador, puntuacion_total=0):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador, puntuacion_total)
        self.codigoLimpio = codigoLimpio
        self.bienDocumentado = bienDocumentado
        self.gitGod = gitGod
        self.arquitecto = arquitecto
        self.detallista = detallista
        self.puntuacion_total = puntuacion_total

