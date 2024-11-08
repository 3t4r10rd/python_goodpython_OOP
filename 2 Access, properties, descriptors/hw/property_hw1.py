class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, m):
        if type(m) is str and 2 <= len(m) <= 100:
            self.__model = m



car = Car()

car.model = 's1'
print(car.model)