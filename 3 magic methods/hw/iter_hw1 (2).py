class Person:
    def __init__(self, fio, job, old, salary, years_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.years_job = years_job
        self.__attrs = list(self.__dict__.values())
        self.__i = -1

    def __getitem__(self, item):
        if item in range(5):
            return self.__attrs[item]

    def __setitem__(self, key, value):
        if key in range(5):
            self.__attrs[key] = value
        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.__i = -1
        return self

    def __next__(self):
        if self.__i < len(self.__attrs) - 1:
            self.__i += 1
            return self[self.__i]
        raise StopIteration




p = Person('Гейтс', "бизнесмен", 61, 1000000, 46)
p[0] = 'Балакирев'
for v in p:
    print(v)
