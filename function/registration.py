import re
import random

from base.base_class import Base

class Registration(Base):

    """Ввод логина по заданным правилам"""
    @staticmethod
    def check_input_login():
        while True:
            login_new = input('Введите новый логин (от 4 до 15 символов), *a-z,A-Z,0-9,_:\n')

            if len(login_new) < 4:
                print('Ошибка! Логин слишком короткий. Минимальная длина - 4 символа.')
                continue
            elif len(login_new) > 15:
                print('Ошибка! Логин слишком длинный. Максимальная длина - 15 символов.')
                continue
            elif not re.match(r'^[a-zA-Z0-9_]{4,15}$', login_new):
                print(
                    'Ошибка! Логин содержит недопустимые символы. Используйте символы латинского алфавита, цифры или "_".')
            else:
                return login_new

    """Проверяем логин в БД"""
    def add_login(self):
        while True:
            login_new = self.check_input_login()

            """Подключаемся к БД"""
            self.connection_db()
            self.get_cursor_db()
            """Достаем данные из БД"""
            user_data = self.get_user_data(login_new)
            """Закрываем БД"""
            self.close_db()

            if user_data:
                print(f'\nЛогин уже занят. Попробуйте: {login_new}_{random.randint(1, 100)}')
            else:
                print('Выбранный логин свободен!')
                return login_new

    """Ввод пароля по заданным правилам"""
    @staticmethod
    def check_and_add_input_password():

        while True:
            print('Введите ваш пароль (от 7 до 20 символов), *a-z,A-Z,0-9,_!@#$%^&*:')

            password_new = input()

            if len(password_new) < 7:
                print('Ошибка! Пароль слишком короткий. Минимальная длина - 7 символов.')
                continue
            elif len(password_new) > 20:
                print('Ошибка! Пароль слишком длинный. Максимальная длина - 20 символов.')
                continue
            elif not re.match(r'^[a-zA-Z0-9_!@#$%^&*]{7,20}$', password_new):
                print('Ошибка! Пароль содержит недопустимые символы. Используйте буквы латинского алфавита, цифры или "_!@#$%^&*" символы.')
                continue

            print('Подтвердите введеный пароль:')

            password_new_2 = input()

            if password_new_2 == password_new:
                print('Пароль выбран успешно')
                return password_new
            else:
                print('Пароли не совпадают! Попробуйте заново ввести пароль...')

    """Ввод кода доступа по заданным правилам"""
    @staticmethod
    def check_and_add_input_code():

        while True:
            print('Введите проверочный код для сброса пароля (от 4 до 6 цифр):')

            code_new = input()

            if len(code_new) < 4:
                print('Ошибка! Код слишком короткий. Минимальная длина - 4 цифры.')
                continue
            elif len(code_new) > 6:
                print('Ошибка! Код слишком длинный. Максимальная длина - 6 цифр.')
                continue
            elif not re.match(r'^[0-9]{4,6}$', code_new):
                print('Ошибка! Код содержит недопустимые символы. Используйте цифры от 0 до 9.')
                continue

            print('Подтвердите проверочный код:')

            code_2 = input()

            if code_2 == code_new:
                print('Код установлен')
                return code_new
            else:
                print('Введеные коды различаются! Попробуйте еще раз...')

    """Ввод пароля, логина и кода в БД"""
    def add_account_in_bd(self, login, password, code):
        new_account = (login, password, code)
        self.cur.execute(
            """
            INSERT INTO users_data
                (Login, Password, Code) 
            VALUES
                (?, ?, ?);
            """, new_account
        )
        self.db.commit()


    # Methods

    def registration(self):
        print('--- Регистрация ---')

        """Сохраняем введеные данные в переменные"""
        login = self.add_login()
        password = self.check_and_add_input_password()
        code = self.check_and_add_input_code()

        """Подключаемся к БД и вводим данные логина, пароля и кода в БД"""
        self.connection_db()
        self.get_cursor_db()
        """Записываем Логин, Пароль и Код в БД"""
        self.add_account_in_bd(login, password, code)
        """Закрываем БД"""
        self.close_db()

        print('--- Регистрация прошла успешно ---')