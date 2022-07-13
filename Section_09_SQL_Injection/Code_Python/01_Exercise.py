"""
Exercise No. 01

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

When working with database, we will often want to use  the values of variables in our queries. This exercise will show
you how not to do it.

The table 'esmartdata_instructor' contains two records. Using the appropriate command, display all data for the
instructor with the following instructor_id:
    instructor_id = 2

In this exercise, use f-string text formatting to insert the value of instructor_id into the query.

CAUTION! Remember that this is not a secure solution. We only do this to show why it's vulnerable(in the next exercise).
When writing your own code, remember not to be exposed to SQL injection attacks.

Expected Result:
    (2, 'takeITeasy', 'Academy', 'Akademia Programowania')
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open("../Query/create_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

instructor_id = 2

cur.execute(f"SELECT * FROM esmartdata_instructor WHERE id = {instructor_id}")

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
