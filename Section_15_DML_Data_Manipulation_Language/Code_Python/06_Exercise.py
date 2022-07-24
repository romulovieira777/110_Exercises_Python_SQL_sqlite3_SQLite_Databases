"""
Exercise No. 06

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

A column named is_banned was added to the "app_user" table with an integer data type and a default value 0. The
is_banned column whether the user is banned or not.

Create a query that will extract all comments from the "app_comment" table for banned users. You can use subqueries in
the solution.

Expected Result:
    (116, 'Money all picture three.', '2021-05-01 21:23:57', 5, 36)
    (278, 'Professional author bring green fine Mrs cup wear happen.', '2021-05-06 17:07:23', 12, 8)
    (140, 'So Mr identify campaign majority all health relate listen.', '2021-05-07 18:50:30', 6, 36)
    (4, 'Enjoy yes loss enough middle.', '2021-05-08 17:56:25', 1, 36)
    (106, 'Door south PM see daughter class wide.', '2021-05-13 07:47:18', 5, 36)
    (16, 'Answer mission radio surface front fill campaign mother.', '2021-05-14 00:01:40', 1, 8)
    (20, 'Any office lead course baby executive international be scientist draw.', '2021-05-14 14:48:58', 1, 8)
    (131, 'The national end involve because during school.', '2021-05-18 02:08:01', 6, 36)
    (70, 'Forward security spring answer contain be imagine support one only.', '2021-05-19 21:51:22', 3, 8)
    (40, 'Stay size study modern consumer wife.', '2021-05-20 16:42:31', 2, 36)
    (274, 'Region surface unit onto chance.', '2021-05-21 05:06:09', 11, 8)
    (283, 'History oil establish receive single establish step while.', '2021-05-21 10:46:41', 12, 8)
    (195, 'Short consumer seek trial human be stock.', '2021-05-22 03:46:04', 8, 8)
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

cur.execute('''SELECT * FROM app_comment WHERE user_id IN (SELECT id FROM app_user WHERE is_banned = 1) 
ORDER BY created;''')  # print the banned users.

for row in cur.fetchall():
    print(row)

conn.close()  # close the connection.
