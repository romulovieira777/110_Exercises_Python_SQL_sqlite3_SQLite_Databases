"""
Exercise No. 03

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

In tha "app_user" table for the id = 10, update the email address (email column) to "terry@esmartdata.org".

In response, print the first fifteen records of the "app_user" table.

Expected Result:
    (1, 'John', 'Lewis', 61, 'Tonga', 'East Michael', 'johnsonjack@esmartdata.org')
    (2, 'Lance', 'Boyer', 21, 'Seychelles', 'Janicetown', 'thodges@esmartdata.org')
    (3, 'Michael', 'Larson', 22, 'Czech Republic', 'West Melissa', 'kmalone@esmartdata.org')
    (4, 'Alexandra', 'Marshall', 50, 'Malaysia', 'Lunamouth', 'yperry@esmartdata.org')
    (5, 'Rebecca', 'Maldonado', 51, 'Canada', 'Lake Sandrastad', 'mwade@esmartdata.org')
    (6, 'Ronald', 'Ward', 61, 'French Guiana', 'Kennethview', 'lisa46@esmartdata.org')
    (7, 'Justin', 'Wolf', 19, 'French Southern Territories', 'Kristinestad', 'greenjustin@esmartdata.org')
    (8, 'Nicole', 'Fuentes', 63, 'Gambia', 'Port Frank', 'brandonchandler@esmartdata.org')
    (9, 'Melissa', 'Rowland', 45, 'Sudan', 'Alexiston', 'gibsonjennifer@esmartdata.org')
    (10, 'Sean', 'Schmidt', 42, 'Nauru', 'Alyssafort', 'terry@esmartdata.org')
    (11, 'Charles', 'Rios', 54, 'Burkina Faso', 'Sandraside', 'davidharvey@esmartdata.org')
    (12, 'Kimberly', 'Smith', 33, 'Saint Pierre and Miquelon', 'Stokesborough', 'rhodesanne@esmartdata.org')
    (13, 'Patrick', 'Burke', 31, 'South Africa', 'Victorland', 'omurphy@esmartdata.org')
    (14, 'Jerry', 'Patton', 48, 'New Caledonia', 'West Ronald', 'ashley44@esmartdata.org')
    (15, 'Albert', 'Adams', 49, 'Botswana', 'Hartland', 'lance67@esmartdata.org')
"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_database_sql = file.read()  # read the create_database_sql file.
cur.executescript(create_database_sql)  # create database schema and insert data.

cur.execute('''UPDATE app_user SET email = 'terry@esmartdata.org' WHERE id = 10;''')  # update the email address.
cur.execute('''SELECT * FROM app_user LIMIT 15;''')  # print the first fifteen records.

for row in cur.fetchall():
    print(row)

conn.commit()  # commit the changes.
conn.close()  # close the connection.
