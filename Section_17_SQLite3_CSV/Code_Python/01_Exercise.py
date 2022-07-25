"""
Exercise No. 01

Using the built-in sqlite3 package, create a SQLite database named "app_db".

Create a table "app_user" with the following columns (column name - data type):
    - id - integer
    - first_name - text
    - last_name - text
    - age - integer
    - country - text
    - city - text
    - email - text

Add a NOT NULL constraint to each column, Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

The app_user.csv file is attached to the exercise. Using the built-in csv module, insert the data from this file into
the "app_user" table.
"""
import csv
import sqlite3

conn = sqlite3.connect("app_db")    # create a database
cur = conn.cursor()    # create a cursor

cur.executescript('''DROP TABLE IF EXISTS app_user;
                     CREATE TABLE app_user (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         first_name TEXT NOT NULL,
                         last_name TEXT NOT NULL,
                         age INTEGER NOT NULL,
                         country TEXT NOT NULL,
                         city TEXT NOT NULL,
                         email TEXT NOT NULL
                         );''')    # create a table

print("Table created successfully.")

with open("../Dataset/app_user.csv", "r") as file:
    reader = csv.DictReader(file)   # create a reader
    records = tuple(reader)        # create a tuple

cur.executemany("INSERT INTO app_user (id, first_name, last_name, age, country, city, email) "
                    "VALUES (:id, :first_name, :last_name, :age, :country, :city, :email)", records)   # insert data into the table

print("Data inserted successfully.")

conn.commit()   # commit the changes
conn.close()    # close the connection
