"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

When working with database, we will often want to use  the values of variables in our queries. This exercise will show
you how not to do it.

The table 'esmartdata_instructor' contains two records. We have the following query:
    cur.execute(
        f"SELECT * FROM esmartdata_instructor WHERE id = {instructor_id}"
    )

We get the value of the instructor_id variable from the user. A picky user passed the following value for the
instructor_id variable:
    instructor_id = '2; DELETE FROM "esmartdata_instructor;"'

Execute this query. Then, in response, display the number of records in the 'esmartdata_instructor' table and print to
the console.

Note that the user of our application can make queries on our database. In particular, queries that may be irreversible
(delete of data).

CAUTION! Remember that this is not a secure solution. We only do this to show why it's vulnerable(in the next exercise).
When writing your own code, remember not to be exposed to SQL injection attacks.

Expected Result:
    0
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open("Querys\create_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

instructor_id = '2; DELETE FROM "esmartdata_instructor"'

cur.executescript(f"SELECT * FROM esmartdata_instructor WHERE id = {instructor_id}")
conn.commit()

cur.execute('SELECT COUNT(*) FROM esmartdata_instructor')
num_rows = cur.fetchone()[0]
print(num_rows)

conn.close()


