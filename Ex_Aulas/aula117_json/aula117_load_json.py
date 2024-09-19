import json

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)