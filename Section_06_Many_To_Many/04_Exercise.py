"""
Exercise No. 04

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

Using the script load_esmartdata_learningpath_courses.sql, attached to the exercise, load the data into the
"esmartdata_learningpath_courses" table.

In response, create script a query that will select all records from the "esmartdata_learningpath_courses" table and
print result to the console as shown below.

Expected Result:
    (1, 1, 41)
    (2, 1, 42)
    (3, 2, 43)
    (4, 2, 44)
    (5, 2, 45)
    (6, 3, 4)
    (7, 3, 38)
    (8, 3, 14)
    (9, 3, 22)
    (10, 3, 24)
    (11, 3, 25)
    (12, 3, 29)
    (13, 3, 30)
    (14, 4, 4)
    (15, 4, 6)
    (16, 4, 7)
    (17, 4, 38)
    (18, 4, 9)
    (19, 4, 14)
    (20, 4, 22)
    (21, 4, 24)
    (22, 4, 25)
    (23, 4, 27)
    (24, 4, 28)
    (25, 4, 29)
    (26, 4, 30)
    (27, 5, 32)
    (28, 5, 33)
    (29, 5, 4)
    (30, 5, 5)
    (31, 5, 6)
    (32, 5, 38)
    (33, 5, 11)
    (34, 5, 14)
    (35, 5, 15)
    (36, 5, 22)
    (37, 5, 24)
    (38, 5, 25)
    (39, 5, 27)
    (40, 5, 28)
    (41, 5, 29)
    (42, 6, 1)
    (43, 6, 3)
    (44, 6, 4)
    (45, 6, 6)
    (46, 6, 11)
    (47, 6, 12)
    (48, 6, 13)
    (49, 6, 14)
    (50, 6, 15)
    (51, 6, 21)
    (52, 6, 22)
    (53, 6, 24)
    (54, 6, 25)
    (55, 6, 27)
    (56, 6, 28)
    (57, 6, 29)
    (58, 6, 32)
    (59, 6, 33)
    (60, 6, 38)
    (61, 7, 1)
    (62, 7, 2)
    (63, 7, 4)
    (64, 7, 6)
    (65, 7, 8)
    (66, 7, 10)
    (67, 7, 11)
    (68, 7, 12)
    (69, 7, 13)
    (70, 7, 14)
    (71, 7, 15)
    (72, 7, 21)
    (73, 7, 22)
    (74, 7, 24)
    (75, 7, 25)
    (76, 7, 27)
    (77, 7, 28)
    (78, 7, 29)
    (79, 7, 32)
    (80, 7, 33)
    (81, 7, 38)
    (82, 8, 1)
    (83, 8, 2)
    (84, 8, 3)
    (85, 8, 4)
    (86, 8, 5)
    (87, 8, 6)
    (88, 8, 7)
    (89, 8, 8)
    (90, 8, 9)
    (91, 8, 10)
    (92, 8, 11)
    (93, 8, 12)
    (94, 8, 13)
    (95, 8, 14)
    (96, 8, 15)
    (97, 8, 21)
    (98, 8, 22)
    (99, 8, 24)
    (100, 8, 25)
    (101, 8, 27)
    (102, 8, 28)
    (103, 8, 29)
    (104, 8, 32)
    (105, 8, 33)
    (106, 8, 38)
    (107, 8, 41)
    (108, 8, 42)
    (109, 8, 43)
    (110, 8, 44)
    (111, 8, 45)
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

with open('Querys/load_esmartdata_course.sql', 'r', encoding='utf-8') as file:
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

with open('Querys/load_esmartdata_learningpath.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

with open('Querys/load_esmartdata_learningpath_courses.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

print('Data successfully loaded!')

cur.execute('''SELECT * FROM "esmartdata_learningpath_courses";''')

for rows in cur.fetchall():
    print(rows)

conn.commit()
conn.close()
