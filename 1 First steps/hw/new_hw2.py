# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
#
# # здесь объявляйте класс Dialog
#
# class Dialog:
#
#     def __new__(cls, *args, **kwargs):
#
#         obj = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
#         obj.name = args[0]
#         return obj
#
#
#     def __init__(self, name):
#         self.name = name
#
# dlg = Dialog('hello')
#
# print(dlg.name)


TYPE_OS = 1

class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = None
        obj = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
        # obj = DialogWindows()
        obj.name = args[0]
        return obj


os1 = Dialog('ОС')
print(os1)






