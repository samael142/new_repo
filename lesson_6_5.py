class Stationery:

    def __init__(self, title=None):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):

    def __init__(self):
        super().__init__(title="Pen")

    def draw(self):
        return f"Запуск отрисовки инструментом {self.title}"


class Pencil(Stationery):

    def __init__(self):
        super().__init__(title="Pencil")

    def draw(self):
        return f"Запуск отрисовки инструментом {self.title}"


class Handle(Stationery):

    def __init__(self):
        super().__init__(title="Handle")

    def draw(self):
        return f"Запуск отрисовки инструментом {self.title}"


a = Pen()
print(a.draw())
b = Pencil()
print(b.draw())
c = Handle()
print(c.draw())
d = Stationery()
print(d.draw())
