from time import sleep

while True:
    numero_1 = input('Digite um número: ').strip()
    numero_2 = input('Digite o segundo número: ').strip()
    operador = input('Qual operação você deseja realizar? (+ - * /): ').strip()

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
# tente converter os inputs numero 1 e 2 em float, caso esteja certo, números validos se torna TRUE
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
#caso os um dos numeros não seja válido -- numeros validos se torna None
    except:
        numeros_validos = None

#checando se os numeros informados são válidos
    if numeros_validos is None:
        print('Um ou ambos os números informados são inválidos. ')
        continue

    operadores_permitidos = '+-*/'

#checando se os operadores lógicos são permitidos
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

# condição para não ser digitado mais de um operador logico
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta...')
    sleep(2)
    print('=-=' * 20)
    print('Confira o resultado a baixo:')
    print('=-=' * 20)
# condições para realizar operação matematica
    if operador == '+':
        print (f'{numero_1_float} + {numero_2_float} =', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} =', numero_1_float - numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} =', numero_1_float * numero_2_float)
    else:
        print(f'{numero_1_float} / {numero_2_float} =', numero_1_float // numero_2_float)

    

 #     #função para sair do loop
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    

    if sair is True:
        break
print('Fim da operação')