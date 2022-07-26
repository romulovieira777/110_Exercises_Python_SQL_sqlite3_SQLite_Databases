"""
Exercise No. 06

Using the built-in sqlite3 package, create a SQLite database named "app.db".

A JSON file "app_user.json" is attached to the exercise. Using the pandas package, load this file into the DataFrame
object. Then, using this object, create a table named "test_app_user" in the database "app.db".

In response, create a query which extracts al records from the "test_app_user" table and print to the console as shown
below.

Expected Result:
    ('John', 'Lewis', 61, 'Tonga', 'East Michael', 'johnsonjack@esmartdata.org')
    ('Lance', 'Boyer', 21, 'Seychelles', 'Janicetown', 'thodges@esmartdata.org')
    ('Michael', 'Larson', 22, 'Czech Republic', 'West Melissa', 'kmalone@esmartdata.org')
    ('Alexandra', 'Marshall', 50, 'Malaysia', 'Lunamouth', 'yperry@esmartdata.org')
    ('Rebecca', 'Maldonado', 51, 'Canada', 'Lake Sandrastad', 'mwade@esmartdata.org')
    ('Ronald', 'Ward', 61, 'French Guiana', 'Kennethview', 'lisa46@esmartdata.org')
    ('Justin', 'Wolf', 19, 'French Southern Territories', 'Kristinestad', 'greenjustin@esmartdata.org')
    ('Nicole', 'Fuentes', 63, 'Gambia', 'Port Frank', 'brandonchandler@esmartdata.org')
    ('Melissa', 'Rowland', 45, 'Sudan', 'Alexiston', 'gibsonjennifer@esmartdata.org')
    ('Sean', 'Schmidt', 42, 'Nauru', 'Alyssafort', 'vterry@esmartdata.org')
"""
import pandas as pd
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database
cur = conn.cursor()  # create a cursor object

df = pd.read_json("../Dataset/app_user.json")  # read the data from the database
df.to_sql("test_app_user", con=conn, index=False, if_exists="replace")  # write the data to the database

cur.execute("SELECT * FROM test_app_user;")  # execute the sql query

for row in cur.fetchall():
    print(row)  # print the data to the console

conn.close()  # close the connection
