def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

def executar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

multiplicacao_10 = executar_funcao(multiplicacao, 10)
soma_100 = executar_funcao(soma, 100)

print(multiplicacao_10(20))
print(soma_100(10))

