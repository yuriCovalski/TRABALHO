from Local import Local as local


class Galeria:

    def __init__(self,conjunto_artes: tuple, endereco: str, nome: str, conjunto_locais: tuple = ()):
        self.conjunto_artes = conjunto_artes
        self.endereco = endereco
        self.nome = nome
        self.conjunto_locais = ()


    def adicionaLocal(self, local: local):
            self.conjunto_locais = (self.conjunto_locais, local)
            return 'Adicionado com sucesso'

galeria = Galeria(('paiarte','maearte'),'papai da silva','yuri')

print(galeria.conjunto_locais)
print(galeria.conjunto_locais(local('batata')))
print(galeria.conjunto_locais)