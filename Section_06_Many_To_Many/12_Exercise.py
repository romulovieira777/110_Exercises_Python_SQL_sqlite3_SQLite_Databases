"""
Exercise No. 12

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

All operations performed so far on this database can be found in the file create_database.sql.

From the database, we need to extract all names of the learning paths with names of courses appearing in the path and
name of the instructor (see below).

Create a query that will extract the following information:
    - tile column from the 'esmartdata_learningpath' table, assign alias 'path_title'.
    - title column from the 'esmartdata_course' table, assign alias 'course_title'.
    - instructor - concatenation of the first_name and last_name columns with a space character('esmartdata_instructor'
    table).

Limit the output to the first 10 rows records and print to the console as shown below.

Expected Result:
    ('Ścieżka C Developer', 'Programowanie w języku C - od A do Z', 'takeITeasy Academy')
    ('Ścieżka C Developer', '150+ Ćwiczeń - Programowanie w języku C - od A do Z', 'takeITeasy Academy')
    ('Ścieżka C++ Developer', 'Programowanie w języku C++ - od A do Z', 'takeITeasy Academy')
    ('Ścieżka C++ Developer', '150+ Ćwiczeń - Programowanie w języku C++ - od A do Z', 'takeITeasy Academy')
    ('Ścieżka C++ Developer', '150+ Ćwiczeń - Programowanie obiektowe w języku C++ - OOP', 'takeITeasy Academy')
    ('Ścieżka Python Developer', 'Programowanie w języku Python - od A do Z', 'Paweł Krakowiak')
    ('Ścieżka Python Developer', '100+ Ćwiczeń - Zaawansowane programowanie w języku Python', 'Paweł Krakowiak')
    ('Ścieżka Python Developer', '200+ Ćwiczeń - Programowanie w języku Python - od A do Z', 'Paweł Krakowiak')
    ('Ścieżka Python Developer', '210+ Ćwiczeń - Python - Moduły wbudowane - od A do Z', 'Paweł Krakowiak')
    ('Ścieżka Python Developer', 'Programowanie obiektowe w języku Python - OOP - od A do Z', 'Paweł Krakowiak')
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open('Querys\create_database.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''SELECT
    esmartdata_learningpath.title                                               AS path_title
  , esmartdata_course.title                                                     AS course_title
  , esmartdata_instructor.first_name || ' ' || esmartdata_instructor.last_name  AS instructor
FROM
    esmartdata_learningpath_courses
LEFT JOIN
    esmartdata_learningpath
ON
    esmartdata_learningpath_courses.learningpath_id = esmartdata_learningpath.id
LEFT JOIN
    esmartdata_course
ON
    esmartdata_learningpath_courses.course_id = esmartdata_course.id
LEFT JOIN
    esmartdata_instructor
ON
    esmartdata_course.instructor_id = esmartdata_instructor.id
LIMIT
    10;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
