"""
Exercise No. 11

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'

Create a query that will join the 'esmartdata_course' and 'esmartdata_instructor'(LEFT JOIN), group the data by the
instructor_id column of the 'esmartdata_course' table and calculate the average rating rounded to two places for each
instructor(the rating column).

Display four columns in the output table:
    - instructor_id('esmartdata_course' table)
    - first_name('esmartdata_instructor' table)
    - last_name('esmartdata_instructor' table)
    - avg_rating(average rating)

In response, print the result to the console as shown below.

Expected Result:
    (1, 'Pawel', 'Krakowiak', 4.63)
    (2, 'takeITeasy', 'Academy', 4.53)
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
    course.instructor_id
  , instructor.first_name
  , instructor.last_name
  , ROUND(AVG(course.rating), 2) AS "AVG_Rating"
FROM
    esmartdata_course course
LEFT JOIN
    esmartdata_instructor instructor
ON
    course.instructor_id = instructor.id
GROUP BY
    course.instructor_id
  , instructor.first_name
  , instructor.last_name;
''')

for row in cur.fetchall():
    print(row)

conn.close()
