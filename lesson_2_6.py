structure = []
answer = '0'
structure_position = 1
analysis = {}
analysis_list = []
while answer != '1':
    goods = input('Введи название товара ')
    price = int(input('Введи цену товара '))
    quantity = int(input('Введи количество '))
    unit = input('Введи единицу измерения ')
    structure.append((structure_position,
                      {'название': goods,
                       'цена': price,
                       'количество': quantity,
                       'ед': unit}))
    structure_position += 1
    answer = input('Ещё товар? Любая кнопка - Да, 1 - нет ')
for key in structure[0][1]:
    for value in structure:
        analysis_list.append(value[1][key])
    analysis[key] = analysis_list
    analysis_list = []
print('\n')
for item in structure:
    print(item)
print('\n')
for key, value in analysis.items():
    print(key, value)
