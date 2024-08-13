produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 10}
]
# a esquerda do for é mapeamento e a direita é filtro
novos_produtos = [{**produto, 'preco': produto['preco'] * 1.10} if produto['preco'] > 20 else {**produto} for produto in produtos if produto['preco'] > 10]

#desempacotando a list novos produtos
print(produtos)
print(*novos_produtos, sep='\n')


# lista = [n for n in range(10) if n > 4]

# print(lista)