"""
Exercise No. 14

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create a query that will extract names (sorted in ascending order) of all indexes in the database and print them to the
console as shown below.

Expected Result:
    ('index', 'app_comment_thread_id_idx')
    ('index', 'app_comment_user_id_idx')
    ('index', 'app_group_user_group_id_idx')
    ('index', 'app_group_user_group_id_user_idx_uniq')
    ('index', 'app_group_user_user_id_idx')
    ('index', 'app_thread_creator_id_idx')
"""
import sqlite3

conn = sqlite3.connect("app.db")    # Connect to the database
cur = conn.cursor() # Create a cursor object

with open('../Query/create_schema.sql', 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()
cur.executescript(create_schema_sql)    # Create the database schema

print("Table created successfully!")    # Print the result

with open('../Query/load_data.sql', 'r', encoding='utf-8') as file:
    load_data_sql = file.read()
cur.executescript(load_data_sql)    # Load the data into the database

print("Data entered successfully!") # Print the result

cur.executescript('''DROP INDEX IF EXISTS app_thread_creator_id_idx;
CREATE INDEX app_thread_creator_id_idx ON app_thread (creator_id);

DROP INDEX IF EXISTS app_comment_thread_id_idx;
CREATE INDEX app_comment_thread_id_idx ON app_comment (thread_id);

DROP INDEX IF EXISTS app_comment_user_id_idx;
CREATE INDEX app_comment_user_id_idx ON app_comment (user_id);

DROP INDEX IF EXISTS app_group_user_group_id_idx;
CREATE INDEX app_group_user_group_id_idx ON app_group_user (group_id);

DROP INDEX IF EXISTS app_group_user_user_id_idx;
CREATE INDEX app_group_user_user_id_idx ON app_group_user (user_id);

DROP INDEX IF EXISTS app_group_user_group_id_user_id_idx_uniq;
CREATE UNIQUE INDEX app_group_user_group_id_user_id_idx_uniq ON app_group_user (group_id, user_id);
''')

print("Index created successfully!")    # Index created successfully!

cur.execute('''SELECT type, name FROM sqlite_master WHERE type='index' ORDER BY name;''')   # Execute the query

for row in cur.fetchall():
    print(row)  # ('index', 'app_comment_thread_id_idx')

conn.commit()   # Commit the changes
conn.close()    # Close the connection
