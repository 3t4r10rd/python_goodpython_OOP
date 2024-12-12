class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, d=None):
        d = {} if d is None else d
        if d:
            for x in d.keys():
                if not isinstance(x, Thing):
                    raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__()


    def __setitem__(self, key, value):
        if type(key) != Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)


thing1 = Thing('Лыжи', 11000, 30)
thing2 = Thing('Книга', 1500, 2)
dict_things = DictShop()
dict_things[thing1] = thing1
dict_things[thing2] = thing2

for x in dict_things:
    print(x.name)

# dict_things[1] = thing1