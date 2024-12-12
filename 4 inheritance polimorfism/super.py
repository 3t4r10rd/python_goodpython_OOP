class Geom:
    name = 'Geom'
    def __init__(self, x):
        self.x = x

class Line(Geom):
    def __init__(self, x, y):
        super().__init__(x) 
        self.y = y


l = Line(1, 2)
print(l.__dict__)