import sqlite3 as sql
from pathlib import Path

path_sql = Path(__file__).resolve().parent.parent / 'registration.db'

db = sql.connect(path_sql)

print(f'Подключились к Базе Данных - {path_sql.name}')

cur = db.cursor()

cur.execute(
    """
    DELETE FROM users_data
    WHERE UserID = 11;
    """
)
print('Строка удалена')

db.commit()