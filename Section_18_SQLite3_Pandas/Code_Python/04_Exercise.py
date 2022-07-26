"""
Exercise No. 04

Using the built-in sqlite3 package, a SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

A query was created that extracts the first ten records of the "app_user" table and transforms into a DataFrame
(df variable). Export this DataFrame to a JSON file named "app_user.json" (set indent level = 4).

Content of the "app_user.json" file:
{
    "first_name":{
        "1":"John",
        "2":"Lance",
        "3":"Michael",
        "4":"Alexandra",
        "5":"Rebecca",
        "6":"Ronald",
        "7":"Justin",
        "8":"Nicole",
        "9":"Melissa",
        "10":"Sean"
    },
    "last_name":{
        "1":"Lewis",
        "2":"Boyer",
        "3":"Larson",
        "4":"Marshall",
        "5":"Maldonado",
        "6":"Ward",
        "7":"Wolf",
        "8":"Fuentes",
        "9":"Rowland",
        "10":"Schmidt"
    },
    "age":{
        "1":61,
        "2":21,
        "3":22,
        "4":50,
        "5":51,
        "6":61,
        "7":19,
        "8":63,
        "9":45,
        "10":42
    },
    "country":{
        "1":"Tonga",
        "2":"Seychelles",
        "3":"Czech Republic",
        "4":"Malaysia",
        "5":"Canada",
        "6":"French Guiana",
        "7":"French Southern Territories",
        "8":"Gambia",
        "9":"Sudan",
        "10":"Nauru"
    },
    "city":{
        "1":"East Michael",
        "2":"Janicetown",
        "3":"West Melissa",
        "4":"Lunamouth",
        "5":"Lake Sandrastad",
        "6":"Kennethview",
        "7":"Kristinestad",
        "8":"Port Frank",
        "9":"Alexiston",
        "10":"Alyssafort"
    },
    "email":{
        "1":"johnsonjack@esmartdata.org",
        "2":"thodges@esmartdata.org",
        "3":"kmalone@esmartdata.org",
        "4":"yperry@esmartdata.org",
        "5":"mwade@esmartdata.org",
        "6":"lisa46@esmartdata.org",
        "7":"greenjustin@esmartdata.org",
        "8":"brandonchandler@esmartdata.org",
        "9":"gibsonjennifer@esmartdata.org",
        "10":"vterry@esmartdata.org"
    }
}
"""
import pandas as pd
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database
cur = conn.cursor()  # create a cursor object

with open("../Query/create_database.sql", "r", encoding='utf-8') as file:
    create_database_sql = file.read()  # read the sql query from the file
cur.executescript(create_database_sql)  # execute the sql query

df = pd.read_sql_query("SELECT * FROM app_user LIMIT 10;", conn, index_col='id')  # read the data from the database
df.to_json('../Dataset/app_user.json', indent=4)  # export the data to a JSON file

conn.close()  # close the connection
