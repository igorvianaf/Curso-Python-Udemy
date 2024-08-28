# iteravel = acessa valores sequencialmente/ iterator = acessa apenas o proximo valor

iteravel = ['EU', 'Tenho', '__iter__', 'Joao']
iterator = iter(iteravel)

for item in range(0, len(iteravel)):
    print(next(iterator))
