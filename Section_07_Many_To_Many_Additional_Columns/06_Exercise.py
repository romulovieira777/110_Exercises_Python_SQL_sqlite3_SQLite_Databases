"""
Exercise No. 06

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

From the created column of the 'esmartdata_membership' table, extract a symbol representing the quarter
('Q1', 'Q2', 'Q3', 'Q4') and assign it to the 'quarter'. Then group the data by quarter and count the number of all
courses for each quarter and assign it to the 'num_courses' column.

The output table should have the following columns:
    - quarter column with the symbol of the quarter.
    - num_courses column with the number of courses in a given quarter.

Use the SELECT CASE statement in your solution. In response, print the result to the console as shown below.

"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open("Querys\create_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

cur.execute('''SELECT CASE
    WHEN CAST(strftime('%m', created) AS INTEGER) IN(0, 1, 2) THEN 'Q1'
    WHEN CAST(strftime('%m', created) AS INTEGER) IN(3, 4, 5) THEN 'Q2'
    WHEN CAST(strftime('%m', created) AS INTEGER) IN(6, 7, 8) THEN 'Q3'
    WHEN CAST(strftime('%m', created) AS INTEGER) IN(10, 11, 12) THEN 'Q4'
END AS quarter,
COUNT(*) AS num_courses
FROM
    esmartdata_membership
GROUP BY quarter;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
