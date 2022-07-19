"""
Exercise No. 16

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create a query that will extract all records from the "app_comment" table for user_id = 43 sorted in ascending order by the
created column.

Expected Result:
    (243, 'Begin strong many history include similar former employee eye.', '2021-05-03 05:22:45', 10, 43)
    (219, 'Keep mission most talk network reduce get member growth build which.', '2021-05-04 17:35:04', 9, 43)
    (23, 'National maybe product government.', '2021-05-10 00:53:07', 1, 43)
    (14, 'Service true various attorney until factor culture let.', '2021-05-12 01:05:33', 1, 43)
    (98, 'Expert over and particularly attention drop democratic buy forget various.', '2021-05-13 01:03:52', 4, 43)
    (13, 'Customer color stuff around serious.', '2021-05-14 02:50:15', 1, 43)
    (295, 'Ago expert population relationship artist.', '2021-05-18 21:27:19', 12, 43)
    (52, 'Story six discuss up material anything medical film bad discussion.', '2021-05-20 14:16:02', 3, 43)
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
conn.commit()

print("Data loaded successfully!")

cur.execute('''SELECT * FROM app_comment WHERE user_id = 43 ORDER BY created ASC;''')

for row in cur.fetchall():
    print(row)

conn.close()
