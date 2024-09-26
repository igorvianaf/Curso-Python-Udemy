class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('property')
        return self.cor_tinta

    @property
    def marca(self):
        print('Novo property')
        return 'Bic'

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.marca)
