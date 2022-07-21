"""
Exerc No. 24

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create a query to the "app_comment" table that will extract information about comments added between "2021-05-23" and
"2021-05-25".

Extract the following columns from the table:
    - id
    - body
    - created

Sorted the output table in descending order by the created column, limit the result to the first ten records and print
to the console.

Expected result:
    (3, 'Herself stuff size inside probably personal.', '2021-05-24 21:25:36')
    (85, 'Painting follow rock whole check health research treatment.', '2021-05-24 19:22:15')
    (258, 'Popular husband less civil customer issue mouth position network particularly.', '2021-05-24 16:39:17')
    (118, 'Deep we who whole race study various house order.', '2021-05-24 15:58:50')
    (169, 'Would woman clear bad season close fast.', '2021-05-24 13:27:35')
    (79, 'Man smile nature let hotel development.', '2021-05-24 12:08:57')
    (207, 'Return win natural with read want recent sea administration room.', '2021-05-24 10:29:49')
    (143, 'Their capital peace PM face feeling cold part third choose.', '2021-05-24 09:19:46')
    (213, 'And area local thus raise yeah produce theory action future strategy.', '2021-05-24 07:49:01')
    (67, 'Truth series manager example game represent various increase.', '2021-05-24 07:42:22')
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

cur.execute('''SELECT id, body, created 
FROM app_comment 
WHERE created BETWEEN '2021-05-23' AND '2021-05-25' 
ORDER BY created DESC LIMIT 10;''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
