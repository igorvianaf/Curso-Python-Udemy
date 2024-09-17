caminho = 'aula116.txt'

with open(caminho, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Linha1 \n')
    arquivo.write('Linha2 \n')
    arquivo.writelines(
        ('linha 3 \n', 'linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('READLINE - NEXT')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')

    print()

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('*' * 30)
print('READ')
with open(caminho, 'r', encoding='utf8') as arquivo:
    print(arquivo.read())
