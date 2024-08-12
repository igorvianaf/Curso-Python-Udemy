entrada = input('Digite um número: ')
#condição para analisar se a entrada é um número, caso seja, prosseguir
if entrada.isdigit:
#transformar a entrada para número inteiro 
    entrada_int = int(entrada)
#número divisivel por dois com resto 0 
    par_impar = entrada_int % 2 == 0
#texto caso o numero seja impar
    par_impar_texto = 'ímpar'
#Caso o valor de par_impar retorne true, entramos nessa etapa e retornamos o valor par
    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')