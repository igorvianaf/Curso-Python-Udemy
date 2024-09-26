class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self):
        print('Também podemos executar ações dentro do getter')
        return self.cor

caneta = Caneta('Azul')

print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
