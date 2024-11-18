class Dimensions:
    def __init__(self, a, b, c):

        self.a = float(a) if a.count('.') else int(a)
        self.b = float(b) if b.count('.') else int(b)
        self.c = float(c) if c.count('.') else int(c)

        if min(self.a, self.b, self.c) <= 0:
            raise ValueError('Габаритные значения должны быть больше 0')

    def __hash__(self):
        return hash((self.a, self.b, self.c))


s_inp = '1 2 3; 4 5 6.78; 1 2 3; 0.1 1 2.5'
lst_dims = [Dimensions(*i) for i in [j.split() for j in s_inp.split(';')]]
lst_dims.sort(key=lambda x: hash(x))



