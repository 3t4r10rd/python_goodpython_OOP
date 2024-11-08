class PhoneBook:

    def __init__(self):
        self.phone_book = list()
    def add_phone(self, phone):
        if isinstance(phone, PhoneNumber):
            self.phone_book.append(phone)

    def remove_phone(self, indx):
        if indx < len(self.phone_book) - 1:
            self.phone_book.pop(indx)

    def get_phone_list(self):
        return self.phone_book


class PhoneNumber:

    def __new__(cls, *args, **kwargs):
        if cls.__isNumber(args[0]) and isinstance(args[1], str):
            return super().__new__(cls)
        return None

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

    @classmethod
    def __isNumber(cls, number):
        if isinstance(number, int) and len(str(number)) == 11:
            return True
        else:
            return False



p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, 'Сергей Сергеев'))
p.add_phone(PhoneNumber(21345678901, 'Панда'))
p.add_phone(PhoneNumber(123, 'Лол'))
phones = p.get_phone_list()
print([i.__dict__ for i in phones])
