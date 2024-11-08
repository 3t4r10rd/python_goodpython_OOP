from accessify import private, protected

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y


    #объявим приватный метод класса для проверки формата данных
    @protected
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    #объявим сеттер для доступа к приватным атрибутам
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    #объявим геттер, для вывода значений приватных атрибутов

    def get_coord(self):
        return self.__x, self.__y



pt = Point()

pt.check_value(5)