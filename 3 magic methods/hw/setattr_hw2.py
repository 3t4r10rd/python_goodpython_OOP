class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if self.goods.count(product):
            self.goods.remove(product)


class Product:
    id = 1
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product.id
        Product.id += 1


    def __setattr__(self, key, value):
        check_atr = {'id': int, 'name': str, 'weight': int, 'price': int }
        if check_atr[key] == type(value):
            return object.__setattr__(self, key, value)
        else:
            # print(check_atr[key])
            # print(type(value))
            raise AttributeError('Неверный тип присваиваимых данных')

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError('Атрибут id удалять запрещено')
        else:
            object.__delattr__(self, item)



shop = Shop('Магазин')
book = Product('Python ООП', 100, 10)
shop.add_product(book)
shop.add_product(Product('Python', 150, 512))

for p in shop.goods:
    print(f'{p.id}, {p.name}, {p.weight}, {p.price}')


