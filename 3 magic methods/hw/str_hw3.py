class WordString:
    def __init__(self, string=None):
        self.string = string


    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        if value:
            while value.count('  '):
                value = value.replace('  ', ' ')
        self.__string = value

    def __len__(self):
        return len(list(self.string.split()))

    def __call__(self, indx, *args, **kwargs):
        return list(self.string.split())[indx]



words = WordString()
words.string = "Курс    по    Python"
n = len(words)
first = '' if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")