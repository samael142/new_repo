# Использую словари

month_number = int(input('Введи номер месяца от 1 до 12 '))
seasons = {'Зима': (12, 1, 2),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
for key in seasons:
    if month_number in seasons[key]:
        print(key)


# Использую списки (которые кортежи)

month_number = int(input('Введи номер месяца от 1 до 12 '))
month_list = ((12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
seasons_list = ('Зима', 'Веснa', 'Лето', 'Осень')
for i in month_list:
    if month_number in i:
        print(seasons_list[month_list.index(i)])


