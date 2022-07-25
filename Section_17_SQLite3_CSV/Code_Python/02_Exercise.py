"""
Exercise No. 02

Using the built-in sqlite3 package,a SQLite database called "app_db" was created with "app_user" table.

Create a query that groups tha data by age (age column) and calculates the number of users for a given age. Display two
columns in the output table:
    - age
    - cnt_users - number of users for a given age

Sort the output in descending order by cnt_users, then in descending order by age, and leave only those records where
the value in the cnt_users column is greater than 1 (there are at least two users for a given age). Print the result to
the console as shown below.

Expected output:
    (31, 4)
    (61, 3)
    (18, 3)
    (65, 2)
    (60, 2)
    (50, 2)
    (48, 2)
    (47, 2)
    (35, 2)
    (33, 2)
    (28, 2)
    (24, 2)
    (22, 2)
    (21, 2)
"""
import csv
import sqlite3

conn = sqlite3.connect("app_db")    # create a database
cur = conn.cursor()    # create a cursor

cur.executescript('''DROP TABLE IF EXISTS "app_user";
CREATE TABLE IF NOT EXISTS "app_user" (
  "id" integer NOT NULL,
  "first_name" text NOT NULL,
  "last_name" text NOT NULL,
  "age" integer NOT NULL,
  "country" text NOT NULL,
  "city" text NOT NULL,
  "email" text NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
)''')   # create a table

print("Table created successfully.\n")

with open('../Dataset/app_user.csv', 'r') as file:
    reader = csv.DictReader(file)   # create a reader
    records = tuple(reader)       # create a tuple

cur.executemany('''INSERT INTO
  "app_user" (
    "id",
    "first_name",
    "last_name",
    "age",
    "country",
    "city",
    "email"
  )
VALUES
  (
    :id,
    :first_name,
    :last_name,
    :age,
    :country,
    :city,
    :email
  );''', records)   # insert data into the table

print("Data inserted successfully.")

conn.commit()   # commit the changes

cur.execute('''SELECT "age", COUNT("age") AS "cnt_users"
FROM "app_user"
GROUP BY "age"
HAVING COUNT("age") > 1
ORDER BY "cnt_users" DESC, "age" DESC;''')

for row in cur.fetchall():
    print(row)  # print the result to the console

conn.close()    # close the connection
