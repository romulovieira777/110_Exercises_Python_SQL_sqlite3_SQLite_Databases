"""
Exercise No. 25

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

The following query is given:
    SELECT
        id
      , body
      , created
    FROM
        app_comment
    WHERE
        created BETWEEN '2021-05-23' AND '2021-05-25'
    ORDER BY
        created DESC
    LIMIT
        10;

This query returns ten records from the table "app_comment". Using the pandas package, create a DataFrame from these
records and assign to the df variable.

The content of the df variable:
                                                  body              created
    id
    3         Herself stuff size inside probably personal.  2021-05-24 21:25:36
    85   Painting follow rock whole check health resear...  2021-05-24 19:22:15
    258  Popular husband less civil customer issue mout...  2021-05-24 16:39:17
    118  Deep we who whole race study various house order.  2021-05-24 15:58:50
    169           Would woman clear bad season close fast.  2021-05-24 13:27:35
    79             Man smile nature let hotel development.  2021-05-24 12:08:57
    207  Return win natural with read want recent sea a...  2021-05-24 10:29:49
    143  Their capital peace PM face feeling cold part ...  2021-05-24 09:19:46
    213  And area local thus raise yeah produce theory ...  2021-05-24 07:49:01
    67   Truth series manager example game represent va...  2021-05-24 07:42:22
"""
import sqlite3
import pandas as pd

conn = sqlite3.connect("app.db")  # connect to the database
cur = conn.cursor()  # create a cursor

with open('../Query/create_schema.sql', 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()
cur.executescript(create_schema_sql)  # create schema

print("Table created successfully!") # print message

with open('../Query/load_data.sql', 'r', encoding='utf-8') as file:
    load_data_sql = file.read()
cur.executescript(load_data_sql)  # Load data into the database

print("Data loaded successfully!") # print a message

cur.execute('''SELECT id, body, created 
FROM app_comment 
WHERE created BETWEEN '2021-05-23' AND '2021-05-25' 
ORDER BY created DESC LIMIT 10;''')

columns = [desc[0] for desc in cur.description]  # get column names
df = pd.DataFrame(data=cur.fetchall(), columns=columns)  # fetchall() returns a list of tuples
df = df.set_index('id')  # set the index to the id column
print(df)  # print the DataFrame

conn.commit()  # commit the changes
conn.close()  # close the connection to the database
