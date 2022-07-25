"""
Exercise No. 03

Using the built-in sqlite3 package, a SQLite database called "app_db" was created with "app_user" table.

Create a query that extracts all records from the "app_user" table for users between 20 and 30 years old (inclusive)
sorted by ascending id.

Query result:
    (2, 'Lance', 'Boyer', 21, 'Seychelles', 'Janicetown', 'thodges@esmartdata.org')
    (3, 'Michael', 'Larson', 22, 'Czech Republic', 'West Melissa', 'kmalone@esmartdata.org')
    (17, 'Michael', 'Turner', 23, 'Gambia', 'West Timothy', 'matthewcox@esmartdata.org')
    (19, 'Scott', 'Berry', 20, 'Macedonia', 'New Joshua', 'uhanson@esmartdata.org')
    (24, 'Kimberly', 'Myers', 28, 'Aruba', 'West Lauraland', 'mccormickdavid@esmartdata.org')
    (25, 'Carol', 'Walton', 24, 'Mauritania', 'New Ethan', 'stephen65@esmartdata.org')
    (26, 'Larry', 'Rowe', 27, 'Jersey', 'West Alexander', 'riverajames@esmartdata.org')
    (28, 'Benjamin', 'Lopez', 22, 'Cape Verde', 'Nancybury', 'william31@esmartdata.org')
    (29, 'Kenneth', 'Perry', 30, 'Guinea-Bissau', 'Romeroburgh', 'choidaniel@esmartdata.org')
    (41, 'Dwayne', 'Nelson', 21, 'Bulgaria', 'Port Destiny', 'larrypace@esmartdata.org')
    (44, 'Nicole', 'Sanchez', 24, 'Lesotho', 'Hallmouth', 'christina47@esmartdata.org')
    (48, 'Sara', 'Hensley', 28, 'Saudi Arabia', 'Randybury', 'crystalscott@esmartdata.org')

Using the built-in csv module, save the result of this query to afile named "users_20_to)30.csv".

Expected content of the file "users_20_to_30.csv":
    id,first_name,last_name,age,country,city,email
    2,Lance,Boyer,21,Seychelles,Janicetown,thodges@esmartdata.org
    3,Michael,Larson,22,Czech Republic,West Melissa,kmalone@esmartdata.org
    17,Michael,Turner,23,Gambia,West Timothy,matthewcox@esmartdata.org
    19,Scott,Berry,20,Macedonia,New Joshua,uhanson@esmartdata.org
    24,Kimberly,Myers,28,Aruba,West Lauraland,mccormickdavid@esmartdata.org
    25,Carol,Walton,24,Mauritania,New Ethan,stephen65@esmartdata.org
    26,Larry,Rowe,27,Jersey,West Alexander,riverajames@esmartdata.org
    28,Benjamin,Lopez,22,Cape Verde,Nancybury,william31@esmartdata.org
    29,Kenneth,Perry,30,Guinea-Bissau,Romeroburgh,choidaniel@esmartdata.org
    41,Dwayne,Nelson,21,Bulgaria,Port Destiny,larrypace@esmartdata.org
    44,Nicole,Sanchez,24,Lesotho,Hallmouth,christina47@esmartdata.org
    48,Sara,Hensley,28,Saudi Arabia,Randybury,crystalscott@esmartdata.org
"""
import csv
import sqlite3

conn = sqlite3.connect("app_db")    # create a database
cur = conn.cursor()    # create a cursor

cur.executescript('''DROP TABLE IF EXISTS "app_user";
CREATE TABLE IF NOT EXISTS "app_user" (
    "id" integer NOT NULL,
    "first_name" text NOT NULL,
    "last_name" text NOT NULL,
    "age" integer NOT NULL,
    "country" text NOT NULL,
    "city" text NOT NULL,
    "email" text NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
)''')   # create a table

print("Table created successfully.\n")

with open('../Dataset/app_user.csv', 'r') as file:
    reader = csv.DictReader(file)   # create a reader
    records = tuple(reader)       # create a tuple

cur.executemany('''INSERT INTO
    "app_user" (
        "id",
        "first_name",
        "last_name",
        "age",
        "country",
        "city",
        "email"
    )
VALUES
    (
        :id,
        :first_name,
        :last_name,
        :age,
        :country,
        :city,
        :email
    );''', records)   # insert data into the table

print("Data inserted successfully.\n")

conn.commit()   # commit the changes

cur.execute('''PRAGMA table_info("app_user");''')   # get the table info
headers = [row[1] for row in cur.fetchall()]   # get the headers

cur.execute('''SELECT *
FROM "app_user"
WHERE "age" BETWEEN 20 AND 30
ORDER BY "id" ASC;''')   # create a table

rows = cur.fetchall()   # fetch all the rows

with open('../Dataset/users_20_to_30.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')   # create a writer
    writer.writerow(headers)   # write the rows to the file
    for row in rows:
        writer.writerow(row)   # write the rows to the file

conn.close()   # close the connection
