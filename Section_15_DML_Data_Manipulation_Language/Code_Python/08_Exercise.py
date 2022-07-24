"""
Exercise No. 08

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create a query that will extract total number of threads from the table "app_thread".

Expected result:
    12
"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_database_sql = file.read()  # read the create_database_sql file.
cur.executescript(create_database_sql)  # execute the create_database_sql file.

cur.execute("SELECT COUNT(*) FROM app_thread;")

for row in cur.fetchall():
    print(row[0])

conn.commit()  # commit the changes.
conn.close()  # close the connection.
