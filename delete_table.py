import sqlite3 as sql
from pathlib import Path

path_sql = str(Path(__file__).resolve().parent / 'db' / 'registration.db')

db = sql.connect(path_sql)

print(f'Подключились к Базе Данных - {path_sql.split("/")[-1]}')

cur = db.cursor()

cur.execute('DROP TABLE IF EXISTS users_data')
db.commit()