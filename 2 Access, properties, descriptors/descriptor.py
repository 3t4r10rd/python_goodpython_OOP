class Integer:
    #при объявлении дескриптора в классе автоматически сработает функция __set_name
    def __set_name__(self, owner, name):
        # self - ссылка на экземпляр класса дескриптора Integer
        # owner - ссылка на класс, в котором объявляется экземпляр класса дескриптора - x = Integer()
        # name - переменная, которой присваивается экземпляр класса
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        # return instance.__dict__[self.name]


    def __set__(self, instance, value):
        setattr(instance, self.name, value)
        # instance.__dict__[self.name] = value

        #self - ссылка на экземпляр класса дескриптора Integer
        #instance - ссылается на ЭКЗЕМПЛЯР класса, из которого дескриптор был вызван
        #value - числовое значение, которое присваивается


class GetInt:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Point3D:

    x = Integer() #дескриптор для координаты x
    y = Integer()
    z = Integer()

    xr = GetInt()



    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



pt = Point3D(1, 2, 3)
print(pt.__dict__)
print(pt.xr) #1
print(Point3D.__dict__)
