class NewList:
    def __init__(self, *args):
        self.lst = list(*args)

    def get_list(self):
        return self.lst

    def __sub__(self, other):
        f = self.lst[:]
        if isinstance(other, list):
            sub = other
        if isinstance(other, NewList):
            sub = other.get_list()

        for i in sub:
            for j in range(len(f)):
                if i == f[j] and type(i) == type(f[j]):
                    f.pop(j)
                    break

        return NewList(f)

    def __rsub__(self, other):
        sub = self.lst[:]
        if isinstance(other, list):
            f = other
        if isinstance(other, NewList):
            f = other.get_list()

        for i in sub:
            for j in range(len(f)):
                if i == f[j] and type(i) == type(f[j]):
                    f.pop(j)
                    break

        return NewList(f)

    def __isub__(self, other):
        return self - other


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2
print(res_1.get_list())
lst1 -= lst2
print(lst1.get_list())
res_2 = lst2 - [0, True]
print(res_2.get_list())
res_3 = [1, 2, 3, 4.5] - res_2
print(res_3.get_list())
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a
print(res_4.get_list())