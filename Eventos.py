from datetime import date
from datetime import time

class Evento:
    def __init__(self, nome: str, data: date, hora: time, local: Local):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.local = local


    def numeroPlateia(self, plateia: Plateia):
        return plateia.n_pessoas