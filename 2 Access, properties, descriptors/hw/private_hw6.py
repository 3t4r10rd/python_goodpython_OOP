class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_obj(self, obj):
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            ptr = self.tail
            self.tail = obj
            self.tail.set_prev(ptr)
            ptr.set_next(self.tail)


    def remove_obj(self):
        if self.tail != self.head:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail = None
        if self.tail is None:
            self.head = None



    def get_data(self):
        res = []
        ptr = self.head
        while ptr:
            res.append(ptr.get_data())
            ptr = ptr.get_next()
        return res


class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data



lst = LinkedList()

lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
# lst.remove_obj()
# lst.remove_obj()
# lst.remove_obj()
res = lst.get_data()

print(res)
