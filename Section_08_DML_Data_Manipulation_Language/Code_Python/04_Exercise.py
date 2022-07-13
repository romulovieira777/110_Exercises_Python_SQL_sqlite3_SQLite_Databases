"""
Exercise No. 04

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

The table 'esmartdata_instructor' contains two records. Using the appropriate statement, insert another record using the
dictionary below:
    record = {
        'id': 3, 'first_name': 'Mike', 'last_name': 'Json', 'description': 'Python Developer'
    }

You shouldn't assemble your query using Python's string operations because doing so is insecure. It makes your program
vulnerable to an SQL injection attack. Instead, use DB-API's parameter substitution. An SQL statement may use one of two
kinds of placeholders: question marks(qmark style) or named placeholders(named style). For the named style, it can be
for example a dict instance. If a dict is given, it must contain keys for all named parameters. Put all named parameters
wherever you want to use a value, and then provide a dict instance as the second argument to the cursor's execute()
method.

Commit the changes and create a query which will display the contents of the 'esmartdata_instructor' table to the
console as show below.

Tip: https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute

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

record = {
    'id': 3, 'first_name': 'Mike', 'last_name': 'Json', 'description': 'Python Developer'
}

cur.execute('''INSERT INTO "esmartdata_instructor" ("id", "first_name", "last_name", "description")
VALUES(:id, :first_name, :last_name, :description);''', record)

print('Data entered successfully!\n')

cur.execute("SELECT * FROM esmartdata_instructor;")

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
