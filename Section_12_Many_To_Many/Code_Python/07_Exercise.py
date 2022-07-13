"""
Exercise No. 07

Using the built-in sqlite3 package, SQLite database called 'company.db' was prepared, which contains the following
tables:
    - 'esmartdata_user'
    - 'esmartdata_developer'
    - 'esmartdata_tech'
    - 'esmartdata_developer_techs'

We want to extract information from the database about the number of developers broken down by experience.

Create a query that will join the tables 'esmartdata_user' and 'esmartdata_developer', 'esmartdata_developer_techs',
(INNER JOIN). In the output table, display the columns:
    - level
    - num_developers - number of developers for given level of experience.

Sort the output table in ascending order by the level column print it to the console as shown below.

Expected Result:
    ('junior', 3)
    ('mid', 3)
    ('senior', 4)
"""
import sqlite3

conn = sqlite3.connect("../company.db")
cur = conn.cursor()

with open("../Query/load_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

cur.execute('''SELECT esmartdata_developer.level, COUNT(esmartdata_developer.level) AS num_developers
    FROM esmartdata_developer
    GROUP BY esmartdata_developer.level
    ORDER BY esmartdata_developer.level ASC;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
