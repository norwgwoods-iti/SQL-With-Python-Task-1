import sqlite3 as sql
from pathlib import Path

path_sql = Path(__file__).resolve().parent.parent / 'registration.db'

db = sql.connect(path_sql)

print(f'Подключились к Базе Данных - {path_sql.name}')

cur = db.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users_data(
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Login TEXT NOT NULL UNIQUE,
        Password TEXT NOT NULL,
        Code TEXT NOT NULL
        );"""
)

insert_parameter = ('Ivan', 'qwer1234', '1234')

cur.execute(
    """
    INSERT INTO users_data
        (Login, Password, Code) 
    VALUES
        (?, ?, ?);
    """, insert_parameter
)
db.commit()


db.close()