from math import factorial


def fact(n):
    for el in range(1, n + 1):
        yield factorial(el)


for x in fact(4):
    print(x)
