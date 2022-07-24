"""
Exercise No. 10

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Remove the user from the "app_user" table with the given e-mail address:
    - "lisa46@esmardata.org".

Also, remember to enable foreign key support (PRAGMA command).
"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_database_sql = file.read()  # read the create_database_sql file.
cur.executescript(create_database_sql)  # execute the create_database_sql file.

cur.execute('''PRAGMA foreign_keys = ON;''')
cur.execute("DELETE FROM app_user WHERE email = 'lisa46@esmardata.org';")

conn.commit()  # commit the changes.
conn.close()  # close the connection.
