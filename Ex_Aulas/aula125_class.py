#atributos de class
import datetime


class Pessoa:
    ano_atual = datetime.datetime.now().year


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def calcular_idade(self):
        return  Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Igor', 19)
p2 = Pessoa('João', 27)
p3 = Pessoa('José', 78)


print(p1.calcular_idade())
print(p2.calcular_idade())
print(p3.calcular_idade())
