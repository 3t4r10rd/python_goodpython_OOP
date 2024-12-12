class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def __getitem__(self, item):
        return self.marks[item]

    def __setitem__(self, key, value):
        if isinstance(key, int) and key > 0: #если индекс целое положительное число
            self.marks[key] = value

    def __delitem__(self, key):
        del self.marks[key]


s1 = Student('Сергей', [5, 5, 3, 2, 5])

print(s1.marks[2]) #3
print(s1[2]) #3 - возвратится значение s1.marks[2] с помощью метода __getitem__
print(s1.marks[2] == s1[2]) #True

s1[2] = 5 # s.marks[2] примет значение 5 с помощью метода __setitem__

del s1[2] # удалит из списка s1.marks элемент с индексом 2 с помощью метода __delitem__