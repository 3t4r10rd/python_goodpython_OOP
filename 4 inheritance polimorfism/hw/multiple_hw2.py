class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView

class ShopGenericView:

    def __str__(self):
        return "\n".join(map(lambda i: f"{i}: {self.__dict__[i]}", self.__dict__.keys()))

    def __repr__(self):
        return self.__str__

class ShopUserView:
    def __str__(self):
        l = len(self.__dict__.keys())
        result = ''
        for k, i in enumerate(self.__dict__.keys()):
            if i != '_id':
                result += f"{i}: {self.__dict__[i]}"
                result += '\n' if k != len(self.__dict__.keys())-1 else ''

        return result

    def __repr__(self):
        return self.__str__

class Book1(ShopItem, ShopGenericView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

class Book2(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

book1 = Book1("Python ООП", "Балакирев", 2022)
print(book1)

print()

book2 = Book2("Python ООП", "Балакирев", 2022)
print(book2)
