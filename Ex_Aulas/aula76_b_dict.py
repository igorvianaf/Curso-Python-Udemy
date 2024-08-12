pessoa = {}

chave = 'nome'
pessoa [chave] = 'Igor' 
pessoa ['Sobrenome'] = 'Viana'

print(pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['Sobrenome:']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('Sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['Sobrenome'])
