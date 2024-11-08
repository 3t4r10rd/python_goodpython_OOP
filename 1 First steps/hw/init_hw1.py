# # 1-------------------------
# class Money:
#     def __init__(self, money):
#         self.money = money
#
# my_money = Money(100)
#
# # 2--------------------------
#
# class Point():
#
#     def __init__(self, x, y, color = 'black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = [Point(x, x) for x in range(1, 2000, 2)]
#
# points[1].color = 'yellow'
#
# print(points[1].__dict__)
#
#
#1------------------------------------------------

class Money:

    def __init__(self, money=0):
        self.money = money


m1 = Money(100)
m2 = Money(1000)
m3 = Money()

print(m1.money, m2.money, m3.money)

#2------------------------------------------------

class Point:

    def __init__(self, x=0, y=0, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) for i in range(1, 2000, 2)]

points[1].color = 'yellow'

print(len(points))
print(points[0].color, points[1].color)































