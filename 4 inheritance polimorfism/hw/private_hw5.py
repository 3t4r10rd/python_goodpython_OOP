# def class_log(lst):
#
#     def func_decorated(func):
#         def wrapper(*args, **kwargs):
#             lst.append(func.__name__)
#             return func(*args, **kwargs)
#         return wrapper
#
#     def f(cls):
#         methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#         for k, v in methods.items():
#             setattr(cls, k, func_decorated(v))
#
#         return cls
#     return f

class class_log1:
    def func_decorated(self, func):
        def wrapper(*args, **kwargs):
            self.lst.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper

    def __init__(self, lst):
        self.lst = lst

    def __call__(self, cls, *args, **kwargs):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, self.func_decorated(v))

        return cls



vector_log = []   # наименование (vector_log) в программе не менять!


@class_log1(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
v[1] = 11
print(vector_log)