def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa(
    lambda m: lambda n: n*m, 2
)
print(duplica(4))


print(
    executa(
        lambda x, y: x + y, 2, 3
        ),
        executa(soma, 2, 4),
        soma(2, 4)
)
