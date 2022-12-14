from datetime import date

import Seguranca
import Galeria

class Administracao:

    def __init__(self, verba: float, galeria: Galeria):
        if verba >= 0:
            self.__verba = verba


    @property
    def verba(self):
        return self.__verba

    @verba.setter
    def verba(self, novaVerba):
        if (novaVerba + self.verba) >= 0:
            self.__verba = novaVerba

    def contratarSeguranca(self,seguranca: Seguranca.Seguranca):
        if seguranca.custo > self.verba:
            return 'É MUITO CARO'
        else:
            data_inicio = input('Insira a data de inicio no formato YYYY/MM/DD: ')
            data_fim = input('Insira a data do fim no formato YYYY/MM/DD: ')
            trajetoria = list(input('Digite os lugares para a ronda: '))
            self.verba -= seguranca.custo
            seguranca.rota(data_inicio, data_fim, trajetoria)
            return f"Contratado com sucesso! a verba agora é {self.verba}"
