from itertools import cycle

c = 1
my_list = [23, 1, 3, 10, 4, 11]
n = 10
for el in cycle(my_list):
    if c > n:
        break
    print(el)
    c += 1

# Ну, и традиционно:


def my_func(my_list_func, n_func):
    c_func = 1
    for el_func in cycle(my_list_func):
        if c_func > n_func:
            break
        c_func += 1
        yield el_func


for x in my_func([100, 200, 300, 400, 500], 10):
    print(x)
