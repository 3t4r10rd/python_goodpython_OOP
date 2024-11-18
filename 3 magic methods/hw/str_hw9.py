class PolyLine:
    def __init__(self, start_coord, *args):
        # self.start_coord = start_coord
        self.__coord = [start_coord] + [i for i in args]


    def add_coord(self, x, y):
        self.__coord.append((x, y))

    def remove_coord(self, indx):
        if indx < len(self.__coord):
            self.__coord.pop(indx)

    def get_coords(self):
        return self.__coord


poly = PolyLine((1,2), (3,5), (0,10), (-1,8))
poly.add_coord(5, 6)
poly.remove_coord(2)
print(poly.get_coords())


