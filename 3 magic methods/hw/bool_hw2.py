class MailBox:
    def __init__(self):
        self.inbox_lsit = []

    def recieve(self):
        lst_in = [
            'sc_lib@list.ru; От Балакирева; Успехов в IT!',
            'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
            'mail123@list.ru; Розыгрыш; Вы выйграли миллион рублей. Или нет.'
        ]
        [self.inbox_lsit.append(MailItem(*(i.split(';')))) for i in lst_in]


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_form = mail_from
        self.title = title
        self.content = content
        self.is_read = False


    def set_read(self, fl_read):
        if type(fl_read) == bool:
            self.is_read = fl_read

    def __bool__(self):
        return self.is_read

mail = MailBox()

mail.recieve()

mail.inbox_lsit[0].set_read(True)
mail.inbox_lsit[-1].set_read(True)

inboox_list_filtered = list(filter(bool, mail.inbox_lsit))

print(inboox_list_filtered)



