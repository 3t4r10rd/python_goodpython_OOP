class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.__lst = [cell()] * max_length

    def __getitem__(self, item):
        return self.__lst[item].value

    def __setitem__(self, key, value):
        self.__lst[key].value = value

    def __str__(self):
        return " ".join(map(str, self.__lst))

class Integer:
    def __init__(self, start_value=0):
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return str(self.__value)

class Float:
    def __init__(self, start_value=0.0):
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != float:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return str(self.__value)


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)
ar_int[1] = 10
# ar_int[1] = 10.5
# ar_int[10] = 1


