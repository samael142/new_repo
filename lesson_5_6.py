import re


lessons = {}
with open('lesson_5_6.txt', 'r', encoding='UTF-8') as f_obj:
    for line in f_obj:
        lessons[line.split(':')[0]] = sum(map(int, re.findall('\d+', line.split(':')[1])))
print(lessons)
