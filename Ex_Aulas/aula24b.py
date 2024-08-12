nome = input('Digite seu nome: ')
encontrar = input('Qual palavra você deseja encontrar: ')
#tornar maiusculo para conferir, mesmo que a entrada seja maiuscula ou não
encontrar_m = encontrar.upper()
nome_m = nome.upper()

if encontrar_m in nome_m:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
