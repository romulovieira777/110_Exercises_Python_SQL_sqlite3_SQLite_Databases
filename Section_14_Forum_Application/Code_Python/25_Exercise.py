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
    id      body      created
"""
import sqlite3
import pandas as pd

conn = sqlite3.connect("app.db")  # connect to the database
cur = conn.cursor()  # create a cursor

with open('../Query/create_schema.sql', 'r', encoding='utf-8') as file:
    create_schema_sql = file.read()
cur.executescript(create_schema_sql)  # create schema

print("Table created successfully!")

with open('../Query/load_data.sql', 'r', encoding='utf-8') as file:
    load_data_sql = file.read()
cur.executescript(load_data_sql)  # Load data into the database

print("Data loaded successfully!")

cur.execute('''SELECT id, body, created 
FROM app_comment 
WHERE created BETWEEN '2021-05-23' AND '2021-05-25' 
ORDER BY created DESC LIMIT 10;''')

columns = [desc[0] for desc in cur.description]  # get column names
df = pd.DataFrame(data=cur.fetchall(), columns=columns)  # fetchall() returns a list of tuples
df = df.set_index('id')  # set the index to the id column
print(id)  # print the DataFrame

conn.commit()  # commit the changes
conn.close()  # close the connection to the database
