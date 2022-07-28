"""
Exercise No. 04

Using the built-in sqlite3 package, a SQLite database called "app.db" was prepared which contains "instructor" table.

We need to assign each instructor pseudo-randomly to one of the three groups. We will do this by assigning the
appropriate group number to the instructor (1, 2, 3).

Using the sqlite3 package and the random built-in module, create a user-defined RANDOM_GROUP() function that will assign
a group number to the instructor.

In response, display all data from the "instructor" table, additionally displaying a column with pseudo-randomly
generated group numbers designated by the SQL function RANDOM_GROUP().

Tip: https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function -> create_function

Expected Result:
    (1, 'Mike', 'Nagelsman', '1990-03-15', 2)
    (2, 'John', 'Smith', '2005-06-21', 3)
    (3, 'Sharon', 'Johnson', '1999-03-10', 2)
    (4, 'Paula', 'Burke', '1999-04-12', 1)
    (5, 'William', 'Lopez', '1988-10-17', 2)
    (6, 'James', 'Simson', '1988-09-21', 3)
    (7, 'Mason', 'Robinson', '1978-11-24', 1)
"""
import random
import sqlite3

conn = sqlite3.connect('app.db')  # create a database connection
cur = conn.cursor()  # create a cursor object

cur.executescript('''DROP TABLE IF EXISTS "instructor";
CREATE TABLE IF NOT EXISTS "instructor" (
  "id" integer NOT NULL,
  "first_name" text NOT NULL,
  "last_name" text NOT NULL,
  "birth_date" text NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO
  "instructor" ("id", "first_name", "last_name", "birth_date")
VALUES
  (1, "Mike", "Nagelsman", "1990-03-15"),
  (2, "John", "Smith", "2005-06-21"),
  (3, "Sharon", "Johnson", "1999-03-10"),
  (4, "Paula", "Burke", "1999-04-12"),
  (5, "William", "Lopez", "1988-10-17"),
  (6, "James", "Simson", "1988-09-21"),
  (7, "Mason", "Robinson", "1978-11-24");
''')  # create a table and insert data

print("Table created successfully.")
print("Records inserted successfully.")

conn.commit()  # commit the changes to the database


def random_group():
    return random.randint(1, 3)  # return a random number between 1 and 3


conn.create_function('random_group', 0, random_group)  # create a user-defined function

cur.execute('''SELECT *, RANDOM_GROUP() FROM "instructor"''')  # execute a SQL statement

for row in cur.fetchall():
    print(row)  # print all rows

conn.close()  # close the connection
