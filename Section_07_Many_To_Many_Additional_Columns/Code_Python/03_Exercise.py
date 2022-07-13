"""
Exercise No. 03

Using the built-in sqlite3 package, SQLite database 'esmartdata_sqlite3' was prepared, which contains the following
tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_membership'

Using the script load_membership.sql attached to the exercise, load the data into the 'esmartdata_learningpath' and
'esmartdata_membership' tables.

Due to Polish characters, use the 'utf8' encoding when opening the script(encoding argument of the open() function).
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open("../Query/create_database.sql", encoding="utf-8") as file:
    sql = file.read()
cur.executescript(sql)

print("Table created successfully!")

with open('../Query/load_membership.sql', encoding="utf-8") as file:
    sql = file.read()
cur.executescript(sql)

print('Data entered successfully!')

conn.commit()
conn.close()
