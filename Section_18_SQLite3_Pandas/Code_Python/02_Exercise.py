"""
Exercise No. 02

Using the built-in sqlite3 package, a SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

A query was created that extracts the first ten records of the "app_user" table and transforms into a DataFrame
(df variable). Export this DataFrame to a CSV file called "app_user.csv".

Content of the "app_user.csv" file:
    id,first_name,last_name,age,country,city,email
    1,John,Lewis,61,Tonga,East Michael,johnsonjack@esmartdata.org
    2,Lance,Boyer,21,Seychelles,Janicetown,thodges@esmartdata.org
    3,Michael,Larson,22,Czech Republic,West Melissa,kmalone@esmartdata.org
    4,Alexandra,Marshall,50,Malaysia,Lunamouth,yperry@esmartdata.org
    5,Rebecca,Maldonado,51,Canada,Lake Sandrastad,mwade@esmartdata.org
    6,Ronald,Ward,61,French Guiana,Kennethview,lisa46@esmartdata.org
    7,Justin,Wolf,19,French Southern Territories,Kristinestad,greenjustin@esmartdata.org
    8,Nicole,Fuentes,63,Gambia,Port Frank,brandonchandler@esmartdata.org
    9,Melissa,Rowland,45,Sudan,Alexiston,gibsonjennifer@esmartdata.org
    10,Sean,Schmidt,42,Nauru,Alyssafort,vterry@esmartdata.org
"""
import pandas as pd
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database
cur = conn.cursor()  # create a cursor object

with open("../Query/create_database.sql", "r", encoding='utf-8') as file:
    create_database_sql = file.read()  # read the sql query from the file
cur.executescript(create_database_sql)  # execute the sql query

df = pd.read_sql_query("SELECT * FROM app_user LIMIT 10;", conn, index_col='id')  # read the data from the database
df.to_csv('../Dataset/app_user.csv')  # export the data to a CSV file

conn.close()  # close the connection
