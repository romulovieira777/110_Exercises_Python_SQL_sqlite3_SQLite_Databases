"""
Exercise No. 05

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

A column named is_banned was added to the "app_user" table with an integer data type and a default value 0. The
is_banned column whether the user is banned or not.

Block users with id = 8 and id = 36 (set the value in the is_banned column to 1).

In response, print all banned users from the "app_user" table.

Expected Result:
    (8, 'Nicole', 'Fuentes', 63, 'Gambia', 'Port Frank', 'brandonchandler@esmartdata.org', 1)
    (36, 'Christopher', 'Moore', 18, 'Malawi', 'North Morganburgh', 'herringcalvin@esmartdata.org', 1)
"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_database_sql = file.read()  # read the create_database_sql file.
cur.executescript(create_database_sql)  # create database schema and insert data.

cur.execute('''ALTER TABLE app_user ADD COLUMN is_banned INTEGER DEFAULT 0;''')  # add a column is_banned to the app_user table.
cur.execute('''UPDATE app_user SET is_banned = 1 WHERE id in(8, 36);''')  # update the is_banned column.

conn.commit()  # commit the changes.

cur.execute('''SELECT * FROM app_user WHERE is_banned = 1;''')  # print the banned users.

for row in cur.fetchall():
    print(row)

conn.close()  # close the connection.
