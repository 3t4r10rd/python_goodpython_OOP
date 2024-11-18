class Clock:
    __DAY = 86400

    def __init__(self, seconds: int): #
        if not isinstance(seconds, int):
            raise TypeError("Введите целое число")
        self.seconds = seconds % self.__DAY


    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24

        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')


    def __add__(self, other): #other - это значение, которое стоит от значения +
        if not isinstance(other, int):
            raise ArithmeticError('Должно быть целое число')
        return Clock(self.seconds + other)


c1 = Clock(1000)
print(c1.get_time()) # 00:16:40

c1.seconds = c1.seconds + 100
print(c1.get_time())


def __add__(self, other):  # other - это значение, которое стоит  справа от значения +
    if isinstance(other, int):
         return Clock(self.seconds + other)
    if isinstance(other, Clock):
        return Clock(self.seconds + other.seconds)

def __iadd__(self, other):
    return self.seconds + other




