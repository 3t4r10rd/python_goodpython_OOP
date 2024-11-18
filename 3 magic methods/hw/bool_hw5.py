from random import randint

class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = True

    @staticmethod
    def __is_correct(value, tp):
        if type(value) != tp:
            raise ValueError('недопустимое значенние атрибута')

    @property
    def is_mine(self):
        return self.__is_mine
    @is_mine.setter
    def is_mine(self, value):
        self.__is_correct(value, bool)
        self.__is_mine = value

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, value):
        self.__is_correct(value, int)
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open
    @is_open.setter
    def is_open(self, value):
        self.__is_correct(value, bool)
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open



class GamePole:
    __instanse = None
    __mines = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for i in range(M)) for i in range(N))


    def __new__(cls, *args, **kwargs):
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)
        return cls.__instanse

    def __del__(self):
        GamePole.__instanse = None


    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for i in self.pole:
            for j in i:
                j.is_mine = False
                # j.is_open = False

        l = self.total_mines
        while (l):
            a = randint(0, self.N - 1)
            b = randint(0, self.M - 1)
            if self.pole[a][b].is_mine == False:
                self.pole[a][b].is_mine = True
                l -= 1
                for i,j in self.__mines:
                    if 0 <= a + i < self.N and 0 <= b + j < self.M:
                        self.pole[a+i][b+j].number += 0 if self.pole[a+i][b+j].is_mine else 1




    def open_cell(self, i, j):
        if i > self.M or j > self.N:
            raise IndexError('некорректные индексы')
        self.pole[i][j].is_open = True


    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: '#' if x else x.number if not x.is_mine else '*', row))

        # for i in self.pole:
        #     print('\n')
        #     for j in i:
        #         if j.is_open:
        #             print('*', end=' ') if j.is_mine else print(j.number, end=' ')
        #         else:
        #             print('#', end=' ')



pole = GamePole(10, 20, 10)
# pole.show_pole()
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.show_pole()