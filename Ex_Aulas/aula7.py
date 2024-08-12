# Variáveis são utilizadas para salvar algo na memória do computador
# PEP8, inicie variáveis com letras minusculas e elas podem conter números e underline
# O sinal de = é o operador de atribuição
# Ele é utilizado para atribuir um nome ou valor a uma variável
# Ex: nome_variavel = expressão
#nome_completo = 'Igor José Viana de Figueirêdo'
#soma_dois_mais_dois = 2 + 2
#print(nome_completo, soma_dois_mais_dois)

nome = input('Qual o seu nome: ')


idade = input('Qual a sua idade: ')

if int(idade) >= 18:
    print(f'Bem vindo, {nome}, sua idade é: {idade}, você é maior de idade')
else:
    print('Você ainda é menor de idade')
