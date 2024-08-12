def par_impar(*args):
    for numero in args:
        if numero % 2 == 0:
            print(f'O numero {numero} é par')
            
        else:
            print(f'O número {numero} é ímpar')
            

resultado = par_impar(10, 3, 50, 80, 37, 25, 15)


#checar porque retorna none quando nao inseri o return e quando inseri volta o valor, mesmo sem mandar printar