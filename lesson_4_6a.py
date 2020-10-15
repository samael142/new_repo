from itertools import count


start_num = 3
end_num = 10

for el in count(start_num):
    if el > end_num:
        break
    else:
        print(el)

# Ну или так:


def my_func(start, end):
    for i in range(start, end + 1):
        yield i


for x in my_func(300, 305):
    print(x)
