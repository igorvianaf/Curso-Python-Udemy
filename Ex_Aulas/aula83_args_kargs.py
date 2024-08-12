#Empacotamento / desempacotamento
a, b = 1, 2
b, a = a, b
# print(a, b)

pessoa = {
    'nome':'Igor',
    'sobrenome': 'Viana'
}

dados_pessoas = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoas}
# print(pessoa_completa)

# Empacotamento / desempacotamento - lista
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1,a2)
# print(b1,b2)

# *args e **kwargs

def argumentos(*args, **kwargs):
    print('Argumentos não nomeados: ', (args))

    for chave, valor in kwargs.items():
        print(chave, valor)

# argumentos(1, 3, Nome='Igor', Sobrenome='Viana')

argumentos(**pessoa_completa)
