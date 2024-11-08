class LessonItem:
    attributes = {'title': str, 'practies': int, 'duration': int}

    def __init__(self, title, practies, duration):
        self.title = title
        self.practies = practies
        self.duration = duration


    def __setattr__(self, key, value):
        if key in self.attributes and self.attributes[key] == type(value):
            return super().__setattr__(key, value)
        else:
            raise TypeError('Неверный тип данных')

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if not item in self.attributes:
            super().__delattr__(item)

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


course = Course("Python ООП")
module_1 = Module('Часть первая')
module_1.add_lesson(LessonItem('Урок 1', 7, 1000))
module_1.add_lesson(LessonItem('Урок 2', 2, 1200))
course.add_module(module_1)



