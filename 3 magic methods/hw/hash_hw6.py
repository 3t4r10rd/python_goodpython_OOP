import math


class Coord:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not (type(value) in (int, float) and value > 0):
            raise ValueError('Должно быть положительным')

        setattr(instance, self.name, value)



class Triangle:
    a = Coord()
    b = Coord()
    c = Coord()

    def __init__(self, a, b, c):

        if self.is_not_triangle(a, b, c):
            raise ValueError('Нельзя образовать треугольник')

        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return int(self.a + self.b + self.c)

    def tr(self):
        p = len(self) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


    @staticmethod
    def is_not_triangle(a, b, c):
        return max(a, b, c) >= a + b + c - max(a, b, c)


tr1 = Triangle(2, 4, 5)

print(len(tr1), tr1.tr())