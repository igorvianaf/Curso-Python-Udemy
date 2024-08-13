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

s1 = {2 * i for i in range(10)}

print(new_dc2)
print(s1)