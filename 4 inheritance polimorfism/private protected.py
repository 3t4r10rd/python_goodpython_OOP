class Geom:
    def __init__(self, x1, x2, x3, x4):
        print(f"инициализатор Geom для {self.__class__}")
        self.__x1 = x1
        self.__x2 = x2
        self.__x3 = x3
        self.__x4 = x4

class Rect(Geom):
    def __init__(self, x1, x2, x3, x4, fill='red'):
        super().__init__(x1, x2, x3, x4)
        self.fill = fill


r = Rect(0, 0, 10, 20)

print(r.__dict__) # {'_Geom__x1': 0, '_Geom__x2': 0, '_Geom__x3': 10, '_Geom__x4': 20, 'fil': 'red'}