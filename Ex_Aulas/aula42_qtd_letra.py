frase = input('Digite um texto, para saber qual letra mais se repete: ')


#define o inicio da contagem
i = 0   
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

#loop para passar em toda letra da frase
while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)

#condição para não precisar contar os espaços/ adicionar contador antes do continue
    if letra_atual == ' ':
        i += 1
        continue

#mudando a variável para saber se a letra anterior apareceu mais vezes que a letra atual
    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi: {letra_apareceu_mais_vezes}')
print(f'A letra apareceu {qtd_apareceu_mais_vezes} vezes')