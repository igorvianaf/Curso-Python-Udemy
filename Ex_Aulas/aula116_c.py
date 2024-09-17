import os


caminho = 'aula116_c.txt'

with open(caminho, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção \n')
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n')
    arquivo.writelines(
        ('linha 3 \n', 'linha 4\n')
    )

# os.remove(caminho)
# os.rename(caminho, 'caminho_novo')