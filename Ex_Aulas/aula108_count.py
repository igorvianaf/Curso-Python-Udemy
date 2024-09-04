from itertools import count

c1 = count(10, 2)
r1 = range(10, 20, 2)
print("count")
for i in c1:
    if i >= 20:
        break
    print(i)

print('Range')
for i in r1:
    print(i)