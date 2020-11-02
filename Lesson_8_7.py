class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(2, -4)
c_2 = ComplexNumber(7, 8)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)
