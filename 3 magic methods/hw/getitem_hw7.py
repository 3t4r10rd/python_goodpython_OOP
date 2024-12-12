class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0


    def __bool__(self):
        return self.is_free

class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3))for _ in range(3))

    def clear(self):
        for i in self.pole:
            for j in i:
                j.is_free = True
                j.value = 0

    def __getitem__(self, item):
        x = True
        for i in item:
            if type(i) == slice:
                x = False
        if x:
            return self.pole[item[0]][item[1]].value

        return " ".join([str(x.value) for x in self.pole[item[0]][item[1]]])


    def __setitem__(self, key, value):
        if self.pole[key[0]][key[1]].is_free:
            self.pole[key[0]][key[1]].value = value
            self.pole[key[0]][key[1]].is_free = False


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
print(game[0, 0], game[1, 0])
v1 = game[0, :]
v2 = game[:, 0]
print(v1)
