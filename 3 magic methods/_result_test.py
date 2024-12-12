import random


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.__size = 3
        self.pole = tuple(tuple(Cell() for _ in range(self.__size)) for _ in range(self.__size))

    def __check_index(self, index):
        i, j = index
        if not (type(i) == int and type(j) == int and 0 <= i < self.__size and 0 <= j < self.__size):
            raise IndexError('некорректно указанные индексы')
        return i, j

    def __getitem__(self, item):
        i, j = self.__check_index(item)
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i, j = self.__check_index(key)
        self.pole[i][j].value = value

    def __iter__(self):
        for i in range(self.__size):
            for j in range(self.__size):
                yield self.pole[i][j]

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL

    def show(self):
        for row in self.pole:
            for cell in row:
                match cell.value:
                    case self.HUMAN_X:
                        print('X', end=' ')
                    case self.COMPUTER_O:
                        print('O', end=' ')
                    case _:
                        print('-', end=' ')
            print()

    def human_go(self):
        i = True
        while i:
            step = input("Введите координаты хода через пробел: ").strip()
            if len(step) == 3 and step[0].isdigit() and step[-1].isdigit():
                x, y = self.__check_index(tuple(map(int, step.split())))
                if self[x, y] == self.FREE_CELL:
                    self[x, y] = self.HUMAN_X
                    i = self.FREE_CELL
                else:
                    print('Клетка уже занята, попробуйте выбрать другую')
            else:
                print('Координаты введены некорректно, попробуйте еще раз')

    def computer_go(self):
        i = True
        while i:
            x = random.randint(0, self.__size - 1)
            y = random.randint(0, self.__size - 1)
            if self[x, y] == self.FREE_CELL:
                self[x, y] = self.COMPUTER_O
                i = self.FREE_CELL
    @property
    def is_draw(self):
        return all([x.value != self.FREE_CELL for row in self.pole for x in row])

    def __is_anybody_win(self, value):
        s = []
        for i in self.pole:
            for j in i:
                s.append(j.value)

        x = [s[0:3:], s[3:6:], s[6:9:], s[0::3], s[1::3], s[2::3], s[0::4], s[2:7:2]]
        return any(map(lambda i: i[0] == value and i[1] == value and i[2] == value, x))

    @property
    def is_human_win(self):
        return self.__is_anybody_win(self.HUMAN_X)
    @property
    def is_computer_win(self):
        return self.__is_anybody_win(self.COMPUTER_O)

    def __bool__(self):
        return not (self.is_draw or self.is_human_win or self.is_computer_win)




game = TicTacToe()
game.init()
step_game = 0
while game:


    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
        game.show()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

