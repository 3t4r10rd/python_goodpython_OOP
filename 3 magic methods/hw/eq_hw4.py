class Morph:
    def __init__(self, *args):
        self.words = list(args)

    def add_word(self, word):
        self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        t_words = list(map(lambda x: x.lower(), self.words))
        return other.lower() in self.words


dict_words = [Morph("связь", "связи", "связью", "связям"),
              Morph("формула", "формулы", "формуле", "формулой"),
              Morph("вектор", "вектора", "вектору", "вектором"),
              Morph("эффект", "эффекта", "эффекту", "эффектом", "эффекте"),
              Morph("день", "дня", "дню", "днем", "дне", "дни")]

text = "Мы будем устанавливать связь завтра днем."

res = sum(list(x == i for x in text.strip('.,!?-').split() for i in dict_words))

print(res) 