# import random
# class Line:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c,d)
#
# class React:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Ellipse:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# elements = [random.choice([Line(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)),
#        React(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)),
#        Ellipse(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))])
#             for i in range(217)]
#
# for i in elements:
#     if type(i) == Line:
#         i.sp, i.ep = 0, 0
#
# [print(elements[i].__dict__) for i in range(50)]
#
#
#
import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)

rnd = [Line, Rect, Ellipse]

elements = [
    random.choice(rnd)(random.random(), random.random(), random.random(), random.random())
    for i in range(217)
]

for el in elements:
    if type(el) is Line:
        # print(el)
        el.sp = (0, 0)
        el.ep = (0, 0)


print(elements[0], elements[0].__dict__)


















