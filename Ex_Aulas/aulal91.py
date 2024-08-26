# yield generator function

def generator(n=0, maximun=10):
    while True:
        yield n
        n += 1
        if n > maximun:
            return


gen = generator(20, 50)

for n in gen:
    print(n)
