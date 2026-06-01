from getpass import getpass

from base.base_class import Base

class Authorization(Base):

    """Запрашиваем Логин у пользователя"""
    @staticmethod
    def input_login():
        login = input('Введите Логин:\n').lower()
        return login

    """Запрашиваем Пароль у пользователя"""
    @staticmethod
    def input_password():
        print('Введите Пароль')
        password = getpass()
        return password


    # Methods

    """Метод авторизации"""
    def authorization(self):
        while True:
            print('--- Авторизация ---')
            """Логин и пароль записываем в переменные"""
            login = self.input_login()
            password = self.input_password()

            """Подключаемся к БД"""
            self.connection_db()
            self.get_cursor_db()
            """Достаем данные из БД"""
            user_data = self.get_user_data(login)
            """Закрываем БД"""
            self.close_db()

            """Сверяем данные с БД"""
            # Если user_data пустая - значит логина нет в БД, user_data[0] содержит пароль из base_class
            if user_data and user_data[0] == password:
                print('--- Авторизация прошла успешно ---\n')
                return login
            else:
                print('Логин или пароль ввведены неверно')


