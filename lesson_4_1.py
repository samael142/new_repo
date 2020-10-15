from sys import argv

script_name, salary, work_time, bonus = argv


def my_func():
    money = int(salary) * int(work_time) + int(bonus)
    return money


print(my_func())
