# is.istance - checar se um objeto é de determinado tipo
lista = ['b', 1, 5.4, False, [1, 4, 6], (1, 4), {3, 6}, {'nome': 'igor'}]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print('STR')
        print(item.upper())

    if isinstance(item, (int, float)):
        print('INT E FLOAT')
        print(item * 2)