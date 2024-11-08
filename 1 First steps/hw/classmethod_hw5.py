class AppStore:
    apps = set()
    def add_application(self, app):
        self.apps.add(app)
    def remove_application(self, app):
        self.apps.discard(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        print(len(self.apps))


class Application:

    def __init__(self, name):
        self.name = name
        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.block_application(app_youtube)
store.total_apps()
print(store.apps)