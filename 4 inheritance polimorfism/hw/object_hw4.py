class Tuple(tuple):
    def __add__(self, other):
        try:
            iter(other)
        except:
            raise TypeError('Введен неитерируемый объект')
        return Tuple([*self] + [*other])



t = Tuple([1, 2, 3])
t = t + 'Pyhton'
print(t)

t = (t + 'Python') + 'ООП' + '1'

print(t)