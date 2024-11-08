class Book:
    def __init__(self, a='', b='', c=0, d=0):
        self.title = a
        self.author = b
        self.pages = c
        self.year = d

    def __setattr__(self, key, value):
        if (key in ('title', 'author') and not isinstance(value, str)) or \
            (key in ('pages', 'year') and not isinstance(value, int)):
            raise ValueError('Ошибка')
        else:
            print(super(), '\n', object)
            super().__setattr__(key, value)




book = Book('lol', 'kek', 3, 4)

print(book.__dict__)