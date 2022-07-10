"""
Exercise No. 03

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

The table 'esmartdata_instructor' contains two records. We have the following instructor_id variable:
    instructor_id = 2

Transform the following query:
    '''SELECT * FROM esmartdata_instructor WHERE id = {instructor_id}'''

so that it is not exposed to SQL injection attacks. Use question marks(qmark style) placeholders in the solution.

In response, execute this query and print result to the console as shown below.

Expected Result:
    (2, 'takeITeasy', 'Academy', 'Akademia Programowania')
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open("Querys\create_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

instructor_id = 2

cur.execute('SELECT * FROM esmartdata_instructor WHERE id = ?', (instructor_id,),)

for row in cur.fetchall():
    print(row)

conn.close()
