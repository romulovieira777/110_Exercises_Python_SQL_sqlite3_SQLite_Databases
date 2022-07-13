"""
Exercise No. 06

Using the built-in sqlite3 package, SQLite database called 'company.db' was prepared, which contains the following
tables:
    - 'esmartdata_user'
    - 'esmartdata_developer'
    - 'esmartdata_tech'
    - 'esmartdata_developer_techs'

We want to extract from the database information about the number of know technology for each developer.

Create a query that will join the tables 'esmartdata_user', 'esmartdata_developer', 'esmartdata_developer_techs',
'esmartdata_tech'(all INNER JOIN). In the output table, display the columns:
    - first_name
    - last_name
    - level
    - num_techs - number of technologies for each developer.

Sort the output by the num_techs column in descending order and the first_name column in ascending order. Print result
to the console as shown below.

Expected Result:
    ('William', 'Lopez', 'mid', 6)
    ('Daniel', 'Thompson', 'mid', 5)
    ('Paula', 'Burke', 'junior', 5)
    ('Carol', 'Horn', 'mid', 4)
    ('James', 'Simons', 'senior', 4)
    ('Sharon', 'Johnson', 'junior', 4)
    ('Daniel', 'Harris', 'junior', 3)
    ('John', 'Taylor', 'senior', 3)
    ('Michaela', 'Garrison', 'senior', 3)
    ('Shelly', 'Hudson', 'senior', 3)
"""
import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

with open("Querys\load_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

cur.execute('''SELECT esmartdata_user.first_name, esmartdata_user.last_name, esmartdata_developer.level,
    COUNT(esmartdata_developer_techs.tech_id) AS num_techs
    FROM esmartdata_user
    INNER JOIN esmartdata_developer ON esmartdata_user.id = esmartdata_developer.user_id
    INNER JOIN esmartdata_developer_techs ON esmartdata_developer.user_id = esmartdata_developer_techs.developer_id
    INNER JOIN esmartdata_tech ON esmartdata_developer_techs.tech_id = esmartdata_tech.id
    GROUP BY esmartdata_user.first_name, esmartdata_user.last_name, esmartdata_developer.level
    ORDER BY num_techs DESC, esmartdata_user.first_name ASC''')

for rows in cur.fetchall():
    print(rows)

conn.commit()
conn.close()
