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

"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()  # read the create_schema_sql file.
cur.executescript(create_schema_sql)  # create database schema and insert data.

cur.execute('''UPDATE app_user SET email = 'terry@esmartdata.org' WHERE id = 10;''')  # update the email address.

cur.execute('''SELECT * FROM app_user LIMIT 15;''')  # print the first fifteen records.

for row in cur.fetchall():
    print(row)

conn.commit()  # commit the changes.
conn.close()  # close the connection.
