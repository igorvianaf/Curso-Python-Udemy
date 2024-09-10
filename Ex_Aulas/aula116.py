caminho_pasta_diferente = 'C:\\Users\\igorv\\OneDrive\\Área de Trabalho\\pasta-teste\\'
caminho_pasta_diferente += 'aula116.txt'

with open(caminho_pasta_diferente, 'w') as arquivo:
    print('Olá, mundo!')
    print('Agora vou fechar o arquivo!')
