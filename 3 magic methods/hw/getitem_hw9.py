class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = self.cols = 0
        self.__cells = {}

    def __check_index(self, x):
        if type(x) != int or x < 0:
            raise TypeError('не целое число')

    def __set_rows_cols(self, row, col):
        self.rows = row + 1 if self.rows < row else self.rows
        self.cols = col + 1 if self.cols < col else self.cols

    def add_data(self, row, col, data):
        self.__check_index(row)
        self.__check_index(col)
        self.__cells[(row, col)] = data
        self.__set_rows_cols(row, col)

    def remove_data(self, row, col):
        self.__check_index(row)
        self.__check_index(col)
        if self.__cells.pop((row, col), None):
            a = max(list(map(lambda x: x[0], self.__cells)))
            b = max(list(map(lambda x: x[1], self.__cells)))
            self.__set_rows_cols(a, b)
            # self.cols = max(list(map(lambda x: x[0], self.__cells))) if self.rows < row else self.rows
            # self.rows = max(list(map(lambda x: x[1], self.__cells))) if self.cols < col else self.cols
        else:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __getitem__(self, item):
        x = self.__cells.get(item, None)
        if x is None:
            raise ValueError('данные по указанным индексам отсутствуют')
        return x.value

    def __setitem__(self, key, value):
        self.add_data(key[0], key[1], Cell(value))



st = SparseTable()
st.add_data(2, 5, Cell('cell_25'))
st.add_data(0, 0, Cell('cell_00'))
st[2, 5] = 25
print(st[2, 5])
st[11, 7] = 'cell_117'
print(st[11, 7])
print(st[0, 0])
st.remove_data(2, 5)
print(st.rows, st.cols)
# val = st[2, 5]
# st.remove_data(12, 3)