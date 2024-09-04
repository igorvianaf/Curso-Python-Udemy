def param_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)
        def nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return nova_funcao
    return decorador

@param_decorador(nome='Primeiro')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)