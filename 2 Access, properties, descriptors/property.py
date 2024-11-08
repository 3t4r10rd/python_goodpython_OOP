class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.__old = old
    @old.deleter
    def old(self):
        del self.__old


    # old = property(get_old, set_old) #добавляем в объект геттер и сеттер


p = Person('Сергей', 20)
p.get_old = '25' # тут используется как сеттер и записывает данные
print(p.get_old) # тут используется как геттер и возвращает данные
del p.old