produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 10}
]

# faz uma "copia" da lista produtos, e altera o preço dos produtos em 10%, adicionando a condição se o preço for maior que 20
novos_produtos = [{**produto, 'preco': produto['preco'] * 1.10} if produto['preco'] > 20 else {**produto} for produto in produtos]

#desempacotando a list novos produtos
print(produtos)
print(*novos_produtos, sep='\n')