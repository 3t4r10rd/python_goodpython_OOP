class Box3D:
    def __init__(self, w, h, d):
        if not (type(w) in (int, float) and type(h) in (int, float) and type(d) in (int, float)):
            raise TypeError('Неправильный тип данных')
        self.width = w
        self.height = h
        self.depth = d

    def __is_Correct(self, val):
        if not type(val) in (Box3D, int, float):
            raise TypeError('Неправильный тип данных')
    def __add__(self, other):
        self.__is_Correct(other)
        w = self.width + other.width if type(other) == Box3D else self.width + other
        h = self.height + other.height if type(other) == Box3D else self.height + other
        d = self.depth + other.depth if type(other) == Box3D else self.depth + other
        return Box3D(w, h, d)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        self.__is_Correct(other)
        w = self.width * other.width if type(other) == Box3D else self.width * other
        h = self.height * other.height if type(other) == Box3D else self.height * other
        d = self.depth * other.depth if type(other) == Box3D else self.depth * other
        return Box3D(w, h, d)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other


    def __sub__(self, other):
        self.__is_Correct(other)
        w = self.width - other.width if type(other) == Box3D else self.width - other
        h = self.height - other.height if type(other) == Box3D else self.height - other
        d = self.depth - other.depth if type(other) == Box3D else self.depth - other
        return Box3D(w, h, d)

    def __truediv__(self, other):
        self.__is_Correct(other)
        w = self.width / other.width if type(other) == Box3D else self.width / other
        h = self.height / other.height if type(other) == Box3D else self.height / other
        d = self.depth / other.depth if type(other) == Box3D else self.depth / other
        return Box3D(w, h, d)

    def __floordiv__(self, other):
        self.__is_Correct(other)
        w = self.width // other.width if type(other) == Box3D else self.width // other
        h = self.height // other.height if type(other) == Box3D else self.height // other
        d = self.depth // other.depth if type(other) == Box3D else self.depth // other
        return Box3D(w, h, d)

    def __mod__(self, other):
        self.__is_Correct(other)
        w = self.width % other.width if type(other) == Box3D else self.width % other
        h = self.height % other.height if type(other) == Box3D else self.height % other
        d = self.depth % other.depth if type(other) == Box3D else self.depth % other
        return Box3D(w, h, d)

    def __str__(self):
        return f"{(self.width, self.height, self.depth)}"


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box2 % 3
print(box)
