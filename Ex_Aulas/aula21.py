# Para o operador logico AND, todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_correta = '123456'
if entrada == 'E' and senha_digitada == senha_correta:
    print('Senha correta. Bem vindo!')
else:
    print('Senha incorreta')

#Se a expressão possuir um valor falsy, essa expressão irá parar no valor falsy
#ex: print(True and False and True)
# a expressão irá parar no false, após o primeiro true