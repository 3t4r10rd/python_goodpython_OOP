class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_into_exhibit(self, indx):
        if 0 <= indx <= len(self.exhibits) - 1:
            print(f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}")


class Picture:

    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:

    def __init__(self, name, location, descr):
        self.name = name
        self.author = location
        self.descr = descr

class Papyri:

    def __init__(self, name, date, descr):
        self.name = name
        self.author = date
        self.descr = descr


mus = Museum('Эрмитаж')
mus.add_exhibit(Picture('Картина', "Неизвестный автор", "Красивая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россиия", "Просветитель"))
p = Papyri('Ученья для', "Древняя Россиия", "Рукописное свидетельств обучения")
mus.add_exhibit(p)

for x in range(len(mus.exhibits)):
    mus.get_into_exhibit(x)