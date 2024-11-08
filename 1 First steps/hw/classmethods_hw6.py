class Viber:

    msgs = dict()
    @classmethod
    def add_message(cls, msg):
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.msgs.pop(id(msg), False)

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_messages(cls, num):
        _msgs = cls.msgs.copy()
        num = len(_msgs) if num > len(_msgs) else num
        for i in range(num):
            print(_msgs.popitem()[1].text)

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)
  

class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False




msg = Message("Всем привет")
Viber.add_message(msg)
Viber.add_message(Message('Это курс по Python'))
Viber.set_like(msg)

Viber.show_last_messages(1)
print(msg.fl_like)
Viber.remove_message(Message('Это курс по Pyhton '))
