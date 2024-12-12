class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        # self.__len = len(self.lst) - 1

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i+1):
                yield self.lst[i][j]


    # def __iter__(self):
    #     self.__row = 0
    #     self.__col = -1
    #     self.__step = 1
    #     return self
    #
    # def __next__(self):
    #     self.__col += 1 #0, 1
    #     if self.__col >= self.__step:
    #         self.__row += 1 #1
    #         self.__col = 0 #0
    #         self.__step += 1
    #
    #     if self.__row > self.__len:
    #         raise StopIteration
    #
    #     return self.lst[self.__row][self.__col] #00,10




lst = [['00'],
       ['10', '11'],
       ['20', '21', '22'],
       ['30', '31', '32', '34']
      ]

it = TriangleListIterator(lst)

for x in it:
    print(x)
