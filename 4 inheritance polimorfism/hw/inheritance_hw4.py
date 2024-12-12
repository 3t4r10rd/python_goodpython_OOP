class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):

        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base

        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

class Game(Singleton):
    __name = None
    def __init__(self, name):
        if self.__dict__.get('name') is None:
            self.name = name


s = Singleton()
game = Game('первый')
game2 = Game('второй')

print(game2.name)