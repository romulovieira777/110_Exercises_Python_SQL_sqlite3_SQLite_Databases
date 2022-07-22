"""
Exercise No. 01

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Add a column named is_banned to the "app_user" table with an integer data type and a default value of 0. The is_banned
column shows whether the user is banned or not. Since SQLite does not have a separate data type for boolean values
(True / False) we use an integer (0 means false, 1 means true).

In response, print the first ten records of the "app_user" table.

Expected Result:
    (1, 'John', 'Lewis', 61, 'Tonga', 'East Michael', 'johnsonjack@esmartdata.org', 0)
    (2, 'Lance', 'Boyer', 21, 'Seychelles', 'Janicetown', 'thodges@esmartdata.org', 0)
    (3, 'Michael', 'Larson', 22, 'Czech Republic', 'West Melissa', 'kmalone@esmartdata.org', 0)
    (4, 'Alexandra', 'Marshall', 50, 'Malaysia', 'Lunamouth', 'yperry@esmartdata.org', 0)
    (5, 'Rebecca', 'Maldonado', 51, 'Canada', 'Lake Sandrastad', 'mwade@esmartdata.org', 0)
    (6, 'Ronald', 'Ward', 61, 'French Guiana', 'Kennethview', 'lisa46@esmartdata.org', 0)
    (7, 'Justin', 'Wolf', 19, 'French Southern Territories', 'Kristinestad', 'greenjustin@esmartdata.org', 0)
    (8, 'Nicole', 'Fuentes', 63, 'Gambia', 'Port Frank', 'brandonchandler@esmartdata.org', 0)
    (9, 'Melissa', 'Rowland', 45, 'Sudan', 'Alexiston', 'gibsonjennifer@esmartdata.org', 0)
    (10, 'Sean', 'Schmidt', 42, 'Nauru', 'Alyssafort', 'vterry@esmartdata.org', 0)
"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()
cur.executescript(create_schema_sql)  # create database schema and insert data.

cur.execute('''ALTER TABLE app_user ADD COLUMN is_banned INTEGER DEFAULT 0''')  # add a column.

print('New field successfully added!')

cur.execute('''SELECT * FROM app_user LIMIT 10''')  # print the first ten records.

for row in cur.fetchall():
    print(row)

conn.commit()  # commit the changes.
conn.close()  # close the connection.
