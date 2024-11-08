class RadiusVector2D:

    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, a=0, b=0):
        self.__x = self.__y = 0
        self.x = a
        self.y = b

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, a):
        if (type(a) in (int, float) and
                RadiusVector2D.MIN_COORD <= a <= RadiusVector2D.MAX_COORD):
            self.__x = a

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, a):
        if (type(a) in (int, float) and
                RadiusVector2D.MIN_COORD <= a <= RadiusVector2D.MAX_COORD):
            self.__y = a

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2



v1 = RadiusVector2D()
v2 = RadiusVector2D(1)
v3 = RadiusVector2D(1, 2)

v3.x  = -101

print(RadiusVector2D.norm2(v3))