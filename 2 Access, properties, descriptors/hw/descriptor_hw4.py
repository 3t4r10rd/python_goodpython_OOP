class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.things.append(thing)
        else:
            print(f"Добавить \"{thing.name}\" не получится, не влазит по весу")

    def remove_thing(self, indx):
        self.things.pop(indx, False)

    def get_total_weight(self):
        return sum(i.weight for i in self.things)

class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight



bag = Bag(1000)
bag.add_thing(Thing("Книга 1", 100))
bag.add_thing(Thing("Книга 2", 200))
w = bag.get_total_weight()
print(f"Предельный вес: {bag.max_weight}, занято: {w}")
for t in bag.things:
    print(f"{t.name}: {t.weight}")