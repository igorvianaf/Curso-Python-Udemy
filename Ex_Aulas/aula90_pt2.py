#generator
import sys


iteravel = ['EU', 'Tenho', '__iter__', 'Joao']
iterator = iter(iteravel)
generator = (n for n in range(10))
lista = [n for n in range(10)]

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

for n in generator:
    print(n)
