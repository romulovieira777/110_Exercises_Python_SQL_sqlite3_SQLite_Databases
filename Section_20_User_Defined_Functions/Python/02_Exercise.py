"""
Exercise No. 02

Using the built-in sqlite3 package, a SQLite database called "app.db" was prepared which contains "instructor" table.

We assume that the first_name anb last_name columns consist of at least 3 characters. We want to assign an e-mail
address to each user based on the first 3 letters of the first name and the first letters of the last name. The domain
of all e-mail addresses is "esmartdata.org".

Example: For the given values: "Mike", "Nagelsman" the e-mail address is: "miknag@esmartdata.org".

Using sqlite3, create a user-defined function that will extract instructor e-mail addresses from two arguments (
first_name, last_name) and which can be used in SQL statements under the EMAIL() name.

In response, display all data from the "instructor" table, additionally add a column with e-mail addresses extracted by
the SQL EMAIL() function.

TIP: https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function

Expected Result:
    (1, 'Mike', 'Nagelsman', 'miknag@esmartdata.org')
    (2, 'John', 'Smith', 'johsmi@esmartdata.org')
    (3, 'Sharon', 'Johnson', 'shajoh@esmartdata.org')
    (4, 'Paula', 'Burke', 'paubur@esmartdata.org')
    (5, 'William', 'Lopez', 'willop@esmartdata.org')
    (6, 'James', 'Simson', 'jamsim@esmartdata.org')
    (7, 'Mason', 'Robinson', 'masrob@esmartdata.org')
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
    ''')    # insert data into the table

print("Table created successfully.")
print("Records inserted successfully.")

conn.commit()  # commit the changes


def email(first_name, last_name):  # create a user-defined function
    return (first_name[0:3] + last_name[0:3]).lower() + "@esmartdata.org"


conn.create_function('email', 2, email)  # create a user-defined function
cur.execute("SELECT *, email(first_name, last_name) AS email FROM instructor")  # execute a SQL statement

for row in cur.fetchall():
    print(row)  # display the row

conn.close()  # close the connection
