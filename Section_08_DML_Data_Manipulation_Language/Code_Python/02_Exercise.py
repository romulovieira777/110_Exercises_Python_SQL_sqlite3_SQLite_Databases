"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

The tble 'esmartdata_instructor' contains two records. Using the appropriate statement, insert another record with the
following tuple:
    record = (3, 'Mike', 'Json', 'Python Developer')

You shouldn't assemble your query using Python's string operations because doing so is insecure. It makes your program
vulnerable to an SQL injection attack. Instead, use DB-API's parameter substitution. Put a placeholder ? wherever you
want to use a value, and then provide a tuple of values as the second argument to the cursor's execute() method.

Commit the changes and create a query which will display the contents of the 'esmartdata_instructor' table to the
console as show below.

Tip: https://docs.python.org/3/library/sqlite3.html

Expected Result:
    (1, 'Paweł', 'Krakowiak', 'Data Scientist/Python Developer/Securities Broker')
    (2, 'takeITeasy', 'Academy', 'Akademia Programowania')
    (3, 'Mike', 'Json', 'Python Developer')
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open("../Query/create_database.sql", "r", encoding="utf8") as file:
    sql = file.read()
cur.executescript(sql)

record = (3, 'Mike', 'Json', 'Python Developer')

cur.execute('''INSERT INTO "esmartdata_instructor" ("id", "first_name", "last_name", "description") 
VALUES(?, ?, ?, ?);''', record)

print('Data entered successfully!\n')

cur.execute("SELECT * FROM esmartdata_instructor;")

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
