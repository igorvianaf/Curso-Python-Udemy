class Animal: 
    def __init__(self, nome):
        self.nome = nome

    def comer(self, comida):
        print(f'O {self.nome} está comendo {comida}')

animal = Animal(input('Informe o animal: '))
comida = input(f'Informe a comida que o {animal.nome} está comendo: ')
animal.comer(comida)