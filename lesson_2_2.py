list_1 = input('Введи элементы списка через пробел').split()
for i in range(1, len(list_1), 2):
    list_1[i - 1], list_1[i] = list_1[i], list_1[i - 1]
print(list_1)




