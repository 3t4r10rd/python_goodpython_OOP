import math

class PathLines:
    def __init__(self, *args):
        self.lst_lines = list((LineTo(0, 0), )) + list(args)
        # self.lst_lines = [LineTo(0, 0)]
        #
        # for i in args:
        #     self.add_line(i)


    def get_path(self):
        return self.lst_lines

    def get_length(self):
        sum = 0
        for i in range(1, len(self.lst_lines)):
             sum += math.sqrt((self.lst_lines[i].x - self.lst_lines[i-1].x) ** 2 +
                       (self.lst_lines[i].y - self.lst_lines[i - 1].y) ** 2)
        return sum

    def get_length2(self):
        g = ((self.lst_lines[i-1], self.lst_lines[i]) for i in range(1, len(self.lst_lines)))
        return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g))



    def add_line(self, line):
        self.lst_lines.append(line)

class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))

print(p.get_path())
print(p.get_length())
print(p.get_length2())