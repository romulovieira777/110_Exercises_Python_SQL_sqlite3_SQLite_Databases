"""
Exercise No. 02

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Rename the table "app_group_user" to "app_membership".

Commit the changes and print to the console a list with all table names starting with "app", sorted alphabetically.

Expected Result:
    ['app_comment', 'app_group', 'app_membership', 'app_thread', 'app_user']
"""
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database.
cur = conn.cursor()  # create a cursor.

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    create_database_sql = file.read()  # read the create_schema_sql file.
cur.executescript(create_database_sql)  # create database schema and insert data.

cur.executescript('''
    DROP TABLE IF EXISTS app_membership;
    ALTER TABLE app_group_user RENAME TO app_membership;
''')  # rename the table.

print('Table successfully renamed!')

cur.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'app_%' ORDER BY name;''')  # print the table names.
tables = [item[0] for item in cur.fetchall() if item[0].startswith('app_')]
print(tables)

conn.commit()  # commit the changes.
conn.close()  # close the connection.
