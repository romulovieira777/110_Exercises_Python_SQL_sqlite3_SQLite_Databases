"""
Exercise No. 01

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

The tble 'esmartdata_instructor' contains two records. Using the appropriate statement, insert another record with the
following data:
    (3, 'Mike', 'Json', 'Python Developer')

Commit the changes and execute the command which will displpay the contents of the 'esmartdata_instructor' table to the
console as show below.

Expected Result:
    (1, 'Paweł', 'Krakowiak', 'Data Scientist/Python Developer/Securities Broker')
    (2, 'takeITeasy', 'Academy', 'Akademia Programowania')
    (3, 'Mike', 'Json', 'Python Developer')
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open("Querys\create_database.sql", "r", encoding="utf8") as file:
    sql = file.read()
cur.executescript(sql)

cur.execute('''INSERT INTO "esmartdata_instructor" ("id", "first_name", "last_name", "description") 
VALUES (3, 'Mike', 'Json', 'Python Developer');''')

print('Data entered successfully!\n')

cur.execute("SELECT * FROM esmartdata_instructor;")

for row in cur.fetchall():
    print(row)

''' 1 - Example
for row in cur.execute("SELECT * FROM esmartdata_instructor;"):
    print(row)
'''

conn.commit()
conn.close()
