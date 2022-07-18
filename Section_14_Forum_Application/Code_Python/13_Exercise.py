"""
Exercise No. 13

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create unique index named "app_group_user_group_id_user_idx_uniq" consisting of two columns: group_id and user_id of the
table "app_group_user".
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

cur.executescript('''DROP INDEX IF EXISTS app_group_user_group_id_user_idx_uniq;
CREATE UNIQUE INDEX app_group_user_group_id_user_idx_uniq ON app_group_user (group_id, user_id);
;''')

print("Index created successfully!")

conn.commit()
conn.close()
