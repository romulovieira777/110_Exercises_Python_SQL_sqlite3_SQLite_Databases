"""
Exercise No. 19

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

We want to extract the ten most commenting users from the database. To odo this, create a query that will join the
appropriate tables and display the following columns to the console:
    - user_id - column from the "app_comment" table.
    - first_name - column from the "app_user" table.
    - last_name - column from the "app_user" table.
    - email - column from the "app_user" table.
    - cnt - number of comments for a given user.

Sort the output table in descending order by the cnt column and print it to the console as shown below:

Expected Result:
    (33, 'Timothy', 'Johnson', 'andre95@esmartdata.org', 14)
    (47, 'David', 'Mcdonald', 'sharris@esmartdata.org', 10)
    (4, 'Alexandra', 'Marshall', 'yperry@esmartdata.org', 9)
    (32, 'Denise', 'Foster', 'jeremy68@esmartdata.org', 8)
    (31, 'Diane', 'Castro', 'aaron40@esmartdata.org', 8)
    (40, 'Jennifer', 'Wallace', 'frankdodson@esmartdata.org', 8)
    (7, 'Justin', 'Wolf', 'greenjustin@esmartdata.org', 8)
    (22, 'Justin', 'Anderson', 'wanda97@esmartdata.org', 8)
    (29, 'Kenneth', 'Perry', 'choidaniel@esmartdata.org', 8)
    (43, 'Kevin', 'Fisher', 'jamesjonathan@esmartdata.org', 8)
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

cur.execute('''SELECT app_comment.user_id, app_user.first_name, app_user.last_name, app_user.email, COUNT(*) AS cnt
FROM app_comment
LEFT JOIN app_user ON app_comment.user_id = app_user.id
GROUP BY app_comment.user_id
ORDER BY cnt DESC, app_user.first_name
LIMIT 10;''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
