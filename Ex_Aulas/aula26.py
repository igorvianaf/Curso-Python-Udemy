"""
Formatação básica de strings
s - string
i e d - int
f - float
. <Número de digitos>
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> esquerda
< direita
^ centro
= - Força o numero a aparecer antes do 0
sinal - + ou -
ex.: 0>-100, .1f
conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')