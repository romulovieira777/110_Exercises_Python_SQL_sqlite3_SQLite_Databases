"""
Exercise No. 10

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

All operations performed so far on this database can be found in the file create_database.sql.

From the database, we need to extract all the names of the learning paths with the names of the courses appearing in the
paths and the subcategory ofg a given course(see below).

Create a query that will extract the following information.
    - title column from 'esmartdata_learningpath' table, assign alias 'path_title.
    - title column from 'esmartdata_course' table, assign alias 'course_title.
    - subcategory column from 'esmartdata_course' table.

Sort the output table by the path_title and course_title columns in ascending order. Limit the result to the first
10 records and print to the console as shown below.

Expected Result:
    ('Ścieżka All-in-One', '100+ Ćwiczeń - Zaawansowane programowanie w języku Python', 'programming languages')
    ('Ścieżka All-in-One', '120+ Ćwiczeń w języku Python - Data Science - NumPy', 'data science')
    ('Ścieżka All-in-One', '130+ Ćwiczeń w języku Python - Data Science - Pandas', 'data science')
    ('Ścieżka All-in-One', '150+ Ćwiczeń - Programowanie obiektowe w języku C++ - OOP', 'programming languages')
    ('Ścieżka All-in-One', '150+ Ćwiczeń - Programowanie obiektowe w języku Python - OOP', 'programming languages')
    ('Ścieżka All-in-One', '150+ Ćwiczeń - Programowanie w języku C - od A do Z', 'programming languages')
    ('Ścieżka All-in-One', '150+ Ćwiczeń - Programowanie w języku C++ - od A do Z', 'programming languages')
    ('Ścieżka All-in-One', '200+ Ćwiczeń - Programowanie w języku Python - od A do Z', 'programming languages')
    ('Ścieżka All-in-One', '210+ Ćwiczeń - Python - Moduły wbudowane - od A do Z', 'programming languages')
    ('Ścieżka All-in-One', '250+ Ćwiczeń - Data Science Bootcamp w języku Python', 'programming languages')
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open('Querys\create_database.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)


cur.execute('''SELECT esmartdata_learningpath.title AS path_title, esmartdata_course.title AS course_title, esmartdata_course.subcategory
FROM esmartdata_learningpath
LEFT JOIN esmartdata_learningpath_courses
ON esmartdata_learningpath.id = esmartdata_learningpath_courses.learningpath_id
LEFT JOIN esmartdata_course
ON esmartdata_learningpath_courses.course_id = esmartdata_course.id
ORDER BY path_title, course_title
LIMIT 10;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
