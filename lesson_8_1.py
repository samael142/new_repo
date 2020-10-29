import re


class Date:

    def __init__(self, str_date):
        self.date = Date.parse_date(str_date)
        self.some_parameter = "some_parameter"

    @classmethod
    def parse_date(cls, str_date):
        date_list = (re.findall('\d+', str_date))
        dd, mm, yyyy = int(date_list[0]), int(date_list[1]), int(date_list[2])
        return dd, mm, yyyy

    def __str__(self):
        return Date.validation(self.date)

    @staticmethod
    def validation(n):
        if n[0] in range(1, 32):
            if n[1] in range(1, 13):
                if n[2] in range(1, 2021):
                    return "Всё верно"
                else:
                    return "Неправильный год"
            else:
                return "Неправильный месяц"
        else:
            return "Неправильный день"


b = Date('12-01-1979')
print(b)
c = Date("32 числа 12 месяца 2020 года нашей эры")
print(c)
