num_1 = int(input('Digite um valor: '))
num_2 = int(input('Digite o segundo valor: '))
num_3 = int(input('Digite o terceiro valor: '))

if num_1 < num_2 < num_3:
    print(num_1, num_2, num_3)
elif num_1 < num_3 < num_2:
    print(num_1, num_3, num_2)
elif num_2 < num_1 < num_3:
    print(num_2, num_1, num_3)
elif num_2 < num_3 < num_1: 
    print(num_2, num_3, num_1)
elif num_3 < num_2 < num_1:
    print(num_3, num_2, num_1)
elif num_3 < num_1 < num_2:
    print (num_3, num_1, num_2)
    