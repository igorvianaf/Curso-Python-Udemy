def criar_funcao(funcao):
    def interna(*args):
        print('Decorando função')
        for arg in args:
            is_string(arg)
        resultado = funcao(*args)
        print(f'O resultado será {resultado}')
        print('Agora a função foi decorada')
        return resultado
    return interna


def is_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('O parametro informado deve ser uma str')
    

@criar_funcao
def inverter_string(string):
    return string[::-1]


inverter = inverter_string('ABC')
print(inverter)