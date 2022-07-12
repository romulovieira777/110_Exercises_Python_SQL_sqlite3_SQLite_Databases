"""
Exercise No. 03

Using the built-in sqlite3 package, SQLite database called 'company.db' was prepared, which contains the following
tables:
    - 'esmartdata_user'
    - 'esmartdata_developer'
    - 'esmartdata_tech'
    - 'esmartdata_developer_techs'

Create a query that will join the data from the 'esmartdata_user' table with the 'esmartdata_developer' table(LEFT JOIN).
In the output table, display the following columns:
    - first_name
    - last_name
    - level

Print the result to the console as shown below.

Expected Result:
    ('Daniel', 'Harris', 'junior')
    ('Daniel', 'Thompson', 'mid')
    ('Shelly', 'Hudson', 'senior')
    ('John', 'Taylor', 'senior')
    ('Sharon', 'Johnson', 'junior')
    ('Carol', 'Horn', 'mid')
    ('Paula', 'Burke', 'junior')
    ('Michaela', 'Garrison', 'senior')
    ('William', 'Lopez', 'mid')
    ('James', 'Simons', 'senior')
    ('Joshua', 'Brown', None)
    ('Mason', 'Robinson', None)
    ('Lisa', 'Johnson', None)
"""
import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

with open("Querys\load_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

cur.execute('''SELECT esmartdata_user.first_name, esmartdata_user.last_name, esmartdata_developer.level 
FROM esmartdata_user LEFT JOIN esmartdata_developer ON esmartdata_user.id = esmartdata_developer.user_id;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
