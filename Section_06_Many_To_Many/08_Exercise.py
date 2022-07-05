"""
Exercise No. 08

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

All operations performed so far on this database can be found in the file create_database.sql.

Create a query that will display the names of all indexes from the 'esmartdata_sqlite3' database.

Expected Result:
    esmartdata_course_instructor_id_idx
    esmartdata_learningpath_courses_learningpath_id_idx
    esmartdata_learningpath_courses_course_id_idx
    esmartdata_learningpath_courses_learningpath_id_course_id_idx
"""
import sqlite3


conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open('create_database.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''SELECT name FROM sqlite_master WHERE type='index' AND name NOT LIKE 'sqlite_%';''')

for row in cur.fetchall():
    print(row[0])

conn.commit()
conn.close()
