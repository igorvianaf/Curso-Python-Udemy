# or - Qualquer condição True (verdadeiro) avalia toda a expressão como True (verdadeiro)
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor (Ou seja, verdadeiro)

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
