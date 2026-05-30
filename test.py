from function.authorization import Authorization
from base.base_class import Base
from pathlib import Path
import sqlite3 as sql

# path_sql = str(Path(__file__).resolve().parent / 'db' / 'registration.db')

aut = Authorization()
aut.authorization()


