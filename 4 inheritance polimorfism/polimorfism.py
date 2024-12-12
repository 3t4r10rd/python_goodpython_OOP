class Geom:
    def get_pr(self):
        raise NotImplementedError('в дочернем классе должен быть метод get_pr()')

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)

class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)

geom = [r1, r2, s1, s2]

for g in geom:
    print(g.get_pr())