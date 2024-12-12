class Animal:
    def __init__(self, name, kind, old):
        self.name = name
        self.kind = kind
        self.old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


animals = [
    Animal('Васька', "Дворцовый кот", 5),
    Animal('Рекс', "Немецкая овчарка", 8),
    Animal('Кеша', "Попугай", 3)
]

print(animals)