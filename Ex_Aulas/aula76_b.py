import copy

d1 = {
    'nome': 'Igor',
    'sobrenome': 'Viana',
    'idade': 900,
    'l1': [0,1,2]
}
#copia rasa só copia valores imutaveis

d2 = copy.deepcopy(d1)

d2['l1'][1] = 1000
d2['idade'] = 100

print(d1)
print(d2)