"""
Exercise No. 01

Using the built-in sqlite3 package, create SQLite database named esmartdata.sqlite3.

Then create a tabela in this database called esmartdata._instructor with the following columns (column name - data type);
    - id - integer
    - first_name - text
    - last_name - text
    - description - text

Add a NOT NULL constraint to each column. Also add a primary key constraint with AUTOINCREMENT option to the id column.

Before creating the table, use the appropriate SQL command that will delete the esmartdata_instructor table if such a
table already exists in database.

Commit the changes and close the database connection.
"""
import sqlite3


# Connecting...
conn = sqlite3.connect('esmartdata.sqlite3')

# Defining a cursor
cursor = conn.cursor()

# Creating the table (Schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    description TEXT NOT NULL
)""")

print("Table created successfully!")

conn.commit()
conn.close()

"""
#SOLUTION I:

import sqlite3

conn = sqlite3.connect('esmartdata.sqlite3')
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS "esmartdata_instructor";
CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
 "id" integer NOT NULL,
 "first_name" text NOT NULL,
 "last_name" text NOT NULL,
 "description" text NOT NULL,
 PRIMARY KEY("id" AUTOINCREMENT)
 );''')

print("Table created successfully!")

conn.commit()
conn.close()


Solution II:
import sqlite3


conn = sqlite3.connect('esmartdata.sqlite3')
cur = conn.cursor()
 
cur.execute('''DROP TABLE IF EXISTS "esmartdata_instructor"''')
cur.execute('''CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
  "id" integer NOT NULL,
  "first_name" text NOT NULL,
  "last_name" text NOT NULL,
  "description" text NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
)''')

print("Table created successfully!")

conn.commit()
conn.close()
"""
