import json


CAMINHO = 'C:\\Users\\igorv\\OneDrive\\Documentos\\ADS\\cursos\\python_udemy\\Curso-Python-Udemy\\Ex_Aulas\\ex_aula127_class_json\\arquivo.json'

class Pessoa:
    def __init__(self, nome, idade, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.sexo = sexo

pessoa1 = Pessoa('João', 27, 1.90, 'M')
pessoa2 = Pessoa('José', 42, 1.83, 'M')
pessoa3 = Pessoa('Maria', 35, 1.55, 'F')
pessoa4 = Pessoa('Julia', 54, 1.50, 'F')

dados = [pessoa1.__dict__, pessoa2.__dict__, pessoa3.__dict__]

def executar_dump():
    print('Realizando dump...')
    with open(CAMINHO, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    print('__main__ executado')
    executar_dump()
