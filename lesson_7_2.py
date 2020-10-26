from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def square(self, *args):
        pass


class Coat(Clothes):

    def square(self, v):
        return f"Площадь ткани {v / 6.5 + 0.5}"


class Suit(Clothes):

    def square(self, h):
        return f"Площадь ткани {2 * h * 0.3}"


a = Coat()
b = Suit()

print(a.square(30))
print(b.square(140))
