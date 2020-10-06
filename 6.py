a = 2
b = 3
day = 1
print('{}-ый день: {}'.format(day, a))
while a < b:
    a *= 1.1
    day += 1
    print('{}-ый день: {}'.format(day, a))
print('На {}-й день спортсмен достиг результата — не менее {} км'.format(day, int(a)))
