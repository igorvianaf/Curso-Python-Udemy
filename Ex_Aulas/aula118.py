def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_cliente('Igor')
adiciona_cliente('João', cliente1)
adiciona_cliente('Maria', cliente1)
cliente1.append('Julio')
cliente1.sort()
print(cliente1)