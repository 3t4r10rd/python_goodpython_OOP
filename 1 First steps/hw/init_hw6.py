# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#
#     def remove(self, indx):
#         self.goods.pop(indx) if indx in range(len(self.goods)) else None
#
#     def get_list(self):
#         return [f"{i.name}:{i.price}" for i in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
#
# t = Table("стол",1500)
# tv = TV("Самсунг", 15000)
# nb = Notebook("ASUS", 25000)
# c = Cup('lattecup', 800)
#
# cart.add(t)
# cart.add(tv)
# cart.add(nb)
# cart.add(c)
# cart.remove(10)
#
# print(cart.get_list())




class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx) if indx < len(self.goods) else print("Нет такого индекса")

    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price



cart = Cart()

cart.add(Table('Стол', 1500))
cart.add(Notebook('Ноутбук', 25000))
cart.add(TV('Телевизор', 13000))
cart.add(Cup('Кружки', 300))

cart.remove(9)
print(cart.get_list())






















