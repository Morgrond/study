import sqlite3

conn = sqlite3.connect(r'/home/protas/PycharmProjects/pythonProject/Basics Python/My_cats.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS types (
id INTEGER PRIMARY KEY AUTOINCREMENT,
type VARCHAR(100) NOT NULL); ''')
conn.commit()


def insert_type(String_type):
    try:
        sqlite_connection = sqlite3.connect('My_cats.db')
        cursor = sqlite_connection.cursor()
        print('Подключен к SQLite')

        sqlite_insert_query = """INSERT INTO types (id, type) VALUES (?, ?);"""

        cursor.executemany(sqlite_insert_query, String_type)
        sqlite_connection.commit()
        print('Записи успешно вставлены в таблицу types', cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print('Ошибка при работе с SQLite', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Соединение с SQLite закрыто')

records_to_insert = [(1, 'Абиссинская кошка'),
                     (2, 'Австралийский мист'),
                     ('3', 'Американская жесткошерстная')]

insert_type(records_to_insert)






















