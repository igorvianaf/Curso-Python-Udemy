
nome = input('Qual o seu primeiro nome: ')
tamanho = len(nome)
if tamanho > 1:
    if tamanho <= 4:
        print('seu nome é curto')
    elif tamanho >= 5 and tamanho <= 6:
        print('seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Por favor, digire alguma coisa')