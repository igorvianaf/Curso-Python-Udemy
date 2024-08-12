lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista [2]

# print(lista)
# print(lista[2])

lista.append(50)
lista.append(60)
lista.append(70)
rem_1 = lista.pop(3)

print(f'{lista}, Removido {rem_1}')
