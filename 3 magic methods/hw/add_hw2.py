class ListMath:
    def __init__(self, lst=None):
        self.lst_math = list(filter(lambda x: type(x) in (int, float), lst)) if lst else []

    @property
    def lst_math(self):
        return self.__lst

    @lst_math.setter
    def lst_math(self, value):
        self.__lst = value

    def __add__(self, other):
        if type(other) in (int, float):
            return ListMath(list(map(lambda x: x + other, self.lst_math)))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.lst_math = [i + other for i in self.lst_math]
        return self

    def __sub__(self, other):
        if type(other) in (int, float):
            return ListMath(list(map(lambda x: x - other, self.lst_math)))

    def __rsub__(self, other):
        if type(other) in (int, float):
            return ListMath(list(map(lambda x: other - x, self.lst_math)))

    def __isub__(self, other):
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __mul__(self, other):
        if type(other) in (int, float):
            return ListMath(list(map(lambda x: x * other, self.lst_math)))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.lst_math = [i * other for i in self.lst_math]
        return self

    def __truediv__(self, other):
        if type(other) in (int, float):
            return ListMath(list(map(lambda x: x / other, self.lst_math)))

    def __rtruediv__(self, other):
        if type(other) in (int, float):
            return ListMath(list(map(lambda x: other / x, self.lst_math)))

    def __itruediv__(self, other):
        self.lst_math  = [i / other for i in self.lst_math]
        return self


lst = ListMath([1, 'abc', -5, 7.68, True])
print(lst.lst_math)
lst = lst + 76
print(lst.lst_math)
lst = 6.5 + lst
print(lst.lst_math)
lst = lst - 1
print(lst.lst_math)
lst = 7.0 - lst
print(lst.lst_math)
lst = lst * 2
print(lst.lst_math)
lst = 2 * lst
print(lst.lst_math)
lst = lst / 4
print(lst.lst_math)
lst = 0 / lst
print(lst.lst_math)
lst += 100
lst -= 10
lst *= 1000
lst /= 0.01
lst -= 8
print(lst.lst_math)