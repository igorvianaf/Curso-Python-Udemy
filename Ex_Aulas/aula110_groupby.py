from itertools import groupby

def ordena(aluno):
    return aluno['nota']
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_ordem = sorted(alunos, key=ordena)

grupos = groupby(alunos_ordem, key=ordena)

for chave, grupo in grupos:
    print(f'Alunos com nota {chave}')
    for aluno in grupo:
        print(aluno['nome'], end=' | ')
        print(aluno['nota'])
