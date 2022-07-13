"""
Exercise No. 05

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'

Using the script load_esmartdata_course.sql attached to the exercise, load the data about the courses into the
'esmartdata_course' table.

Due to Polish characters, use the 'utf-8' encoding when opening the script(encoding argument of the open() function).

In response, create a query that returns the number of records in the 'esmartdata_course' table and print it to the
console.

Expected Result:
    - 45
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

cur.execute('''INSERT INTO "esmartdata_instructor"
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
)
''')

cur.execute('''INSERT INTO "esmartdata_instructor"
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

with open('../Query/load_esmartdata_course.sql', 'r', encoding='utf8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''SELECT COUNT(*) FROM esmartdata_course;''')
n_rows = cur.fetchall()[0][0]
print(n_rows)

conn.commit()
conn.close()
