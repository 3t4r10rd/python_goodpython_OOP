class GeomRange:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.v = self.a

    def __next__(self):
        if self.v < self.c:
            d = self.v
            self.v *= self.b
            return d
        else:
            raise StopIteration
    def __iter__(self):
        self.v = self.a
        return self



g = GeomRange(1, 1.2, 2)

it = iter(g)
res = next(g)