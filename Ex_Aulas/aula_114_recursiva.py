# def recursiva(inicio=0, fim=10):
#     if inicio >= fim:
#         return fim
    
#     print(inicio, fim)
#     inicio+=1
#     return recursiva(inicio, fim)

# print(recursiva())
def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n-1)

print(fatorial(10))