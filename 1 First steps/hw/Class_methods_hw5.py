# class Translator:
#
#     def add(self, eng, rus):
#         if 'dictionary' not in self.__dict__:
#             self.dictionary = dict()
#
#         if eng not in self.dictionary:
#             self.dictionary[eng] = set()
#         self.dictionary[eng].add(rus)
#
#     def remove(self, eng):
#         return self.dictionary.pop(eng, False)
#
#     def translate(self, eng):
#         return list(self.dictionary[eng]) if eng in self.dictionary else 'Слова нет в словаре'
#
#
# t = Translator()
#
# t.add('hello', "привет")
# t.add('hello', "приветики")
# print(t.dictionary)
# #t.remove('hello')
#
# res = t.translate('hello')
#
# print(res) if type(res) == str else print(*res)
#
#



class Translator:
    def add(self, eng, rus):
        if 'd' not in self.__dict__:
            self.d = {}
        if eng not in self.d:
            self.d[eng] = set()
        if rus not in self.d[eng]:
            self.d[eng].add(rus)


    def remove(self, eng):
        if self.d.get(eng, False):
            self.d.pop(eng)

    def translate(self, eng):
        if self.d.get(eng, False):
            return list(self.d[eng])


tr = Translator()
tr.add('tree', 'дерево')
tr.add('tree', '1дерево')

print(*tr.translate('tree'))



















