from itertools import combinations, permutations, product


def print_iterator(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['Preta', 'Branca'], 
    ['P', 'M'],
    ['Masculino', 'Feminino', 'Unisex'],
    ['Algodão', 'Poliester']
]

print_iterator(combinations(pessoas, 2))
print_iterator(permutations(pessoas, 2))
print_iterator(product(*camisetas))

