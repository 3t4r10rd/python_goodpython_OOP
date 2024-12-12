class Goods: #базовый класс
    def __init__(self, name, weight, price):
        super().__init__() #при создании дочерних классов функция значет, что нужно обратиться к инициализатору второго родительского класса
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog: #Пропишем Миксин для расширения функционала дочерних функций
    ID = 0
    def __init__(self):
        print('init MixinLog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

class NoteBook(Goods, MixinLog): #дочерних класс наследует сразу от двух базовых
    pass

n = NoteBook("Acer", 1.5, 30000)

n.print_info()
n.save_sell_log()

# C:\Python312\python.exe "J:\_learn\IT\Python\Добрый, добрый Python ООП\practis\4 inheritance polimorfism\multiple inheritance.py"
# init MixinLog
# init Goods
# Acer, 1.5, 30000
# 1: товар был продан в 00:00 часов