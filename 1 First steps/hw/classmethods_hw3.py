# from string import ascii_lowercase, digits
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
#     @staticmethod
#     def check_card_number(number):
#
#         x = number.split('-')
#         if len(x) != 4:
#             return False
#         if not all(map(lambda i: len(i) == 4, x)):
#             return False
#         if not all(map(lambda i: i.isdigit(), x)):
#             return False
#
#         # for i in x:
#         #     if len(i) != 4:
#         #         return False
#         #     for j in i:
#         #         if not j.isdigit():
#         #             return False
#
#         return True
#
#     @classmethod
#     def check_name(cls, name):
#         x = name.split(' ')
#         if len(x) != 2:
#             return False
#
#         return all(map(lambda i: set(i) < set(cls.CHARS_FOR_NAME),x))
#
#
#         # if (not (set(name.split(' ')[0]) < set(cls.CHARS_FOR_NAME)) and
#         #         (not (set(name.split(' ')[1]) < set(cls.CHARS_FOR_NAME)))):
#         #     print('lol')
#         #     return False
#         # print(set(name))
#         # print(set(cls.CHARS_FOR_NAME))
#         # return True
#
#
# is_number = CardCheck.check_card_number("1244-5678-1111-0000")
# is_name = CardCheck.check_name("YAMONEY V")
#
# print(is_number, is_name)
#
#

from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits + ' '

    @staticmethod
    def check_card_number(number):
        if type(number) != str:
            return False
        l1 = list(number.split('-'))
        for i in l1:
            if len(i) != 4 or not i.isdigit():
                return False
        return True
    @classmethod
    def check_name(cls, name):
        if type(name) != str:
            return False
        if set(name) < set(cls.CHARS_FOR_NAME) and len(name.split(' ')) == 2:
            return True
        return False


is_number = CardCheck.check_card_number("1144-5678-1111-0000")
is_name = CardCheck.check_name("YAMONEY V")

print(is_number, is_name)
