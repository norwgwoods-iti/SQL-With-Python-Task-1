import sqlite3 as sql
from pathlib import Path

class Base:
    def __init__(self):
        self.db = None
        self.cur = None

    def connection_db(self, path_sql):
        self.db = sql.connect(path_sql)
        self.cur = self.db.cursor()

        db_name = Path(path_sql).name
        print(f'Подключились к Базе Данных - {db_name}')
        return self.cur


    def get_fields(self):
        try:
            self.cur.execute("SELECT * FROM users_data")
            return self.cur.fetchall()
        except AttributeError as a:
            print('Сначала необходимо подключиться к БД с помощью connection_db()')
            return []


    def close_db(self):
        if self.db:
            self.db.close()
            print('База Данных закрыта')
        else:
            print('Соединение не было открыто')
