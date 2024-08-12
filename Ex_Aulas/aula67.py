def soma (x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}' , x + y + z)

    else:
        print(f'{x=} {y=}' , x + y)



soma(1, 2)
soma(3, 5)
soma(100, 200, 300)
soma(7, 2, 0)