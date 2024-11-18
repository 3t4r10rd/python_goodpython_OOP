class Track:
    def __init__(self, x, y):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError('Ошибка типа данных')
        self.start_x = x
        self.start_y = y
        self.lst = []

    def add_track(self, tr):
        if isinstance(tr, TrackLine):
            self.lst.append(tr)

    def get_track(self):
        return tuple(self.lst)

    def __len__(self):

        f = ((self.lst[0].to_x - self.start_x) ** 2 + (self.lst[0].to_y - self.start_y) ** 2) ** 0.5
        res = sum((((self.lst[i].to_x - self.lst[i-1].to_x) ** 2 + (self.lst[i].to_y - self.lst[i-1].to_y) ** 2) ** 0.5) for i in range(1, len(self.lst)))
       
        return int(f + res)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        if not (isinstance(to_x, (int, float)) and \
                isinstance(to_y, (int, float)) and \
                isinstance(max_speed, int)):
            raise TypeError('Ошибка типа данных')
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


tr1 = Track(0,0)
tr1.add_track(TrackLine(2, 4, 100))
tr1.add_track(TrackLine(5, -4, 100))

tr2 = Track(0, 1)
tr2.add_track(TrackLine(3, 2, 90))
tr2.add_track(TrackLine(10, 8, 90))

print(len(tr1), len(tr2))

print(tr1 == tr2)
print(tr1 != tr2)
print(tr1 > tr2)
print(tr1 < tr2)