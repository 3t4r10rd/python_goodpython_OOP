class Item:
    def __init__(self, name, money):
        if not (type(name) is str and type(money) in (int, float)):
            raise TypeError('Неправильный тип данных')
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other

    def __radd__(self, other):
        return self + other


class Budget:
    def __init__(self):
        self.__items = []

    def __is_correct(self, i, t):
        if not isinstance(i, t):
            raise TypeError('Неправильный тип данных')
    def add_item(self, it):
        self.__is_correct(it, Item)
        if not self.__items.count(it):
            self.__items.append(it)

    def remove_item(self, num):
        self.__is_correct(num, int)
        if num in range(len(self.__items)):
            self.__items.pop(num)

    def get_items(self):
        return self.__items if len(self.__items) else None


my_budget = Budget()
i_1 = Item('Курс по Python', 2000)
i_2 = Item('Курс по Django', 5000.01)
i_3 = Item('Курс по NumPy', 0)

my_budget.add_item(i_1)
my_budget.add_item(i_2)
my_budget.add_item(i_3)

s = 0
for x in my_budget.get_items():
    s = s + x

print(s)

