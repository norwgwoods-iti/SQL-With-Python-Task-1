

from base.base_class import Base
from function.registration import Registration

class ResetPassword(Base):

    """Ввод логина"""
    @staticmethod
    def input_login():
        login = input('Введите Логин: ').lower()
        return login

    """Воод кода проверки"""
    @staticmethod
    def input_code():
        code = input('Введите проверочный код: ')
        return code

    """Метод проверки логина и получения кода по логину"""
    def check_login_and_code_in_bd(self):
        while True:
            login = self.input_login()
            code = self.input_code()

            """Подключаемся к БД"""
            self.connection_db()
            self.get_cursor_db()
            """Достаем данные из БД"""
            user_data = self.get_user_data(login)
            """Закрываем БД"""
            self.close_db()

            """Сверяем данные с БД"""
            # Если user_data пустая - значит логина нет в БД, user_data[1] содержит код из base_class
            if user_data and user_data[1] == code:
                print('Логин и проверочный код введены верно')
                return login
            else:
                print('Логин или проверочный код введены неверно')

    """Метод смены пароля в БД по Логину"""
    def change_password_in_bd(self, new_password, login):
        login_and_password = (new_password, login)

        self.cur.execute(
            """
            UPDATE users_data
            SET Password = ?
            WHERE LOWER(Login) = LOWER(?);
            """, login_and_password
        )
        self.db.commit()


    # Methods
    """Сброс пароля"""
    def reset_password(self):
        print('--- Восстановление пароля ---')

        """Получаем Логин и Пароль и записываем в переменную"""
        login = self.check_login_and_code_in_bd()
        new_password = Registration.check_and_add_input_password()

        """Подключаемся к БД"""
        self.connection_db()
        self.get_cursor_db()
        """Меняем пароль в БД"""
        self.change_password_in_bd(new_password, login)
        """Закрываем БД"""
        self.close_db()

        print('--- Сброс пароля прошел успешно ---')