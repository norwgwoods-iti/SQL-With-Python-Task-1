from base.base_class import Base


class Authorization(Base):
    def __init__(self):
        super().__init__()
        self.login = None

    # def input_login(self):
    #     login = input('Введите Логин: ').lower()
    #
    # """Ввод логина"""
    #
    # def input_login(self):
    #     while True:
    #         login = input('Введите Логин: ').lower()
    #         if login == self.check_login(login):
    #             print('Логин введен верно')
    #             return login
    #         else:
    #             print('Такого логина не существует')
    #             continue


    """Функция"""
    def input_password(self, login):
        self.login = login
        print(f'Логин введен верно: {login}')
        password = input('Введите Пароль: ')
        if password == self.check_password(login):
            print('Пароль верный')
        else:
            print('Пароль не совпадает')



    # Methods

    def authorization(self):
        self.connection_db()
        self.get_cursor_db()
        self.input_password(self.input_login())
        self.close_db()
        print('Авторизация прошла успешно')

