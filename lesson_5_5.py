with open('lesson_5_5.txt', 'w') as f_obj:
    f_obj.write(input('Ввводи числа через пробел '))
with open('lesson_5_5.txt', 'r') as f_obj:
    content = f_obj.readline()

try:
    print(f'Сумма чисел в файле {sum(map(int, content.split()))}')
except ValueError as err:
    print(f'Файл не соответсвует стандарту. {err}')
