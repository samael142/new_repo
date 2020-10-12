"""
Прерывание любым символом,
возможно я не так понял задание
"""

breaking_key = True
summa = 0
while breaking_key is True:
    array = input('Вводи числа через пробел. '
                  'Прерывание любым не цифровым символом ').split()
    for i in array:
        if i.isdigit():
            summa = summa + int(i)
        else:
            breaking_key = False
            break
    print(f'Промежуточная сумма: {summa}')
print(f'Итого: {summa}')
