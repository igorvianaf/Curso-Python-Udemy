def somar_lista(lista1, lista2):
    intervalo_menor = min(len(lista1), len(lista2))
    return[(lista1[i] + lista2[i]) for i in range(intervalo_menor)]


l1 = [10, 4, 20, 30, 53, 47]
l2 = [54, 3, 70, 32, 4.57, 77, 20, 304]
print(somar_lista(l1, l2))


lista = (list(zip(l1, l2)))
for i, v in enumerate(lista):
    print(sum(lista[i]))

#solução curso
lista_soma = [x+y for x, y in zip(l1, l2)]
print(lista_soma)