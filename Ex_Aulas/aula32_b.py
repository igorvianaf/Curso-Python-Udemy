entrada = input('Que horas são? ')

try:
# transformando o input para trabalhar com inteiro
    hora = int(entrada)
# checando se é o input retorna bom dia
    if hora >=0 and hora <= 11:
        print('Bom dia')
# checando se é o input retorna boa tarde
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
# checando se é o input retorna noite
    elif hora > 17 and hora <= 23:
        print('Boa noite')
# Informando caso o input não esteja no formato de horário   
    else:
        print('Formato de hora de 0 a 23')
except:
    print('Por favor, digite apenas números inteiros')
    