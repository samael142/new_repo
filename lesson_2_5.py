my_list = [7, 5, 3, 3, 1]
new_element = int(input('Введи число '))
if new_element < min(my_list):
    my_list.append(new_element)
else:
    if new_element in my_list:
        for element in my_list[::-1]:
            if new_element == element:
                my_list.insert(my_list.index(element) + 1, new_element)
                break
    else:
        for i in range(0, len(my_list)):
            if new_element > my_list[i]:
                my_list.insert(i, new_element)
                break
print(my_list)

# Решение обратной сортировкой. Не знаю, правильно или нет.

my_list = [7, 5, 3, 3, 1]
new_element = int(input('Введи число '))
my_list.append(new_element)
my_list.sort(reverse=True)
print(my_list)
