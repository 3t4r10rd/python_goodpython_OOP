class IterColumn:
    def __init__(self, lst, indx):
        self.lst = lst
        self.indx = indx


    def __iter__(self):
        for i in self.lst:
            yield i[self.indx]


lst = [['00', '01', '02'],
       ['10', '11', '12'],
       ['20', '21', '22'],
       ['30', '31', '32']
]

it = IterColumn(lst, 1)


for x in it:
    print(x)

it_iter = iter(it)
x = next(it_iter)