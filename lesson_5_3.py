staff = 0
all_salary = 0
with open('lesson_5_3.txt', 'r') as f_obj:
    for line in f_obj:
        if int(line.split()[-1]) < 20000:
            print(line)
        staff += 1
        all_salary += int(line.split()[-1])
print(f'\nВсего сотрудников {staff}, средняя зарплата {all_salary / staff}')
