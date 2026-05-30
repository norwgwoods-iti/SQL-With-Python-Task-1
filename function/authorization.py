from base.base_class import Base

class Authorization(Base):
    def __init__(self):
        super().__init__()

    def input_login(self, login):
        if login.lower() in self.get_list_logins():
            print('Логин совпалоу')
        else:
            print('Логин не совпалоу')


    def input_password(self, login, password):
        if password == self.get_list_password(login):
            print('Пароль совпалоу')
        else:
            print('Пароль не совпалоу')


    def authorization(self):
        self.connection_db()
        self.get_cursor_db()
        self.input_login(input())
        self.close_db()


