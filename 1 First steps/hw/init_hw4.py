# class Graph:
#     def __init__(self, data):
#         self.data = data[:]
#         self.is_show = True
#
#
#     def set_data(self, data):
#         self.data = data[:]
#
#
#     def show_table(self):
#         print(*self.data) if self.is_show else print("Отображение данных закрыто")
#
#
#     def show_graph(self):
#         print("Графическое отображение данных:", *self.data) if self.is_show else print("Отображение данных закрыто")
#
#
#     def show_bar(self):
#         print("Столбчатая диаграмма: ", *self.data) if self.is_show else print("Отображение данных закрыто")
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
#
# data_graph = [8, 11, 10, -32, 0, 7, 18]
#
# gr = Graph(data_graph)
#
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()
#


class Graph:
    is_show = True

    def __init__(self, data):
        self.data = data[:]

    def set_data(self, data):
        self.data = data[:]

    def show_table(self):
        print(*self.data) if self.is_show else print("Отображение данных закрыто")

    def show_graph(self):
        print("Графическое отображение данных:", *self.data) if self.is_show else print("Отображение данных закрыто")

    def show_bar(self):
        print("Столбчатая диаграмма:", *self.data) if self.is_show else print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show

data_graph = [8, 11, 10, -32, 0, 7, 18]

gr = Graph(data_graph)

gr.show_bar()

gr.set_show(False)

gr.show_table()
