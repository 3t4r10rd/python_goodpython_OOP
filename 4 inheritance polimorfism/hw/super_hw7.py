class StringDigit(str):
    @classmethod
    def __check_digit(self, s):
        if any(char.isdigit() is False for char in s):
            raise ValueError('в стркое должны быть только цифры')

    def __new__(cls, *args, **kwargs):
        cls.__check_digit(args[0])
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, value):
        super().__init__()
        self.value = value

    def __add__(self, other):
        if isinstance(other, str):
            self.__check_digit(other)
            return StringDigit(self.value + other)

    def __radd__(self, other):
        return self + other

sd = StringDigit('123')
print(sd)
sd = sd + str('4562')
print(type(sd))