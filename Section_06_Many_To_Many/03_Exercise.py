"""
Exercise No. 03

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

Using the script load_esmardata_learningpath.sql attached to the exercise, load the data about the learning paths into
"esmartdata_learningpath" table.

Due to Polish characters, use the 'utf-8' encoding when opening the script(encoding argument of the open() function).

In response, create a query that will display the following columns from the "esmartdata_learningpath" table:
    - id
    - title
    - url
and print them to the console as shown below.

Expected Result:
    (1, 'Ścieżka C Developer', 'https://e-smartdata.teachable.com/p/sciezka-c-developer')
    (2, 'Ścieżka C++ Developer', 'https://e-smartdata.teachable.com/p/sciezka-cpp-developer')
    (3, 'Ścieżka Python Developer', 'https://e-smartdata.teachable.com/p/sciezka-python-developer')
    (4, 'Ścieżka Big Data Analyst', 'https://e-smartdata.teachable.com/p/sciezka-big-data-analyst')
    (5, 'Ścieżka BI Analyst / Data Analyst', 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst')
    (6, 'Ścieżka Data Scientist / Machine Learning Engineer', 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer')
    (7, 'Ścieżka Data Scientist / Deep Learning Engineer', 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer')
    (8, 'Ścieżka All-in-One', 'https://e-smartdata.teachable.com/p/sciezka-all-in-one')
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

with open('load_esmartdata_course.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

print('Data successfully loaded!')

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

with open('load_esmartdata_learningpath.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

print('Data successfully loaded!')

cur.execute('''SELECT "id", "title", "url" FROM "esmartdata_learningpath"''')

for rows in cur.fetchall():
    print(rows)

conn.commit()
conn.close()
