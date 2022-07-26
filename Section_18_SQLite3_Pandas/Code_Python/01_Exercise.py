"""
Exercise No. 01

Using the built-in sqlite3 package, a SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create a query that retrieve the first ten records from the "app_user" table. Present the result of this query as a
DataFrame from the pandas package and assign to the variable. Set the id column as the DataFrame.
"""
import pandas as pd
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database
cur = conn.cursor()  # create a cursor object

with open("../Query/create_database.sql", "r", encoding='utf-8') as file:
    create_database_sql = file.read()  # read the sql query from the file
cur.executescript(create_database_sql)  # execute the sql query

df = pd.read_sql_query("SELECT * FROM app_user LIMIT 10;", conn, index_col='id')  # read the data from the database

conn.close()  # close the connection
