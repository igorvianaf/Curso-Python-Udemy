# lista de retorno False
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'trufhy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy('TESTE'))
print(f'{dicionario=}', falsy('TESTE'))
print(f'{conjunto=}', falsy('TESTE'))
print(f'{tupla=}', falsy('TESTE'))
print(f'{string=}', falsy('TESTE'))
print(f'{inteiro=}', falsy('TESTE'))
print(f'{flutuante=}', falsy('TESTE'))
print(f'{nada=}', falsy('TESTE'))
print(f'{falso=}', falsy('TESTE'))
print(f'{intervalo=}', falsy('TESTE'))
