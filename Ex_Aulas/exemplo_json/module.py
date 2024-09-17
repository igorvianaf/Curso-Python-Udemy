import json
import os


pessoas = [
    {
        "nome": 'maria',
        "sobrenome": 'vieira',
        "idade": 26,
        "ativo": False,
        "notas": ['A', 'A+'],
        "telefones": {
            "residencia" : "00 0000-0000",
            "celular" : "00 0000-0000"
        }
    },
        {
        "nome": 'joana',
        "sobrenome": 'moreira',
        "idade": 32,
        "ativo": True,
        "notas": ['B', 'A'],
        "telefones": {
            "residencia" : "00 0000-0000",
            "celular" : "00 0000-0000"
        }
    }
]

BASE_DIR = os.path.dirname(__file__)
#salvar arquivo/nome
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(SAVE_TO, 'w', encoding='utf8') as arquivo:
    json.dump(pessoas, arquivo, indent=2)