# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def calcular_idade(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('João', 19)
p2 = Pessoa('Maria', 24)
p3 = Pessoa('José', 34)

p1.__dict__['adicionar'] = 'novo'
print(p1.__dict__)
print(vars(p1))