class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __eq__(self, other):
        return len(self.lst_words) == len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __lt__(self, other):
        return len(self.lst_words) <= len(other.lst_words)


stich = ['Я к вам пишу - чего же боле?',
         'Что я могу еще сказать?',
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

chars = ' -?!,.;'

lst_text = [StringText(list(filter(len, map(lambda i: i.strip(chars), x.split())))) for x in stich]

lst_text_sorted = sorted(lst_text, reverse=True)

lst_text_sorted = [' '.join(i.lst_words) for i in lst_text_sorted]

print(lst_text_sorted)