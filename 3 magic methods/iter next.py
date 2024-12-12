class FRange:
    def __init__(self, start=0.0, stop=0.0, step = 1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step # значение арифметической последовательности

#опишем действие итератора объекта
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self


class FRange2D:
    #определим в инициализаторе при создании объекта количество строк (rows) и экземпляр класса FRange
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

#Создадим из класса FRange2D итератор, который можно будет обходить двумя вложенными циклами for

    def __iter__(self):
        self.value = 0
        return self

    # next будет возвращать итератор, который будет генерировать числовые значения
    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=' ')
    print()


fr = FRange(0, 2, 0.5)

print(next(fr)) # 0.0
print(next(fr)) # 0.5
print(next(fr)) # 1.0
print(next(fr)) # 1.5

for x in fr:
    print(x, end=' ')
