from datetime import date

#input para saber o ano de nascimento: 
ano_de_nascimento = int(input('Informe em que ano você nasceu: '))

#condição para verificar a idade
if (date.today().year - ano_de_nascimento) >= 16:
    print('Parabéns, você está apto a votar')
else: 
    print('Você ainda não pode votar esse ano')
