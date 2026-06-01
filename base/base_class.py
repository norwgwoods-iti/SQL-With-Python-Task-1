import sqlite3 as sql
from pathlib import Path

class Base:

    def __init__(self):
        """Присваем None, чтобы потом в функции задать значение и использовать в других методах"""
        self.db = None
        self.cur = None
        self.sql_path = Path(__file__).resolve().parent.parent / 'db' / 'registration.db'

    """Возвращаем db"""
    def connection_db(self):
        self.db = sql.connect(self.sql_path)
        """print для тестов"""
        # print(f'Подключились к Базе Данных - {self.sql_path.name}')
        return self.db


    """Возвращаем курсор"""
    def get_cursor_db(self):
        try:
            self.cur = self.db.cursor()
            return self.cur
        except AttributeError:
            print('Сначала необходимо подключиться к БД с помощью connection_db()')
            return None


    """Получаем все поля таблицы"""
    def get_fields(self):
        try:
            self.cur.execute("SELECT * FROM users_data")
            print('Список всех полей таблицы:')
            return self.cur.fetchall()
        except AttributeError:
            print('Сначала необходимо подключиться к БД с помощью connection_db()')
            return None

    """Получаем Пароль и Код по Логину"""
    def get_user_data(self, login):
        self.cur.execute(
            """
            SELECT Password, Code
            FROM users_data
            WHERE LOWER (Login) = LOWER(?);
            """, (login,)
        )

        return self.cur.fetchone()


    """Закрываем БД"""
    def close_db(self):
        if self.db:
            self.db.close()
            """print для тестов"""
            # print('База Данных закрыта')
        else:
            print('Соединение не было открыто')