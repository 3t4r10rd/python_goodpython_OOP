class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #переопределим __getattribute__
    def __getattribute__(self, item):
        if item =='x':
            raise ValueError("Нельзя обращаться к перемнной x")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value


    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)


pt1 = Point(1, 2)


pt1.x # __getattrbute__








# __setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
# __delattr__(self, item) - автоматически вызывается при удалении свойства item (неважно, существующего или нет)