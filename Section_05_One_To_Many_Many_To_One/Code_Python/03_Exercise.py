"""
Exercise No. 03

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'

Insert into the 'esmartdata_instructor' table two records with the following data:
    - 1, 'Pawel', 'Krakowiak', 'Data Scientist/Python Developer/Securities Broker'
    - 2, 'takeITeasy, 'Academy', 'Akademia Programowania'

Commit the changes and close the database connection.
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS "esmartdata_instructor";
CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
    "id" INTEGER NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_course";
CREATE TABLE IF NOT EXISTS "esmartdata_course" (
    "id" INTEGER NOT NULL,
    "title" TEXT NULL,
    "subtitle" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "category" TEXT NOT NULL,
    "subcategory" TEXT NOT NULL,
    "language" TEXT NOT NULL,
    "length" TEXT NOT NULL,
    "rating" REAL NOT NULL,
    "referral_link" TEXT NOT NULL,
    "instructor_id" INTEGER NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("instructor_id") REFERENCES "esmartdata_instructor"(id)
    ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

cur.execute('''INSERT INTO "esmartdata_instructor"
(
    "id",
    "first_name",
    "last_name",
    "description"
) 
VALUES
(
    1,
    "Pawel",
    "Krakowiak",
    "Data Scientist/Python Developer/Securities Broker"
)
''')

cur.execute('''INSERT INTO "esmartdata_instructor"
(
    "id",
    "first_name",
    "last_name",
    "description"
) 
VALUES
(
    2,
    "takeITeasy",
    "Academy",
    "Akademia Programowania"
)
''')

print('Data entered successfully!')

conn.commit()
conn.close()
