# def duplicar(num):
#     return num * 2

# def triplicar(num):
#     return num * 3

# def quadriplicar(num):
#     return num * 4


# print(duplicar(10))
# print(triplicar(10))
# print(quadriplicar(10))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)



print(duplicar(2))
print(triplicar(3))
print(quadriplicar(10))
