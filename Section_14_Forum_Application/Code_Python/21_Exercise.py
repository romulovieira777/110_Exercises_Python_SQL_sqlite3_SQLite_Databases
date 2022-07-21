"""
Exercise No. 21

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create a query that will extract information about all created views in the database "app.db" and print it to the
console as shown below:

Expected result:
    ('view', 'top_10_users_view')
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

cur.execute('''SELECT type, name FROM sqlite_master WHERE type='view';''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
