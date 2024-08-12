def soma(*args):
    total = 0
    for numero in args:
        total += numero   
    return total

soma_1 = soma(1,2,3)
print(soma_1)

soma_2 = soma(4,5,6)
print(soma_2)