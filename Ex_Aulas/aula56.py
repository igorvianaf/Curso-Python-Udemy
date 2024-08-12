frase = input('Digite uma frase: ')
lista_frases_cruas = frase.split()

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

frase_unida = '-'.join(lista_frases)

print(lista_frases)
print(frase_unida)

