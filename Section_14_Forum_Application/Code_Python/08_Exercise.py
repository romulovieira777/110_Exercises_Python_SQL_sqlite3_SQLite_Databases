"""
Exercise No. 08

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Using the scripts attached to this exercise:
    - create_schema.sql
    - load_database.sql

Create a database schema and load data into tables.
"""
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

with open("../Query/create_schema.sql", 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()
cur.executescript(create_schema_sql)

print("Table created successfully!")

with open("../Query/load_data.sql", 'r', encoding='utf-8') as file:
    load_data_sql = file.read()
cur.executescript(load_data_sql)

print("Data entered successfully!")

conn.commit()
conn.close()
