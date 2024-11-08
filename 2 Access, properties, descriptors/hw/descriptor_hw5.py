class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        a = []
        for i in self.items:
            if i.uid == indx:
                a.append(i)
        [self.items.remove(i) for i in a]

class Telecast:
    def __init__(self, num, name, long):
        self.__id = num
        self.__name = name
        self.__duration = long

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.name = value


    @property
    def duration(self):
        return self.__duration


    @duration.setter
    def duration(self, value):
        self.duration = value

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, 'Доброе утро', 10000))
pr.add_telecast(Telecast(2, 'Новости', 2000))
pr.add_telecast(Telecast(2, 'Интервью', 20))
pr.remove_telecast(2)
for i in pr.items:
    print(f"{i.name}: {i.duration}")
