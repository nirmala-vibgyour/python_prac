import sqlite3


connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE band='Lions'")
rows = cursor.fetchall()
print(rows)

newRows = [('Cats', 'Cat city', '2088.10.18'),
            ('Hens', 'Hen city', '2088.10.14')]

cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", newRows)
connection.commit()


