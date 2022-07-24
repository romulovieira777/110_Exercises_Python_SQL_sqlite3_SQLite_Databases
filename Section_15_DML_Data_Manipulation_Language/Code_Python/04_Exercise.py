"""
Exercise No. 04

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

In the "app_user" table for the id = 5, update the country (country column) to "France" and city (city column) to
"Paris".

In response, print the first ten records of the "app_user" table.

Expected Result:
    (1, 'John', 'Lewis', 61, 'Tonga', 'East Michael', 'johnsonjack@esmartdata.org')
    (2, 'Lance', 'Boyer', 21, 'Seychelles', 'Janicetown', 'thodges@esmartdata.org')
    (3, 'Michael', 'Larson', 22, 'Czech Republic', 'West Melissa', 'kmalone@esmartdata.org')
    (4, 'Alexandra', 'Marshall', 50, 'Malaysia', 'Lunamouth', 'yperry@esmartdata.org')
    (5, 'Rebecca', 'Maldonado', 51, 'France', 'Paris', 'mwade@esmartdata.org')
    (6, 'Ronald', 'Ward', 61, 'French Guiana', 'Kennethview', 'lisa46@esmartdata.org')
    (7, 'Justin', 'Wolf', 19, 'French Southern Territories', 'Kristinestad', 'greenjustin@esmartdata.org')
    (8, 'Nicole', 'Fuentes', 63, 'Gambia', 'Port Frank', 'brandonchandler@esmartdata.org')
    (9, 'Melissa', 'Rowland', 45, 'Sudan', 'Alexiston', 'gibsonjennifer@esmartdata.org')
    (10, 'Sean', 'Schmidt', 42, 'Nauru', 'Alyssafort', 'vterry@esmartdata.org')
"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_database_sql = file.read()  # read the create_database_sql file.
cur.executescript(create_database_sql)  # create database schema and insert data.

cur.execute('''UPDATE app_user SET country = 'France', city = 'Paris' WHERE id = 5;''')  # update the country and city.
cur.execute('''SELECT * FROM app_user LIMIT 10;''')  # print the first ten records.

for row in cur.fetchall():
    print(row)

conn.commit()  # commit the changes.
conn.close()  # close the connection.
