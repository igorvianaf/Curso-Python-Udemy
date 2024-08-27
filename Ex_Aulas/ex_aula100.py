import copy


from dados_aula100 import produtos


novos_produtos = [{**p, 'preco': round(p['preco']*1.1, 2)} for p in copy.deepcopy(produtos)]
produtos_por_nome = sorted(novos_produtos, key=lambda p: p['nome'], reverse=True)
produtos_por_preco = sorted(novos_produtos, key=lambda p: p['preco'])


print('Lista Original')
print(*produtos, sep='\n')
print()
print('Lista com novos produtos - (+10%)')
print(*novos_produtos, sep='\n')
print()
print('Lista de produtos organizados por nome - ordem decrescente')
print(*produtos_por_nome, sep='\n')
print()
print('Lista de produtos organizados por preço - ordem crescente')
print(*produtos_por_preco, sep='\n')