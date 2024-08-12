# coletando informações para saber o peso ideal, sendo masc ou fem
altura = float(input('Informe sua altura em metros: '))
sexo = int(input('1 - MASCULINO \n 2 - FEMININO \n' ))

if sexo == 1:
    print(f'O seu peso ideal é: {72.7 * altura - 58}')
elif sexo == 2:
    print(f'O seu peso ideal é: {62.1 * altura - 44.7}')
else:
    print('Você precisa digitar 1 ou 2 para validar o cálculo')
