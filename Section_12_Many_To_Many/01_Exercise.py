"""
Exercise No. 01

Using the built-in sqlite3 package, SQLite database called 'company.db' was prepared, which contains the following
tables:
    - esmartdata_user
    - esmartdata_developer

in this database, create a 'esmartdata_tech' with the following columns (column name - data type):
    - id - integer
    - name - text

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

Also create a table 'esmartdata_developer_techs' with the following columns (column name - data type):
    - id - integer
    - developer_id - integer
    - tech_id - integer

Add a NOT NULL constraint to each column. Also add a primary key constraint with the AUTOINCREMENT option to the id
column.

To the developer_id column, add a foreign key constraint referring to the id column of the table 'esmartdata_developer'
table with ON DELETE CASCADE ON UPDATE CASCADE options.

To the tech_id column, add a foreign key constraint referring to the id column of the table 'esmartdata_tech' table with
ON DELETE CASCADE ON UPDATE CASCADE options.

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS "esmartdata_user";

CREATE TABLE IF NOT EXISTS "esmartdata_user" (
  "id" integer NOT NULL,
  "first_name" text NOT NULL,
  "last_name" text NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_developer";

CREATE TABLE IF NOT EXISTS "esmartdata_developer" (
  "user_id" integer NOT NULL,
  "level" text NOT NULL,
  PRIMARY KEY("user_id"),
  FOREIGN KEY("user_id") REFERENCES "esmartdata_user"("id")
  ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "esmartdata_tech";

CREATE TABLE IF NOT EXISTS "esmartdata_tech" (
    "id" integer NOT NULL,
    "name" text NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_developer_techs";

CREATE TABLE IF NOT EXISTS "esmartdata_developer_techs" (
    "id" integer NOT NULL,
    "developer_id" integer NOT NULL,
    "tech_id" integer NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("developer_id") REFERENCES "esmartdata_developer"("user_id")
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY("tech_id") REFERENCES "esmartdata_tech"("id")
    ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

conn.commit()
conn.close()
