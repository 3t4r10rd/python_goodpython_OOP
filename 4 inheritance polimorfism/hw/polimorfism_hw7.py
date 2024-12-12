class PointTrack:
    def __init__(self, x ,y):
        self.__check_points(x, y)
        self.x = x
        self.y = y

    def __check_points(self, x, y):
        if not (type(x) in (int, float) and type(y) in (int, float)):
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *args):
        self.__points = []

        if isinstance(args[0], PointTrack):
            self.__points += list(args)

        if self.__is_digits(args):
            self.__points.append(PointTrack(args[0], args[1]))

    def __is_digits(self, t):
        return len(t) == 2 and type(t[0]) in (int, float) and type(t[1]) in (int, float)

    @property
    def points(self):
        return tuple(self.__points)


    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points = list(pt) + self.__points

    def pop_back(self):
        self.__points.pop(-1)

    def pop_front(self):
        self.__points.pop(0)



tr = Track(0, 0)
tr.add_back(PointTrack(1.4, 0))
# tr.pop_front()
for pt in tr.points:
    print(pt)
