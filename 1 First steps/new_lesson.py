# __new__() - вызывается перед созданием объекта класса
# в методе new обязательный параметр cls, который ссылается на класс
# метод new должен возвращать адрес нового созданного объекта return super().__new__(cls), иначе экземпляр не создастся


class Point:
    def __new__(cls,  ):
        print("new " + str(cls))
        return super().__new__(cls)

    def __init__(self, x = 0, y = 0):
        print("init " + str(self))
        self.x = x
        self.y = y


pt = Point()


# Паттерн Singleton - если может быть только 1 экземпляр объекта, а все новые экземпляры должны ссылаться на первый

    class DataBase:
         __instance = None # будет ссылкой на экземпляр класса
         #если экземпляра класса нет, то будет None
         #таким образом, можно контролировать, существует ли объект класса

         def __new__(cls, *args, **kwargs):
             if cls.__instance is None:
                 cls.__instance = super().__new__(cls) # если экземпляра еще нет - запишет его адрес в инстанс
             return cls.__instance # вернет ссылку на адрес единственного экземпляра

         def __del__(self):
             """
             Вызывается при удалении объекта
             :return: 
             """""
            DataBase.__instance = None # при удалении объекта, очистит переменную с адресом экземпляра
         def __init__(self, user, psw):
             '''
             Инициализация экземляра класса
             :param user: Имя пользователя
             :param psw: Пароль
             '''
             self.user = user
             self.psw = psw

