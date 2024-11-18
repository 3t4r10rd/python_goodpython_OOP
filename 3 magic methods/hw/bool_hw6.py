class Vector:
    def __init__(self, *args):
        self.coords = args


    def __is_correct(self, a, b):
        if len(a) != len(b):
            raise ArithmeticError('размерности ветокров не совпадают')
    def __len__(self):
        return len(self.coords)
    def __add__(self, other):
        new_coords = []

        if type(other) == int:
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + other)

        if type(other) == Vector:
            self.__is_correct(self, other)
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] + other.coords[i])

        return Vector(*new_coords)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        new_coords = []

        if type(other) == int:
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - other)

        if type(other) == Vector:
            self.__is_correct(self, other)
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - other.coords[i])

        return Vector(*new_coords)

    def __rsub__(self, other):
        self.__is_correct(self, other)
        new_coords = []
        for i in range(len(self.coords)):
            new_coords.append(other.coords[i] - self.coords[i])
        return Vector(*new_coords)

    def __isub__(self, other):
        return self - other


    def __mul__(self, other):
        self.__is_correct(self, other)
        new_coords = []
        for i in range(len(self.coords)):
            new_coords.append(self.coords[i] * other.coords[i])
        return Vector(*new_coords)

    def __eq__(self, other):
        self.__is_correct(self, other)
        a = self.coords
        b = other.coords
        for i in range(len(a)):
            if a[i] != b[i]:
                return False

        return True


v1 = Vector(1, 2, 3, 4)
v2 = Vector(1, 2, 3, 4)

print(v1 == v2)