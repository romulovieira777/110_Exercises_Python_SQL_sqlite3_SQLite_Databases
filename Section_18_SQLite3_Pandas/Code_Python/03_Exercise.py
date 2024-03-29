"""
Exercise No. 03

Using the built-in sqlite3 package, a SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

A query was created that extracts the first ten records of the "app_user" table and transforms into a DataFrame
(df variable). Export this DataFrame to an HTML file named "app_user.html".

Content of the "app_user.html" file:
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>country</th>
      <th>city</th>
      <th>email</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>John</td>
      <td>Lewis</td>
      <td>61</td>
      <td>Tonga</td>
      <td>East Michael</td>
      <td>johnsonjack@esmartdata.org</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lance</td>
      <td>Boyer</td>
      <td>21</td>
      <td>Seychelles</td>
      <td>Janicetown</td>
      <td>thodges@esmartdata.org</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Michael</td>
      <td>Larson</td>
      <td>22</td>
      <td>Czech Republic</td>
      <td>West Melissa</td>
      <td>kmalone@esmartdata.org</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alexandra</td>
      <td>Marshall</td>
      <td>50</td>
      <td>Malaysia</td>
      <td>Lunamouth</td>
      <td>yperry@esmartdata.org</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Rebecca</td>
      <td>Maldonado</td>
      <td>51</td>
      <td>Canada</td>
      <td>Lake Sandrastad</td>
      <td>mwade@esmartdata.org</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Ronald</td>
      <td>Ward</td>
      <td>61</td>
      <td>French Guiana</td>
      <td>Kennethview</td>
      <td>lisa46@esmartdata.org</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Justin</td>
      <td>Wolf</td>
      <td>19</td>
      <td>French Southern Territories</td>
      <td>Kristinestad</td>
      <td>greenjustin@esmartdata.org</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Nicole</td>
      <td>Fuentes</td>
      <td>63</td>
      <td>Gambia</td>
      <td>Port Frank</td>
      <td>brandonchandler@esmartdata.org</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Melissa</td>
      <td>Rowland</td>
      <td>45</td>
      <td>Sudan</td>
      <td>Alexiston</td>
      <td>gibsonjennifer@esmartdata.org</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Sean</td>
      <td>Schmidt</td>
      <td>42</td>
      <td>Nauru</td>
      <td>Alyssafort</td>
      <td>vterry@esmartdata.org</td>
    </tr>
  </tbody>
</table>
"""
import pandas as pd
import sqlite3

conn = sqlite3.connect("app.db")  # connect to the database
cur = conn.cursor()  # create a cursor object

with open("../Query/create_database.sql", "r", encoding='utf-8') as file:
    create_database_sql = file.read()  # read the sql query from the file
cur.executescript(create_database_sql)  # execute the sql query

df = pd.read_sql_query("SELECT * FROM app_user LIMIT 10;", conn, index_col='id')  # read the data from the database
df.to_html('../Dataset/app_user.html')  # export the data to a HTML file

conn.close()  # close the connection
