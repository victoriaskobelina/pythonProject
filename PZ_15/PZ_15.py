#Приложение ПАРИКМАХЕРСКАЯ для некоторой организации. БД должна
#содержать таблицу Услуги со следующей структурой записи: ФИО мастера, ФИО клиента,
#пол, название стрижки, стоимость.
import sqlite3 as sq
from services import info_clients

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS services")
    cur.execute("CREATE TABLE IF NOT EXISTS services("
        "id_service INTEGER PRIMARY KEY AUTOINCREMENT,"
        "fullname_master TEXT NOT NULL,"
        "fullname_client TEXT NOT NULL,"
        "sex TEXT NOT NULL,"
        "haircut_name TEXT NOT NULL,"
        "price DECIMAL(5,2) NOT NULL)")

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?, ?)", info_clients)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM")
    result = cur.fetchall()
    print(result)
