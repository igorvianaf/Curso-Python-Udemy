# variavel livre + nonlocal

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_concatenar):
        nonlocal valor_final
        valor_final += valor_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))