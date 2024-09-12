caminho = 'aula116.txt'

with open(caminho, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

with open(caminho, 'r') as arquivo:
    print(arquivo.read())
