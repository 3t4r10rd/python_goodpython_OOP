class Track:
    def __init__(self, start_x, start_y):
        self.lst_coords = [[(start_x, start_y), 0]]

    def add_point(self, x, y, speed):
        self.lst_coords.append([(x, y), speed])

    def __getitem__(self, item):
        if item < 0 or item > len(self.lst_coords) - 2:
            raise IndexError('некорректный индекс')
        return self.lst_coords[item + 1]

    def __setitem__(self, key, value):
        if key < 0 or key > len(self.lst_coords) - 2:
            raise IndexError('некорректный индекс')
        self.lst_coords[key+1][1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)
tr.add_point(50, -20, 80)
tr.add_point(63.45, 1.24, 60.34)

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3]