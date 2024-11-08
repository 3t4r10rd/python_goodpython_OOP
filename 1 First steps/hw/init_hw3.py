# # здесь объявите класс TriangleChecker
# class TriangleChecker:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if self.a <= 0 or self.b <= 0 or self.c <= 0 or (type(self.a) not in (float, int) or
#                                              type(self.b) not in (float, int) or
#                                              type(self.c) not in (float, int)):
#             return 1
#         if max(self.a, self.b, self.c) > self.a + self.b + self.c - max(self.a, self.b, self.c):
#             return 2
#         else:
#             return 3
#
#
# a, b, c = 0, 4, 5
# # здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
#
# tr = TriangleChecker(a, b, c)
#
# print(tr.is_triangle())



class TriangleChecker:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def is_triangle(self):
        if type(self.a) not in (int, float) or type(self.b) not in (int, float) or type(self.c) not in (int, float) or min(self.a, self.b, self.c) <= 0:
            return 1
        return 2 if max(self.a, self.b, self.c) > self.a + self.b + self.c - max(self.a, self.b, self.c) else 3



tr = TriangleChecker(3, 4, 'lol')

print(tr.is_triangle())


























