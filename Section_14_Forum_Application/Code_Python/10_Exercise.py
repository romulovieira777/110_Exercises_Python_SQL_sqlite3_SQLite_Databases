"""
Exercise No. 10

Using the built-in sqlite3 package, SQLite database called 'app_db' was prepared, which contains the following tables:
    - 'app_user'
    - 'app_thread'
    - 'app_comment'
    - 'app_group'
    - 'app_group_user'

Create the appropriate queries that will display the number of records for all tables.

In response, print the result to the console as shown below.
"""
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

with open('../Query/create_schema.sql', 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()
cur.executescript(create_schema_sql)

print("Table created successfully!")

with open('../Query/load_data.sql', 'r', encoding='utf-8') as file:
    load_data_sql = file.read()
cur.executescript(load_data_sql)

print("Data entered successfully!")

cur.executescript('''SELECT COUNT(*) FROM app_user;
                SELECT COUNT(*) FROM app_thread;
                SELECT COUNT(*) FROM app_comment;
                SELECT COUNT(*) FROM app_group;
                SELECT COUNT(*) FROM app_group_user;''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
