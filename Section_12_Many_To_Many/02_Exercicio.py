"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database called 'company.db' was prepared, which contains the following
tables:
    - esmartdata_user
    - esmartdata_developer

All the statements that create the database are in the load_database.sql script that is included with this exercise.
Load this script and execute all statements on our database.
"""
import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

with open("Querys\load_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

conn.commit()
conn.close()
