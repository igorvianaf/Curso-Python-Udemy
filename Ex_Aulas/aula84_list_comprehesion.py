# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

#o local da primeira letra é o valor adicionado a lista
# o segundo local letra tem funcao relacionada a cada item do iteravel 
lista2 = [letra for letra in 'abcde']
# print(lista)

# adicionar logica no list comprehension
# oara cada numero in range - multiplique por 2
lista = [numero * 2 for numero in range(10)]
print(list(range(10)))
print(lista)

