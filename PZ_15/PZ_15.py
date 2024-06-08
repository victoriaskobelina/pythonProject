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
    cur.execute("SELECT * FROM services WHERE sex='женский'")
    result_1 = cur.fetchall()
    print(result_1)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM services WHERE sex='мужской'")
    result_2 = cur.fetchall()
    print(result_2)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM services WHERE fullname_master='Пупыркина Е.В.'")
    result_3 = cur.fetchall()
    print(result_3)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE services SET price=1550 WHERE price==1300")
    cur.execute("SELECT * FROM services where price=1550")
    result_4 = cur.fetchall()
    print(result_4)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE services SET price=1199 WHERE price==1550 AND fullname_master=='Пупыркина Е.В.'")
    cur.execute("SELECT * FROM services WHERE fullname_master='Пупыркина Е.В.'")
    result_5 = cur.fetchall()
    print(result_5)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE services SET fullname_master='Мальцева А.В.' WHERE fullname_master=='Баринова Ю.В.'")
    cur.execute("SELECT * FROM services WHERE fullname_master='Мальцева А.В.'")
    result_6 = cur.fetchall()
    print(result_6)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM services WHERE haircut_name=='Полубокс' OR haircut_name=='Андеркат'")
    cur.execute("SELECT * FROM services")
    result_7 = cur.fetchall()
    print(result_7)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM services WHERE fullname_master=='Мальцева А.В.'")
    cur.execute("SELECT * FROM services")
    result_8 = cur.fetchall()
    print(result_8)

with sq.connect('salon.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM services WHERE sex=='мужской'")
    cur.execute("SELECT * FROM services")
    result_9 = cur.fetchall()
    print(result_9)