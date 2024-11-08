class WindowDlg:
    def __init__(self, title, w, h):
        self.__title = title
        self.__width = self.__high = None
        self.width = w
        self.high = h

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__high}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) is int and 0 <= w <= 10000:
            self.__width = w
        if self.__width and self.__high:
            self.show()

    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self, h):
        if type(h) == int and 0 <= h <= 10000:
            self.__high = h
        if self.__width and self.__high:
            self.show()



wnd = WindowDlg('title', 5, 10)

wnd.width = 55
wnd.high = 33


