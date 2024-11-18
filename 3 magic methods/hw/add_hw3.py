class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        # if not (type(value) == None or  type(value) == StackObj):
        #     raise TypeError('Неправильный тип данных')
        self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not type(value) in (str,):
            raise TypeError('Неправильный тип данных')
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if not self.top:
            self.top = obj
        else:
            ptr = self.top
            while ptr.next:
                ptr = ptr.next

            ptr.next = obj

    def pop_back(self):
        if self.top:
            ptr = self.top
            if ptr.next:
                while ptr.next.next:
                    ptr = ptr.next
                ptr.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self


st = Stack()
st += StackObj('lol')
# st.pop_back()
print(st.top.data)
