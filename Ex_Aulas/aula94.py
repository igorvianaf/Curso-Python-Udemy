try:
    print('Abrir arquivo')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Divisão por 0')
except IndexError as erro:
    print('Index Error')
except (NameError, ImportError):
    print('Name Error, Import Error')
else:
    print('Não deu erro ')
finally:
    print('Fechar arquivo')