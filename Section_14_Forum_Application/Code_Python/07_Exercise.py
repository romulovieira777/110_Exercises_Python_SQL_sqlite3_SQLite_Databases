"""
Exercise No. 07

Using tge built-in sqlite3 package, create a SQLite database named "app.db".

Use the create_schema.sql script attached to this exercise to create schema.
"""
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

with open("../Query/create_schema.sql", 'r', encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

print("Table created successfully!")

conn.commit()
conn.close()
