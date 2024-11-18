class CentralBank:


    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls

class Money:

    type_money = None
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def get_it(self, other):
        if not self.cb:
            raise ValueError('Неизвестен курс валют')
        if self.type_money is None:
            raise ValueError('Неизвестный тип валюты')

        return self.volume / self.cb.rates[self.type_money], other.volume / other.cb.rates[other.type_money]

    def __eq__(self, other):
        x, y = self.get_it(other)
        return (x - y) < 0.1

    def __le__(self, other):
        x, y = self.get_it(other)
        return x < y

    def __lt__(self, other):
        x, y = self.get_it(other)
        return x <= y

class MoneyR(Money):
    type_money = 'rub'

class MoneyE(Money):
    type_money = 'euro'

class MoneyD(Money):
    type_money = 'dollar'


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyE(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print('неплохо')
else:
    print('надо поднажать')