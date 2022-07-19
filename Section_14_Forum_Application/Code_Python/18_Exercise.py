"""
Exercise No. 18

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create a query that will extract all records from the table "app_group_user" for a user with user_id = 41 and
group_id = 2 and print to the console.

Expected Result:
    (9, 2, 41)
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

print("Data loaded successfully!")

cur.execute('''SELECT * FROM app_group_user WHERE user_id = 41 AND group_id = 2;''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
