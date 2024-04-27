#Приложение ПАРИКМАХЕРСКАЯ для некоторой организации. БД должна
#содержать таблицу Услуги со следующей структурой записи: ФИО мастера, ФИО клиента,
#пол, название стрижки, стоимость.
import sqlite3 as sq
from salon import info_salon
with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS services")
    cur.execute("""CREATE TABLE IF NOT EXISTS services(
        fullname_master TEXT PRIMARY KEY, 
        fullname_client TEXT NOT NULL,
        sex TEXT NOT NULL,
        haircut_name TEXT NOT NULL,
        price DECIMAL(5,2) NOT NULL
    )""")
with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", salon.py)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM")
    result = cur.fetchall()
    print(result)
