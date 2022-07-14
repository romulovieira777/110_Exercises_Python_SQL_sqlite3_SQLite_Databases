"""
Exercise No. 03

Using the built-in sqlite3 package, SQLite database called "app.db" was prepared, which contains the following table:
    - "app_user"
    - "app_thread"

In this database, create a table "app_comment" with the following columns (column name - data type):
    - id - integer
    - body - text
    - created - text
    - thread_id - integer
    - user_id - integer

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

Add a foreign key constraint to the thread_id referring to the id column of the "app_thread" table with ON DELETE
CASCADE ON UPDATE CASCADE options.

Add a foreign key constraint to the user_id column relating to the id column of the "app_user" table with ON DELETE
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
);

DROP TABLE IF EXISTS app_comment;
CREATE TABLE IF NOT EXISTS app_comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    body TEXT NOT NULL,
    created TEXT NOT NULL,
    thread_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (thread_id) REFERENCES app_thread(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES app_user(id) ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

conn.commit()
conn.close()
