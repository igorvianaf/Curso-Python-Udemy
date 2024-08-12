pessoa = {
    'Nome:': 'Igor',
    'Sobrenome:': 'Viana',
    'Idade:': 27,
    'Altura': 1.9,
    'Endereço:' : [
        {'Rua': 'tal tal', 'Número': 123},
        {'Rua': 'Outra rua', 'Número': 321}
    ],
}

# print(pessoa, type(pessoa))
# print(pessoa['Nome'])
for chave in pessoa:
    print(chave, pessoa[chave])