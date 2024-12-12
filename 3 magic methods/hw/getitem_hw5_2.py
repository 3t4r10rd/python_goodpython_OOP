class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__count = 0 #количество добавленных объектов

    def push(self, obj):
        last = self[self.__count - 1] if self.__count else None

        if last:
            last.next = obj

        if self.top is None:
            self.top = obj

        self.__count += 1

    def pop(self):
        if not self.__count:
            return None

        if self.__count == 1:
            self.top = None
        else:
            self[self.__count - 2].next = None

        self.__count -= 1

    def __check_index(self, i):
        if type(i) != int and not (0 <= i <= self.__count):
            raise IndexError('Неправильный индекс')

    def __getitem__(self, item):
        self.__check_index(item)

        count = 0
        x = self.top

        while x and count < item:
            x = x.next
            count += 1

        return x

    def __setitem__(self, key, value):
        self.__check_index(key)

        obj = self[key]
        prev = self[key - 1] if key > 0 else None

        value.next = obj.next
        if prev:
            prev.next = value


st = Stack()
st.push(StackObj('obj1'))
st.push(StackObj('obj2'))
st.push(StackObj('obj3'))

st[1] = StackObj('new obj')

print(st[2].data)
print(st[1].data)

print(st[0].next.data)