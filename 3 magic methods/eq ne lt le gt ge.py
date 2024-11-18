class Clock:
    __DAY = 86400 #число секунд в одном дне

    def __init__(self, seconds):
        self.seconds = seconds % self.__DAY

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Неверный тип данных')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Неверный тип данных')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

    def __le__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Неверный тип данных')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds <= sc

c1 = Clock(1000)
c2 = Clock(1000)

print(c1 < c2) # True