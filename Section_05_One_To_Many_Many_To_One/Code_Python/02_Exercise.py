"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
'esmartdata_instructor' table.

The table 'esmartdata_instructor' stores basic information about the instructors on the platform. Each instructor can
have multiple courses on the platform. We will store courses in a separate table called 'esmartdata_course'. Before
creating this table, you should consider the type of relationship between these tables. In this case, the answer is
simple, one instructor -> many courses(one-to-many).

Before creating the table, use the appropriate SQL command that will delete the 'esmartdata_course' table if such a
table already exists in the database.

Then, in the specified database, create a table named 'esmartdata_course' with the following columns(column name - data
type):
    - id - integer
    - title - text
    - subtitle - text
    - description - text
    - category - text
    - subcategory - text
    - language - text
    - length - text
    - rating - real
    - referral_link - text
    - instructor_id - integer

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

Add a foreign key constraint to the column instructor_id referring to the id column of the table 'esmartdata_instructor'
with the ON DELETE CASCADE ON UPDATE CASCADE options.

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect('../esmartdata.sqlite3')
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS "esmartdata_instructor";
CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
    "id" INTEGER NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);''')

cur.executescript('''DROP TABLE IF EXISTS "esmartdata_course";
CREATE TABLE IF NOT EXISTS "esmartdata_course" (
    "id" INTEGER NOT NULL,
    "title" TEXT NULL,
    "subtitle" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "category" TEXT NOT NULL,
    "subcategory" TEXT NOT NULL,
    "language" TEXT NOT NULL,
    "length" TEXT NOT NULL,
    "rating" REAL NOT NULL,
    "referral_link" TEXT NOT NULL,
    "instructor_id" INTEGER NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("instructor_id") REFERENCES "esmartdata_instructor"(id)
    ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

conn.commit()
conn.close()
