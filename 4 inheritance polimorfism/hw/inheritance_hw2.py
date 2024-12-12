class Thing:
    ID = 0
    def __init__(self, name, price):
        Thing.ID += 1
        self.id = Thing.ID
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    def get_data(self):
        return tuple(getattr(self, i) for i in self.__dict__ if not getattr(self, i) is None)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims

class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm

table = Table('Круглый', 1024, 812.55, (700, 750, 700))
book = ElBook('Python ООП', 2000, 2048, 'pdf')

print(*table.get_data())
print(*book.get_data())