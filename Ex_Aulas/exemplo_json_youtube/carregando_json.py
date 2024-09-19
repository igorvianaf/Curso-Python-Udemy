import os
import json


BASE_DIR = os.path.dirname(__file__)
FILE_JSON = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(FILE_JSON, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    
    for pessoa in pessoas:
        print(pessoa['nome'])
