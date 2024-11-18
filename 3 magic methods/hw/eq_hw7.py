class Body:
    def __init__(self, name, ro, value):
        self.name = name
        self.ro = ro
        self.value = value

    def m(self):
        return self.ro * self.value

    def get_compare(self, other):
        if not type(other) in (int, Body):
            raise ValueError('Ошибка')

        return other.m() if type(other) == Body else other

    def __eq__(self, other):
        return self.m() == self.get_compare(other)

    def __le__(self, other):
        return self.m() < self.get_compare(other)

    def __lt__(self, other):
        return self.m() <= self.get_compare(other)



body1 = Body('1', 5, 6)
body2 = Body('2', 7, 4)

print(body1 == 30)