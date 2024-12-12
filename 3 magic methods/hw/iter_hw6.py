class Matrix:
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == list:
            self.lst = args[0]
            for i in self.lst:
                if len(i) != len(self.lst) or not (all(map(lambda x: type(x) == int, i))):
                    raise TypeError('неверный список')
        else:
            rows, cols, fill_value = args
            if type(rows) != int or type(cols) != int or not (type(fill_value) in (int, float)):
                raise TypeError('неверный тип данных')
            self.rows = rows
            self.cols = cols
            self.fill_value = fill_value
            self.lst = [[fill_value for _ in range(rows)] for _ in range(cols)]

    def __getitem__(self, item):
        return self.lst[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.lst[key[0]][key[1]] = value

    def __add__(self, other):
        if type(other) == Matrix and len(self.lst) != len(other.lst):
            raise ValueError('матрицы разных размерностей')
        res_lst = []
        for i in range(len(self.lst)):
            res_lst.append([])
            for j in range(len(self.lst[i])):
                res_lst[i].append(self.lst[i][j] + other.lst[i][j]) if type(other) == Matrix else res_lst[i].append(self.lst[i][j] + other)

        return Matrix(res_lst)

    def __sub__(self, other):
        if type(other) == Matrix and len(self.lst) != len(other.lst):
            raise ValueError('матрицы разных размерностей')
        res_lst = []
        for i in range(len(self.lst)):
            res_lst.append([])
            for j in range(len(self.lst[i])):
                res_lst[i].append(self.lst[i][j] - other.lst[i][j]) if type(other) == Matrix else res_lst[i].append(self.lst[i][j] - other)

        return Matrix(res_lst)


mt1 = Matrix([
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2],
])

mt2 = Matrix(3, 3, 10)

res = mt1 + 5

print(res.lst)