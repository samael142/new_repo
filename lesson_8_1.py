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
        if n[0] not in range(1, 32) or n[1] not in range(1, 13) or n[2] not in range(1, 2021):
            return "Date is not valid"
        else:
            return "Date is valid"


b = Date('12-12-1979')
print(b)
c = Date("31 числа 2 месяца 2020 года нашей эры")
print(c)
