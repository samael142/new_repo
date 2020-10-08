words = input('Введи несколько слов через пробел ').split()
for number, element in enumerate(words):
    print(number + 1, element[0:10])
