class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

class CellString:
    def __init__(self, start_value='#'):
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) != str:
            raise ValueError('возможны только строковые значения')
        self.__value = value

class CellInteger:

    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

class TabletValues:
    def __init__(self, rows, cols, cell=None):
        if cell is None:
            raise ValueError('Параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cell = cell

        self.cells = tuple(tuple(cell() for i in range(cols)) for i in range(rows))

    def __getitem__(self, item):
        a, b = item
        return self.cells[a][b].value

    def __setitem__(self, key, value):
        a, b = key
        self.cells[a][b].value = value


table = TabletValues(2, 3, cell=CellString)

print(table[0, 1])

table[1, 0] = '5'
table[0, 2] = '1'

print(table.cells)

for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()