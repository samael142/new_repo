lines = 1
n_line = 0
with open('lesson_5_2.txt', 'r') as f_obj:
    for line in f_obj:
        n_line = line.split().count('line')
        print(f'Строка {lines} - {len(line.split())} слова, из них слово line - {n_line} раз')
        lines += 1
print(f'Строк: {lines - 1}')
