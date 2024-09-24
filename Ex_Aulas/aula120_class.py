# string = 'igor'
# print(string.upper())

# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Igor','Viana')

p2 = Pessoa('João', 'Henrique')

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)
