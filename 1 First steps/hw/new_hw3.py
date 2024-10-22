# class Point:
#
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def clone(self):
#         return Point(self.x, self.y)
#
#
#
#
# pt = Point(1, 2)
# pt1 = pt.clone()
#
# print(pt.__dict__, pt1.__dict__)




class Point:
    def __init__(self, x ,y):
        self.x, self.y = x, y

    def clone(self):
        return Point(self.x, self.y)

pt1 = Point(1, 2)

print(pt1.__dict__)

pt_clone = pt1.clone()

print(pt_clone.__dict__)

print(pt1, pt_clone)















