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

user = cur.execute('''SELECT COUNT(*) FROM app_user;''').fetchall()[0]
thread = cur.execute('''SELECT COUNT(*) FROM app_thread;''').fetchall()[0]
comment = cur.execute('''SELECT COUNT(*) FROM app_comment;''').fetchall()[0]
group = cur.execute('''SELECT COUNT(*) FROM app_group;''').fetchall()[0]
group_user = cur.execute('''SELECT COUNT(*) FROM app_group_user;''').fetchall()[0]

print(f'user: {user[0]}')
print(f'thread: {thread[0]}')
print(f'comment: {comment[0]}')
print(f'group: {group[0]}')
print(f'group_user: {group_user[0]}')

conn.commit()
conn.close()
