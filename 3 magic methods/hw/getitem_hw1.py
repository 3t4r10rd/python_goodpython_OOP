class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__lst_attr = list(self.__dict__)
        print(self.__lst_attr)
        # for i in kwargs.keys():
        #     self.__dict__[i] = kwargs[i]
        #     self.__lst_attr.append(i)

    def __getitem__(self, item):
        if len(self.__lst_attr) <= item:
            raise IndexError('Неверный индекс поля')
        # return self.__dict__[self.__lst_attr[item]]
        return getattr(self, self.__lst_attr[item])
    def __setitem__(self, key, value):
        if len(self.__lst_attr) <= key:
            raise IndexError('Неверный индекс поля')
        setattr(self, self.__lst_attr[key], value)
        # self.__dict__[self.__lst_attr[key]] = value
        




r = Record(pk=1, title='python', author = 'Балакирев')
r[0] = 2

r[1] = 'Супер курс'
r[2] = "Балакирев С.М."
# r[3] = 'lol'

print(r[0], r[1], r[2])
