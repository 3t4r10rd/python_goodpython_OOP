 class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

 def set_coords(self, x1, y1):
     self.x1 = x1
     self.y1 = y1
class Line(Geom):
    def draw(self):
        print('Линия')


class Rect(Geom):
    def draw(self):
        print('Прямоугольнк')

l = Line()
r = Rect()
l.set_coords(1, 2)
r.set_coords(3, 4)





class Parent:
    x = 1

class Child(Parent):
    y = 2

c = Child()

print(c.y) # 2
print(c.x) # 1