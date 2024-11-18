class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        len_first = len(matrix[0])
        if len_first == 0:
            return [[]]
        if type(matrix) != list:
            raise ValueError("Неверный формат")
        for i in matrix:
            if list(filter(lambda x: type(x) != int, i)) or len_first != len(i):
                raise ValueError("Неверный формат")

        res = []
        lst = []
        tmp = []
        a0 = b0 = 0
        a1, b1 = self.size

        while True:

            for i in range(a0, a1):
                for j in range(b0, b1):
                    tmp.append(matrix[i][j])
            lst.append(max(tmp))
            tmp = []

            if b1 + self.size[0] <= len_first:
                b0 = b1
                b1 += self.size[0]
            else:
                res.append(lst)
                lst = []

                if a1 + self.size[1] <= len(matrix):
                    a0 = a1
                    a1 += self.size[1]
                    b0 = 0
                    b1 = self.size[0]
                else:
                    break
        return res

mp = MaxPooling()
res = mp([[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]])

lst1 = [[5, 0, 88, 2, 7, 65],
        [1, 33, 7, 45, 0, 1],
        [54, 8, 2, 38, 22, 7],
        [73, 23, 6, 1, 15, 0],
        [4, 12, 9, 1, 76, 6],
        [0, 15, 10, 8, 11, 78]]

res1 = mp(lst1)

print(res1)






