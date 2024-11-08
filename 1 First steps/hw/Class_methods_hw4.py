# import sys
#
# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def select(self, a, b):
#         return list(filter(lambda x: a <= self.lst_data.index(x) <= b, self.lst_data))
#
#     def insert(self, data):
#         for i, k in enumerate(data):
#             self.lst_data.append({})
#             x =  0
#             for j in k.split():
#                 self.lst_data[i][self.FIELDS[x]] = j
#                 x += 1
#
#
# db = DataBase()
# db.insert(lst_in)
# print(db.select(0, 10))


import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self, a, b):
        b = min(len(self.lst_data)-1, b)
        return self.lst_data[a:b+1]

    def insert(self, data):
        for x in data:
            d = {}
            for i, k in enumerate(x.split()):
                d[self.FIELDS[i]] = k
            self.lst_data.append(d)




db = DataBase()
db.insert(lst_in)

print(db.select(0, 10))
