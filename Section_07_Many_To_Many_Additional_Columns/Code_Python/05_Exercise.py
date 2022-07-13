"""
Exercise No. 05

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

From the created column of the 'esmartdata_membership' table, extract the month number and assign it to the 'month' column.
Also extract the symbol representing the quarter ('Q1', 'Q2', 'Q3', 'Q4') and assign it to the 'quarter' column.

The output table should have the following columns:
    - created column from the table 'esmartdata_membership'
    - month column with the month number.
    - quarter column with the quarter symbol.

Use the SELECT CASE statement in your solution. In response, print the result to the console as shown below.

Expected Result:
    ('2021-02-03', 2, 'Q1')
    ('2021-02-17', 2, 'Q1')
    ('2021-03-15', 3, 'Q2')
    ('2021-03-22', 3, 'Q2')
    ('2021-05-12', 5, 'Q2')
    ('2021-01-05', 1, 'Q1')
    ('2021-01-26', 1, 'Q1')
    ('2021-02-05', 2, 'Q1')
    ('2021-03-08', 3, 'Q2')
    ('2021-03-30', 3, 'Q2')
    ('2021-05-11', 5, 'Q2')
    ('2021-04-13', 4, 'Q2')
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open("../Query/create_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

cur.execute('''SELECT created, CAST(strftime('%m', created) AS INTEGER) AS month,
CASE
   WHEN CAST(strftime('%m', created) AS INTEGER) IN(0, 1, 2) THEN 'Q1'
   WHEN CAST(strftime('%m', created) AS INTEGER) IN(3, 4, 5) THEN 'Q2'
   WHEN CAST(strftime('%m', created) AS INTEGER) IN(6, 7, 8) THEN 'Q3'
   WHEN CAST(strftime('%m', created) AS INTEGER) IN(10, 11, 12) THEN 'Q4'
END AS quarter
FROM
    esmartdata_membership;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
