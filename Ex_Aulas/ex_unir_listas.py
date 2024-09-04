from itertools import zip_longest


def ziper(cidades, estados):
    intervalo = min(len(cidades), len(estados))
    return [(cidades[i], estados[i] )for i in range(intervalo)]


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Recife']
estados = ['BA', 'SP', 'MG', 'RJ', 'PE', 'PR', 'AM', 'TO']
print(ziper(cidades, estados))

#forma com zip para unir listas baseado na menor lista
print(list(zip(cidades, estados)))
#forma com zip para unir listas baseado na maior lista
print(list(zip_longest(cidades, estados, fillvalue='Sem Registro')))
