import sqlite3 as sql
from pathlib import Path


class Base:
    def __init__(self):
        self.db = None
        self.cur = None
        self.sql_path = str(Path(__file__).resolve().parent.parent / 'db' / 'registration.db')

    """Возвращаем db"""
    def connection_db(self):
        self.db = sql.connect(self.sql_path)
        db_name = Path(self.sql_path).name

        print(f'Подключились к Базе Данных - {db_name}')
        return self.db


    """Возвращаем курсор"""
    def get_cursor_db(self):
        self.cur = self.db.cursor()
        return self.cur


    """Получаем все поля таблицы"""
    def get_fields(self):
        try:
            self.cur.execute("SELECT * FROM users_data")

            print('Список всех полей таблицы:')
            return self.cur.fetchall()
        except AttributeError:
            print('Сначала необходимо подключиться к БД с помощью connection_db()')
            return []


    """Получаем список логинов"""
    def get_list_logins(self):
        self.cur.execute(
            """
            SELECT Login
            FROM users_data
            """
        )

        login_list = []

        login_db = self.cur.fetchall()

        for login in login_db:
            login_list.append(login[0].lower())

        return login_list


    """Получаем Пароль по Логину"""
    def get_list_password(self, login):
        self.cur.execute(
            """
                SELECT Password
                FROM users_data
                WHERE Login = ?;
            """, (login,)
        )

        password_db = self.cur.fetchone()

        return password_db[0]


    """Получаем Код по Логину"""
    def get_list_code(self, login):
        self.cur.execute(
            """
                SELECT Code
                FROM users_data
                WHERE Login = ?;
            """, (login,)
        )

        code_db = self.cur.fetchone()

        return code_db[0]


    """Закрываем БД"""
    def close_db(self):
        if self.db:
            self.db.close()
            print('База Данных закрыта')
        else:
            print('Соединение не было открыто')
