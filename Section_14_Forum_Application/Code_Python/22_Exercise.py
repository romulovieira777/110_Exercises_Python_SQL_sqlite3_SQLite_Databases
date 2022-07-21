"""
Exercise No. 22

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create the appropriate queries that will display:
    - column names from the "app_user" table.
    - column names in the "top_10_users_view" view.

Print the column names as list to the console as shown below.

Expected result:
    ['id', 'first_name', 'last_name', 'age', 'country', 'city', 'email']
    ['user_id', 'first_name', 'last_name', 'email', 'cnt']
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

cur.execute('''SELECT * FROM app_user;''')
app_user_cols = [desc[0] for desc in cur.description]
print(app_user_cols)

cur.execute('''SELECT * FROM top_10_users_view;''')
views = [desc[0] for desc in cur.description]
print(views)

conn.commit()
conn.close()
