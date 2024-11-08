# import random
#
# class Cell:
#     def __init__(self, around_mines=0, mine=False):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = False
#
#
# class GamePole:
#     def __init__(self, N, M):
#         self.N = N
#         self.M = M
#         self.pole = [[Cell() for i in range(self.N)] for j in range(self.N)]
#         self.init()
#
#
#     def init(self):
#         x = self.M
#         while x:
#             i = random.randint(0, self.N - 1)
#             j = random.randint(0, self.N - 1)
#             if self.pole[i][j].mine:
#                 continue
#             else:
#                 self.pole[i][j].mine = True
#                 x += -1
#                 self.add_mines(i, j)
#
#
#     def add_mines(self, i, j):
#         for a in range(-1, 2):
#             for b in range(-1, 2):
#                 if (i + a) in range(0, self.N) and (j + b) in range(0, self.N):
#                     self.pole[i + a][j + b].around_mines += 1 if not self.pole[i+a][j+b].mine else 0
#
#
#     def show(self):
#         for i in self.pole:
#             print(*list(j.mine if j.fl_open else '#' for j in i))
#
#
#     def show_mines_and_around(self):
#         for i in self.pole:
#             print(*list('*' if j.mine else j.around_mines for j in i))
#
#
#
# pole_game = GamePole(10, 12)
#
#     # pole_game.show()
# pole_game.show_mines_and_around()
import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for i in range(N)] for j in range(N)]

    def add_mines_around(self, a, b):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (a + i in range(self.N)) and (b + j in range(self.N)):
                    self.pole[a + i][b + j].around_mines = self.pole[a + i][b + j].around_mines + 1 \
                        if not self.pole[a + i][b + j].mine \
                        else '*'


    def init(self):
        for i in range(self.M):
            a = random.randint(0, self.N-1)
            b = random.randint(0, self.N-1)
            if self.pole[a][b].mine:
                i -= 1
            else:
                self.pole[a][b].mine = True
                self.add_mines_around(a, b)

    def show(self):
         for i in self.pole:
            print(*list(j.around_mines if j.fl_open else '#' for j in i))


pole_game = GamePole(10, 12)

pole_game.init()
pole_game.show()








































