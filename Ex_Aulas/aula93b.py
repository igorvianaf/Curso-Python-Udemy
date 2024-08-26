try:
    a = 19
    b = 0
    print('Linha 1'[50])
    c = a/b
except ZeroDivisionError:
    print('Um número não pode ser dividido por 0')
except NameError:
    print('Valor não definido.')
except (TypeError, IndexError) as error:
    print('MSG', error)
    print('Nome', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('Continuar')