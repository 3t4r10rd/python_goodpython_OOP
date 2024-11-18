class Record:
    pk = 0

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.pk
        Record.pk += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)





class DataBase:
    def __init__(self, path):
        if type(path) != str:
            raise ValueError('Неверный тип данных')
        self.path = path
        self.dict_db = {}


    def get_eq(self, i, lst):
        return [x for x in lst if x == i]

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        for i in self.dict_db:
            if i.pk == pk:
               return i

        return


lst_in = ['Б; пр; 33',
          'к; р-н; 35',
          "с; пол; 42",
          "ив; ф в п с; 26",
          "б; преп; 33"]

db = DataBase('База данных')

def get_lst(s):
    a, b, c = list(map(str.strip, s.split(';')))
    print(a, b, c)
    return a, b, int(c)

[db.write(Record(*get_lst(i))) for i in lst_in]

print(db.dict_db)

