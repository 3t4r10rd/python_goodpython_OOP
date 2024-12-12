class ItemAttrs:
    def __getitem__(self, item):
        return getattr(self, list(self.__dict__.keys())[item])

    def __setitem__(self, key, value):
        self.__dict__[list(self.__dict__.keys())[key]] = value

class Point(ItemAttrs):
    def __init__(self, x, y):

        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]
y = pt[1]
pt[0] = 5
print(x, y)
print(pt.__dict__)
