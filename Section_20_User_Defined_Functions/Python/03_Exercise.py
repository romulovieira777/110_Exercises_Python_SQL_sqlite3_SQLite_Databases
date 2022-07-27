"""
Exercise No. 03

Using the built-in sqlite3 package, a SQLite database called "app.db" was prepared which contains "instructor" table.

We need to find out the age of the instructor based on the date of birth (birth_date column).

Using the sqlite3 package and the datetime built-in module, create a user-defined function that will calculate the age
of the instructors based on one argument: birth_date, and which can be used SQL statements under the AGE() name.

In response, display all data from the "instructor" table, additionally displaying a column with the age determined by
the AGE() function.

TIP: https://docs.python.org/3/library/datetime.html#datetime.datetime.now

Expected Result:
    (1, 'Mike', 'Nagelsman', '1990-03-15', 32)
    (2, 'John', 'Smith', '2005-06-21', 17)
    (3, 'Sharon', 'Johnson', '1999-03-10', 23)
    (4, 'Paula', 'Burke', '1999-04-12', 23)
    (5, 'William', 'Lopez', '1988-10-17', 34)
    (6, 'James', 'Simson', '1988-09-21', 34)
    (7, 'Mason', 'Robinson', '1978-11-24', 44)
"""
import datetime
import sqlite3


def get_age(birth_date):
    return datetime.date.today().year - int(birth_date.split('-')[0])


conn = sqlite3.connect('app.db')  # create a database connection
conn.create_function('age', 1, get_age)  # create a user-defined function
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
  (7, "Mason", "Robinson", "1978-11-24");''')

print("Table created successfully.")
print("Records inserted successfully.")

conn.commit()  # commit the changes

cur.execute('''SELECT *, age(birth_date) AS age FROM instructor;''')  # execute a SQL statement

for row in cur.fetchall():
    print(row)  # display the data from the table

conn.close()  # close the connection to the database
