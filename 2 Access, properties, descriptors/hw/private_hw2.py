class Money:
    def __init__(self, money):
        self.__money = 0
        if self.__check_money(money):
            self.__money = money


    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money


    def get_money(self):
        return self.__money

    def add_money(self, mn):
        print(self.__money)
        print(mn.__money)
        self.__money += mn.__money

    @classmethod
    def __check_money(cls, money):
        return True if type(money) is int and money >= 0 else False

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()
m2 = mn_2.get_money()

print(m1, m2)