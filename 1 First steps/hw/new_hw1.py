# # 1----------------------------
#
# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Объекты нельзя создавать"
#
#
#
# obj = AbstractClass()
# print(obj)
#
# # 2-----------------------------
#
# class SingletonFive:
#     __way = None
#     __i = 0
#     def __new__(cls, *args, **kwargs):
#         if cls.__i < 6:
#              cls.__way = super().__new__(cls)
#              cls.__i += 1
#         return cls.__way
#
#
#
#     def __init__(self, name):
#         self.name = name
#
#
#
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]
#
# print(*objs)
#
#

class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка"


Obj = AbstractClass()
print(Obj)



#2-------
class SingletonFive:
    _i = 0
    _ins = None
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        print(cls._i)
        cls._i += 1
        if cls._i < 5:
            return super().__new__(cls)
        elif cls._i == 5:
            cls._ins = super().__new__(cls)
            return cls._ins
        else:
            return cls._ins

objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять
print(*objs)




























