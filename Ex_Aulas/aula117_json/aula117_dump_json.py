import json


pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Viana',
    'enderecos': [
        {'rua': 'R1', 'numero': 1},
        {'rua': 'R2', 'numero': 2}
    ],
    'altura': 1.9,
    'numeros_preferidos': (1, 5, 7),
    'dev': True,
    'nada': None
}

with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo)