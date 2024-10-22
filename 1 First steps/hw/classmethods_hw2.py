#
# from string import ascii_lowercase, digits
#
# # здесь объявляйте классы TextInput и PasswordInput
# class TextInput:
#
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size = 10):
#         if self.check_name(name):
#             self.name = name
#         else:
#             raise ValueError("некорректное поле name")
#         self.size = size
#
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#
#     @classmethod
#     def check_name(cls, name):
#         if 3 > len(name) or len(name) > 50:
#             return False
#         for i in name:
#             if i not in cls.CHARS_CORRECT:
#                 return False
#
#         return True
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size = 10):
#         if self.check_name(name):
#             self.name = name
#         else:
#             raise ValueError("некорректное поле name")
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if 3 > len(name) or len(name) > 50:
#             return False
#         for i in name:
#             if i not in cls.CHARS_CORRECT:
#                 return False
#
#         return True
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
# print(html)




from string import ascii_lowercase, digits

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size
        else:
            raise ValueError("некорректное поле name")
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            return False
        for ch in name:
            if ch not in cls.CHARS_CORRECT:
                return False
        return True

class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS #+ CHARS.upper() + digits
    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size
        else:
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            return False
        for ch in name:
            if ch not in cls.CHARS_CORRECT:
                return False
        return True


# эти строчки не менять
login = FormLogin(TextInput("hlo"), PasswordInput("word"))
html = login.render_template()

print(html)



















