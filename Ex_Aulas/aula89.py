nome = 'igor'
metodo = 'upper'

if hasattr(nome, metodo):
    print('Existe upper aqui')
    print(getattr(nome, metodo)())
else:
    print(f'Naão existe o metódo {metodo}')