def print_iterator(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
#filtro com list comprehesion
novos_produtos = [p for p in produtos if p['preco'] > 20]
#function filter
novos_produtos_function = filter(
    lambda p: p['preco'] > 30, produtos
)
print_iterator(novos_produtos)
print_iterator(produtos)
print_iterator(novos_produtos_function)