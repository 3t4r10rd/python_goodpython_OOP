class ValidateString:
    def __init__(self, min=3, max=100):
        self.min_length = min
        self.max_length = max

    def validate(self, string):
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator):
        if isinstance(validator, ValidateString):
            self.validator = validator
        else:
            raise TypeError('Данные некорректны')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class RegisterForm:

    login = StringValue(ValidateString(3, 100))
    password = StringValue(ValidateString(3, 100))
    email = StringValue(ValidateString(3, 100))

    def __init__(self, a, b, c):
        self.login = a
        self.password = b
        self.email = c

    def get_fields(self):
        return [self.__dict__[i] for i in self.__dict__]

    def show(self):
        print(f"<form>\n"
              f"Логин: {self.login}\n"
              f"Пароль: {self.password}\n"
              f"Email: {self.email}\n"
              f"</form>")



rg = RegisterForm('Андрей', "123", "маил@маил.рф")

rg.show()