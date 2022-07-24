"""
Exercise No. 07

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

A column named is_banned was added to the "app_user" table with an integer data type and a default value 0. The
is_banned column whether the user is banned or not.

Create and execute a query that will remove all banned users from the database.
"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_database_sql = file.read()  # read the create_database_sql file.
cur.executescript(create_database_sql)  # create database schema and insert data.

cur.execute('''PRAGMA foreign_keys = ON;''')  # enable foreign keys.
cur.execute('''ALTER TABLE app_user ADD COLUMN is_banned INTEGER DEFAULT 0;''')  # add a column is_banned to the app_user table.
cur.execute('''UPDATE app_user SET is_banned = 1 WHERE id in(8, 36);''')  # update the is_banned column.
cur.execute('''DELETE FROM app_user WHERE is_banned = 1;''')  # delete the banned users.

conn.commit()  # commit the changes.
conn.close()  # close the connection.
