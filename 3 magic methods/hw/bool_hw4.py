class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args
        else:
            self.x1 = None

    def __bool__(self):
        return not (self.x1 is None)

    def get_coords(self):
        if self:
            return (self.x1, self.y1, self.x2, self.y2)
        raise AttributeError('Нет координат')



lst_geom = [Ellipse(), Ellipse(), Ellipse(0, 1, 2, 3), Ellipse(3,4, 5, 6)]



for i in lst_geom:
    if i:
        print(i.get_coords())
