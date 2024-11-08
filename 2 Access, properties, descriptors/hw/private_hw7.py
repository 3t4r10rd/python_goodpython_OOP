import random
from string import ascii_lowercase, digits

class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None


    lst1 = ascii_lowercase + digits
    lst = lst1 + '._'
    @classmethod
    def get_random_email(cls):

        x = random.randint(1, 100)
        name = ""
        for i in range(x):
            if i == 0 or i == x-1:
                name += random.choice(cls.lst1)
            else:
                name += random.choice(cls.lst)
        return f"{name}@gmail.com"

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        email = email.lower()
        c = email.split('@')

        if len(c) != 2:
            return False

        if set(email) < set(cls.lst) | set('@') \
            and len(c[0]) <= 100 \
            and len(c[1]) <= 50 \
            and email.find('..') == -1 \
            and c[1].find('.') != -1:
            return True
        else:
            return False


    @staticmethod
    def __is_email_str(email):
        return type(email) == str


res = EmailValidator.check_email("sc_libslis@t.ru")

print(res)

print(EmailValidator.get_random_email())