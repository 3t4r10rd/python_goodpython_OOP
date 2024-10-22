# Декораторы @classmethod и @staticmethod

# classmethod - работает исключительно с атрибутами класса, можно вызывать только через класс
# staticmethod - не имеют доступ ни к атрибутам класса, ни к атрибутам экземпляра
class Vector:
    MIN = 0
    MAX = 100

    @classmethod # - работает исключительно с атрибутами класса, можно вызывать
    # только через класс Vector.validate(5)
    def vlidate(cls, arg):
        return cls.MIN <= arg <= cls.MAX


    def __init__(self, x, y):
        self.x = self.y = 0
        if self.vlidate(x) and self.vlidate(y):
            self.x = x
            self.y = y


    @staticmethod
    def norm2(x, y): # сервисная функция, которая работает автономна
        return x*x + y*y

v = Vector(0, 1)

v1 = Vector(0, 1000)
print(v1.y)
print(v.y)

print(Vector.norm2(5, 6))
