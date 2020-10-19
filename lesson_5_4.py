eng_dig = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
rus_dig = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
in_list = []
with open('lesson_5_4.txt', 'r') as f_obj_in:
    for line in f_obj_in:
        in_list.append(line.split()[0])
with open('lesson_5_4_out.txt', 'w', encoding='UTF-8') as f_obj_out:
    for el in in_list:
        f_obj_out.write(f'{rus_dig[eng_dig.index(el)]} - {eng_dig.index(el) + 1}\n')
