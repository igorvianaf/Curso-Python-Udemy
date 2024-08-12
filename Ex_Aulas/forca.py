import os


palavra_secreta = input('Digite a palavra que outro jogador terá que adivinhar: ')
qtd_letras = len(palavra_secreta)
os.system('cls')
print(f'A palavra secreta tem {qtd_letras} letras')
acertos = ''
num_tentativas = 0


while True:
    letra_digitada = input('Digite uma letra: ')
    
    num_tentativas += 1

#checar se o usuario digitou apenas uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')     
        continue

#adicionar letra digitada a variavel de acertos, fora do while
    if letra_digitada in palavra_secreta:
        acertos += letra_digitada

#logica para mostrar a palavra ou *        
    palavra_formada = ''

    # iteração
    for letra_secreta in palavra_secreta:

        #condição para adicionar uma letra a palavra formada
        if letra_secreta in acertos:
            palavra_formada += letra_secreta

        #condição para letra digitada errado    
        else:
            palavra_formada += '*'

    

    print(f'Palavra formada: {palavra_formada}')
    

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS')
        print(f'A palavra era: {palavra_formada}')
        print(f'Tentativas: {num_tentativas}')
        break
    
    if num_tentativas >= 25:
        print('Você atingiu o número máximo de tentativas. Você perdeu!!')
        break
