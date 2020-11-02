class NotNum(Exception):

    def __init__(self):
        self.txt = "This is not a number"

    def __str__(self):
        return self.txt


class ListOfNums:

    def __init__(self):
        self.my_list = []

    def collect_nums(self):

        while True:
            try:
                user_enter = input("Enter number: ")
                if user_enter.isdigit():
                    self.my_list.append(int(user_enter))
                    print(f"Current List {self.my_list}")
                else:
                    raise NotNum
            except NotNum as err:
                return f"{err}\n Current List {self.my_list}"


a = ListOfNums()
print(a.collect_nums())
