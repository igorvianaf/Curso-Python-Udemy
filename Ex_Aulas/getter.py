class Caneta:
    def __init__(self, cor):
        self._cor = cor

    def get_cor(self):
        print('retornando valor da cor' )
        return self._cor

caneta = Caneta('Azul')
caneta = Caneta('Laranja')
caneta = Caneta('Verde')


print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
