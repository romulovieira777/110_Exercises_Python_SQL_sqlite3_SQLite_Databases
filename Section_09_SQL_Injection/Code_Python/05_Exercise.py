"""
Exercise No. 05

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

All operations performed so far on this database can be found in the file create_database.sql.

Implement a function named insert_row() that takes four arguments:
    - id
    - first_name
    - last_name
    - description

And inserts a record with theses values into the table 'esmartdata_instructor'. Remember that your code should not be
exposed to SQL injection attacks. Use named placeholders in your solution.

Then call the insert_row() function and insert the following records:
    - 3, "Mike", "Json", "Software Engineer"
    - 4, "Jonathan", "Parquet", "SQL Developer"

Commit the changes and print all records from the table 'esmartdata_instructor' to the console as shown below.

Expected Result:
    (1, 'Paweł', 'Krakowiak', 'Data Scientist/Python Developer/Securities Broker')
    (2, 'takeITeasy', 'Academy', 'Akademia Programowania')
    (3, 'Mike', 'Json', 'Software Engineer')
    (4, 'Jonathan', 'Parquet', 'SQL Developer')
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open("../Query/create_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)


def insert_row(id, first_name, last_name, description):
    record = {
        'id': id,
        'first_name': first_name,
        'last_name': last_name,
        'description': description
    }
    cur.execute('''INSERT INTO esmartdata_instructor(id, first_name, last_name, description) 
        VALUES (:id, :first_name, :last_name, :description)''', record)
    print("data entered successfully!")


insert_row(3, "Mike", "Json", "Software Engineer")
insert_row(4, "Jonathan", "Parquet", "SQL Developer")
conn.commit()

cur.execute('''SELECT * FROM esmartdata_instructor''')

for row in cur.fetchall():
    print(row)

conn.close()
