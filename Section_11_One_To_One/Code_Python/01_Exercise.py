"""
Exercise No. 01

Using the built-in sqlite3 package, create a SQLite database e named 'company.db'.

In this database, create a table 'esmartdata_user' with the following columns (column name - data type):
    - id integer
    - first_name text
    - last_name text

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("../company.db")
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS esmartdata_user;
CREATE TABLE esmartdata_user
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);''')

print("Table created successfully")

conn.commit()
conn.close()
