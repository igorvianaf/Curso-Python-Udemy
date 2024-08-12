"""
interpolação básica de strings

s -- string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Igor'
preco = 1000.95897643
variavel = '%s, o preço é de R$: %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %i é %x' % 15, 15)