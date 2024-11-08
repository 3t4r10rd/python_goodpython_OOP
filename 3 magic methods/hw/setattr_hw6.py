class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, val):
        self.__radius = val

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if key in ('x', 'y'):
            if not type(value) in (int, float):
                raise TypeError("Неверный тип данных")
        elif key == 'radius':
            if not type(value) in (int, float):
                raise TypeError("Неверный тип данных")
            elif value < 0:
                return

        super().__setattr__(key, value)



circle = Circle(10.5, 7, 22)

circle.radius = -10

x, y = circle.x, circle.y

res = circle.name

print(circle.radius, res)