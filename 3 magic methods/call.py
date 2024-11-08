import math


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter

c = Counter()
c()
c()
c()
c()
print(c())



# Класс, который будет удалять определенные переменные сзади и спереди строки
class StripChars:
    def __init__(self, chars):
        self.__chars = chars
    def __call__(self, *args, **kwargs):
        return args[0].strip(self.__chars)

s1 = StripChars(' ')
s2 = StripChars(';.!')
st = "   Hello world.!;...."
res = s1(st)
res2 = s2(st)
print(res, res2, sep='\n')


#Определим класс-декоратор для расчета производной
class Derivate:
    #func - это, функция, производную которой будем считать
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.01, *args, **kwargs):
        return ((self.__fn(x+dx) - self.__fn(x)) / dx)


def df_sin(x):
    return math.sin(x)

print(df_sin(math.pi/4))
#Превратим функцию в экземлпяр класса, который возвращает производную функции
df_sin = Derivate(df_sin)


print(df_sin(math.pi/3))

@Derivate
def df_sin(x):
    return math.sin(x)