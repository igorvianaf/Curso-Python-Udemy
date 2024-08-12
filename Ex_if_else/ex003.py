# coletar a informação de quantas maçãs seram compradas
quantidade_de_macas = int(input('Quantas maçãs você deseja comprar? '))

if quantidade_de_macas >= 12:
    print(f'Cada maçã custou 0,25 e sua compra deu R$: {quantidade_de_macas * 0.25}')
else:
    print(f'Cada maça custou 0,30 e sua compra deu um total de: {quantidade_de_macas * 0.3}')