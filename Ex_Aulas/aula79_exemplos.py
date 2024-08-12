#exemplo de uso de set
letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra)

    if 'l' in letras:
        break

    print(letras)
print('Parabéns, você encontrou a letra misteriosa!')