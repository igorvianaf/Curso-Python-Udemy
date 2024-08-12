valor_1 = input('Digite um valor: ')
valor_2 = input('Digite outro valor: ')

if valor_1 > valor_2:
    print(f'O primeiro valor é {valor_1} e é maior que {valor_2}')
elif valor_2 > valor_1:
    print(f'O segundo valor é {valor_2}. Este valor é maior que {valor_1}')
else:
    print(f'Os valores {valor_1} e {valor_2} são iguais')
    