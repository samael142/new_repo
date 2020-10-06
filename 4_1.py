a = int(input('Введи целое положительное число\n'))
b = a
max_digit = 0
zeros = 1
while b > 0:
    while a > 10:
        a = a // 10
        zeros = zeros * 10
    if a > max_digit:
        max_digit = a
    b = b % zeros
    zeros = 1
    a = b
print(max_digit)
