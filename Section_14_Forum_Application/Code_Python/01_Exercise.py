"""
Exercise No. 01

Using the built-in sqlite3 package, create a SQLite database named "app.db".

In this database, create a table "app_user" with the following columns(column name - data type):
    - id - integer
    - first_name - text
    - last_name - text
    - age - integer
    - country - text
    - city - text
    - email - text

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS app_user;
CREATE TABLE IF NOT EXISTS app_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    email TEXT NOT NULL
);''')

print("Table created successfully!")

conn.commit()
conn.close()
