input_string = None
with open('lesson_5_1_out.txt', 'w', encoding='UTF-8') as f_obj:
    while input_string != '':
        input_string = input()
        f_obj.write(f'{input_string}\n')
