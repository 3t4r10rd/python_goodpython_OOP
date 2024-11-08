class Server:
    count = 1

    def __init__(self):
        self.buffer = list()
        self.ip = Server.count
        Server.count += 1
        self.linked_router = None

    def send_data(self, data):

        if type(data) is Data and self.linked_router:
            self.linked_router.buffer.append(data)
        elif not self.linked_router:
            print("Нет подключенных роутеров")
        else:
            print("Неверный формат данных")

    def get_data(self):
        res = self.buffer[:]
        self.buffer.clear()
        return res

    def get_ip(self):
        return self.ip

class Router:
    def __init__(self):
        self.buffer = list()
        self.servers = list()

    def link(self, server):
        if server in self.servers:
            print("Сервер уже подключен")
        else:
            server.linked_router = self
            self.servers.append(server)

    def unlink(self, server):
        if server in self.servers:
            server.linked_router = None
            self.servers.pop(server)


    def send_data(self):
        if len(self.buffer) == 0:
            print("Нет данных для отправки")
        elif len(self.servers) == 0:
            print("Нет серверов для отправки")
        else:
            for x in self.buffer:
                for y in self.servers:
                    if x.ip == y.ip:
                        y.buffer.append(x.data)

        self.buffer = []

class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

router = Router()


sv_from = Server()
sv_from2 = Server()


router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(router.__dict__)
print(sv_from.__dict__)
print(sv_from2.__dict__)
print(sv_to.__dict__)

print(msg_lst_to, msg_lst_from)