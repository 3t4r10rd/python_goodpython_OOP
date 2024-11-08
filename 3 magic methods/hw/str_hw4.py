class ObjList:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head == None:
            self.head = self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        if indx == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            ch = 1
            ptr = self.head.next
            while ch != indx and ptr.next:
                if ptr:
                    ptr = ptr.next
                    ch += 1

            if ptr == self.tail:
                self.tail = ptr.prev
                self.tail.next = None
            else:
                ptr.prev.next = ptr.next
                ptr.next.prev = ptr.prev






    def __len__(self):
        ptr = self.head
        i = 0
        while ptr:
            ptr = ptr.next
            i += 1

        return i

    def __call__(self, indx, *args, **kwargs):
        ptr = self.head
        while indx:
            ptr = ptr.next
            indx -= 1

        return ptr.data if ptr else None



linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(0)
linked_lst.add_obj(ObjList("Python ООП"))
print(len(linked_lst))
print(linked_lst(0))

