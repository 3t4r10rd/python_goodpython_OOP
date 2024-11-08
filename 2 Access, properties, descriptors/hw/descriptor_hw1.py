class FloatValue:

    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Только вещественный тип данных")
        setattr(instance, self.name, value)


class Cell:

    value = FloatValue()
    def __init__(self, v = 0.0):
        self.value = v


class TabletSheet:
    def __init__(self, n, m):
        self.cells = [[Cell() for i in range(n)] for j in range(m)]


table = TabletSheet(5, 3)

i = 1
for x in table.cells:
    for y in x:
        y.value = float(i)
        i += 1


for x in table.cells:
    print('-----------')
    for y in x:
        print(y.value)
print('-----------')






