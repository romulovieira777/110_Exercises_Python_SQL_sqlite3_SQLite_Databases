"""
Exercise No. 12

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create the following indexes:
    - "app_thread_creator_id_idx" for the creator_id column of the "app_thread" table.
    - "app_comment_thread_id_idx" for the thread_id column of the "app_comment" table.
    - "app_comment_user_id_idx" for the user_id column of the "app_comment" table.
    - "app_group_user_group_id_idx" for the group_id column of the "app_group_user" table.
    - "app_group_user_user_id_idx" for the user_id column of the "app_group_user" table.
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

cur.executescript('''DROP INDEX IF EXISTS app_thread_creator_id_idx;
CREATE INDEX app_thread_creator_id_idx ON app_thread (creator_id);

DROP INDEX IF EXISTS app_comment_thread_id_idx;
CREATE INDEX app_comment_thread_id_idx ON app_comment (thread_id);

DROP INDEX IF EXISTS app_comment_user_id_idx;
CREATE INDEX app_comment_user_id_idx ON app_comment (user_id);

DROP INDEX IF EXISTS app_group_user_group_id_idx;
CREATE INDEX app_group_user_group_id_idx ON app_group_user (group_id);

DROP INDEX IF EXISTS app_group_user_user_id_idx;
CREATE INDEX app_group_user_user_id_idx ON app_group_user (user_id)
;''')

print("Index created successfully!")

conn.commit()
conn.close()
