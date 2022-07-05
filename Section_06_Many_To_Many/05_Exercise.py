"""
Exercise No. 05

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

All operations performed so far on this database can be found in the file create_database.sql.

Create an index named 'esmartdata_learningpath_courses_learningpath_id_idx' for the learningpath_id column of the
"esmartdata_learningpath_courses" table.

Before creating the index, use the appropriate SQL command that will remove the index
'esmartdata_learningpath_courses_learningpath_id_idx if it exists in the database.

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open('Querys/create_database.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.executescript('''DROP INDEX IF EXISTS "esmartdata_learningpath_courses_learningpath_id_idx";
CREATE INDEX "esmartdata_learningpath_courses_learningpath_id_idx" ON "esmartdata_learningpath_courses" 
("learningpath_id");''')

print('Index created successfully!')

conn.commit()
conn.close()
