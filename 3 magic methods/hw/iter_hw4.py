class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.__last.next = obj
        self.__last = obj


    def push_front(self, obj):
        if self.top is None:
            self.__last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __check_indx(self, indx):
        if not (0 <= indx < len(self)):
            print(indx, len(self))
            raise IndexError('неверный индекс')

    def __get_obj(self, item):
        self.__check_indx(item)
        x = self.top
        i = item
        while i and x:
            x = x.next
            i -= 1
        return x

    def __getitem__(self, item):
        return self.__get_obj(item).data if self.top else None



    def __setitem__(self, key, value):
        self.__get_obj(key).data = value

    def __len__(self):
        if self.top is None:
            return 0
        i = 1
        x = self.top
        while x != self.__last:
            i += 1
            x = x.next
        return i

    def __iter__(self):
        x = self.top
        while x:
            yield x
            x = x.next


st = Stack()

st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
st.push_back(StackObj('4'))
st[3] = 'lol'
print(st[0])
print(len(st))

for obj in st:
    print(obj.data)