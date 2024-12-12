class Vector:
    def __init__(self, *args):
        self.coords = list(args)
        self.len_vector = len(self.coords)
        self._allowed_types = (int, float)
        for x in self.coords:
            if type(x) not in self._allowed_types:
                raise ValueError('координаты должны быть целыми числами')

    def get_coords(self):
        return tuple(self.coords)



    def _check_vector(self, other):
        if self.len_vector != other.len_vector:
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self._check_vector(other)
        fl = all(map(lambda x: type(x) in self._allowed_types, self.coords)) and all(map(lambda x: type(x) in self._allowed_types, other.coords))

        for i in range(self.len_vector):
            self.coords[i] += other.coords[i]

        return self.__class__(*self.coords) if fl else Vector(*self.coords)

    def __sub__(self, other):
        self._check_vector(other)
        fl = all(map(lambda x: type(x) == int, self.coords)) and all(map(lambda x: type(x) == int, other.coords))

        for i in range(self.len_vector):
            self.coords[i] -= other.coords[i]

        return self.__class__(*self.coords) if fl else Vector(*self.coords)

class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__(*args)
        self._allowed_types = (int, )
        for x in self.coords:
            if type(x) not in self._allowed_types:
                raise ValueError('координаты должны быть целыми числами')


v1 = VectorInt(1, 2, 3, 4)
v2 = Vector(1, 2, 3, 4)
v3 = v1 + v2

print(v3.coords)
print(type(v3))