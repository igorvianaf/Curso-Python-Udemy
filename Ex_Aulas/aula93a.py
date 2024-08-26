try:
    a = 19
    b = 0
    c = a/b
except ZeroDivisionError:
    print('Um número não pode ser dividido por 0')
except NameError:
    print('Valor não definido.')
except Exception:
    print('ERRO DESCONHECIDO')

print('Continuar')