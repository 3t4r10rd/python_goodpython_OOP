class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight



class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__all_bag = []

    def __is_correct_index(self, indx):
        if (not type(indx) == int) or (not 0 <= indx < len(self.__all_bag)):
            raise IndexError('неверный индекс')

    def __check_weight(self, thing, old_thing=0):
        if sum(map(lambda x: x.weight, self.__all_bag)) + thing.weight - old_thing > self.max_weight:
            raise ValueError('превышен максимальный вес предметов')


    def add_thing(self, thing):
        self.__check_weight(thing)
        self.__all_bag.append(thing)

    def __getitem__(self, item):
        self.__is_correct_index(item)
        return self.__all_bag[item]

    def __delitem__(self, key):
        self.__is_correct_index(key)
        self.__all_bag.pop(key)

    def __setitem__(self, key, value):
        self.__is_correct_index(key)
        self.__check_weight(value, self.__all_bag[key].weight)
        self.__all_bag[key] = value


bag = Bag(1000)
bag.add_thing(Thing('книга1', 100))
bag.add_thing(Thing('книга2', 200))
bag.add_thing(Thing('книга3', 500))
bag.add_thing(Thing('книга4', 300))
print(bag[2].name)
bag[1] = Thing("платок", 100)
print(bag[1].name)
del bag[0]
print(bag[0].name)
t = bag[4]