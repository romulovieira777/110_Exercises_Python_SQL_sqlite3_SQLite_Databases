"""
Exercise No. 17

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Consider the following query:
    SELECT * FROM app_group_user WHERE group_id = 2 AND user_id = 41;

Using the appropriate SQL statement, check how the records of the "app_group_user" table are filtered. Print the answer
to the console as shown below.

Expected Result:
    SCAN TABLE app_group_user
"""
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

with open('../Query/create_schema.sql', 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()
cur.executescript(create_schema_sql)
conn.commit()

print("Table created successfully!")

cur.execute('''EXPLAIN QUERY PLAN SELECT * FROM app_group_user WHERE group_id = 2 AND user_id = 41;''')

for row in cur.fetchall():
    print(row[3])

conn.close()
