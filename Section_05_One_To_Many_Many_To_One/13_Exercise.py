"""
Exercise No. 13

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'

Create a query that will join from the tables 'esmartdata_course' and 'esmartdara_instructor'(LEFT JOIN) and retrieve
all records that contain in the course name(title column) "Python" and the language of the course(language column) is
set to "eng".

Display four columns in the output table:
    - first_name('esmartdata_instructor' table)
    - last_name('esmartdata_instructor' table)
    - title('esmartdata_course' table)
    - subcategory('esmartdata_course' table)

In response, print the result to the console as shown below.

Expected Result:
    ('Pawel', 'Krakowiak', '200+ Exercises - Programming in Python - from A to Z', 'programming languages')
    ('Pawel', 'Krakowiak', '250+ Exercises - Data Science Bootcamp in Python', 'data science')
    ('Pawel', 'Krakowiak', '100+ Exercises - Python Programming - Data Science - NumPy', 'data science')
    ('Pawel', 'Krakowiak', '130+ Exercises - Python Programming - Data Science - Pandas', 'data science')
    ('Pawel', 'Krakowiak', '100+ Exercises - Python - Data Science - scikit-learn', 'data science')
    ('Pawel', 'Krakowiak', '210+ Exercises - Python Standard Libraries - from A to Z', 'programming languages')
    ('Pawel', 'Krakowiak', '150+ Exercises - Object Oriented Programming in Python - OOP', 'programming languages')
    ('Pawel', 'Krakowiak', '100+ Exercises - Unit tests in Python - unittest framework', 'programming languages')
    ('Pawel', 'Krakowiak', '100+ Exercises - Advanced Python Programming', 'programming languages')
    ('Pawel', 'Krakowiak', '150+ Exercises - Data Structures in Python - Hands-On', 'programming languages')
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

conn.commit()

cur.execute('''SELECT
    instructor.first_name
  , instructor.last_name
  , course.title
  , course.subcategory
FROM
    esmartdata_course course
LEFT JOIN
    esmartdata_instructor instructor
ON
    course.instructor_id = instructor.id
WHERE
    course.title LIKE '%Python%' AND course.language = "eng"
''')

for row in cur.fetchall():
    print(row)

conn.close()
