class Pessoa:
    ano = 2013

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)
    @classmethod
    def nome_joão(cls, idade):
        return cls('João', idade)

p1 = Pessoa('Igor', 27)
print(Pessoa.ano)
p1.metodo_de_classe()
p2 = Pessoa.criar_50_anos('José')
print(p2.nome, p2.idade)
p3 = Pessoa.nome_joão(23)
print(p3.nome, p3.idade)