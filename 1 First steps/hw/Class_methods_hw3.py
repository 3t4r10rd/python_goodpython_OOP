# import sys
#
# # здесь объявляется класс StreamData
# class StreamData:
#     def create(self, fields, lst_values):

#         if len(fields) == len(lst_values):
#             for x in range(len(fields)):
#                 setattr(self, fields[x], lst_values[x])
#             return True
#
#         else:
#             return False
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()
# print(data, result)
#
#
#
#
#
#
#
#


import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            [setattr(self, fields[i], lst_values[i]) for i in range(len(fields))]
            return True
        else:
            return False



class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readLines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readLines()

print(data, result)
print(data.__dict__)
