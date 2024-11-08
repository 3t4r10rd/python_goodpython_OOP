class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        for i in self.apps:
            if type(i) == type(app):
                return
        self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"

class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max

class AppPhone:
    def __init__(self, d):
        self.name = "Phone"
        self.phone_list = d



sm = SmartPhone('Honor')
sm.add_app(AppVK())
sm.add_app(AppVK())
sm.add_app(AppYouTube(2048))
for x in sm.apps:
    print(x.name)