"""
Exercise No. 11

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

All operations performed so far on this database can be found in the file create_database.sql.

From the database, we need to extract all names of the learning paths with the number of courses in each path(see below).

Create a query that will extract the following information:
    - tile column from the 'esmartdata_learningpath' table, assign alias 'path_title'.
    - num_courses - the calculated number of courses for a given path.

Sort the output table by num_courses in descending order and print to the console as shown below.

Expected Result:

"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''SELECT esmartdata_learningpath.title AS path_title, COUNT(esmartdata_learningpath_courses.course_id) AS num_courses
FROM esmartdata_learningpath
LEFT JOIN esmartdata_learningpath_courses
ON esmartdata_learningpath.id = esmartdata_learningpath_courses.learningpath_id
GROUP BY esmartdata_learningpath.title
ORDER BY num_courses DESC;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
