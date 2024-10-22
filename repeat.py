class Point:
    color = 'red'
    circle = 2

s1 = Point()
s2 = Point()
s2.circle = 3

b = s1.circle

print(id(b))
print(id(Point.circle))