import json
from aula127_open import CAMINHO, Pessoa, executar_dump



with open(CAMINHO, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    pessoa1 = Pessoa(**pessoa[0])
    pessoa2 = Pessoa(**pessoa[1])
    pessoa3 = Pessoa(**pessoa[2])

    print(pessoa1.__dict__)
    print(pessoa2.__dict__)
    print(pessoa3.__dict__)
