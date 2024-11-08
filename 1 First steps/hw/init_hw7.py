# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# lst = ['1', '2', '3', '4']
#
# head_obj = ListObject(lst[0])
# s = head_obj
#
# for i in range(1, len(lst)):
#     s.link(ListObject(lst[i]))
#     s = ListObject(lst[i])


class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj


lst_in = ['Строка 1', 'Строка 2', 'Строка 3', 'Строка 4', '5']

head_obj = ListObject(lst_in[0])
s = head_obj

for i in range(1, len(lst_in)):
    s1 = ListObject(lst_in[i])
    s.link(s1)
    s = s1



print(head_obj.next_obj.next_obj.next_obj.__dict__)












