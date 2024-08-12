print('Vamos criar sua senha!')
print('A senha precisa ter ao menos 10 caracteres, incluindo números e letras maiúsculas e minúsculas')

while True:
    senha = input('Digite sua senha: ')
    
    if len(senha) < 10:
        print('Sua senha precisa conter mais que 10 caracteres')

    cont_minusc = 0
    cont_maiusc = 0
    cont_num = 0
    cont_espaco = 0
   
    def verificador ():
        for verificador in senha:
            if verificador.isupper():
                cont_maiusc += 1 
            if verificador.islower():
                cont_minusc += 1
            if verificador.isdecimal():
                cont_num += 1
            if verificador.isspace():
                cont_espaco += 1

    erro = []

    if cont_maiusc == 0:
        erro.append('A senha precisa ter ao menos uma letra maiúscula. ')
    if cont_minusc == 0:
        erro.append('A senha precisa ter ao menos uma letra minúscula.')
    if cont_num == 0:
        erro.append('A senha precisa ter ao menos um número.')
    if cont_espaco >= 1:
        erro.append('A senha não pode conter espaços')


    if erro:
        print(erro)
    else:
        print('Sua senha passou pelos padrões de segurança. Senha criada com sucesso')
        break
