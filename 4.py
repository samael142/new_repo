a = int(input('Введи целое положительное число\n'))
last_dig = a % 10
a = a // 10
while a > 0:
    if a % 10 > last_dig:
        last_dig = a % 10
    a = a // 10
print(last_dig)
