contador = 0

while contador <= 100:
    contador += 1
    
# condição para caso o contador seja igual a 6 ele continue, sem informar o numero    
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

# condição para pular de 10 a 27
    if contador >= 10 and contador <= 27:
         continue
    
    print(contador)

#condição + break - se a condição for atingida, o while para (break)
    if contador == 40:
        break

print('Acabou')