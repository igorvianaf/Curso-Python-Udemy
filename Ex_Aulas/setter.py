class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor_tinta(self):
        return self._cor
#usado para atribuir novo valor a self._cor
    @cor_tinta.setter
    def cor(self, valor):
        print('Entrando no setter')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
#dentro do setter também é possivel realizar condições e tratamento de erro
    @cor_tampa.setter
    def cor_tampa(self, valor):
        if valor == 'Rosa':
            raise ValueError('Erro! Não é possível adicionar essa cor')
        self._cor_tampa = valor

caneta = Caneta('Azul')
caneta.cor = 'Azul'
print(caneta.cor)
caneta.cor_tampa = 'Rosa'
print(caneta.cor_tampa)