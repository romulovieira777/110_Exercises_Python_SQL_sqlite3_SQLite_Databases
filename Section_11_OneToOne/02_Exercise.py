"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database called 'company.db' was prepared, which contains the
'esmartdata_user' table.

The 'esmartdata_user' table contains basic information about software house users. Some users can also be developers. We
will store additional developer information in a separate table named 'esmartdata_developer'. Before creating this table,
you should consider the type of relationship between the two tables. In this case, the answer is simple, one user -> one
developer (one-to-one).

In this database, create a table named 'esmartdata_developer' with the following columns (column name - data type):
    - user_id - integer
    - level - text

Add a NOT NULL constraint to each column. Add a primary key constraint to the user_id column.

Also add to the user_id column the foreign key constraint referring to the id column of the table 'esmartdata_user'
with the ON DELETE CASCADE ON UPDATE CASCADE options.

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS esmartdata_user;

CREATE TABLE IF NOT EXISTS esmartdata_user
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

DROP TABLE IF EXISTS esmartdata_developer;

CREATE TABLE IF NOT EXISTS esmartdata_developer
(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    level TEXT NOT NULL,
    FOREIGN KEY ("user_id") REFERENCES "esmartdata_user"("id") ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

conn.commit()
conn.close()
