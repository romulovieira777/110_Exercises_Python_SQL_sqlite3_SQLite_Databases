"""
Exercise No. 09

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'

Create a query that will group from the 'esmartdata_course' by the instructor_id column and calculate the number of
courses for each instructor. Print the result to the console as shown below(instructor_id, num_courses).

Expected Result:
    (1, 40)
    (2, 5)
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

with open('../Query/load_esmartdata_course.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''DROP INDEX IF EXISTS esmartdata_course_instructor_id_idx;''')
cur.execute('''CREATE INDEX IF NOT EXISTS esmartdata_course_instructor_id_idx ON esmartdata_course('instructor_id');
''')

print('Index created successfully!')

conn.commit()

cur.execute('''SELECT instructor_id, COUNT(*) AS "num_courses" FROM esmartdata_course GROUP BY instructor_id;''')

for rows in cur.fetchall():
    print(rows)

conn.close()
