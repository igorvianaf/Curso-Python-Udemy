# list comprehesion - for dentro de outro for
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista1 = [(x, y) for x in range(3) for y in range(3)]


letras = [[letra for letra in 'igor'] for x in range(3)]


print(lista1)
print(letras)