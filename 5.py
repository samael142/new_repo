proceeds = int(input('Введи выручку '))
costs = int(input('Введи расходы '))
profit = 0
staff = 0
if proceeds > costs:
    print('У нас прибыль!!!')
    profit = int((proceeds - costs) / proceeds * 100)  # Привёл к int для красоты
    print('Наша рентабельность {}%'.format(profit))
    staff = int(input('А сколько сотрудников? '))
    print('Каждый заработал {} денег'.format((proceeds - costs) / staff))
else:
    print('Отработали в минус, прибыли нет!!!')
