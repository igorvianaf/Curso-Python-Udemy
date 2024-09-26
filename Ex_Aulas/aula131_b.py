class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('property')
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'rosa':
            raise ValueError('A cor informada não é aceita')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
print(caneta._cor)

caneta.cor = 'preto'
print(caneta._cor)

caneta._cor_tampa = 'vermelho'
print(caneta._cor_tampa)
