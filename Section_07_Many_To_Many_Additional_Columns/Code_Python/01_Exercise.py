"""
Exercise No. 01

Using the built-in sqlite3 package, create a SQLite database named 'esmartdata_sqlite3'.

Perform all the instructions from the create_database.sql script attached to the exercise on this database.

Due to Polish characters, use the 'utf-8' encoding when opening the script(encoding argument of the open() function).
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open("../Query/create_database.sql", encoding="utf-8") as file:
    sql = file.read()
    # cur.executescript(file.read())

cur.executescript(sql)

print("Table created successfully!")

conn.commit()
conn.close()
