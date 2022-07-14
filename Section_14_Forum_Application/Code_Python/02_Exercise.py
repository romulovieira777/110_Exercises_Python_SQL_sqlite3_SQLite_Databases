"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database called "app.db" was prepared, which contains the "app_user" table:

In this database create a table "app_thread" with the following columns(column name - data type):
    - id - integer
    - title - text
    - creator_id - integer

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

To the creator_id column, add a foreign key constraint referring to the id column of the "app_user" table with ON DELETE
CASCADE ON UPDATE CASCADE options.

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
);

DROP TABLE IF EXISTS app_thread;
CREATE TABLE IF NOT EXISTS app_thread (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title TEXT NOT NULL,
    creator_id INTEGER NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES app_user(id) ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

conn.commit()
conn.close()
