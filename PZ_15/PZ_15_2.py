import sqlite3
# Создание подключения к базе данных
conn = sqlite3.connect('salon2.db')
cursor = conn.cursor()
# Создание таблицы Услуги
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Услуги (
        ФИО_мастера TEXT,
        ФИО_клиента TEXT,
        пол TEXT,
        название_стрижки TEXT,
        стоимость REAL
    )
''')
# Добавление данных в таблицу
cursor.execute("INSERT INTO Услуги VALUES ('Иванов Иван', 'Петрова Елена', 'женский', 'Стрижка горячими ножницами', 1500)")
cursor.execute("INSERT INTO Услуги VALUES ('Петров Петр', 'Иванова Анна', 'мужской', 'Стрижка под машинку', 1000)")
# добавить еще данные
# Сохранение изменений
conn.commit()
# Закрытие подключения
conn.close()
def update_service(master_name, client_name, new_service_name, new_cost):
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Услуги SET название_стрижки=?, стоимость=? WHERE ФИО_мастера=? AND ФИО_клиента=?",
                   (new_service_name, new_cost, master_name, client_name))
    conn.commit()
    conn.close()
# Пример использования
update_service('Иванов Иван', 'Петрова Елена', 'Подкраска волос', 2000)

def delete_service(master_name, client_name):
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Услуги WHERE ФИО_мастера=? AND ФИО_клиента=?", (master_name, client_name))
    conn.commit()
    conn.close()
# Пример использования
delete_service('Иванов Иван', 'Петрова Елена')
def search_master(master_name):
    conn = sqlite3.connect('salon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Услуги WHERE ФИО_мастера=?", (master_name,))
    results = cursor.fetchall()
    conn.close()
    return results
# Пример использования
results = search_master('Иванов Иван')
for result in results:
    print(result)