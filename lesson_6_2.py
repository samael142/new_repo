class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def formula(self, asphalt_width):
        self.asphalt_width = asphalt_width
        return f'{(self._length * self._width * 25 * self.asphalt_width) // 1000} т'


a = Road(5000, 20)
print(a.formula(5))

b = Road(5000, 20)
print(b.formula(1))
