class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'Скорость {self.speed}, Превышение'
        else:
            return self.speed


class SportCar(Car):
    def show_speed(self):
        return self.speed


class WorkCar(Car):
    def show_speed(self):

        if self.speed > 40:
            return f'Скорость {self.speed}, Превышение'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

    def show_speed(self):
        return self.speed


a = SportCar(50, "Blue", "Toyota", False)
print(a.show_speed())
b = PoliceCar(150, "Toyota", "Blue")
print(b.show_speed(), b.is_police)
