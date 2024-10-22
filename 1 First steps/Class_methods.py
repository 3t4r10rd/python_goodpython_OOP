# Методы - это функции внутри классов

class Point:
    color = 'red'
    circle = 2

    def set_coards(self, x, y): # self указывается всегда, если планируется вызов из экземпляра,
        # потому что self ссылается на экземпляр, из которого вызван метод
        # сам метод не копируется в экземпляры
        self.x = x # переменные создадутся локально в экземпляре
        self.y = y

    def get_coords(self):
        return (self.x, self.y) # вернет атрибуты конкретного экземпляра, из которого метод был вызван
pt = Point()


pt.set_coards(1, 2)

print(pt.__dict__)

# При вызове метода через экземпляр класса, в вызов метода(функции) подставляется параметр self, который
# является ссылкой на экземпляр класса, из которого был вызван метод


pt2 = Point()

pt2.set_coards(10, 20)
print(pt2.__dict__)

print(pt.get_coords(), pt2.get_coords())