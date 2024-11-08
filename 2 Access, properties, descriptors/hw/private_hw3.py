class Book:
    def __init__(self, author, title, price):
        self.__title = 'author'
        self.__author = 'title'
        self.__price = price


    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_(self):
        return self.__title

    def get_(self):
        return self.__author

    def get_price(self):
        return self.__price