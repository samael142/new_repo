def dv(a, b):
    if b != 0:
        return a / b
    else:
        return 'Деление на 0 невозможно'


dig = input('Введи делимое и делитель через пробел ').split()
dig_int = [int(i) for i in dig]
print(dv(*dig_int))
