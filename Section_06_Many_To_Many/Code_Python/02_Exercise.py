"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'

In our database create a table named "esmartdata_learningpath_courses" with the following columns(column name -
data type):
    - id integer
    - learningpath_id integer
    - course_id integer

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

To the learningpath_id column, add a FOREIGN KEY constraint referring to the id column of the "esmartdata_learningpath"
table with ON DELETE CASCADE ON UPDATE CASCADE options.

To the course_id column, add a FOREIGN KEY constraint referring to the id column of the "esmartdata_course" table with
the ON DELETE CASCADE ON UPDATE CASCADE options.

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
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
    FOREIGN KEY("instructor_id") REFERENCES "esmartdata_instructor"(id) ON DELETE CASCADE ON UPDATE CASCADE
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

with open('../Query/load_esmartdata_course.sql', 'r', encoding='utf-8') as file:
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
  , PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_learningpath_courses";
CREATE TABLE IF NOT EXISTS "esmartdata_learningpath_courses" (
    "id" INTEGER NOT NULL
  , "learningpath_id" INTEGER NOT NULL
  , "course_id" INTEGER NOT NULL
  , PRIMARY KEY("id" AUTOINCREMENT)
  , FOREIGN KEY("learningpath_id") REFERENCES "esmartdata_learningpath"(id) ON DELETE CASCADE ON UPDATE CASCADE
  , FOREIGN KEY("course_id") REFERENCES "esmartdata_course"(id) ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

conn.commit()
conn.close()
