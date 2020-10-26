# Ну, раз работа творческая, сделал со звёздочками.

class Cell:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return Cell.stars(self.amount)

    def __add__(self, other):
        return Cell.stars(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return Cell.stars(self.amount - other.amount)
        else:
            return "Большая клетка пожрала маленькую и отравилась"

    def __mul__(self, other):
        return Cell.stars(self.amount * other.amount)

    def __truediv__(self, other):
        if self.amount > other.amount != 0:
            return Cell.stars(round(self.amount / other.amount))
        else:
            return "Большая клетка пожрала маленькую и отравилась"

    def make_order(self, row):
        order = ""
        for i in range(self.amount // row):
            order += f"{'*' * row}\\n"
        order += f'{"*" * (self.amount % row)}'
        return order

    @staticmethod
    def stars(n):
        return ''.join("*" for el in range(n))


a = Cell(7)
b = Cell(2)
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(2))
print(b.make_order(3))
