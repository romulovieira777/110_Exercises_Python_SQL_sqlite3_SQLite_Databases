"""
Exercise No. 11

Using the built-in sqlite3 package, SQLite database called 'app_db' was prepared, which contains the following tables:
    - 'app_ser'
    - 'app_thread'
    - 'app_comment'
    - 'aap_group'
    - 'app_group_user'

Create a query that will display the names (sorted in ascending order) of all tables in the database 'app_db' and print
it to the console as show below.

Expected Result:

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

cur.execute('''SELECT tbl_name FROM sqlite_master ORDER BY 1; ''')

for row in cur.fetchall():
    print(f'table name: {row[0]}')

conn.commit()
conn.close()
