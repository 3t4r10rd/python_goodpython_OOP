class Model:
    def __init__(self):
        self.atr = None
    def query(self, *args, **kwargs):
        self.atr = kwargs

    def __str__(self):
        return 'Model: ' + ', '.join(f"{i} = {k}" for i, k in self.atr.items()) if self.atr else 'Model'

model = Model()

model.query(d = 1, fio = "Sergey", old = 33)

print(model)