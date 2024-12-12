class IteratorAttrs:
    def __iter__(self):
        for i in self.__dict__.items():
            yield i

class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone('Айфон', 10, 256)

for attr, value in phone:
    print(attr, value)