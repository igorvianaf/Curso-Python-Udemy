class Carro: 
    def __init__(self, nome):
        self.nome = nome
        print(nome)
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)