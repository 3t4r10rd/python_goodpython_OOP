class Cell:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __repr__(self):
        return str(self.data)


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.__tbl = tuple(tuple((Cell()) for _ in range(rows)) for _ in range(cols))

    def __iter__(self):
        for i in self.__tbl:
            yield i

    def __check_indx(self, indx):
        if type(indx[0]) != int or type(indx[1]) != int or \
                indx[0] < 0 or indx[1] < 0 or \
                indx[0] > self.rows or indx[1] > self.cols:
            raise IndexError('неверный индекс')


    def __getitem__(self, item):
        self.__check_indx(item)
        return self.__tbl[item[0]][item[1]].data

    def __setitem__(self, key, value):
        self.__check_indx(key)
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.__tbl[key[0]][key[1]].data = value

tv1 = TableValues(4, 5)



tv1[0, 1] = 5

for row in tv1:
    for value in row:
        print(value, end=' ')
    print()