# dict e set comprehesion

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria' : 'Escritório'
}

new_dc = {
    chave: valor for chave, valor in produto.items()
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c')
]

new_dc2 = {chave: valor for chave, valor in lista}

print(new_dc2)