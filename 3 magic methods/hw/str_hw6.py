import math

class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = [0] * args[0]
        if len(args) == 4:
            self.coords = list(args)

    def set_coords(self, *args):
        x = min(len(self.coords), len(args))
        for i in range(x):
            self.coords[i] = args[i]

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return math.sqrt(sum(map(lambda x: x * x, self.coords)))


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.get_coords())
a, b, c = vector3D.get_coords()
print(a, b, c)
vector3D.set_coords(3, -5.6, 8, 10, 11)
print(vector3D.get_coords())
vector3D.set_coords(1, 2)
print(vector3D.get_coords())
print(len(vector3D))
print(abs(vector3D))

