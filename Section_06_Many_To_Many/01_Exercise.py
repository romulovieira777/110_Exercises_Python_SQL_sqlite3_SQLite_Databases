"""
Exercise No. 01

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'

The table "esmartdata_instructor" contains basic information about instructors on the platform. We will store the
courses in a separate table called "esmartdata_course".

We also want to add learning paths to our platform. The learning path consists of many thematically related courses.
One course may follow multiple learning paths, and a learning path may contain multiple courses.

Consider the type of relationship you will use in the solution. In this case, the answer is simple, we will use a
many-to-many relationship. To do this we need to create two tables. We will deal with the first one in this exercise.

In our database create a table named "esmartdata_learningpath" with the following columns(column name - data type):
    - id integer
    - title text
    - subtitle text
    - url text
Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS "esmartdata_instructor";
CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
    "id" INTEGER NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_course";
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

cur.executescript('''INSERT INTO "esmartdata_instructor"
(
    "id",
    "first_name",
    "last_name",
    "description"
) 
VALUES
(
    1,
    "Pawel",
    "Krakowiak",
    "Data Scientist/Python Developer/Securities Broker"
);

INSERT INTO "esmartdata_instructor"
(
    "id",
    "first_name",
    "last_name",
    "description"
)
VALUES
(
    2,
    "takeITeasy",
    "Academy",
    "Akademia Programowania"
)
''')

print('Data entered successfully!')

with open('load_esmartdata_course.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''DROP INDEX IF EXISTS esmartdata_course_instructor_id_idx;''')
cur.execute('''CREATE INDEX IF NOT EXISTS esmartdata_course_instructor_id_idx ON esmartdata_course('instructor_id');
''')

print('Index created successfully!')

cur.executescript('''DROP TABLE IF EXISTS "esmartdata_learningpath";
CREATE TABLE IF NOT EXISTS "esmartdata_learningpath" (
    "id" INTEGER NOT NULL
  , "title" TEXT NOT NULL
  , "subtitle" TEXT NOT NULL
  , "url" TEXT NOT NULL
  , PRIMARY KEY("id" AUTOINCREMENT));
''')

print("Table created successfully!")

conn.commit()
conn.close()
