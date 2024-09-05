from functools import reduce


def funcao_reduce(acumulador, produto):
    print('Acumulador', acumulador)
    print('Produto', produto)
    print()
    return acumulador + produto['preco']


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = reduce(
    funcao_reduce, produtos, 0
)
