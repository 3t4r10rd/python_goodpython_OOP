class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Автор"
    views = 14356
    comments = 12

class Goods:
    title = "Мороженое"
    weight = 153
    tp = "Еда"
    price = 1024

#Goods.price = 2048
#.inflation = 100

# или

setattr(Goods, 'inflation', 100)
setattr(Goods, 'price', 2048)

print(Goods.__dict__)


class Car:
    pass

setattr(Car, 'model', 'Тойтоа')
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', 'П111УУ77')

print(Car.__dict__['color'])


class Notes:
    uid = 1005435
    title = 'Шутка'
    author = 'И.С. Бах'
    pages = 2

a1 = getattr(Notes, 'author')
print(a1)

class Dictionary:
    rus = 'Питон'
    eng = 'Python'

a2 = getattr(Dictionary, 'rus_world', False)

print(a2)
