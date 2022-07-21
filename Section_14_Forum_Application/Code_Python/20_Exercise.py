"""
Exercise No. 20

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

The following query is give:

    SELECT
        app_comment.user_id
      , app_user.first_name
      , app_user.last_name
      , app_user.email
      , COUNT(*) AS cnt
    FROM
        app_comment
    LEFT JOIN
        app_user
    ON
        app_comment.user_id = app_user.id
    GROUP BY
        app_comment.user_id
    ORDER BY
        cnt DESC
      , app_user.first_name
    LIMIT 10;

This query returns information about the top ten comments on the forum. Create a view named "top_10_users_view" from
this query.
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

cur.executescript('''DROP VIEW IF EXISTS top_10_users_view;
CREATE VIEW top_10_users_view AS
SELECT
    app_comment.user_id
  , app_user.first_name
  , app_user.last_name
  , app_user.email
  , COUNT(*) AS cnt
FROM
    app_comment
LEFT JOIN
    app_user
ON
    app_comment.user_id = app_user.id
GROUP BY
    app_comment.user_id
ORDER BY
    cnt DESC
  , app_user.first_name
LIMIT 10;''')

for row in cur.execute('''SELECT * FROM top_10_users_view;'''):
    print(row)

conn.commit()
conn.close()
