class Note:

    notes = ("до", "ре", "ми", "фа", "соль", "ля", "си")
    tones = (-1, 0, 1)

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton


    def __setattr__(self, key, value):
        if key == '_name' and value not in self.notes or \
            key == '_ton' and value not in self.tones:
            raise ValueError("недопустимое значение аргумента")
        object.__setattr__(self, key, value)

class Notes:
    __slots__ = ("_do", "_re", "_mi", "_fa", "_solt", "_la", "_si")
    obj = None


    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super().__new__(cls, *args, **kwargs)

        return cls.obj

    def __del__(self):
        Notes.obj = None

    def __init__(self):

        self._do = Note('до', 0)
        self._re = Note('ре', 0)
        self._mi = Note('ми', 0)
        self._fa = Note('фа', 0)
        self._solt = Note('соль', 0)
        self._la = Note('ля', 0)
        self._si = Note('си', 0)


    def __getitem__(self, item):
        if len(self.__slots__) <= item:
            raise IndexError('недопустимый индекс')

        return getattr(self, self.__slots__[item])



n = Notes()

nota = n[6]

print(nota._name)