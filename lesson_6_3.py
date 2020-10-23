class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def get_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Ivan', 'Ivanov', 'Manager', 10000, 3000)
print(f'{a.get_fullname()} - {a.get_income()}')
