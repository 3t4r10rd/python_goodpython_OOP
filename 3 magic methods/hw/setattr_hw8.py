import time

class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and getattr(self, key, False):
            return
        super().__setattr__(key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and getattr(self, key, False):
            return
        super().__setattr__(key, value)

class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and getattr(self, key, False):
            return
        super().__setattr__(key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100
    check_slots = {1: Mechanical, 2: Aragon, 3: Calcium}



    def __init__(self):
        self.slots = [None, None, None]


    def add_filter(self, slot_num, filtr):
        if self.slots[slot_num - 1] == None and self.check_slots[slot_num] == type(filtr):
            self.slots[slot_num - 1] = filtr



    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None 

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        if all(self.slots) and all(filter(lambda x: 0 <= x.date - time.time() <= self.MAX_DATE_FILTER, self.slots)):
            return True
        return False






my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()
print(w)
f1, f2, f3 = my_water.get_filters()
print(f1, f2, f3)
my_water.add_filter(3, Calcium(time.time()))
my_water.add_filter(2, Calcium(time.time()))
my_water.remove_filter(2)
print(my_water.slots)