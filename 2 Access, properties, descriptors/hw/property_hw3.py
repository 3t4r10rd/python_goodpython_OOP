class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        if isinstance(n, StackObj) or n is None:
            self.__next = n

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):

        if not self.top:
            self.top = obj
            self.top.next = None
        else:
            node = self.top
            while node.next:
                node = node.next
            node.next = obj

    def pop(self):
        if self.top is None:
            print('No objects')
        if self.top.next is None:
            self.top = None
        else:
            node = self.top
            while node.next.next:
                node = node.next
            last = node.next
            node.next = None

        return last

    def get_data(self):
        lst = list()
        node = self.top
        while node:
            lst.append(node.data)
            node = node.next
        return lst





st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()

res = st.get_data()

print(res)