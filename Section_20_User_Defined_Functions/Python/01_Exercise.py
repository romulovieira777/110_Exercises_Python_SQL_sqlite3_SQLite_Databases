"""
Exercise No. 01

Using the built-in sqlite3 package, create a SQLite database named "app.db".

Then create "instructor" table with the following columns (column name - data type):
    - id - integer
    - first_name - text
    - last_name - text

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

Then insert the following records into the "instructor" table (you can copy the command from the insert.sql file):
    INSERT INTO
        "instructor" ("id", "first_name", "last_name")
    VALUES
        (1, "Mike", "Nagelsman"),
        (2, "John", "Smith"),
        (3, "Sharon", "Johnson"),
        (4, "Paula", "Burke"),
        (5, "William", "Lopez"),
        (6, "James", "Simson"),
        (7, "Mason", "Robinson")

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("app.db")  # create a database connection
cur = conn.cursor()  # create a cursor object

cur.executescript('''DROP TABLE IF EXISTS "instructor";
CREATE TABLE "instructor" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL
    );
        
    INSERT INTO "instructor" ("id", "first_name", "last_name")
    VALUES
        (1, "Mike", "Nagelsman"),
        (2, "John", "Smith"),
        (3, "Sharon", "Johnson"),
        (4, "Paula", "Burke"),
        (5, "William", "Lopez"),
        (6, "James", "Simson"),
        (7, "Mason", "Robinson");
    ''')    # insert data into the "instructor" table

print("Table created successfully.")
print("Records inserted successfully.")

conn.commit()  # commit the changes
conn.close()  # close the connection
