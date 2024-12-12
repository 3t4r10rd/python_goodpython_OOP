class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square

class Agency:
    def __init__(self, name):
        self.name = name
        self.objs = []
    def add_object(self, obj):
        self.objs.append(obj)

    def remove_object(self, obj):
        if self.objs.count(obj):
            self.objs.remove(obj)

    def get_objects(self):
        return self.objs


ag = Agency('Рога и копыта')
ag.add_object(Flat("квартира", 10000000, 121.5, 3))
ag.add_object(Flat("квартира 2", 1000000, 74.5, 2))
ag.add_object(Flat("квартира 3", 7500000, 54, 1))
ag.add_object(House('дом кирпичный', price=35000000, material='кирпич', square=186.5))
ag.add_object(Land('участок', 30000000, 6.74))

for obj in ag.get_objects():
    print(obj.name)

print(*[x.name for x in ag.get_objects() if isinstance(x, House)])