class ListInteger(list):
    def __init__(self, x):
        if x:
            for i in x:
                if type(i) != int:
                    raise TypeError('только целые числа')
        super().__init__(x)

    def __setitem__(self, key, value):
        if type(value) != int:
            raise TypeError('только целые числа')

        return super().__setitem__(key, value)

    def append(self, __object):
        if type(__object) != int:
            raise TypeError('только целые числа')

        return super().append(__object)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5