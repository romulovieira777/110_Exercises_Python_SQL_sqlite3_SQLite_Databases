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

conn = sqlite3.connect("app.db")  # Connect to the database
cur = conn.cursor() # Create a cursor object

with open('../Query/create_schema.sql', 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()
cur.executescript(create_schema_sql)    # Create the database schema

print("Table created successfully!")    # Print the result

with open('../Query/load_data.sql', 'r', encoding='utf-8') as file:
    load_data_sql = file.read()
cur.executescript(load_data_sql)    # Load the data into the database

print("Data entered successfully!") # Print the result

cur.executescript('''DROP INDEX IF EXISTS app_group_user_group_id_user_id_idx_uniq;
CREATE UNIQUE INDEX app_group_user_group_id_user_id_idx_uniq ON app_group_user (group_id, user_id)
;''')   # Create the index

print("Index created successfully!")    # Index created successfully!

conn.commit()   # Commit the changes
conn.close()    # Close the connection
