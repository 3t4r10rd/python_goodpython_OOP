class Dimensions:

    MIN_DIMENSIONS = 10
    MAX_DIMENSIONS = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_volume(self):
        return self.a * self.b * self.c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.MIN_DIMENSIONS <= value <= self.MAX_DIMENSIONS:
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.MIN_DIMENSIONS <= value <= self.MAX_DIMENSIONS:
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.MIN_DIMENSIONS <= value <= self.MAX_DIMENSIONS:
            self.__c = value

    def __eq__(self, other):
        return self.get_volume() == other.get_volume()

    def __le__(self, other):
        return self.get_volume() < other.get_volume()

    def __lt__(self, other):
        return self.get_volume() <= other.get_volume()


class ShopItem:
    def __init__(self, name, price, dim):
        if not (isinstance(name, str) and isinstance(price, (int, float)) and isinstance(dim, Dimensions)):
            raise ValueError('Неверный тип данных')
        self.name = name
        self.price = price
        self.dim = dim

    def __str__(self):
        return self.name



lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
ShopItem('табуретка', 2000.99, Dimensions(50, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

print([str(x) for x in lst_shop])
print([str(x) for x in lst_shop_sorted])


