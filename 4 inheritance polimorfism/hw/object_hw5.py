class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()

class VideoRating:
    def __init__(self):
        self.rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not (0 <= value <= 5 and type(value) == int):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value



v = VideoItem('Курс Pyhton', 'Подробный курс по Python', "D:/videos/python_oop.mp4")
print(v.rating.rating)
v.rating.rating = 5

print(v.rating.rating)

title = v.title
descr = v.descr
v.rating.rating = 6