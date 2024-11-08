import random

class RandomPassword:
    def __init__(self, psw_chars, min_lenght, max_lenght):
        self.psw_chars = psw_chars
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght

    def __call__(self, *args, **kwargs):
        res = [random.choice(self.psw_chars) for i in range(random.randint(self.min_lenght, self.max_lenght))]
        return ''.join(res)



rnd = RandomPassword('qwertyertetwetwe', 5, 20)

lst_pass = [rnd() for i in range(3)]

print(*lst_pass)





#Сделаем с помощью замыкания
def get_random_psw(psw_chars, min_lenght, max_lenght):
    def _(*args, **kwargs):
        res = [random.choice(psw_chars) for i in range(random.randint(min_lenght, max_lenght))]
        return ''.join(res)
    return _



c1 = get_random_psw('qwertyertetwetwe', 5, 20)
lst_pass = [c1() for i in range(3)]

print(*lst_pass)