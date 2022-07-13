"""
Exercise No. 13

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

All operations performed so far on this database can be found in the file create_database.sql.

From the database, we need to extract information about the number of courses for each instructor in all paths.

Create a query that will extract the following information:
    - title column from the 'esmartdata_learningpath' table, assign alias 'path_title'.
    - instructor - concatenation of first_name and last_name columns with a space character
    ('esmartdata_instructor' table).
    - num_courses - number of courses per instructor in the given learning path.

Sort the output table in ascending order by the path_title and instructor columns and print it to the console as show
below.

Expected Result:
    ('Ścieżka All-in-One', 'Paweł Krakowiak', 25)
    ('Ścieżka All-in-One', 'takeITeasy Academy', 5)
    ('Ścieżka BI Analyst / Data Analyst', 'Paweł Krakowiak', 15)
    ('Ścieżka Big Data Analyst', 'Paweł Krakowiak', 13)
    ('Ścieżka C Developer', 'takeITeasy Academy', 2)
    ('Ścieżka C++ Developer', 'takeITeasy Academy', 3)
    ('Ścieżka Data Scientist / Deep Learning Engineer', 'Paweł Krakowiak', 21)
    ('Ścieżka Data Scientist / Machine Learning Engineer', 'Paweł Krakowiak', 19)
    ('Ścieżka Python Developer', 'Paweł Krakowiak', 8)
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''SELECT esmartdata_learningpath.title AS path_title, 
esmartdata_instructor.first_name || ' ' || esmartdata_instructor.last_name AS instructor, 
COUNT(esmartdata_learningpath_courses.course_id) AS num_courses
FROM esmartdata_learningpath_courses
LEFT JOIN esmartdata_learningpath
ON esmartdata_learningpath_courses.learningpath_id = esmartdata_learningpath.id
LEFT JOIN esmartdata_course
ON esmartdata_learningpath_courses.course_id = esmartdata_course.id
LEFT JOIN esmartdata_instructor
ON esmartdata_course.instructor_id = esmartdata_instructor.id
GROUP BY esmartdata_learningpath.title, esmartdata_instructor.first_name || ' ' || esmartdata_instructor.last_name
ORDER BY path_title, instructor;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
