"""
Exercise No. 14

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

All operations performed so far on this database can be found in the file create_database.sql.

From the database, we need to extract information about the number of courses at category, sub-category and instructor
levels(see below).

Create a query that will extract the following information:
    - category column from the 'esmartdata_course' table).
    - sub_category column from the 'esmartdata_course' table).
    - instructor - concatenation of first_name and last_name columns with a space character
    ('esmartdata_instructor' table).
    - num_courses - number of courses per category, subcategory and instructor.

Sort the output table in ascending order by num_courses and print it to the console as show below.

Expected Result:
    ('development', 'programming languages', 'Paweł Krakowiak', 18)
    ('development', 'data science', 'Paweł Krakowiak', 14)
    ('development', 'database design & development', 'Paweł Krakowiak', 7)
    ('development', 'programming languages', 'takeITeasy Academy', 5)
    ('development', 'web development', 'Paweł Krakowiak', 1)
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open('Querys\create_database.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''SELECT
    esmartdata_course.category
  , esmartdata_course.subcategory
  , esmartdata_instructor.first_name || ' ' || esmartdata_instructor.last_name  AS instructor
  , COUNT(esmartdata_course.id)                                                 AS num_courses
FROM
    esmartdata_course
LEFT JOIN
    esmartdata_instructor
ON
    esmartdata_course.instructor_id = esmartdata_instructor.id
GROUP BY
   esmartdata_course.category
 , esmartdata_course.subcategory
 , instructor
ORDER BY
    num_courses DESC;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
