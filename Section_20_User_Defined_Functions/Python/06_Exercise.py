"""
Exercise No. 06

Using the built-in sqlite3 package, a SQLite database called "app.db" was prepared which contains "instructor" table.

Using the sqlite3 package, create a user-defined function that will represent the data in CSV format and that can be
used in SQL statements under the CSV() name. The CSV() function is expected to take any number of arguments.

In response, display the columns: id, first_name, last_name from the table "instructor" in CSV format using the
implemented SQL function called CSV().

TIP: https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function  -> create_function

Expected Result:
    1,Mike,Nagelsman
    2,John,Smith
    3,Sharon,Johnson
    4,Paula,Burke
    5,William,Lopez
    6,James,Simson
    7,Mason,Robinson
"""
import sqlite3

conn = sqlite3.connect("app.db")  # create a database connection
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
''')


print("Table created successfully.")
print("Records inserted successfully.")

conn.commit()  # commit the changes to the database


def csv(*args):
    return ','.join([str(arg) for arg in args])  # return a string with comma separated values


conn.create_function("CSV", -1, csv)  # create a function that can be used in SQL statements

cur.execute("SELECT CSV(id, first_name, last_name) FROM instructor")  # execute a SQL statement

for row in cur.fetchall():
    print(row[0])

conn.close()  # close the connection
