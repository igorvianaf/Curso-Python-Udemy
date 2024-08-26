#raise - lançando exeções (erros)
def erro_divisao_zero(d):
    if d == 0:
        raise ZeroDivisionError('O divisor não pode ser 0')
    return True

def checar_numero(n):
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float')
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float')
    return True


def divide(n, d):
    checar_numero(n)
    checar_numero(d)
    erro_divisao_zero(d)
    return n / d


print(divide(8, 10))