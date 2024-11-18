class Ingridient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self):
        self.i_List = []

    def add_ingridient(self, ing):
        if isinstance(ing, Ingridient):
            self.i_List.append(ing)

    def remove_ingridient(self, ing):
        if isinstance(ing, Ingridient) and ing in self.i_List:
            self.i_List.remove(ing)

    def get_ingridients(self):
        return tuple(self.i_List)

    def  __len__(self):
        return len(self.i_List)



recipie = Recipe()
ing1 = Ingridient("Соль", 1, "столовая ложка")
recipie.add_ingridient(ing1)
recipie.add_ingridient(Ingridient("Мука", 1, "кг"))
recipie.add_ingridient(Ingridient("Мясо баранины", 10, "кг"))
recipie.remove_ingridient(ing1)
ings = recipie.get_ingridients()
print(ings)
n = len(recipie)
print(n)

