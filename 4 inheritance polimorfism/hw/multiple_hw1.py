class Digit:
    def __init__(self, value):
        self.check_type(value)
        self.check_value(value)
        self.value = value

    def check_type(self, value):
        if not (type(value) in (int, float)):
            raise TypeError('значение не соответствует типу объекта')

    def check_value(self, value):
        pass

class Integer(Digit):
    def check_type(self, value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')

class Float(Digit):
    def check_type(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def check_value(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')

class Negative(Digit):
    def check_value(self, value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass

class FloatPositive(Float, Positive):
    pass

digits = [
    PrimeNumber(5),
    PrimeNumber(10),
    PrimeNumber(12),
    FloatPositive(11.1),
    FloatPositive(1.21),
    FloatPositive(13.1),
    FloatPositive(1.41),
    FloatPositive(15.1),
]


lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))

print(*map(lambda x: x.value, lst_positive))
print(*map(lambda x: x.value, lst_float))