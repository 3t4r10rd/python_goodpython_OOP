class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []


    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
        if type(other) == int:
            self.book_list.pop(other)
        return self

    def __isub__(self, other):
        return self - other



lib = Lib()

book_1 = Book('Книга 1', "Автор 1", 2000)
book_2 = Book('Книга 2', "Автор 2", 2000)
book_3 = Book('Книга 3', "Автор 3", 2000)

lib = lib + book_1 + book_2 + book_3

lib -= 0

print([i.title for i in lib.book_list])
