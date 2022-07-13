"""
Exercise No. 05

Using the built-in sqlite3 package, SQLite database called 'company.db' was prepared, which contains the following
tables:
    - 'esmartdata_user'
    - 'esmartdata_developer'
    - 'esmartdata_tech'
    - 'esmartdata_developer_techs'

Create a query that will join the tables 'esmartdata_user' , 'esmartdata_developer', 'esmartdata_developer_techs',
'esmartdata_tech'(all INNER JOIN). In the output table, display the columns:
    - first_name
    - last_name
    - level
    - tech_name(name column from the table 'esmartdata_tech').

Print the result to the console as shown below.

Expected Result:
    ('Daniel', 'Harris', 'junior', 'python')
    ('Daniel', 'Harris', 'junior', 'html')
    ('Daniel', 'Harris', 'junior', 'css')
    ('Daniel', 'Thompson', 'mid', 'python')
    ('Daniel', 'Thompson', 'mid', 'html')
    ('Daniel', 'Thompson', 'mid', 'css')
    ('Daniel', 'Thompson', 'mid', 'javascript')
    ('Daniel', 'Thompson', 'mid', 'django')
    ('Shelly', 'Hudson', 'senior', 'html')
    ('Shelly', 'Hudson', 'senior', 'css')
    ('Shelly', 'Hudson', 'senior', 'javascript')
    ('John', 'Taylor', 'senior', 'java')
    ('John', 'Taylor', 'senior', 'sql')
    ('John', 'Taylor', 'senior', 'git')
    ('Sharon', 'Johnson', 'junior', 'django')
    ('Sharon', 'Johnson', 'junior', 'python')
    ('Sharon', 'Johnson', 'junior', 'html')
    ('Sharon', 'Johnson', 'junior', 'git')
    ('Carol', 'Horn', 'mid', 'flutter')
    ('Carol', 'Horn', 'mid', 'dart')
    ('Carol', 'Horn', 'mid', 'git')
    ('Carol', 'Horn', 'mid', 'linux')
    ('Paula', 'Burke', 'junior', 'c++')
    ('Paula', 'Burke', 'junior', 'c#')
    ('Paula', 'Burke', 'junior', 'unity')
    ('Paula', 'Burke', 'junior', 'git')
    ('Paula', 'Burke', 'junior', 'linux')
    ('Michaela', 'Garrison', 'senior', 'java')
    ('Michaela', 'Garrison', 'senior', 'sql')
    ('Michaela', 'Garrison', 'senior', 'testing')
    ('William', 'Lopez', 'mid', 'python')
    ('William', 'Lopez', 'mid', 'html')
    ('William', 'Lopez', 'mid', 'css')
    ('William', 'Lopez', 'mid', 'javascript')
    ('William', 'Lopez', 'mid', 'django')
    ('William', 'Lopez', 'mid', 'git')
    ('James', 'Simons', 'senior', 'flutter')
    ('James', 'Simons', 'senior', 'dart')
    ('James', 'Simons', 'senior', 'swift')
    ('James', 'Simons', 'senior', 'kotlin')
"""
import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

with open("Querys\load_database.sql", "r", encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)

cur.execute('''SELECT esmartdata_user.first_name, esmartdata_user.last_name, esmartdata_developer.level, esmartdata_tech.name
FROM esmartdata_user INNER JOIN esmartdata_developer ON esmartdata_user.id = esmartdata_developer.user_id
INNER JOIN esmartdata_developer_techs ON esmartdata_developer.user_id = esmartdata_developer_techs.developer_id
INNER JOIN esmartdata_tech ON esmartdata_developer_techs.tech_id = esmartdata_tech.id;
''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
