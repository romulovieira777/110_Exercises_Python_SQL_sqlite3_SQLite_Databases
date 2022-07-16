"""
Exercise No. 09

Using the built-in sqlite3 package, SQLite database called 'app_db' was prepared, which contains the following tables:
    - 'app_user'
    - 'app_thread'
    - 'app_comment'
    - 'app_group'
    - 'app_group_user'

Create a query that will display the number of records in the 'app_user' table.

In response, print the result to the console as shown below.

Expected Result:
    50
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

cur.execute('''SELECT COUNT(*) FROM app_user;''')

for row in cur.fetchall():
    print(row[0])

conn.commit()
conn.close()
