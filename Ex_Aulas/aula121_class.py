class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
celta = Carro('Celta')

print(fusca.nome)
fusca.acelerar()

print(celta.nome)
celta.acelerar()