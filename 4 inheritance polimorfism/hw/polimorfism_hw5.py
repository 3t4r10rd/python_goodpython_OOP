from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass

class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
        else:
            h = self._top
            while h.next:
                h = h.next

            h.next = obj

    def pop_back(self):
        h = self._top

        if h is None:
            return None

        if h.next is None:
            self._top = None
            return h

        while h.next.next:
            h = h.next

        x = h.next
        h.next = None
        return x


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print(del_obj)