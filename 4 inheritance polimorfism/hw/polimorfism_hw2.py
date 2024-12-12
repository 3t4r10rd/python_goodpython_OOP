class ShopInterface:
    def get_id(self):
        raise NotImplementedError('не переопределен метод get_id()')


class ShopItem(ShopInterface):
    _id = 1

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__class__._id
        self.__class__._id += 1

    def get_id(self):
        return self.__id


s1 = ShopItem('товар1', 5, 500)
s2 = ShopItem('товар2', 3, 300)

print(s2.get_id())
