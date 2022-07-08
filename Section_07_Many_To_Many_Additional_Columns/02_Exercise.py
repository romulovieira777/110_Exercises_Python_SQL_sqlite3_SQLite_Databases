"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database 'esmartdata_sqlite3' was prepared, which contains the following
tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'

In this database, create a table named 'esmartdata_membership' with the following columns(column name - data type):
    - id - integer
    - created - text
    - course_id - integer
    - learningpath_id - integer

Add a NOT NULL constraint to each column. Also add a primary key constraint with AUTOINCREMENT option to the id column.

To the course_id column, add a foreign key constraint referring to the id column of the 'esmartdata_course' table with
ON DELETE CASCADE ON UPDATE CASCADE options.

To tthe learningpath_id column, add a foreign key constraint referring to the id column of the 'esmartdata_learningpath'
table with ON DELETE CASCADE ON UPDATE CASCADE options.
"""
import sqlite3

conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

with open("Querys\create_database.sql", encoding="utf-8") as file:
    sql = file.read()
cur.executescript(sql)

cur.executescript('''DROP TABLE IF EXISTS esmartdata_membership;
CREATE TABLE esmartdata_membership (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    created TEXT NOT NULL,
    course_id INTEGER NOT NULL,
    learningpath_id INTEGER NOT NULL,
    FOREIGN KEY (course_id) REFERENCES esmartdata_course(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (learningpath_id) REFERENCES esmartdata_learningpath(id) ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

conn.commit()
conn.close()
