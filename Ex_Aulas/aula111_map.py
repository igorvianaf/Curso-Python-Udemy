from functools import partial


def print_iterator(iterator):
    print(*list(iterator), sep='\n')
    print()

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_vinte_por_cento = partial(
    aumentar_porcentagem, porcentagem=1.2
)

def aumento_produto(produto):
    return {**produto, 'preco': aumentar_vinte_por_cento(produto['preco'])}


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_precos = list(map(
    aumento_produto,
    produtos
))
#map com lambda
valor_vezes_tres = list(
    map(
        lambda x: x*3,
        [2, 4, 6, 8]
)
)
print_iterator(produtos)
print_iterator(novos_precos)
print(valor_vezes_tres)
