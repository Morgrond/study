import sqlite3

conn = sqlite3.connect(r'/home/protas/PycharmProjects/pythonProject/Basics Python/My_cats.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS types (
id INTEGER PRIMARY KEY AUTOINCREMENT,
type VARCHAR(100) NOT NULL); ''')
conn.commit()
