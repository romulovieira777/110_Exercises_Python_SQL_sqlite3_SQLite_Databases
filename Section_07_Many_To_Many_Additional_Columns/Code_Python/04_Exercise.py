"""
Exercise No. 04

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

From the database, we need to extract information about the courses belonging to the paths, which were added from
2021-02-01 to 2021-03-31 (YYYY-MM-DD).

Create a query that will extract the following information:
    - created column from the 'esmartdata_membership' table.
    - title column from the 'esmartdata_course' table.

In response, print the output table to the console as shown below.

Expected Result:
    ('2021-02-03', 'Programowanie w języku C - od A do Z')
    ('2021-02-17', '150+ Ćwiczeń - Programowanie w języku C - od A do Z')
    ('2021-03-15', 'Programowanie w języku C++ - od A do Z')
    ('2021-03-22', '150+ Ćwiczeń - Programowanie w języku C++ - od A do Z')
    ('2021-02-05', '210+ Ćwiczeń - Python - Moduły wbudowane - od A do Z')
    ('2021-03-08', 'Programowanie obiektowe w języku Python - OOP - od A do Z')
    ('2021-03-30', '150+ Ćwiczeń - Programowanie obiektowe w języku Python - OOP')
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open("../Query/create_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

cur.execute('''SELECT esmartdata_membership.created, esmartdata_course.title 
FROM esmartdata_course
LEFT JOIN esmartdata_membership
ON esmartdata_course.id = esmartdata_membership.course_id
WHERE esmartdata_membership.created BETWEEN '2021-02-01' AND '2021-03-31';
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
