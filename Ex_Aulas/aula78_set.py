# s1 = set() #set vazio
# s2 = {2, 3, 4, 4} #set com dados

# for numeros in s2:
#     print(numeros)

# print(3 in s2)

# print(s1)
# print(s2)

# #para adicionar valor ao set:
# s3 = set()
# s3.add(1)
# s3.add('igor')

# #para add varios valores
# s3.update(('maria', 'joana', 1, 3, 5, 69, 9))
# print(s3)

# #para descartar valor especifico:
# s3.discard('igor')
# s3.discard(69)

s1 = {1, 2, 3, 7}
s2 = {3, 2, 5, 8, 10}
s3 = s1 ^ s2
print(s3)
