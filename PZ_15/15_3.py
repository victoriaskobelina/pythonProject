# Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
# которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
# содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
# Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
# выбранная Специальность.
import sqlite3 as sq
from abityr import info_students

with sq.connect('abityrient.db') as con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS students")
    cur.execute("CREATE TABLE IF NOT EXISTS students("
                "reg_n INTEGER PRIMARY KEY AUTOINCREMENT,"
                "second_name TEXT NOT NULL,"
                "first_name TEXT NOT NULL,"
                "patron TEXT NOT NULL,"
                "bth_date DATE NOT NULL,"
                "achiv BOOLEAN NOT NULL,"
                "address TEXT NOT NULL,"
                "spec TEXT NOT NULL)")
with sq.connect('abityrient.db') as con:
    cur=con.cursor()
    cur.executemany("INSERT INTO students VALUES(?,?,?,?,?,?,?,?)", info_students)
# with sq.connect('abityrient.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM students WHERE address=='г.Ростов-на-Дону'")
#     result_1 = cur.fetchall()
#     print(result_1)
#
# with sq.connect('abityrient.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM students WHERE second_name LIKE 'Б%'")
#     result_2 = cur.fetchall()
#     print(result_2)
# # with sq.connect('abityrient.db') as con:
# #     cur = con.cursor()
# #     cur.execute("SELECT * FROM students WHERE achiv=FALSE")
# #     result_3 = cur.fetchall()
# #     print(result_3)
with sq.connect('abityrient.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE students SET achiv=TRUE WHERE achiv==False")
    cur.execute("SELECT * FROM students")
    result_4=cur.fetchall()
    print(result_4)
with sq.connect('abityrient.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE students SET address='г.Ростов-на-Дону' WHERE address!='г.Ростов-на-Дону'")
    cur.execute("SELECT * FROM students")
    result_5=cur.fetchall()
    print(result_5)
with sq.connect('abityrient.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE students SET spec='Программист' WHERE achiv==TRUE AND address=='г.Аксай' ")
    cur.execute("SELECT * FROM students WHERE spec='Программист'")
    result_6=cur.fetchall()
    print(result_6)
# with sq.connect('abityrient.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM students WHERE spec=='Программист'")
#     cur.execute("SELECT * FROM students")
#     result_7=cur.fetchall()
#     print(result_7)
# with sq.connect('abityrient.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM students WHERE spec LIKE 'Б%'")
#     cur.execute("SELECT * FROM students")
#     result_8=cur.fetchall()
#     print(result_8)
# # with sq.connect('abityrient.db') as con:
# #     cur = con.cursor()
# #     cur.execute("DELETE FROM students WHERE achiv==TRUE")
# #     cur.execute("SELECT * FROM students")
# #     result_9=cur.fetchall()
# #     print(result_9)