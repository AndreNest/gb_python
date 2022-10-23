def where(f, col):
    return [x for x in col if f(x)]

data = '3 17 14 32 33 88 100'.split()

res = map(int,data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))

print(res)  